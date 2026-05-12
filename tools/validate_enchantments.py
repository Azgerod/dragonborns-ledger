#!/usr/bin/env python3
"""Validate enchantment-learning support table structure and cross-references."""

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
    "enchantment_record_id",
    "objective_id",
    "enchantment_name",
    "enchantment_type",
    "effect_group",
    "source_content",
    "source_page",
    "source_id",
    "base_magnitude",
    "base_cost",
    "enchantable_item_slots",
    "disenchant_sources",
    "learning_policy",
    "preservation_conflict_item",
    "route_treatment",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "enchantment_type": {"apparel", "weapon"},
    "source_content": {"base_game", "dragonborn", "ae_creation"},
    "learning_policy": {
        "main_route_nonunique_source",
        "main_route_ae_creation_source",
        "excluded_unique_preservation",
        "excluded_unobtainable",
    },
    "route_treatment": {
        "source_listed_enchantment_learning",
        "excluded_unique_preservation",
        "excluded_unobtainable",
    },
}

EXPECTED_COUNTS = {
    "total": 59,
    "apparel": 40,
    "weapon": 19,
    "source_listed_enchantment_learning": 54,
    "excluded_unique_preservation": 4,
    "excluded_unobtainable": 1,
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
    seen_names: set[str] = set()
    counts = {
        "total": len(rows),
        "apparel": 0,
        "weapon": 0,
        "source_listed_enchantment_learning": 0,
        "excluded_unique_preservation": 0,
        "excluded_unobtainable": 0,
    }

    for line_number, row in enumerate(rows, start=2):
        record_id = row["enchantment_record_id"]
        if not re.fullmatch(r"ENCH-\d{6}", record_id):
            errors.append(f"{path}:{line_number}: invalid enchantment_record_id {record_id!r}")
        if record_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate enchantment_record_id {record_id}")
        seen_ids.add(record_id)

        name = row["enchantment_name"]
        if not name:
            errors.append(f"{path}:{line_number}: missing enchantment_name")
        if name in seen_names:
            errors.append(f"{path}:{line_number}: duplicate enchantment_name {name}")
        seen_names.add(name)

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if row["enchantment_type"] in counts:
            counts[row["enchantment_type"]] += 1
        if row["route_treatment"] in counts:
            counts[row["route_treatment"]] += 1

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
        else:
            treatment = row["route_treatment"]
            expected_subcategory = (
                "enchantment_learning"
                if treatment == "source_listed_enchantment_learning"
                else "enchantment_learning_excluded"
            )
            if objective["subcategory"] != expected_subcategory:
                errors.append(
                    f"{path}:{line_number}: objective subcategory is {objective['subcategory']}, "
                    f"expected {expected_subcategory}"
                )
            expected_placement = "main_route" if treatment == "source_listed_enchantment_learning" else "excluded"
            if objective["route_placement"] != expected_placement:
                errors.append(
                    f"{path}:{line_number}: objective route_placement is "
                    f"{objective['route_placement']}, expected {expected_placement}"
                )

        if row["route_treatment"] == "source_listed_enchantment_learning":
            if row["preservation_conflict_item"]:
                errors.append(f"{path}:{line_number}: learnable row has preservation_conflict_item")
        else:
            if not row["preservation_conflict_item"]:
                errors.append(f"{path}:{line_number}: excluded row lacks preservation_conflict_item")

        for column in ["effect_group", "base_magnitude", "base_cost", "enchantable_item_slots", "disenchant_sources"]:
            if not row[column].strip():
                errors.append(f"{path}:{line_number}: missing {column}")

    for key, expected in EXPECTED_COUNTS.items():
        actual = counts[key]
        if actual != expected:
            errors.append(f"{path}: {key} count is {actual}, expected {expected}")

    return errors


def main() -> int:
    template = SKILLS_DIR / "enchantment-learning-catalog.template.csv"
    table = SKILLS_DIR / "enchantment-learning-catalog.csv"
    if not template.exists():
        print(f"Missing enchantment template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing enchantment catalog: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template, template=True) + validate_table(table)
    if errors:
        print("Enchantment table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Enchantment learning catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
