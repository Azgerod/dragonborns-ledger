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
PROTOTYPE_BLOCK_MAP = ROUTE_DIR / "prototype-objective-block-map.csv"
PROTOTYPE_BLOCK_MAP_TEMPLATE = ROUTE_DIR / "prototype-objective-block-map.template.csv"
SQLITE_WORKBENCH = ROUTE_DIR / "route-planning.sqlite"

CONTROLLED_SEVERITIES = {"hard_gate", "branch_or_hard_save", "warning", "planning", "review"}
CONTROLLED_PROTOTYPE_STATUSES = {
    "anchored_window",
    "dependency_anchor_pending",
    "excluded_nonroute",
    "held_appendix",
    "held_branch_deferred",
    "held_candidate_selection",
    "held_checklist_mapping",
    "held_hard_gate",
    "held_option_list",
    "held_progression_layer",
    "inserted_direct_geography",
    "inserted_fixed_early",
    "inserted_setup_support",
    "inserted_support_candidate",
    "manual_validation_required",
    "out_of_scope",
    "support_candidate_conditional",
}
CONTROLLED_PROTOTYPE_BLOCKS = {
    "",
    "G00",
    "G01",
    "G02",
    "G03",
    "G04",
    "G05",
    "G06",
    "G07",
    "G08",
    "G09",
    "G10",
    "G11",
    "G12",
    "G13",
    "G14",
}
CONTROLLED_DISPOSITIONS = {
    "anchored_window",
    "appendix",
    "branch_deferred",
    "checklist_mapping",
    "conditional_support",
    "dependency_anchor",
    "excluded",
    "later_pass",
    "manual_validation",
    "option_list",
    "route_block",
    "unassigned",
}


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
                "route_prototype_block_map",
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
            prototype_count = conn.execute("SELECT COUNT(*) FROM prototype_objective_block_map").fetchone()[0]
            if objective_count != prototype_count:
                errors.append(f"{SQLITE_WORKBENCH}: objectives/prototype map row count mismatch {objective_count} != {prototype_count}")
            prototype_view_count = conn.execute("SELECT COUNT(*) FROM route_prototype_block_map").fetchone()[0]
            if prototype_count != prototype_view_count:
                errors.append(
                    f"{SQLITE_WORKBENCH}: prototype table/view row count mismatch {prototype_count} != {prototype_view_count}"
                )
    except sqlite3.Error as error:
        errors.append(f"{SQLITE_WORKBENCH}: SQLite validation failed: {error}")


def validate_prototype_block_map(
    objectives: dict[str, dict[str, str]],
    route_index: dict[str, dict[str, str]],
    errors: list[str],
) -> None:
    if read_header(PROTOTYPE_BLOCK_MAP) != read_header(PROTOTYPE_BLOCK_MAP_TEMPLATE):
        errors.append("prototype-objective-block-map.csv header does not match its template")
        return

    rows = read_csv(PROTOTYPE_BLOCK_MAP)
    route_ids = [row["objective_id"] for row in rows]
    if Counter(route_ids) != Counter(objectives.keys()):
        errors.append("prototype-objective-block-map.csv must contain exactly one row for every objective")

    for line_number, row in enumerate(rows, start=2):
        objective_id = row["objective_id"]
        if objective_id not in objectives:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: unknown objective_id {objective_id}")
            continue
        objective = objectives[objective_id]
        for column in ["objective_name", "category", "route_placement", "routing_rigidity"]:
            if row[column] != objective[column]:
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: {column} does not match objectives.csv")
        route_row = route_index.get(objective_id, {})
        for column in [
            "source_corridor",
            "candidate_status",
            "route_index_status",
            "constraint_count",
            "constraint_types",
            "hard_level_gate",
        ]:
            route_column = "primary_route_corridor" if column == "source_corridor" else column
            if row[column] != route_row.get(route_column, ""):
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: {column} does not match objective-route-index.csv")
        if row["prototype_status"] not in CONTROLLED_PROTOTYPE_STATUSES:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: invalid prototype_status {row['prototype_status']}")
        if row["route_block"] not in CONTROLLED_PROTOTYPE_BLOCKS:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: invalid route_block {row['route_block']}")
        if row["disposition"] not in CONTROLLED_DISPOSITIONS:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: invalid disposition {row['disposition']}")
        if row["route_placement"] == "main_route" and not row["prototype_status"]:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: main_route row has empty prototype_status")
        if row["prototype_status"] == "inserted_direct_geography":
            if not row["source_corridor"]:
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: direct geography insertion missing source_corridor")
            if not re.fullmatch(r"G\d{2}", row["route_block"]):
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: direct geography insertion missing G-block")
        if row["prototype_status"].startswith("held_") and not row["deferred_to"]:
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: held row missing deferred_to")
        if row["route_block"] and not re.fullmatch(r"G\d{2}", row["route_block"]):
            errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: route_block is not a G-block")
        if row["parent_objective_id"]:
            if row["parent_objective_id"] not in objectives:
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: unknown parent_objective_id {row['parent_objective_id']}")
            elif row["parent_objective_name"] != objectives[row["parent_objective_id"]]["objective_name"]:
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: parent_objective_name does not match objectives.csv")
            if row["parent_route_block"] and row["parent_route_block"] not in CONTROLLED_PROTOTYPE_BLOCKS:
                errors.append(f"{PROTOTYPE_BLOCK_MAP}:{line_number}: invalid parent_route_block {row['parent_route_block']}")


def main() -> int:
    errors: list[str] = []
    required = [
        ROUTE_DIR / "README.md",
        ROUTE_INDEX,
        ROUTE_INDEX_TEMPLATE,
        CONSTRAINT_INDEX,
        CONSTRAINT_INDEX_TEMPLATE,
        PROTOTYPE_BLOCK_MAP,
        PROTOTYPE_BLOCK_MAP_TEMPLATE,
    ]
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

    validate_prototype_block_map(objectives, {row["objective_id"]: row for row in route_rows}, errors)
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
