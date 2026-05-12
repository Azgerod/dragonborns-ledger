#!/usr/bin/env python3
"""Validate merchant-investment support table structure and cross-references."""

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
    "merchant_investment_record_id",
    "objective_id",
    "merchant_name",
    "store_name",
    "town_or_route",
    "hold",
    "source_content",
    "merchant_type",
    "base_gold",
    "invest_status",
    "master_trader_status",
    "investment_policy",
    "availability_notes",
    "source_page",
    "source_id",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "source_content": {"base_game", "dawnguard", "dragonborn", "ae_creation"},
    "invest_status": {
        "available",
        "bugged_unofficial_patch_only",
        "unknown_needs_validation",
    },
    "master_trader_status": {"available", "not_investable"},
    "investment_policy": {
        "main_route_investment",
        "excluded_unofficial_patch_only",
        "needs_validation_unknown_ae",
    },
}

EXPECTED_COUNTS = {
    "total": 50,
    "available": 33,
    "bugged_unofficial_patch_only": 13,
    "unknown_needs_validation": 4,
    "available_base_game": 31,
    "available_dawnguard": 1,
    "available_dragonborn": 1,
    "available_ae_creation": 0,
}

PARENT_OBJECTIVE_ID = "OBJ-002717"


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
    seen_objective_ids: set[str] = set()
    counts = {key: 0 for key in EXPECTED_COUNTS}
    counts["total"] = len(rows)

    parent = objectives.get(PARENT_OBJECTIVE_ID)
    if parent is None:
        errors.append(f"missing parent objective {PARENT_OBJECTIVE_ID}")
    elif parent["category"] != "crafting_unlock" or parent["subcategory"] != "all_merchant_investments":
        errors.append(f"{PARENT_OBJECTIVE_ID} is not the merchant-investment parent objective")

    for line_number, row in enumerate(rows, start=2):
        record_id = row["merchant_investment_record_id"]
        if not re.fullmatch(r"MERINV-\d{6}", record_id):
            errors.append(f"{path}:{line_number}: invalid merchant_investment_record_id {record_id!r}")
        if record_id in seen_record_ids:
            errors.append(f"{path}:{line_number}: duplicate merchant_investment_record_id {record_id}")
        seen_record_ids.add(record_id)

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        for column in [
            "merchant_name",
            "town_or_route",
            "hold",
            "source_page",
            "source_id",
            "citations",
            "notes",
        ]:
            if not row[column].strip():
                errors.append(f"{path}:{line_number}: missing {column}")

        if not row["base_gold"].isdigit():
            errors.append(f"{path}:{line_number}: invalid base_gold {row['base_gold']!r}")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        invest_status = row["invest_status"]
        counts[invest_status] += 1
        if invest_status == "available":
            counts[f"available_{row['source_content']}"] += 1
            if row["investment_policy"] != "main_route_investment":
                errors.append(f"{path}:{line_number}: available row is not main_route_investment")
            objective_id = row["objective_id"]
            if not objective_id:
                errors.append(f"{path}:{line_number}: available row lacks objective_id")
            elif objective_id in seen_objective_ids:
                errors.append(f"{path}:{line_number}: duplicate objective_id {objective_id}")
            else:
                seen_objective_ids.add(objective_id)
                objective = objectives.get(objective_id)
                if objective is None:
                    errors.append(f"{path}:{line_number}: unknown objective_id {objective_id}")
                elif objective["category"] != "crafting_unlock":
                    errors.append(f"{path}:{line_number}: objective is not a crafting_unlock row")
                elif objective["subcategory"] != "merchant_investment":
                    errors.append(f"{path}:{line_number}: objective is not a merchant_investment row")
                elif objective["route_placement"] != "main_route":
                    errors.append(f"{path}:{line_number}: objective is not placed on main_route")
                else:
                    if objective["source_content"] != row["source_content"]:
                        errors.append(f"{path}:{line_number}: objective source_content mismatch")
                    if objective["hold"] and objective["hold"] != row["hold"]:
                        errors.append(f"{path}:{line_number}: objective hold mismatch")
                    if " | " in objective["location"]:
                        parts = [part.strip() for part in objective["location"].split("|")]
                        if len(parts) == 2 and parts[0] == parts[1]:
                            errors.append(f"{path}:{line_number}: duplicated objective location")
                    expected_note = f"support row {record_id}"
                    if expected_note not in objective["notes"]:
                        errors.append(f"{path}:{line_number}: objective notes lack {expected_note!r}")
        else:
            if row["objective_id"]:
                errors.append(f"{path}:{line_number}: non-available row should not have objective_id")
            expected_policy = (
                "excluded_unofficial_patch_only"
                if invest_status == "bugged_unofficial_patch_only"
                else "needs_validation_unknown_ae"
            )
            if row["investment_policy"] != expected_policy:
                errors.append(
                    f"{path}:{line_number}: {invest_status} row has policy {row['investment_policy']!r}"
                )

    for key, expected in EXPECTED_COUNTS.items():
        actual = counts[key]
        if actual != expected:
            errors.append(f"{path}: {key} count is {actual}, expected {expected}")

    return errors


def main() -> int:
    template = SKILLS_DIR / "merchant-investment-catalog.template.csv"
    table = SKILLS_DIR / "merchant-investment-catalog.csv"
    if not template.exists():
        print(f"Missing merchant investment template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing merchant investment catalog: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template, template=True) + validate_table(table)
    if errors:
        print("Merchant investment catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Merchant investment catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
