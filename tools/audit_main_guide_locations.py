#!/usr/bin/env python3
"""Audit location objective/checklist representation for main-guide-v1.

This is an internal QA helper for TB-035-COV-007. It checks every location
objective and every checklist location row against the player-facing guide,
the internal guide coverage ledger, and the location support tables.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MATRIX_CSV = REPO_ROOT / "data" / "checklist-mapping" / "coverage-matrix.csv"
GUIDE_COVERAGE_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-coverage.csv"
OBJECTIVES_CSV = REPO_ROOT / "data" / "objectives" / "objectives.csv"
LOCATION_CATALOG_CSV = REPO_ROOT / "data" / "locations" / "location-catalog.csv"
LOCATION_GEOGRAPHY_CSV = REPO_ROOT / "data" / "locations" / "location-geography.csv"
MAIN_GUIDE = REPO_ROOT / "drafts" / "final-guide" / "main-guide-v1.md"
OUTPUT_CSV = REPO_ROOT / "data" / "guide-coverage" / "main-guide-v1-location-audit.csv"

CHECKLIST_ID_RE = re.compile(r"CHK-[A-Z0-9-]+-\d{4}")
CHECKLIST_RANGE_RE = re.compile(
    r"\b(CHK-[A-Z0-9-]+-)(\d{4})\s*(?:-|through)\s*(?:(?:CHK-[A-Z0-9-]+-)?(\d{4}))\b",
    re.IGNORECASE,
)
OBJECTIVE_ID_RE = re.compile(r"OBJ-\d{6}")
OBJECTIVE_RANGE_RE = re.compile(r"OBJ-\d{6}\s*(?:-|through)\s*OBJ-\d{6}", re.IGNORECASE)

CLEAR_TERMS = ("clear", "cleared", "dungeons cleared", "delver")
DISCOVER_TERMS = ("discover", "discovered", "locations discovered", "explorer")
ENTER_TERMS = ("enter", "entered", "visited", "reached", "boarded", "traversed", "arrive", "travel to", "go to")
HOLD_TERMS = (
    "avoid",
    "excluded",
    "held",
    "later",
    "not routed",
    "not_discovered",
    "not discovered",
    "not started",
    "not_entered",
    "staged",
    "untouched",
)
SECONDARY_TERMS = ("secondary marker", "not independent", "duplicate marker", "inherited")
ROUTE_RESOLUTION_TERMS = ("needs route resolution", "route-resolution")
EXCLUSION_TERMS = ("excluded", "exclusion", "not required", "outside required")


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower()
    compact = re.sub(r"[^a-z0-9]+", " ", lowered).strip()
    return re.sub(r"\s+", " ", compact)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def expand_checklist_refs(raw_value: str, valid_ids: set[str]) -> list[str]:
    raw_value = raw_value.strip()
    if not raw_value:
        return []

    ids: set[str] = set()
    for match in CHECKLIST_RANGE_RE.finditer(raw_value):
        prefix, start_raw, end_raw = match.groups()
        start, end = int(start_raw), int(end_raw)
        if start <= end:
            for number in range(start, end + 1):
                checklist_id = f"{prefix}{number:04d}"
                if checklist_id in valid_ids:
                    ids.add(checklist_id)

    for checklist_id in CHECKLIST_ID_RE.findall(raw_value):
        if checklist_id in valid_ids:
            ids.add(checklist_id)

    return sorted(ids)


def expand_objective_refs(raw_value: str, valid_ids: set[str]) -> list[str]:
    raw_value = raw_value.strip()
    if not raw_value:
        return []

    ids = OBJECTIVE_ID_RE.findall(raw_value)
    if len(ids) == 2 and OBJECTIVE_RANGE_RE.search(raw_value):
        start, end = (int(ids[0][-6:]), int(ids[1][-6:]))
        if start <= end:
            return [f"OBJ-{number:06d}" for number in range(start, end + 1) if f"OBJ-{number:06d}" in valid_ids]

    return [objective_id for objective_id in ids if objective_id in valid_ids]


def strip_location_prefix(value: str) -> str:
    cleaned = value.replace("*", "").replace("\u200e", "").strip()
    cleaned = re.sub(r"^(Clear|Discover)\s+", "", cleaned)
    cleaned = re.sub(r"^Validate AE Location Coverage:\s*", "", cleaned)
    cleaned = re.sub(r"^Reconcile\s+", "", cleaned)
    cleaned = re.sub(r"\s+Cleared Marker$", "", cleaned)
    cleaned = re.sub(r"\([^)]*\)", "", cleaned).strip()
    return cleaned


def name_variants(*values: str) -> set[str]:
    variants: set[str] = set()
    for value in values:
        if not value:
            continue
        cleaned = value.replace("*", "").replace("\u200e", "").strip()
        stripped = strip_location_prefix(cleaned)
        for candidate in {cleaned, stripped, re.sub(r"\([^)]*\)", "", cleaned).strip()}:
            if not candidate:
                continue
            variants.add(candidate)
            if candidate.endswith(" Cavern"):
                variants.add(f"{candidate}s")
            if candidate.endswith(" Caverns"):
                variants.add(candidate[:-1])
    return {variant for variant in variants if variant}


def guide_contains_name(guide_normalized: str, *names: str) -> bool:
    for variant in name_variants(*names):
        normalized_name = normalize(variant)
        if len(normalized_name) < 4:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(normalized_name)}(?![a-z0-9])"
        if re.search(pattern, guide_normalized):
            return True
    return False


def rows_blob(rows: list[dict[str, str]]) -> str:
    return normalize(
        " ".join(
            " ".join(
                row.get(key, "")
                for key in (
                    "record_type",
                    "objective_name",
                    "coverage_status",
                    "player_facing_cue",
                    "player_facing_location",
                    "completion_status",
                    "notes",
                )
            )
            for row in rows
        )
    )


def has_any(blob: str, terms: tuple[str, ...]) -> bool:
    return any(term in blob for term in terms)


def treatment_flags(rows: list[dict[str, str]], catalog_row: dict[str, str]) -> dict[str, str]:
    blob = rows_blob(rows)
    catalog_blob = normalize(
        " ".join(
            catalog_row.get(key, "")
            for key in (
                "location_category",
                "discoverable_status",
                "clearable_status",
                "delver_count_status",
                "quest_or_state_dependency",
                "notes",
            )
        )
    )
    full_blob = f"{blob} {catalog_blob}"
    return {
        "clear_treatment": "Y" if has_any(full_blob, CLEAR_TERMS) else "N",
        "discover_treatment": "Y" if has_any(full_blob, DISCOVER_TERMS) else "N",
        "enter_treatment": "Y" if has_any(full_blob, ENTER_TERMS) else "N",
        "hold_or_avoid_treatment": "Y" if has_any(full_blob, HOLD_TERMS) else "N",
        "secondary_or_duplicate_treatment": "Y" if has_any(full_blob, SECONDARY_TERMS) else "N",
        "route_resolution_treatment": "Y" if has_any(full_blob, ROUTE_RESOLUTION_TERMS) else "N",
        "exclusion_treatment": "Y" if has_any(full_blob, EXCLUSION_TERMS) else "N",
    }


def counter_treatment(catalog_row: dict[str, str]) -> str:
    delver_status = catalog_row.get("delver_count_status", "")
    clearable_status = catalog_row.get("clearable_status", "")
    discoverable_status = catalog_row.get("discoverable_status", "")

    if delver_status == "counts":
        return "delver_candidate_counts_when_cleared"
    if delver_status == "atypical_does_not_count":
        return "clearable_but_not_delver"
    if delver_status == "does_not_count":
        return "does_not_count_for_delver"
    if discoverable_status == "source_lists_discoverable":
        return "explorer_discovery_candidate"
    if clearable_status == "inherited_from_primary":
        return "secondary_marker_no_independent_counter"
    return delver_status or clearable_status or discoverable_status or "not_available"


def expected_treatment_met(subcategory: str, flags: dict[str, str], mapping_type: str = "") -> bool:
    if flags["route_resolution_treatment"] == "Y" or flags["exclusion_treatment"] == "Y":
        return True
    if mapping_type == "Explicit exclusion":
        return flags["exclusion_treatment"] == "Y"
    if subcategory == "clearable_location":
        return any(
            flags[key] == "Y"
            for key in (
                "clear_treatment",
                "hold_or_avoid_treatment",
                "secondary_or_duplicate_treatment",
            )
        )
    if subcategory in {"discoverable_non_clearable", "content_location"}:
        return any(
            flags[key] == "Y"
            for key in (
                "discover_treatment",
                "enter_treatment",
                "clear_treatment",
                "hold_or_avoid_treatment",
            )
        )
    if subcategory in {"secondary_marker", "map_marker_duplicate"}:
        return any(
            flags[key] == "Y"
            for key in (
                "secondary_or_duplicate_treatment",
                "discover_treatment",
                "enter_treatment",
                "hold_or_avoid_treatment",
            )
        )
    return any(value == "Y" for value in flags.values())


def joined(values: set[str] | list[str], limit: int = 6) -> str:
    clean_values = sorted({value for value in values if value})
    if len(clean_values) <= limit:
        return " | ".join(clean_values)
    shown = " | ".join(clean_values[:limit])
    return f"{shown} | ... ({len(clean_values)} total)"


def audit_status_for(
    row_kind: str,
    guide_name_match: bool,
    coverage_rows: list[dict[str, str]],
    subcategory: str,
    flags: dict[str, str],
    mapping_type: str = "",
) -> tuple[str, str, str]:
    if not coverage_rows:
        return (
            f"{row_kind}_missing_internal_coverage",
            "add_internal_location_coverage_row",
            "No exact or mapped internal coverage row was found for this location row.",
        )

    if flags["route_resolution_treatment"] == "Y":
        return (f"{row_kind}_route_resolution_recorded", "none_existing_route_resolution", "")

    if flags["exclusion_treatment"] == "Y" and mapping_type == "Explicit exclusion":
        return (f"{row_kind}_excluded", "none", "")

    if not guide_name_match:
        return (
            f"{row_kind}_missing_guide_name",
            "add_player_facing_location_reference",
            "Internal coverage exists, but the guide does not name this location row.",
        )

    if expected_treatment_met(subcategory, flags, mapping_type):
        return (f"{row_kind}_covered", "none", "")

    return (
        f"{row_kind}_missing_location_treatment",
        "add_location_treatment_context",
        "The guide/internal coverage names this row but lacks clear discover/enter/clear/avoid/secondary treatment.",
    )


def coverage_rollup(rows: list[dict[str, str]]) -> tuple[set[str], set[str], set[str]]:
    return (
        {row.get("coverage_status", "") for row in rows},
        {row.get("completion_status", "") for row in rows},
        {row.get("player_facing_location", "") for row in rows},
    )


def main() -> int:
    objective_rows = read_csv(OBJECTIVES_CSV)
    objective_ids = {row["objective_id"] for row in objective_rows}
    objectives_by_id = {row["objective_id"]: row for row in objective_rows}
    location_objectives = [row for row in objective_rows if row.get("category") == "location"]

    matrix_rows = read_csv(COVERAGE_MATRIX_CSV)
    checklist_ids = {row["checklist_id"] for row in matrix_rows}
    location_checklist_rows = [row for row in matrix_rows if row.get("checklist_tab") == "Locations"]

    catalog_by_objective = {row["objective_id"]: row for row in read_csv(LOCATION_CATALOG_CSV)}
    geography_by_objective = {row["objective_id"]: row for row in read_csv(LOCATION_GEOGRAPHY_CSV)}

    guide_normalized = normalize(MAIN_GUIDE.read_text(encoding="utf-8"))

    coverage_by_checklist_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    coverage_by_objective_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(GUIDE_COVERAGE_CSV):
        raw_id = row.get("objective_id", "")
        for checklist_id in expand_checklist_refs(raw_id, checklist_ids):
            coverage_by_checklist_id[checklist_id].append(row)
        for objective_id in expand_objective_refs(raw_id, objective_ids):
            coverage_by_objective_id[objective_id].append(row)

    output_rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()

    def append_output(
        *,
        row_kind: str,
        row_id: str,
        location_name: str,
        objective_id: str,
        checklist_id: str,
        checklist_entry: str,
        mapping_type: str,
        coverage_rows: list[dict[str, str]],
        guide_name_match: bool,
        objective_row: dict[str, str],
        catalog_row: dict[str, str],
        geography_row: dict[str, str],
    ) -> None:
        subcategory = objective_row.get("subcategory", "") or catalog_row.get("location_category", "")
        flags = treatment_flags(coverage_rows, catalog_row)
        audit_status, recommended_action, notes = audit_status_for(
            row_kind,
            guide_name_match,
            coverage_rows,
            subcategory,
            flags,
            mapping_type,
        )
        coverage_statuses, completion_statuses, guide_locations = coverage_rollup(coverage_rows)

        status_counts[audit_status] += 1
        action_counts[recommended_action] += 1

        output_rows.append(
            {
                "row_kind": row_kind,
                "row_id": row_id,
                "objective_id": objective_id,
                "checklist_id": checklist_id,
                "location_name": location_name,
                "checklist_entry": checklist_entry,
                "subcategory": subcategory,
                "source_content": objective_row.get("source_content", "") or catalog_row.get("source_content", ""),
                "mapping_type": mapping_type,
                "route_placement": objective_row.get("route_placement", ""),
                "location_catalog_category": catalog_row.get("location_category", ""),
                "discoverable_status": catalog_row.get("discoverable_status", ""),
                "clearable_status": catalog_row.get("clearable_status", ""),
                "delver_count_status": catalog_row.get("delver_count_status", ""),
                "counter_treatment": counter_treatment(catalog_row),
                "route_cluster": geography_row.get("route_cluster", ""),
                "route_corridor": geography_row.get("route_corridor", ""),
                "coordinate_status": geography_row.get("coordinate_status", ""),
                "guide_name_match": "Y" if guide_name_match else "N",
                "internal_coverage_row_count": str(len(coverage_rows)),
                **flags,
                "audit_status": audit_status,
                "coverage_statuses": joined(coverage_statuses),
                "completion_statuses": joined(completion_statuses),
                "guide_locations": joined(guide_locations),
                "recommended_action": recommended_action,
                "notes": notes,
            }
        )

    for objective_row in location_objectives:
        objective_id = objective_row["objective_id"]
        catalog_row = catalog_by_objective.get(objective_id, {})
        geography_row = geography_by_objective.get(objective_id, {})
        location_name = catalog_row.get("location_name", "") or strip_location_prefix(objective_row["objective_name"])
        coverage_rows = coverage_by_objective_id.get(objective_id, [])
        guide_name_match = guide_contains_name(guide_normalized, objective_row["objective_name"], location_name)
        append_output(
            row_kind="location_objective",
            row_id=objective_id,
            location_name=location_name,
            objective_id=objective_id,
            checklist_id="",
            checklist_entry="",
            mapping_type="",
            coverage_rows=coverage_rows,
            guide_name_match=guide_name_match,
            objective_row=objective_row,
            catalog_row=catalog_row,
            geography_row=geography_row,
        )

    for checklist_row in location_checklist_rows:
        checklist_id = checklist_row["checklist_id"]
        objective_id = checklist_row.get("objective_id", "")
        objective_row = objectives_by_id.get(objective_id, {})
        catalog_row = catalog_by_objective.get(objective_id, {})
        geography_row = geography_by_objective.get(objective_id, {})
        location_name = catalog_row.get("location_name", "") or strip_location_prefix(checklist_row["checklist_entry"])
        exact_rows = coverage_by_checklist_id.get(checklist_id, [])
        mapped_objective_rows = coverage_by_objective_id.get(objective_id, []) if objective_id else []
        coverage_rows = exact_rows or mapped_objective_rows
        guide_name_match = guide_contains_name(
            guide_normalized,
            checklist_row["checklist_entry"],
            checklist_row.get("matched_objective_name", ""),
            location_name,
        )
        append_output(
            row_kind="location_checklist",
            row_id=checklist_id,
            location_name=location_name,
            objective_id=objective_id,
            checklist_id=checklist_id,
            checklist_entry=checklist_row["checklist_entry"],
            mapping_type=checklist_row.get("mapping_type", ""),
            coverage_rows=coverage_rows,
            guide_name_match=guide_name_match,
            objective_row=objective_row,
            catalog_row=catalog_row,
            geography_row=geography_row,
        )

    fieldnames = [
        "row_kind",
        "row_id",
        "objective_id",
        "checklist_id",
        "location_name",
        "checklist_entry",
        "subcategory",
        "source_content",
        "mapping_type",
        "route_placement",
        "location_catalog_category",
        "discoverable_status",
        "clearable_status",
        "delver_count_status",
        "counter_treatment",
        "route_cluster",
        "route_corridor",
        "coordinate_status",
        "guide_name_match",
        "internal_coverage_row_count",
        "clear_treatment",
        "discover_treatment",
        "enter_treatment",
        "hold_or_avoid_treatment",
        "secondary_or_duplicate_treatment",
        "route_resolution_treatment",
        "exclusion_treatment",
        "audit_status",
        "coverage_statuses",
        "completion_statuses",
        "guide_locations",
        "recommended_action",
        "notes",
    ]

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} location audit rows to {OUTPUT_CSV.relative_to(REPO_ROOT)}.")
    print("By audit_status:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print("By recommended_action:")
    for action, count in action_counts.most_common():
        print(f"  {action}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
