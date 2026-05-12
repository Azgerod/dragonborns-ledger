#!/usr/bin/env python3
"""Validate skill/perk support table structure and cross-references."""

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
    "skill_record_id",
    "skill_name",
    "specialization",
    "source_content",
    "source_page",
    "source_id",
    "skill_100_objective_id",
    "perk_tree_objective_id",
    "perk_nodes",
    "perk_ranks",
    "skill_completion_boundary",
    "perk_completion_boundary",
    "legendary_reset_relevance",
    "route_treatment",
    "citations",
    "notes",
]

CONTROLLED_VALUES = {
    "specialization": {"magic", "combat", "stealth"},
    "source_content": {"base_game"},
    "route_treatment": {"source_listed_skill_tree"},
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


def validate_table(path: Path) -> list[str]:
    errors: list[str] = []
    rows = read_csv(path)
    objectives = read_objectives()
    sources = bibliography_ids()
    seen_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        skill_record_id = row["skill_record_id"]
        if not re.fullmatch(r"SKILL-\d{6}", skill_record_id):
            errors.append(f"{path}:{line_number}: invalid skill_record_id {skill_record_id!r}")
        if skill_record_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate skill_record_id {skill_record_id}")
        seen_ids.add(skill_record_id)

        for column, allowed_values in CONTROLLED_VALUES.items():
            value = row[column]
            if value not in allowed_values:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if row["source_id"] not in sources:
            errors.append(f"{path}:{line_number}: unknown source_id {row['source_id']}")

        for citation in split_pipe(row["citations"]):
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{path}:{line_number}: missing source note {citation}")

        for column, expected_subcategory in [
            ("skill_100_objective_id", "skill_100"),
            ("perk_tree_objective_id", "perk_tree"),
        ]:
            objective_id = row[column]
            objective = objectives.get(objective_id)
            if objective is None:
                errors.append(f"{path}:{line_number}: unknown {column} {objective_id}")
            elif objective["category"] != "skill_perk":
                errors.append(f"{path}:{line_number}: {column} is not a skill_perk row")
            elif objective["subcategory"] != expected_subcategory:
                errors.append(
                    f"{path}:{line_number}: {column} expected {expected_subcategory}, got {objective['subcategory']}"
                )

        for column in ["perk_nodes", "perk_ranks"]:
            value = row[column]
            if not value.isdigit() or int(value) <= 0:
                errors.append(f"{path}:{line_number}: invalid {column} {value!r}")

        if not row["skill_completion_boundary"].strip():
            errors.append(f"{path}:{line_number}: missing skill_completion_boundary")
        if not row["perk_completion_boundary"].strip():
            errors.append(f"{path}:{line_number}: missing perk_completion_boundary")

    return errors


def main() -> int:
    template = SKILLS_DIR / "skill-perk-catalog.template.csv"
    table = SKILLS_DIR / "skill-perk-catalog.csv"
    if not template.exists():
        print(f"Missing skill/perk template: {template}", file=sys.stderr)
        return 1
    if not table.exists():
        print(f"Missing skill/perk catalog: {table}", file=sys.stderr)
        return 1

    errors = validate_table(template) + validate_table(table)
    if errors:
        print("Skill/perk table validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Skill/perk catalog OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
