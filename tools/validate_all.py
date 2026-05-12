#!/usr/bin/env python3
"""Run all lightweight repository validators."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = [
    "tools/validate_objectives.py",
    "tools/validate_coverage.py",
    "tools/validate_sources.py",
    "tools/validate_books.py",
    "tools/validate_npc_options.py",
    "tools/validate_items.py",
    "tools/validate_properties.py",
    "tools/validate_locations.py",
    "tools/validate_location_coordinates.py",
    "tools/validate_location_geography.py",
    "tools/validate_skills.py",
    "tools/validate_enchantments.py",
    "tools/validate_alchemy.py",
    "tools/validate_merchants.py",
    "tools/validate_crafting_systems.py",
]


def main() -> int:
    for validator in VALIDATORS:
        result = subprocess.run([sys.executable, validator], cwd=REPO_ROOT)
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
