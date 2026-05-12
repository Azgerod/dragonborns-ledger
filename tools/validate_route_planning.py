#!/usr/bin/env python3
"""Validate generated route-planning index structure."""

from __future__ import annotations

from collections import Counter
import csv
from pathlib import Path
import re
import sqlite3
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
ROUTE_DIR = REPO_ROOT / "data" / "route-planning"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
SOURCE_NOTES = REPO_ROOT / "sources" / "source-notes"
ROUTE_INDEX = ROUTE_DIR / "objective-route-index.csv"
ROUTE_INDEX_TEMPLATE = ROUTE_DIR / "objective-route-index.template.csv"
CONSTRAINT_INDEX = ROUTE_DIR / "objective-constraints.csv"
CONSTRAINT_INDEX_TEMPLATE = ROUTE_DIR / "objective-constraints.template.csv"
SQLITE_WORKBENCH = ROUTE_DIR / "route-planning.sqlite"

CONTROLLED_SEVERITIES = {"hard_gate", "branch_or_hard_save", "warning", "planning", "review"}


def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle), [])


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def source_note_exists(reference: str) -> bool:
    if not reference:
        return True
    if reference.endswith(".md"):
        return (SOURCE_NOTES / reference).exists()
    return any(path.name.startswith(f"{reference}-") or path.name == f"{reference}.md" for path in SOURCE_NOTES.glob("*.md"))


def validate_sqlite_if_present(errors: list[str]) -> None:
    if not SQLITE_WORKBENCH.exists():
        return
    try:
        with sqlite3.connect(SQLITE_WORKBENCH) as conn:
            expected_views = {
                "route_objective_workbench",
                "route_unclassified_objectives",
                "route_hard_constraint_queue",
                "route_location_objectives_by_corridor",
                "route_candidate_selection_queue",
            }
            rows = conn.execute("SELECT name FROM sqlite_master WHERE type = 'view'").fetchall()
            present = {row[0] for row in rows}
            missing = expected_views - present
            if missing:
                errors.append(f"{SQLITE_WORKBENCH}: missing SQL views: {', '.join(sorted(missing))}")
            objective_count = conn.execute("SELECT COUNT(*) FROM objectives").fetchone()[0]
            index_count = conn.execute("SELECT COUNT(*) FROM objective_route_index").fetchone()[0]
            if objective_count != index_count:
                errors.append(f"{SQLITE_WORKBENCH}: objectives/index row count mismatch {objective_count} != {index_count}")
    except sqlite3.Error as error:
        errors.append(f"{SQLITE_WORKBENCH}: SQLite validation failed: {error}")


def main() -> int:
    errors: list[str] = []
    required = [ROUTE_DIR / "README.md", ROUTE_INDEX, ROUTE_INDEX_TEMPLATE, CONSTRAINT_INDEX, CONSTRAINT_INDEX_TEMPLATE]
    for path in required:
        if not path.exists():
            errors.append(f"Missing route-planning file: {path}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if read_header(ROUTE_INDEX) != read_header(ROUTE_INDEX_TEMPLATE):
        errors.append("objective-route-index.csv header does not match its template")
    if read_header(CONSTRAINT_INDEX) != read_header(CONSTRAINT_INDEX_TEMPLATE):
        errors.append("objective-constraints.csv header does not match its template")

    objective_rows = read_csv(OBJECTIVES)
    objectives = {row["objective_id"]: row for row in objective_rows}
    route_rows = read_csv(ROUTE_INDEX)
    constraint_rows = read_csv(CONSTRAINT_INDEX)

    route_ids = [row["objective_id"] for row in route_rows]
    if Counter(route_ids) != Counter(objectives.keys()):
        errors.append("objective-route-index.csv must contain exactly one row for every objective")

    constraint_counts = Counter(row["objective_id"] for row in constraint_rows)
    seen_constraint_ids: set[str] = set()
    for line_number, row in enumerate(constraint_rows, start=2):
        constraint_id = row["constraint_id"]
        if not re.fullmatch(r"RPCON-\d{6}", constraint_id):
            errors.append(f"{CONSTRAINT_INDEX}:{line_number}: invalid constraint_id {constraint_id}")
        if constraint_id in seen_constraint_ids:
            errors.append(f"{CONSTRAINT_INDEX}:{line_number}: duplicate constraint_id {constraint_id}")
        seen_constraint_ids.add(constraint_id)

        objective_id = row["objective_id"]
        if objective_id not in objectives:
            errors.append(f"{CONSTRAINT_INDEX}:{line_number}: unknown objective_id {objective_id}")
        source_file = REPO_ROOT / row["constraint_source_file"]
        if not source_file.exists():
            errors.append(f"{CONSTRAINT_INDEX}:{line_number}: missing source file {row['constraint_source_file']}")
        if row["severity"] not in CONTROLLED_SEVERITIES:
            errors.append(f"{CONSTRAINT_INDEX}:{line_number}: invalid severity {row['severity']}")
        for reference in [part.strip() for part in row["source_notes"].split(" | ") if part.strip()]:
            if not source_note_exists(reference):
                errors.append(f"{CONSTRAINT_INDEX}:{line_number}: missing source note {reference}")

    for line_number, row in enumerate(route_rows, start=2):
        objective_id = row["objective_id"]
        if objective_id not in objectives:
            errors.append(f"{ROUTE_INDEX}:{line_number}: unknown objective_id {objective_id}")
            continue
        expected = constraint_counts[objective_id]
        actual = int(row["constraint_count"] or "0")
        if expected != actual:
            errors.append(f"{ROUTE_INDEX}:{line_number}: constraint_count {actual} does not match index count {expected}")
        for column in ["support_record_count", "support_location_count"]:
            if not re.fullmatch(r"\d+", row[column]):
                errors.append(f"{ROUTE_INDEX}:{line_number}: {column} is not an integer")

    validate_sqlite_if_present(errors)

    if errors:
        print("Route-planning validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Route-planning indexes OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
