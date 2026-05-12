#!/usr/bin/env python3
"""Validate item-member table structure."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
ITEMS_DIR = REPO_ROOT / "data" / "items"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

REQUIRED_COLUMNS = [
    "item_member_id",
    "parent_objective_id",
    "parent_objective_name",
    "source_creation",
    "item_name",
    "item_category",
    "source_content",
    "source_page",
    "source_id",
    "source_section",
    "existing_objective_id",
    "source_table_detail",
    "route_treatment",
    "citations",
    "notes",
]
ALLOWED_ROUTE_TREATMENTS = {
    "source_listed_member",
    "already_tracked_in_spell_tome_table",
    "crafting_system_cross_reference",
    "excluded_template_or_internal",
    "excluded_unobtainable",
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


def validate_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path)
    objectives = objective_ids()
    sources = bibliography_ids()
    seen_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        item_id = row["item_member_id"]
        if not re.fullmatch(r"ITEM-\d{6}", item_id):
            errors.append(f"{path}:{line_number}: invalid item_member_id {item_id!r}")
        if item_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate item_member_id {item_id}")
        seen_ids.add(item_id)

        parent_id = row["parent_objective_id"]
        if parent_id not in objectives:
            errors.append(f"{path}:{line_number}: unknown parent_objective_id {parent_id}")

        existing_id = row["existing_objective_id"]
        if existing_id and existing_id not in objectives:
            errors.append(f"{path}:{line_number}: unknown existing_objective_id {existing_id}")

        if row["source_content"] != "ae_creation":
            errors.append(f"{path}:{line_number}: expected source_content=ae_creation")

        if row["route_treatment"] not in ALLOWED_ROUTE_TREATMENTS:
            errors.append(f"{path}:{line_number}: invalid route_treatment {row['route_treatment']!r}")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in [part.strip() for part in row["citations"].split(" | ") if part.strip()]:
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        if row["route_treatment"] == "already_tracked_in_spell_tome_table" and not existing_id:
            errors.append(f"{path}:{line_number}: spell-tome member lacks existing_objective_id")

    return errors


def main() -> int:
    template = ITEMS_DIR / "item-members.template.csv"
    table = ITEMS_DIR / "ae-item-members.csv"
    if not template.exists():
        print(f"Missing item-member template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing AE item-member table: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template) + validate_table(table)
    if errors:
        print("Item table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Item member tables OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
