#!/usr/bin/env python3
"""Validate location catalog table structure."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCATIONS_DIR = REPO_ROOT / "data" / "locations"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"
TEMPLATE = LOCATIONS_DIR / "location-catalog.template.csv"
CATALOG = LOCATIONS_DIR / "location-catalog.csv"
REQUIRED_COLUMNS = [
    "location_record_id",
    "objective_id",
    "location_name",
    "location_category",
    "source_content",
    "worldspace",
    "region",
    "hold",
    "source_page",
    "source_id",
    "uesp_categories",
    "discoverable_status",
    "clearable_status",
    "delver_count_status",
    "quest_or_state_dependency",
    "cell_entry_lock_risk",
    "missability",
    "bug_risk",
    "survival_mode_relevance",
    "route_status",
    "citations",
    "notes",
]
CONTROLLED_VALUES = {
    "location_category": {
        "clearable_location",
        "discoverable_non_clearable",
        "map_marker_duplicate",
        "secondary_marker",
        "content_location",
        "location_parent",
    },
    "source_content": {
        "base_game",
        "dawnguard",
        "hearthfire",
        "dragonborn",
        "ae_creation",
        "multiple",
        "not_applicable",
    },
    "discoverable_status": {
        "source_lists_discoverable",
        "source_lists_not_discoverable",
        "needs_research",
        "not_applicable",
    },
    "clearable_status": {
        "source_lists_clearable",
        "source_lists_not_clearable",
        "inherited_from_primary",
        "needs_research",
        "not_applicable",
    },
    "delver_count_status": {
        "counts",
        "does_not_count",
        "atypical_does_not_count",
        "needs_validation",
        "not_applicable",
    },
    "cell_entry_lock_risk": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "missability": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "bug_risk": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "route_status": {
        "source_listed_candidate",
        "route_selected_later",
        "excluded_duplicate",
        "needs_reconciliation",
        "reconciled_secondary_marker",
        "reconciled_duplicate_marker",
        "content_location_pending_validation",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            print(f"{path} has unexpected header.", file=sys.stderr)
            print(f"Expected: {REQUIRED_COLUMNS}", file=sys.stderr)
            print(f"Actual:   {reader.fieldnames}", file=sys.stderr)
            raise SystemExit(1)
        return list(reader)


def read_objectives() -> dict[str, dict[str, str]]:
    with OBJECTIVES.open(newline="", encoding="utf-8") as handle:
        return {row["objective_id"]: row for row in csv.DictReader(handle)}


def bibliography_ids() -> set[str]:
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    return set(re.findall(r"\bSRC-\d{6}\b", text))


def validate_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path)
    objectives = read_objectives()
    sources = bibliography_ids()
    seen_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        location_record_id = row["location_record_id"]
        if not re.fullmatch(r"LOC-\d{6}", location_record_id):
            errors.append(f"{path}:{line_number}: invalid location_record_id {location_record_id!r}")
        if location_record_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate location_record_id {location_record_id}")
        seen_ids.add(location_record_id)

        objective_id = row["objective_id"]
        objective = objectives.get(objective_id)
        if objective is None:
            errors.append(f"{path}:{line_number}: unknown objective_id {objective_id}")
        elif objective.get("category") != "location":
            errors.append(f"{path}:{line_number}: objective_id is not a location row {objective_id}")

        if not row["location_name"].strip():
            errors.append(f"{path}:{line_number}: missing location_name")
        if not row["source_page"].strip():
            errors.append(f"{path}:{line_number}: missing source_page")
        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row.get(column, "")
            if value and value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        for citation in [part.strip() for part in row["citations"].split(" | ") if part.strip()]:
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

    return errors


def main() -> int:
    if not TEMPLATE.exists():
        print(f"Missing location template: {TEMPLATE}", file=sys.stderr)
        return 1
    if not CATALOG.exists():
        print(f"Missing location catalog: {CATALOG}", file=sys.stderr)
        return 1

    errors = validate_table(TEMPLATE) + validate_table(CATALOG)
    if errors:
        print("Location catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Location catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
