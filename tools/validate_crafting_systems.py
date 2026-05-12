#!/usr/bin/env python3
"""Validate practical crafting-system support table structure and references."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "data" / "skills"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

REQUIRED_COLUMNS = [
    "crafting_system_record_id",
    "objective_id",
    "system_name",
    "source_content",
    "system_type",
    "source_page",
    "source_id",
    "existing_objective_ids",
    "coverage_status",
    "route_treatment",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "source_content": {"base_game", "hearthfire", "dragonborn", "ae_creation"},
    "system_type": {
        "skill_controlled",
        "skill_controlled_special_station",
        "special_crafting_station",
        "food_crafting",
        "ae_special_crafting_station",
        "property_construction",
        "material_gathering",
        "material_processing",
    },
    "coverage_status": {
        "represented_existing_objectives",
        "new_system_objective_with_existing_ae_crosslinks",
        "new_system_objective",
        "represented_property_rows_checklist_deferred",
        "represented_new_trophy_row",
        "common_station_action_deferred",
    },
    "route_treatment": {
        "represented_existing_objectives",
        "new_objective_added",
        "checklist_deferred",
        "route_action_only",
    },
}

EXPECTED_SYSTEMS = {
    "Alchemy",
    "Enchanting",
    "Staff Enchanting",
    "Smithing",
    "Atronach Forge",
    "Baking",
    "Bone Forge",
    "Construction",
    "Cooking",
    "Imbuing Chamber",
    "Mining",
    "Smelting",
    "Tanning",
}

EXPECTED_NEW_OBJECTIVE_IDS = {"OBJ-002753", "OBJ-002754", "OBJ-002755"}


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


def split_pipe(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def validate_table(path: Path, *, template: bool = False) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path)
    if template:
        return errors

    objectives = read_objectives()
    sources = bibliography_ids()
    seen_record_ids: set[str] = set()
    seen_systems: set[str] = set()
    seen_new_objectives: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        record_id = row["crafting_system_record_id"]
        if not re.fullmatch(r"CRAFTSYS-\d{6}", record_id):
            errors.append(f"{path}:{line_number}: invalid crafting_system_record_id {record_id!r}")
        if record_id in seen_record_ids:
            errors.append(f"{path}:{line_number}: duplicate crafting_system_record_id {record_id}")
        seen_record_ids.add(record_id)

        system_name = row["system_name"]
        if not system_name:
            errors.append(f"{path}:{line_number}: missing system_name")
        if system_name in seen_systems:
            errors.append(f"{path}:{line_number}: duplicate system_name {system_name}")
        seen_systems.add(system_name)

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        for column in ["source_page", "source_id", "citations", "notes"]:
            if not row[column].strip():
                errors.append(f"{path}:{line_number}: missing {column}")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        objective_id = row["objective_id"]
        if objective_id:
            seen_new_objectives.add(objective_id)
            objective = objectives.get(objective_id)
            if objective is None:
                errors.append(f"{path}:{line_number}: unknown objective_id {objective_id}")
            elif objective["category"] != "crafting_unlock":
                errors.append(f"{path}:{line_number}: objective is not a crafting_unlock row")
            elif objective["subcategory"] != "practical_crafting_system":
                errors.append(f"{path}:{line_number}: objective is not a practical_crafting_system row")
            elif objective["route_placement"] != "main_route":
                errors.append(f"{path}:{line_number}: objective is not placed on main_route")
            if row["route_treatment"] != "new_objective_added":
                errors.append(f"{path}:{line_number}: objective row is not marked new_objective_added")

        for existing_objective_id in split_pipe(row["existing_objective_ids"]):
            if existing_objective_id not in objectives:
                errors.append(
                    f"{path}:{line_number}: unknown existing_objective_id {existing_objective_id}"
                )

    if len(rows) != len(EXPECTED_SYSTEMS):
        errors.append(f"{path}: row count is {len(rows)}, expected {len(EXPECTED_SYSTEMS)}")

    if seen_systems != EXPECTED_SYSTEMS:
        missing = sorted(EXPECTED_SYSTEMS - seen_systems)
        extra = sorted(seen_systems - EXPECTED_SYSTEMS)
        errors.append(f"{path}: system set mismatch; missing {missing}, extra {extra}")

    if seen_new_objectives != EXPECTED_NEW_OBJECTIVE_IDS:
        errors.append(
            f"{path}: new objective ids are {sorted(seen_new_objectives)}, "
            f"expected {sorted(EXPECTED_NEW_OBJECTIVE_IDS)}"
        )

    return errors


def main() -> int:
    template = SKILLS_DIR / "practical-crafting-system-catalog.template.csv"
    table = SKILLS_DIR / "practical-crafting-system-catalog.csv"
    if not template.exists():
        print(f"Missing practical crafting-system template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing practical crafting-system catalog: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template, template=True) + validate_table(table)
    if errors:
        print("Practical crafting-system catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Practical crafting-system catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
