#!/usr/bin/env python3
"""Validate generated location coordinate support data."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
COORDINATES = REPO_ROOT / "data" / "locations" / "location-coordinates.csv"
CATALOG = REPO_ROOT / "data" / "locations" / "location-catalog.csv"
OBJECTIVES = REPO_ROOT / "data" / "objectives" / "objectives.csv"
BIBLIOGRAPHY = REPO_ROOT / "sources" / "bibliography.md"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

HEADER = [
    "coordinate_record_id",
    "location_record_id",
    "objective_id",
    "location_name",
    "location_category",
    "source_content",
    "catalog_worldspace",
    "coordinate_worldspace",
    "world_id",
    "world_name",
    "map_marker_id",
    "map_marker_name",
    "map_marker_page",
    "map_marker_icon_type",
    "map_marker_editor_id",
    "map_marker_form_id",
    "map_marker_dest_form_id",
    "x",
    "y",
    "z",
    "coordinate_status",
    "match_method",
    "match_confidence",
    "distance_scope",
    "source_url",
    "source_id",
    "citations",
    "notes",
]

COORDINATE_STATUSES = {
    "exact_marker",
    "multi_marker",
    "proxy_marker",
    "proxy_nearby_landmark",
    "unmapped_no_marker",
    "unmapped_worldspace",
}
MATCH_METHODS = {
    "uesp_gamemap_page",
    "uesp_gamemap_name",
    "manual_proxy",
    "manual_unmapped",
}
CONFIDENCE_VALUES = {"high", "medium", "low", "none"}
DISTANCE_SCOPES = {
    "same_worldspace_xy",
    "proxy_same_worldspace_xy",
    "multi_marker_choose_candidate",
    "not_comparable",
}


def read_csv(path: Path, expected_header: list[str] | None = None) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if expected_header is not None and reader.fieldnames != expected_header:
            print(f"{path} has unexpected header.", file=sys.stderr)
            print(f"Expected: {expected_header}", file=sys.stderr)
            print(f"Actual:   {reader.fieldnames}", file=sys.stderr)
            raise SystemExit(1)
        return list(reader)


def source_ids() -> set[str]:
    return set(re.findall(r"\bSRC-\d{6}\b", BIBLIOGRAPHY.read_text(encoding="utf-8")))


def validate() -> list[str]:
    errors: list[str] = []
    if not COORDINATES.exists():
        return [f"Missing coordinate table: {COORDINATES}"]

    coordinate_rows = read_csv(COORDINATES, HEADER)
    catalog_rows = {row["location_record_id"]: row for row in read_csv(CATALOG)}
    objective_rows = {row["objective_id"]: row for row in read_csv(OBJECTIVES)}
    bibliography_ids = source_ids()
    seen_coordinate_ids: set[str] = set()
    covered_location_ids: set[str] = set()

    for line_number, row in enumerate(coordinate_rows, start=2):
        coordinate_id = row["coordinate_record_id"]
        if not re.fullmatch(r"COORD-\d{6}", coordinate_id):
            errors.append(f"{COORDINATES}:{line_number}: invalid coordinate_record_id {coordinate_id}")
        if coordinate_id in seen_coordinate_ids:
            errors.append(f"{COORDINATES}:{line_number}: duplicate coordinate_record_id {coordinate_id}")
        seen_coordinate_ids.add(coordinate_id)

        location_id = row["location_record_id"]
        catalog_row = catalog_rows.get(location_id)
        if catalog_row is None:
            errors.append(f"{COORDINATES}:{line_number}: unknown location_record_id {location_id}")
        else:
            covered_location_ids.add(location_id)
            if row["objective_id"] != catalog_row["objective_id"]:
                errors.append(f"{COORDINATES}:{line_number}: objective_id does not match catalog for {location_id}")
            if row["location_name"] != catalog_row["location_name"]:
                errors.append(f"{COORDINATES}:{line_number}: location_name does not match catalog for {location_id}")

        objective = objective_rows.get(row["objective_id"])
        if objective is None:
            errors.append(f"{COORDINATES}:{line_number}: unknown objective_id {row['objective_id']}")
        elif objective.get("category") != "location":
            errors.append(f"{COORDINATES}:{line_number}: objective is not a location row {row['objective_id']}")

        for column, allowed in {
            "coordinate_status": COORDINATE_STATUSES,
            "match_method": MATCH_METHODS,
            "match_confidence": CONFIDENCE_VALUES,
            "distance_scope": DISTANCE_SCOPES,
        }.items():
            if row[column] not in allowed:
                errors.append(f"{COORDINATES}:{line_number}: invalid {column} {row[column]!r}")

        has_xy = bool(row["x"] and row["y"])
        if row["distance_scope"] == "not_comparable" and has_xy:
            errors.append(f"{COORDINATES}:{line_number}: not_comparable row should not have x/y")
        if row["distance_scope"] != "not_comparable" and not has_xy:
            errors.append(f"{COORDINATES}:{line_number}: comparable row is missing x/y")
        for column in ("x", "y", "z"):
            if row[column]:
                try:
                    float(row[column])
                except ValueError:
                    errors.append(f"{COORDINATES}:{line_number}: nonnumeric {column} {row[column]!r}")

        if row["source_id"] not in bibliography_ids:
            errors.append(f"{COORDINATES}:{line_number}: unknown source_id {row['source_id']}")
        for citation in [part.strip() for part in row["citations"].split(" | ") if part.strip()]:
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{COORDINATES}:{line_number}: missing source note {citation}")

    missing_locations = set(catalog_rows) - covered_location_ids
    if missing_locations:
        errors.append(f"{COORDINATES}: missing coordinate rows for {len(missing_locations)} catalog locations")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Location coordinate validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Location coordinates OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
