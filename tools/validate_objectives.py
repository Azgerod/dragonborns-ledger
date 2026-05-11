#!/usr/bin/env python3
"""Validate objective CSV structure.

This check intentionally validates structure only. Gameplay facts and citation
coverage need later research-specific validation.
"""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
TEMPLATE = REPO_ROOT / "data" / "objectives" / "objectives.template.csv"
TAXONOMY = REPO_ROOT / "data" / "objectives" / "taxonomy.md"
SOURCE_NOTES = REPO_ROOT / "sources" / "source-notes"
REQUIRED_TAXONOMY_SECTIONS = [
    "## Row Granularity",
    "## Category Map",
    "## Source Content Map",
    "## Initial Research Batches",
    "## Route Placement Defaults",
]
CONTROLLED_VALUES = {
    "category": {
        "quest",
        "misc_objective",
        "trophy",
        "ae_creation",
        "location",
        "collectible",
        "unique_item",
        "property",
        "pet_mount",
        "npc_relationship",
        "spell_power",
        "skill_perk",
        "crafting_unlock",
        "radiant",
        "book_document",
        "system",
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
    "routing_rigidity": {
        "fixed_early",
        "fixed_late",
        "windowed",
        "region_flexible",
        "dependency_flexible",
        "branch_only",
        "option_list",
        "cleanup_safe",
        "excluded_unbounded",
        "unclassified",
    },
    "route_placement": {
        "main_route",
        "branch_route",
        "option_list",
        "appendix",
        "excluded",
        "unclassified",
    },
    "research_status": {
        "not_started",
        "in_progress",
        "needs_sources",
        "needs_review",
        "validated",
        "blocked",
        "not_applicable",
    },
    "validation_status": {
        "not_started",
        "in_progress",
        "needs_sources",
        "needs_review",
        "validated",
        "blocked",
        "not_applicable",
    },
}
OBJECTIVE_ID_PATTERN = re.compile(r"^OBJ-\d{6}$")


def read_header(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle), [])


def main() -> int:
    try:
        template_header = read_header(TEMPLATE)
        objectives_header = read_header(OBJECTIVES)
    except FileNotFoundError as error:
        print(f"Missing objective CSV: {error.filename}", file=sys.stderr)
        return 1

    if objectives_header != template_header:
        print("Objective CSV header does not match template.", file=sys.stderr)
        print(f"Template:   {template_header}", file=sys.stderr)
        print(f"Objectives: {objectives_header}", file=sys.stderr)
        return 1

    if not TAXONOMY.exists():
        print(f"Missing objective taxonomy: {TAXONOMY}", file=sys.stderr)
        return 1

    taxonomy_text = TAXONOMY.read_text(encoding="utf-8")
    missing_sections = [
        section for section in REQUIRED_TAXONOMY_SECTIONS if section not in taxonomy_text
    ]
    if missing_sections:
        print("Objective taxonomy is missing required sections:", file=sys.stderr)
        for section in missing_sections:
            print(f"- {section}", file=sys.stderr)
        return 1

    with OBJECTIVES.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        seen_ids: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                print(f"Row {line_number} has too many columns.", file=sys.stderr)
                return 1

            objective_id = row.get("objective_id", "")
            if not OBJECTIVE_ID_PATTERN.match(objective_id):
                print(
                    f"Row {line_number} has invalid objective_id: {objective_id}",
                    file=sys.stderr,
                )
                return 1
            if objective_id in seen_ids:
                print(f"Duplicate objective_id: {objective_id}", file=sys.stderr)
                return 1
            seen_ids.add(objective_id)

            for column, allowed_values in CONTROLLED_VALUES.items():
                value = row.get(column, "")
                if value and value not in allowed_values:
                    print(
                        f"Row {line_number} has invalid {column}: {value}",
                        file=sys.stderr,
                    )
                    return 1

            citations = row.get("citations", "")
            for citation in [part.strip() for part in citations.split("|") if part.strip()]:
                if not (SOURCE_NOTES / citation).exists():
                    print(
                        f"Row {line_number} references missing source note: {citation}",
                        file=sys.stderr,
                    )
                    return 1

    print("Objective CSV structure OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
