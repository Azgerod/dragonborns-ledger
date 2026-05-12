#!/usr/bin/env python3
"""Validate property-detail table structure and cross-references."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PROPERTIES_DIR = REPO_ROOT / "data" / "properties"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

REQUIRED_COLUMNS = [
    "property_detail_id",
    "parent_objective_id",
    "property_name",
    "property_group",
    "detail_type",
    "detail_name",
    "source_content",
    "worldspace",
    "region",
    "hold",
    "location",
    "prerequisite_or_trigger",
    "acquisition_or_build_method",
    "cost_or_materials",
    "service_or_npc_dependency",
    "feature_summary",
    "safe_storage_status",
    "display_or_collection_relevance",
    "family_support",
    "survival_mode_relevance",
    "route_treatment",
    "source_id",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "property_group": {
        "city_home",
        "hearthfire_homestead",
        "hearthfire_construction",
        "hearthfire_service",
        "dragonborn_home",
        "ae_home",
        "ae_farm",
        "ae_farm_service",
    },
    "detail_type": {
        "ownership_summary",
        "ownership_and_feature_summary",
        "purchasable_upgrade",
        "construction_module",
        "exterior_construction",
        "wing_choice",
        "steward_furnishing_service",
        "steward_service",
        "farmhouse_furnishing_upgrade",
        "farm_exterior_construction",
        "farm_operation",
        "warning_deferred",
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
    "safe_storage_status": {
        "source_lists_safe_home_storage",
        "source_lists_storage",
        "source_lists_storage_output",
        "construction_chest_source_listed",
        "needs_validation_later",
        "not_applicable",
    },
    "route_treatment": {
        "source_listed_detail",
        "purchasable_upgrade",
        "mutually_exclusive_upgrade",
        "thane_service_unlock",
        "material_planning_row",
        "mutually_exclusive_wing_choice",
        "service_option",
        "validation_deferred",
        "warning_deferred",
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


def objective_ids() -> set[str]:
    with OBJECTIVES.open(newline="", encoding="utf-8") as handle:
        return {row["objective_id"] for row in csv.DictReader(handle)}


def bibliography_ids() -> set[str]:
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    return set(re.findall(r"\bSRC-\d{6}\b", text))


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def validate_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path)
    objectives = objective_ids()
    sources = bibliography_ids()
    seen_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        detail_id = row["property_detail_id"]
        if not re.fullmatch(r"PROPDET-\d{6}", detail_id):
            errors.append(f"{path}:{line_number}: invalid property_detail_id {detail_id!r}")
        if detail_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate property_detail_id {detail_id}")
        seen_ids.add(detail_id)

        parent_id = row["parent_objective_id"]
        if parent_id not in objectives:
            errors.append(f"{path}:{line_number}: unknown parent_objective_id {parent_id}")

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        for source_id in split_pipe(row["source_id"]):
            if source_id not in sources:
                errors.append(f"{path}:{line_number}: unknown source_id {source_id}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        if not row["property_name"].strip():
            errors.append(f"{path}:{line_number}: missing property_name")
        if not row["detail_name"].strip():
            errors.append(f"{path}:{line_number}: missing detail_name")
        if not row["acquisition_or_build_method"].strip() and row["detail_type"] != "warning_deferred":
            errors.append(f"{path}:{line_number}: missing acquisition_or_build_method")

    return errors


def main() -> int:
    template = PROPERTIES_DIR / "property-details.template.csv"
    table = PROPERTIES_DIR / "property-details.csv"
    if not template.exists():
        print(f"Missing property-detail template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing property-detail table: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template) + validate_table(table)
    if errors:
        print("Property table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Property detail tables OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
