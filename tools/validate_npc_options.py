#!/usr/bin/env python3
"""Validate NPC and relationship option table structure."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
NPC_OPTIONS = REPO_ROOT / "data" / "npc" / "relationship-options.csv"
SOURCE_NOTES = REPO_ROOT / "sources" / "source-notes"
OPTION_ID_PATTERN = re.compile(r"^NPCOPT-\d{6}$")
REQUIRED_COLUMNS = [
    "option_id",
    "option_type",
    "name",
    "source_content",
    "source_section",
    "location",
    "prerequisite_or_condition",
    "related_property_or_role",
    "flags",
    "route_treatment",
    "citations",
    "notes",
]


def main() -> int:
    if not NPC_OPTIONS.exists():
        print(f"Missing NPC option table: {NPC_OPTIONS}", file=sys.stderr)
        return 1

    with NPC_OPTIONS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            print("NPC option table header does not match expected columns.", file=sys.stderr)
            print(f"Expected: {REQUIRED_COLUMNS}", file=sys.stderr)
            print(f"Actual:   {reader.fieldnames}", file=sys.stderr)
            return 1

        seen_ids: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            option_id = row["option_id"]
            if not OPTION_ID_PATTERN.match(option_id):
                print(f"Row {line_number} has invalid option_id: {option_id}", file=sys.stderr)
                return 1
            if option_id in seen_ids:
                print(f"Duplicate option_id: {option_id}", file=sys.stderr)
                return 1
            seen_ids.add(option_id)

            if not row["option_type"] or not row["name"] or not row["source_section"]:
                print(f"Row {line_number} is missing required option text.", file=sys.stderr)
                return 1

            for citation in [part.strip() for part in row["citations"].split("|") if part.strip()]:
                if not (SOURCE_NOTES / citation).exists():
                    print(
                        f"Row {line_number} references missing source note: {citation}",
                        file=sys.stderr,
                    )
                    return 1

    print("NPC relationship option table OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
