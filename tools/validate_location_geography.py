#!/usr/bin/env python3
"""Validate generated hub/corridor geography support data."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCATIONS_DIR = REPO_ROOT / "data" / "locations"
TEMPLATE = LOCATIONS_DIR / "location-geography.template.csv"
GEOGRAPHY = LOCATIONS_DIR / "location-geography.csv"
COORDINATES = LOCATIONS_DIR / "location-coordinates.csv"
SOURCE_NOTES_DIR = REPO_ROOT / "sources" / "source-notes"

HEADER = [
    "geography_record_id",
    "coordinate_record_id",
    "location_record_id",
    "objective_id",
    "location_name",
    "location_category",
    "source_content",
    "coordinate_worldspace",
    "coordinate_status",
    "distance_scope",
    "route_cluster",
    "route_corridor",
    "nearest_corridor_hub",
    "nearest_corridor_hub_type",
    "nearest_corridor_hub_distance",
    "nearest_major_carriage_origin",
    "nearest_major_carriage_origin_distance",
    "nearest_ferry_terminal",
    "nearest_ferry_terminal_distance",
    "nearest_inn_or_rest",
    "nearest_inn_or_rest_type",
    "nearest_inn_or_rest_distance",
    "nearest_candidate_base",
    "nearest_candidate_base_type",
    "nearest_candidate_base_distance",
    "worldspace_access_model",
    "transport_access_flags",
    "cold_risk",
    "barrier_flags",
    "geography_confidence",
    "citations",
    "notes",
]

WORLDSPACE_ACCESS_MODELS = {
    "same_worldspace_overland",
    "ferry_gateway_then_local_overland",
    "ferry_or_island_access",
    "dungeon_lift_or_interior_transition",
    "portal_or_quest_transition",
    "local_or_interior_subarea",
    "separate_worldspace_not_comparable",
    "no_marker_manual_validation",
}
COLD_RISKS = {
    "standard",
    "regional_cold",
    "source_listed_cold_interior",
    "solstheim_cold_region",
    "high_elevation_or_mountain",
    "not_comparable",
}
CONFIDENCE_VALUES = {"high", "medium", "low", "none"}


def read_csv(path: Path, expected_header: list[str] | None = None) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if expected_header is not None and reader.fieldnames != expected_header:
            print(f"{path} has unexpected header.", file=sys.stderr)
            print(f"Expected: {expected_header}", file=sys.stderr)
            print(f"Actual:   {reader.fieldnames}", file=sys.stderr)
            raise SystemExit(1)
        return list(reader)


def validate() -> list[str]:
    errors: list[str] = []
    if not TEMPLATE.exists():
        errors.append(f"Missing geography template: {TEMPLATE}")
    if not GEOGRAPHY.exists():
        errors.append(f"Missing geography table: {GEOGRAPHY}")
    if errors:
        return errors

    read_csv(TEMPLATE, HEADER)
    geography_rows = read_csv(GEOGRAPHY, HEADER)
    coordinate_rows = {row["coordinate_record_id"]: row for row in read_csv(COORDINATES)}
    seen_geography_ids: set[str] = set()
    covered_coordinate_ids: set[str] = set()

    for line_number, row in enumerate(geography_rows, start=2):
        geography_id = row["geography_record_id"]
        if not re.fullmatch(r"GEOG-\d{6}", geography_id):
            errors.append(f"{GEOGRAPHY}:{line_number}: invalid geography_record_id {geography_id}")
        if geography_id in seen_geography_ids:
            errors.append(f"{GEOGRAPHY}:{line_number}: duplicate geography_record_id {geography_id}")
        seen_geography_ids.add(geography_id)

        coordinate_id = row["coordinate_record_id"]
        coordinate = coordinate_rows.get(coordinate_id)
        if coordinate is None:
            errors.append(f"{GEOGRAPHY}:{line_number}: unknown coordinate_record_id {coordinate_id}")
        else:
            covered_coordinate_ids.add(coordinate_id)
            for column in (
                "location_record_id",
                "objective_id",
                "location_name",
                "location_category",
                "source_content",
                "coordinate_worldspace",
                "coordinate_status",
                "distance_scope",
            ):
                if row[column] != coordinate[column]:
                    errors.append(f"{GEOGRAPHY}:{line_number}: {column} does not match coordinate row {coordinate_id}")

        if row["worldspace_access_model"] not in WORLDSPACE_ACCESS_MODELS:
            errors.append(f"{GEOGRAPHY}:{line_number}: invalid worldspace_access_model {row['worldspace_access_model']!r}")
        if row["cold_risk"] not in COLD_RISKS:
            errors.append(f"{GEOGRAPHY}:{line_number}: invalid cold_risk {row['cold_risk']!r}")
        if row["geography_confidence"] not in CONFIDENCE_VALUES:
            errors.append(f"{GEOGRAPHY}:{line_number}: invalid geography_confidence {row['geography_confidence']!r}")

        not_comparable = row["distance_scope"] == "not_comparable"
        distance_columns = [
            "nearest_corridor_hub_distance",
            "nearest_major_carriage_origin_distance",
            "nearest_ferry_terminal_distance",
            "nearest_inn_or_rest_distance",
            "nearest_candidate_base_distance",
        ]
        for column in distance_columns:
            value = row[column]
            if value:
                if not re.fullmatch(r"\d+", value):
                    errors.append(f"{GEOGRAPHY}:{line_number}: noninteger {column} {value!r}")
            elif not not_comparable and column != "nearest_major_carriage_origin_distance":
                errors.append(f"{GEOGRAPHY}:{line_number}: comparable row missing {column}")

        if not_comparable:
            if row["geography_confidence"] != "none":
                errors.append(f"{GEOGRAPHY}:{line_number}: not_comparable row should have confidence none")
            if row["nearest_corridor_hub"] or row["nearest_inn_or_rest"] or row["nearest_candidate_base"]:
                errors.append(f"{GEOGRAPHY}:{line_number}: not_comparable row should not have nearest-service values")
        else:
            if not row["route_cluster"].strip() or not row["route_corridor"].strip():
                errors.append(f"{GEOGRAPHY}:{line_number}: comparable row missing route cluster/corridor")
            if not row["nearest_corridor_hub"].strip():
                errors.append(f"{GEOGRAPHY}:{line_number}: comparable row missing nearest corridor hub")

        if not row["barrier_flags"].strip():
            errors.append(f"{GEOGRAPHY}:{line_number}: missing barrier_flags")
        if not row["transport_access_flags"].strip():
            errors.append(f"{GEOGRAPHY}:{line_number}: missing transport_access_flags")

        for citation in [part.strip() for part in row["citations"].split(" | ") if part.strip()]:
            if not (SOURCE_NOTES_DIR / citation).exists():
                errors.append(f"{GEOGRAPHY}:{line_number}: missing source note {citation}")

    missing_coordinates = set(coordinate_rows) - covered_coordinate_ids
    if missing_coordinates:
        errors.append(f"{GEOGRAPHY}: missing geography rows for {len(missing_coordinates)} coordinate rows")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Location geography validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Location geography OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
