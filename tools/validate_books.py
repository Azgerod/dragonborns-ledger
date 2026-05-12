#!/usr/bin/env python3
"""Validate book/location reference tables.

This validates structure and cross-references only. It does not verify the
gameplay accuracy of source-listed locations.
"""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
SOURCE_NOTES = REPO_ROOT / "sources" / "source-notes"
BOOKS_DIR = REPO_ROOT / "data" / "books"
BOOK_LOCATION_TEMPLATE = BOOKS_DIR / "book-locations.template.csv"
SKILL_BOOK_LOCATIONS = BOOKS_DIR / "skill-books-locations.csv"
SPELL_TOME_LOCATIONS = BOOKS_DIR / "spell-tomes-locations.csv"
BOOK_DOCUMENT_LOCATIONS = BOOKS_DIR / "book-document-locations.csv"
BOOK_LOCATION_TABLES = [
    {
        "label": "Skill-book",
        "path": SKILL_BOOK_LOCATIONS,
        "valid_pairs": {("skill_book", "skill_book_title")},
    },
    {
        "label": "Spell-tome",
        "path": SPELL_TOME_LOCATIONS,
        "valid_pairs": {("spell_tome", "spell_tome_title")},
    },
    {
        "label": "Book/document",
        "path": BOOK_DOCUMENT_LOCATIONS,
        "valid_pairs": {
            ("black_book", "black_book_title"),
            ("quest_book", "quest_book_title"),
            ("unique_book", "unique_book_title"),
            ("ae_book", "ae_book_title"),
        },
    },
]
BOOK_LOCATION_ID_PATTERN = re.compile(r"^BOOKLOC-\d{6}$")
REQUIRED_BOOK_LOCATION_COLUMNS = [
    "book_location_id",
    "objective_id",
    "book_title",
    "book_category",
    "source_content",
    "skill_or_school",
    "worldspace",
    "region",
    "hold",
    "location",
    "location_detail",
    "ownership_or_crime_notes",
    "quest_or_state_dependency",
    "cell_entry_lock_risk",
    "missability",
    "bug_risk",
    "survival_mode_relevance",
    "route_candidate_status",
    "citations",
    "notes",
]
CONTROLLED_VALUES = {
    "book_category": {
        "skill_book",
        "spell_tome",
        "black_book",
        "quest_book",
        "ae_book",
        "unique_book",
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
    "cell_entry_lock_risk": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "missability": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "bug_risk": {"none_known", "possible", "confirmed", "unknown", "not_applicable"},
    "route_candidate_status": {
        "provisional_objective_representative",
        "source_listed_candidate",
        "route_selected_later",
        "excluded_duplicate",
    },
}


def read_header(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle), [])


def read_objectives() -> dict[str, dict[str, str]]:
    with OBJECTIVES.open(newline="", encoding="utf-8") as handle:
        return {row["objective_id"]: row for row in csv.DictReader(handle)}


def validate_location_table(
    *,
    config: dict[str, str | Path],
    template_header: list[str],
    objectives: dict[str, dict[str, str]],
    seen_location_ids: set[str],
) -> int:
    path = config["path"]
    if not isinstance(path, Path):
        raise TypeError("Book-location path must be a Path.")
    label = str(config["label"])
    valid_pairs = config["valid_pairs"]
    if not isinstance(valid_pairs, set):
        raise TypeError("Book-location valid_pairs must be a set.")
    subcategory_to_category = {
        str(subcategory): str(book_category) for book_category, subcategory in valid_pairs
    }

    if not path.exists():
        print(f"Missing {label.lower()} location table: {path}", file=sys.stderr)
        return 1

    table_header = read_header(path)
    if table_header != template_header:
        print(f"{label} location CSV header does not match template.", file=sys.stderr)
        print(f"Template: {template_header}", file=sys.stderr)
        print(f"Table:    {table_header}", file=sys.stderr)
        return 1

    missing_columns = [
        column for column in REQUIRED_BOOK_LOCATION_COLUMNS if column not in table_header
    ]
    if missing_columns:
        print("Book-location table is missing required columns:", file=sys.stderr)
        for column in missing_columns:
            print(f"- {column}", file=sys.stderr)
        return 1

    target_objectives = {
        objective_id
        for objective_id, row in objectives.items()
        if row.get("subcategory") in subcategory_to_category
    }
    covered_objectives: set[str] = set()

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                print(f"{label} row {line_number} has too many columns.", file=sys.stderr)
                return 1

            location_id = row["book_location_id"]
            if not BOOK_LOCATION_ID_PATTERN.match(location_id):
                print(
                    f"{label} row {line_number} has invalid book_location_id: {location_id}",
                    file=sys.stderr,
                )
                return 1
            if location_id in seen_location_ids:
                print(f"Duplicate book_location_id: {location_id}", file=sys.stderr)
                return 1
            seen_location_ids.add(location_id)

            objective_id = row["objective_id"]
            objective = objectives.get(objective_id)
            if objective is None:
                print(
                    f"{label} row {line_number} references unknown objective_id: {objective_id}",
                    file=sys.stderr,
                )
                return 1
            objective_subcategory = objective.get("subcategory", "")
            if objective_subcategory not in subcategory_to_category:
                print(
                    f"{label} row {line_number} references wrong objective subtype: "
                    f"{objective_id}",
                    file=sys.stderr,
                )
                return 1
            expected_category = subcategory_to_category[objective_subcategory]
            if row["book_category"] != expected_category:
                print(
                    f"{label} row {line_number} has invalid book_category for "
                    f"{objective_id}: {row['book_category']}",
                    file=sys.stderr,
                )
                return 1
            covered_objectives.add(objective_id)

            if not row["book_title"].strip():
                print(f"{label} row {line_number} is missing book_title.", file=sys.stderr)
                return 1
            if not row["location_detail"].strip():
                print(f"{label} row {line_number} is missing location_detail.", file=sys.stderr)
                return 1

            for column, allowed_values in CONTROLLED_VALUES.items():
                value = row.get(column, "")
                if value and value not in allowed_values:
                    print(
                        f"{label} row {line_number} has invalid {column}: {value}",
                        file=sys.stderr,
                    )
                    return 1

            for citation in [part.strip() for part in row["citations"].split("|") if part.strip()]:
                if not (SOURCE_NOTES / citation).exists():
                    print(
                        f"{label} row {line_number} references missing source note: {citation}",
                        file=sys.stderr,
                    )
                    return 1

    missing_objectives = sorted(target_objectives - covered_objectives)
    if missing_objectives:
        print(f"{label} objectives without location rows:", file=sys.stderr)
        for objective_id in missing_objectives:
            print(f"- {objective_id}", file=sys.stderr)
        return 1

    return 0


def main() -> int:
    if not BOOK_LOCATION_TEMPLATE.exists():
        print(f"Missing book-location template: {BOOK_LOCATION_TEMPLATE}", file=sys.stderr)
        return 1

    template_header = read_header(BOOK_LOCATION_TEMPLATE)
    objectives = read_objectives()
    seen_location_ids: set[str] = set()

    for config in BOOK_LOCATION_TABLES:
        result = validate_location_table(
            config=config,
            template_header=template_header,
            objectives=objectives,
            seen_location_ids=seen_location_ids,
        )
        if result != 0:
            return result

    print("Book location tables OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
