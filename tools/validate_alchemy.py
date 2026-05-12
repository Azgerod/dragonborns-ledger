#!/usr/bin/env python3
"""Validate alchemy ingredient-effect support table structure and cross-references."""

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
    "alchemy_record_id",
    "objective_id",
    "ingredient_name",
    "ingredient_variant",
    "ingredient_section",
    "source_content",
    "source_page",
    "source_id",
    "form_id",
    "effect_1",
    "effect_2",
    "effect_3",
    "effect_4",
    "value",
    "weight",
    "merchant_availability",
    "garden_planting",
    "source_note",
    "content_scope_note",
    "discovery_policy",
    "route_treatment",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "ingredient_section": {"standard", "creation_club", "quest"},
    "source_content": {"base_game", "dawnguard", "dragonborn", "ae_creation"},
    "discovery_policy": {"discover_all_four_effects"},
    "route_treatment": {"source_listed_ingredient_effects"},
}

EXPECTED_COUNTS = {
    "total": 190,
    "standard": 110,
    "creation_club": 74,
    "quest": 6,
    "base_game": 98,
    "dawnguard": 5,
    "dragonborn": 11,
    "ae_creation": 76,
}

PARENT_OBJECTIVE_ID = "OBJ-002526"


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
    seen_ids: set[str] = set()
    seen_ingredient_records: set[tuple[str, str, str]] = set()
    ingredient_name_counts: dict[str, int] = {}
    counts = {key: 0 for key in EXPECTED_COUNTS}
    counts["total"] = len(rows)

    parent = objectives.get(PARENT_OBJECTIVE_ID)
    if parent is None:
        errors.append(f"missing parent objective {PARENT_OBJECTIVE_ID}")
    elif parent["category"] != "crafting_unlock" or parent["subcategory"] != "all_alchemy_effects":
        errors.append(f"{PARENT_OBJECTIVE_ID} is not the alchemy parent objective")

    for line_number, row in enumerate(rows, start=2):
        record_id = row["alchemy_record_id"]
        if not re.fullmatch(r"ALCHEMY-\d{6}", record_id):
            errors.append(f"{path}:{line_number}: invalid alchemy_record_id {record_id!r}")
        if record_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate alchemy_record_id {record_id}")
        seen_ids.add(record_id)

        name = row["ingredient_name"]
        if not name:
            errors.append(f"{path}:{line_number}: missing ingredient_name")
        ingredient_name_counts[name] = ingredient_name_counts.get(name, 0) + 1

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        for key in ["ingredient_section", "source_content"]:
            counts[row[key]] += 1

        record_key = (name, row["form_id"], row["source_content"])
        if record_key in seen_ingredient_records:
            errors.append(f"{path}:{line_number}: duplicate ingredient record {record_key}")
        seen_ingredient_records.add(record_key)

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        objective_id = row["objective_id"]
        objective = objectives.get(objective_id)
        if objective is None:
            errors.append(f"{path}:{line_number}: unknown objective_id {objective_id}")
        elif objective["category"] != "crafting_unlock":
            errors.append(f"{path}:{line_number}: objective is not a crafting_unlock row")
        elif objective["subcategory"] != "alchemy_ingredient_effect_discovery":
            errors.append(f"{path}:{line_number}: objective is not an alchemy effect row")
        elif objective["route_placement"] != "main_route":
            errors.append(f"{path}:{line_number}: objective is not placed on main_route")

        for column in [
            "source_page",
            "form_id",
            "effect_1",
            "effect_2",
            "effect_3",
            "effect_4",
            "value",
            "weight",
            "merchant_availability",
            "garden_planting",
            "source_note",
            "notes",
        ]:
            if not row[column].strip():
                errors.append(f"{path}:{line_number}: missing {column}")

        if row["ingredient_section"] == "quest" and row["garden_planting"] != "not_applicable":
            errors.append(f"{path}:{line_number}: quest row garden_planting should be not_applicable")

        if row["ingredient_name"] == "Aloe Vera Leaves" and "1.6.1130" not in row["content_scope_note"]:
            errors.append(f"{path}:{line_number}: Aloe Vera Leaves lacks patch scope note")

    duplicate_names = {name for name, count in ingredient_name_counts.items() if count > 1}
    if duplicate_names != {"Nightshade"}:
        errors.append(f"{path}: unexpected duplicate ingredient names {sorted(duplicate_names)}")

    for row in rows:
        if row["ingredient_name"] == "Nightshade" and not row["ingredient_variant"]:
            errors.append(f"{path}: Nightshade record lacks ingredient_variant")

    for key, expected in EXPECTED_COUNTS.items():
        actual = counts[key]
        if actual != expected:
            errors.append(f"{path}: {key} count is {actual}, expected {expected}")

    return errors


def main() -> int:
    template = SKILLS_DIR / "alchemy-effect-catalog.template.csv"
    table = SKILLS_DIR / "alchemy-effect-catalog.csv"
    if not template.exists():
        print(f"Missing alchemy template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing alchemy catalog: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template, template=True) + validate_table(table)
    if errors:
        print("Alchemy table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Alchemy effect catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
