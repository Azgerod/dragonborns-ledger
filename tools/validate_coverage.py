#!/usr/bin/env python3
"""Validate the checklist coverage matrix structure.

This is intentionally lightweight until real checklist data exists. It checks
that the expected CSV columns are present and leaves content validation for a
later pass.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
REQUIRED_COLUMNS = [
    "checklist_id",
    "checklist_tab",
    "checklist_entry",
    "category",
    "mapping_type",
    "guide_location",
    "branch_name",
    "exclusion_reason",
    "source_note_refs",
    "status",
    "notes",
]


def main() -> int:
    if not COVERAGE_MATRIX.exists():
        print(f"Missing coverage matrix: {COVERAGE_MATRIX}", file=sys.stderr)
        return 1

    with COVERAGE_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []

    missing = [column for column in REQUIRED_COLUMNS if column not in columns]
    if missing:
        print("Coverage matrix is missing required columns:", file=sys.stderr)
        for column in missing:
            print(f"- {column}", file=sys.stderr)
        return 1

    print("Coverage matrix structure OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
