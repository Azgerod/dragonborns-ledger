#!/usr/bin/env python3
"""Validate source workflow scaffolding.

This validates only the source inventory/template structure. It does not verify
gameplay facts or source quality.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_TEMPLATE = REPO_ROOT / "sources" / "source-notes" / "source-note.template.md"
REQUIRED_BIB_COLUMNS = [
    "source_id",
    "Priority",
    "Source",
    "Type",
    "URL/reference",
    "Accessed",
    "Used for",
    "Notes",
]
REQUIRED_TEMPLATE_SECTIONS = [
    "## Claim",
    "## Routing Relevance",
    "## Sources",
    "## Evidence Summary",
    "## Confidence and Open Questions",
    "## Linked Records",
]


def markdown_table_header(path: Path) -> list[str]:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and "source_id" in stripped:
            return [cell.strip() for cell in next(csv.reader([stripped], delimiter="|")) if cell.strip()]
    return []


def main() -> int:
    if not BIBLIOGRAPHY.exists():
        print(f"Missing bibliography: {BIBLIOGRAPHY}", file=sys.stderr)
        return 1
    if not SOURCE_TEMPLATE.exists():
        print(f"Missing source-note template: {SOURCE_TEMPLATE}", file=sys.stderr)
        return 1

    columns = markdown_table_header(BIBLIOGRAPHY)
    missing_columns = [column for column in REQUIRED_BIB_COLUMNS if column not in columns]
    if missing_columns:
        print("Bibliography is missing required columns:", file=sys.stderr)
        for column in missing_columns:
            print(f"- {column}", file=sys.stderr)
        return 1

    template_text = SOURCE_TEMPLATE.read_text(encoding="utf-8")
    missing_sections = [section for section in REQUIRED_TEMPLATE_SECTIONS if section not in template_text]
    if missing_sections:
        print("Source-note template is missing required sections:", file=sys.stderr)
        for section in missing_sections:
            print(f"- {section}", file=sys.stderr)
        return 1

    print("Source workflow structure OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
