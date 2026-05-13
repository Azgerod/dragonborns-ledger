#!/usr/bin/env python3
"""Flag placeholder phrases that are not acceptable in the final guide.

This is an audit helper for the main-guide-v1 expansion. It intentionally
does not try to infer whether a complete objective list follows the phrase;
future writers should treat every hit as requiring review or replacement.
"""

from __future__ import annotations

import argparse
from pathlib import Path


PLACEHOLDER_PHRASES = [
    "route local",
    "safe local",
    "local objectives",
    "nearby objectives",
    "remaining finite",
    "remaining checklist",
    "as routed",
    "as needed",
    "selected sources",
    "support rows",
    "queue",
    "family",
    "cleanup",
    "verify checklist",
    "finish remaining",
    "collect local",
    "route books",
    "route locations",
    "corridor discoveries",
    "spell sources",
    "support objectives",
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit a guide draft for banned or suspect placeholder phrases.",
    )
    parser.add_argument("guide_path", help="Path to the guide markdown file to audit.")
    parser.add_argument(
        "--section",
        help=(
            "Optional section prefix to audit, for example 'MR-001'. "
            "The audit starts at a heading containing the prefix and stops at the next heading of the same level."
        ),
    )
    args = parser.parse_args()

    guide_path = Path(args.guide_path)
    text = guide_path.read_text(encoding="utf-8")
    if args.section:
        text = extract_section(text, args.section)
    hits: list[tuple[int, str, str]] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        lower = line.lower()
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in lower:
                hits.append((line_number, phrase, line.strip()))

    if not hits:
        target = f"{guide_path} section {args.section}" if args.section else str(guide_path)
        print(f"OK: no placeholder phrases found in {target}")
        return 0

    target = f"{guide_path} section {args.section}" if args.section else str(guide_path)
    print(f"Placeholder phrase hits in {target}:")
    for line_number, phrase, line in hits:
        print(f"{line_number}: {phrase!r}: {line}")
    return 1


def extract_section(text: str, section: str) -> str:
    lines = text.splitlines()
    start_index: int | None = None
    start_level: int | None = None

    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("#") and section in stripped:
            start_index = index
            start_level = len(stripped) - len(stripped.lstrip("#"))
            break

    if start_index is None or start_level is None:
        raise SystemExit(f"Section not found: {section}")

    end_index = len(lines)
    for index in range(start_index + 1, len(lines)):
        stripped = lines[index].lstrip()
        if not stripped.startswith("#"):
            continue
        level = len(stripped) - len(stripped.lstrip("#"))
        if level <= start_level:
            end_index = index
            break

    prefix = "\n" * start_index
    return prefix + "\n".join(lines[start_index:end_index])


if __name__ == "__main__":
    raise SystemExit(main())
