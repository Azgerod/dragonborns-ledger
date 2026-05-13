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
    args = parser.parse_args()

    guide_path = Path(args.guide_path)
    text = guide_path.read_text(encoding="utf-8")
    hits: list[tuple[int, str, str]] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        lower = line.lower()
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in lower:
                hits.append((line_number, phrase, line.strip()))

    if not hits:
        print(f"OK: no placeholder phrases found in {guide_path}")
        return 0

    print(f"Placeholder phrase hits in {guide_path}:")
    for line_number, phrase, line in hits:
        print(f"{line_number}: {phrase!r}: {line}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
