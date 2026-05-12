#!/usr/bin/env python3
"""Build location coordinate support data from UESP Gamemap markers."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable
from urllib.parse import quote, unquote

from fetch_uesp_gamemap import fetch_all


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG = REPO_ROOT / "data" / "locations" / "location-catalog.csv"
OUTPUT = REPO_ROOT / "data" / "locations" / "location-coordinates.csv"
RECONCILIATION = REPO_ROOT / "data" / "locations" / "location-coordinate-reconciliation.md"

SOURCE_ID = "SRC-000423"
SOURCE_NOTE = "SN-000123-location-coordinate-dataset.md"

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


@dataclass(frozen=True)
class ManualProxy:
    lookup_name: str
    confidence: str
    notes: str
    status: str = "proxy_marker"


MANUAL_PROXIES: dict[str, ManualProxy] = {
    "LOC-000146": ManualProxy(
        "Understone Keep",
        "medium",
        "UESP locates Nchuand-Zel inside Understone Keep; no separate Gamemap marker was found.",
    ),
    "LOC-000389": ManualProxy(
        "Riften Docks (CC)",
        "high",
        "UESP names the exterior map marker for Shadowfoot Sanctum as Riften Docks.",
    ),
    "LOC-000432": ManualProxy(
        "Rielle (CC)",
        "high",
        "UESP says Varlais Cavern is not a separate location and forms part of Rielle's first zone.",
    ),
    "LOC-000452": ManualProxy(
        "Blackbone Isle (CC)",
        "high",
        "Blackbone Isle Grotto is routed through the Blackbone Isle map marker.",
    ),
    "LOC-000453": ManualProxy(
        "Blackbone Isle (CC)",
        "medium",
        "Dead Man's Dread is accessed through Blackbone Isle Grotto/Blackbone Isle; no separate ship marker was found.",
    ),
    "LOC-000455": ManualProxy(
        "Fahlbtharz",
        "high",
        "Fahlbtharz Forge is treated as part of the Fahlbtharz route point.",
    ),
    "LOC-000457": ManualProxy(
        "Goldenhills Plantation (CC)",
        "high",
        "Goldenhills Farm Bunkhouse is a sublocation at Goldenhills Plantation.",
    ),
    "LOC-000458": ManualProxy(
        "The Ratway",
        "medium",
        "The Guardian Vault has no map marker and is located in the Ratway.",
    ),
    "LOC-000459": ManualProxy(
        "Giant's Tooth (CC)",
        "high",
        "Iron Tusk Cave is inside Giant's Tooth; use the island's map marker for exterior distance.",
    ),
    "LOC-000460": ManualProxy(
        "Ironback Hideout",
        "high",
        "Ironback Hideout Cellar is a sublocation at Ironback Hideout.",
    ),
    "LOC-000462": ManualProxy(
        "Kagrenzel",
        "low",
        "Nchuanthumz is north of Kagrenzel within Frostroot Cave; no Frostroot/Nchuanthumz Gamemap marker was found.",
        status="proxy_nearby_landmark",
    ),
    "LOC-000463": ManualProxy(
        "Old Attius Farm",
        "high",
        "Old Attius Farm Cellar is a sublocation at Old Attius Farm.",
    ),
    "LOC-000464": ManualProxy(
        "Falkreath Watchtower",
        "low",
        "The Pit is described as northeast of Falkreath Watchtower and lacks its own Gamemap marker.",
        status="proxy_nearby_landmark",
    ),
    "LOC-000466": ManualProxy(
        "Sightless Pit",
        "high",
        "Sightless Vault redirects to the broader Sightless Pit subject.",
    ),
}

NO_COORDINATE: dict[str, tuple[str, str]] = {
    "LOC-000193": (
        "unmapped_worldspace",
        "Skuldafn exists as a separate Gamemap worldspace and has no normal route-comparable exterior location marker.",
    ),
    "LOC-000266": (
        "unmapped_no_marker",
        "Crowstooth's Camp has no matching Gamemap marker; the UESP page gives relative directions only.",
    ),
    "LOC-000454": (
        "unmapped_worldspace",
        "Deadlands is a separate Creation worldspace with no comparable exterior Gamemap coordinate in the Skyrim route graph.",
    ),
    "LOC-000461": (
        "unmapped_no_marker",
        "UESP explicitly says Mythic Dawn Camp has no map marker even after it appears.",
    ),
}

LOCATION_SUFFIX_RE = re.compile(r"\s+\((?:place|settlement|cc|dg|hf)\)$", re.IGNORECASE)


def normalize(value: str, strip_suffix: bool = False) -> str:
    text = unquote(value or "")
    text = re.sub(r"^Skyrim:", "", text)
    text = text.replace("_", " ")
    text = text.replace("’", "'").replace("`", "'")
    if strip_suffix:
        text = LOCATION_SUFFIX_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def page_title(source_page: str) -> str:
    match = re.search(r"/wiki/Skyrim:(.*)$", source_page)
    if not match:
        return ""
    return unquote(match.group(1)).replace("_", " ")


def description_field(description: str, field: str) -> str:
    match = re.search(rf"\b{re.escape(field)}=([^,]+)", description or "")
    return match.group(1).strip() if match else ""


def z_value(location: dict) -> str:
    z = description_field(location.get("description", ""), "z")
    if z:
        return z
    return str(location.get("z") or "")


def source_url(location: dict) -> str:
    world = location["worldName"]
    x = location["x"]
    y = location["y"]
    return f"https://gamemap.uesp.net/sr/?world={quote(str(world))}&x={x}&y={y}&zoom=15"


def build_index(locations: Iterable[dict]) -> dict[str, list[dict]]:
    index: dict[str, list[dict]] = {}
    for location in locations:
        if int(location.get("visible", 0)) != 1:
            continue
        if "teleport dest" in (location.get("description") or "").lower():
            continue
        for value in (location.get("wikiPage", ""), location.get("name", "")):
            for strip_suffix in (False, True):
                key = normalize(value, strip_suffix)
                if key:
                    index.setdefault(key, []).append(location)
    return index


def unique_locations(locations: Iterable[dict]) -> list[dict]:
    seen: set[int] = set()
    result: list[dict] = []
    for location in locations:
        marker_id = int(location["id"])
        if marker_id not in seen:
            seen.add(marker_id)
            result.append(location)
    return result


def expected_world_bonus(row: dict, location: dict) -> int:
    catalog_world = row["worldspace"].strip().lower()
    world_name = location["worldName"].strip().lower()
    if catalog_world == "solstheim" and world_name == "solstheim":
        return 40
    if catalog_world == "skyrim" and world_name == "skyrim":
        return 30
    if catalog_world == "blackreach" and world_name == "skyrim":
        return 15
    if catalog_world and catalog_world == location["worldDisplayName"].strip().lower():
        return 35
    return 0


def score_candidate(row: dict, location: dict, match_method: str) -> int:
    score = 100 if match_method == "uesp_gamemap_page" else 70
    if normalize(location.get("name", ""), True) == normalize(row["location_name"], True):
        score += 35
    if normalize(location.get("wikiPage", ""), True) == normalize(page_title(row["source_page"]), True):
        score += 35
    if int(location.get("iconType") or 0) != 60:
        score += 40
    else:
        score -= 10
    categories = row.get("uesp_categories", "")
    icon_type = int(location.get("iconType") or 0)
    if "Stormcloak Camps" in categories and icon_type == 17:
        score += 50
    if "Imperial Camps" in categories and icon_type == 16:
        score += 50
    score += expected_world_bonus(row, location)
    if int(location.get("displayLevel") or 99) <= 13:
        score += 5
    return score


def lookup_candidates(row: dict, index: dict[str, list[dict]]) -> list[tuple[str, dict]]:
    candidates: list[tuple[str, dict]] = []
    for strip_suffix in (False, True):
        key = normalize(page_title(row["source_page"]), strip_suffix)
        candidates.extend(("uesp_gamemap_page", loc) for loc in index.get(key, []))
    if not candidates:
        for strip_suffix in (False, True):
            key = normalize(row["location_name"], strip_suffix)
            candidates.extend(("uesp_gamemap_name", loc) for loc in index.get(key, []))
    return [(method_from(candidates, loc), loc) for loc in unique_locations(loc for _, loc in candidates)]


def method_from(candidates: list[tuple[str, dict]], location: dict) -> str:
    for method, candidate in candidates:
        if int(candidate["id"]) == int(location["id"]):
            return method
    return "uesp_gamemap_name"


def find_by_name(name: str, index: dict[str, list[dict]]) -> dict | None:
    for strip_suffix in (False, True):
        candidates = index.get(normalize(name, strip_suffix), [])
        if candidates:
            sorted_candidates = sorted(
                unique_locations(candidates),
                key=lambda loc: (int(loc.get("iconType") or 0) == 60, str(loc.get("name", ""))),
            )
            return sorted_candidates[0]
    return None


def coordinate_row(
    sequence: int,
    row: dict,
    location: dict | None,
    *,
    status: str,
    match_method: str,
    confidence: str,
    distance_scope: str,
    notes: str,
) -> dict[str, str]:
    if location is None:
        marker_values = {
            "coordinate_worldspace": "",
            "world_id": "",
            "world_name": "",
            "map_marker_id": "",
            "map_marker_name": "",
            "map_marker_page": "",
            "map_marker_icon_type": "",
            "map_marker_editor_id": "",
            "map_marker_form_id": "",
            "map_marker_dest_form_id": "",
            "x": "",
            "y": "",
            "z": "",
            "source_url": "",
        }
    else:
        description = location.get("description", "")
        marker_values = {
            "coordinate_worldspace": str(location["worldDisplayName"]),
            "world_id": str(location["worldId"]),
            "world_name": str(location["worldName"]),
            "map_marker_id": str(location["id"]),
            "map_marker_name": str(location["name"]),
            "map_marker_page": str(location.get("wikiPage") or ""),
            "map_marker_icon_type": str(location.get("iconType") or ""),
            "map_marker_editor_id": description_field(description, "editorID"),
            "map_marker_form_id": description_field(description, "formID"),
            "map_marker_dest_form_id": description_field(description, "destFormID"),
            "x": str(location["x"]),
            "y": str(location["y"]),
            "z": z_value(location),
            "source_url": source_url(location),
        }
    return {
        "coordinate_record_id": f"COORD-{sequence:06d}",
        "location_record_id": row["location_record_id"],
        "objective_id": row["objective_id"],
        "location_name": row["location_name"],
        "location_category": row["location_category"],
        "source_content": row["source_content"],
        "catalog_worldspace": row["worldspace"],
        **marker_values,
        "coordinate_status": status,
        "match_method": match_method,
        "match_confidence": confidence,
        "distance_scope": distance_scope,
        "source_id": SOURCE_ID,
        "citations": SOURCE_NOTE,
        "notes": notes,
    }


def classify_exact_match(row: dict, candidates: list[tuple[str, dict]]) -> list[tuple[dict, str, str, str, str]]:
    scored = sorted(
        ((score_candidate(row, loc, method), method, loc) for method, loc in candidates),
        key=lambda item: (-item[0], int(item[2]["id"])),
    )
    best_score = scored[0][0]
    tied = [(method, loc) for score, method, loc in scored if score == best_score]
    if len(tied) > 1:
        return [
            (
                loc,
                "multi_marker",
                method,
                "medium",
                "Multiple equally valid Gamemap markers exist for this catalog row; choose the entrance marker that matches the route leg.",
            )
            for method, loc in tied
        ]
    method, location = tied[0]
    return [(location, "exact_marker", method, "high", "Exact UESP Gamemap marker match.")]


def build_rows() -> tuple[list[dict[str, str]], dict[str, int], list[dict[str, str]]]:
    gamemap = fetch_all("sr")
    world_by_id = {int(world["id"]): world for world in gamemap["worlds"]}
    for location in gamemap["locations"]:
        location["worldDisplayName"] = world_by_id[int(location["worldId"])]["displayName"]
        location["worldName"] = world_by_id[int(location["worldId"])]["name"]
    index = build_index(gamemap["locations"])

    with CATALOG.open(newline="", encoding="utf-8") as handle:
        catalog_rows = list(csv.DictReader(handle))

    output_rows: list[dict[str, str]] = []
    sequence = 1
    status_counts: dict[str, int] = {}
    manual_rows: list[dict[str, str]] = []

    for catalog_row in catalog_rows:
        location_id = catalog_row["location_record_id"]
        generated: list[dict[str, str]]
        if location_id in NO_COORDINATE:
            status, note = NO_COORDINATE[location_id]
            generated = [
                coordinate_row(
                    sequence,
                    catalog_row,
                    None,
                    status=status,
                    match_method="manual_unmapped",
                    confidence="none",
                    distance_scope="not_comparable",
                    notes=note,
                )
            ]
        elif location_id in MANUAL_PROXIES:
            proxy = MANUAL_PROXIES[location_id]
            marker = find_by_name(proxy.lookup_name, index)
            if marker is None:
                raise RuntimeError(f"Manual proxy marker not found: {location_id} -> {proxy.lookup_name}")
            generated = [
                coordinate_row(
                    sequence,
                    catalog_row,
                    marker,
                    status=proxy.status,
                    match_method="manual_proxy",
                    confidence=proxy.confidence,
                    distance_scope="proxy_same_worldspace_xy",
                    notes=proxy.notes,
                )
            ]
        else:
            candidates = lookup_candidates(catalog_row, index)
            if not candidates:
                raise RuntimeError(
                    f"No coordinate match or override for {location_id} {catalog_row['location_name']}"
                )
            generated = []
            for location, status, method, confidence, note in classify_exact_match(catalog_row, candidates):
                scope = "multi_marker_choose_candidate" if status == "multi_marker" else "same_worldspace_xy"
                generated.append(
                    coordinate_row(
                        sequence + len(generated),
                        catalog_row,
                        location,
                        status=status,
                        match_method=method,
                        confidence=confidence,
                        distance_scope=scope,
                        notes=note,
                    )
                )

        for generated_row in generated:
            if generated_row["coordinate_record_id"] != f"COORD-{sequence:06d}":
                generated_row["coordinate_record_id"] = f"COORD-{sequence:06d}"
            output_rows.append(generated_row)
            status_counts[generated_row["coordinate_status"]] = (
                status_counts.get(generated_row["coordinate_status"], 0) + 1
            )
            if generated_row["match_method"].startswith("manual"):
                manual_rows.append(generated_row)
            sequence += 1

    return output_rows, status_counts, manual_rows


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_reconciliation(rows: list[dict[str, str]], status_counts: dict[str, int], manual_rows: list[dict[str, str]]) -> None:
    exact_catalog_ids = {row["location_record_id"] for row in rows}
    numeric_rows = [row for row in rows if row["x"] and row["y"]]
    lines = [
        "# Location Coordinate Reconciliation",
        "",
        "Status: TB-021A complete.",
        "",
        "This file summarizes the generated coordinate support table. It is not route prose.",
        "",
        "## Generation",
        "",
        f"* Input catalog rows: {len(exact_catalog_ids)}.",
        f"* Coordinate rows: {len(rows)}.",
        f"* Rows with numeric x/y coordinates: {len(numeric_rows)}.",
        f"* Source note: `{SOURCE_NOTE}`.",
        f"* Generator: `tools/build_location_coordinates.py`.",
        "",
        "## Coordinate Status Counts",
        "",
        "| coordinate_status | Rows |",
        "| --- | ---: |",
    ]
    for status in sorted(status_counts):
        lines.append(f"| {status} | {status_counts[status]} |")

    lines.extend(
        [
            "",
            "## Distance Policy",
            "",
            "Compute straight-line distance only between rows with numeric `x` and `y` values and the same `coordinate_worldspace`.",
            "",
            "Rows marked `proxy_marker` or `proxy_nearby_landmark` are useful for coarse routing, but later route passes should validate the actual entrance or access path before treating them as precise travel endpoints.",
            "",
            "Rows marked `multi_marker` intentionally preserve multiple entrance markers for one catalog row. Use the matching entrance marker for the planned route leg instead of averaging the points.",
            "",
            "Rows marked `unmapped_no_marker` or `unmapped_worldspace` are not distance-comparable until a later plugin-data extraction or manual route validation supplies a defensible point.",
            "",
            "## Manual Proxy and Unmapped Rows",
            "",
            "| location_record_id | location_name | coordinate_status | proxy_marker | confidence | Notes |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in manual_rows:
        proxy_name = row["map_marker_name"] or "N/A"
        lines.append(
            "| {location_record_id} | {location_name} | {coordinate_status} | {proxy} | {confidence} | {notes} |".format(
                location_record_id=row["location_record_id"],
                location_name=row["location_name"].replace("|", "\\|"),
                coordinate_status=row["coordinate_status"],
                proxy=proxy_name.replace("|", "\\|"),
                confidence=row["match_confidence"],
                notes=row["notes"].replace("|", "\\|"),
            )
        )
    RECONCILIATION.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows, status_counts, manual_rows = build_rows()
    write_csv(rows)
    write_reconciliation(rows, status_counts, manual_rows)
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)} ({len(rows)} coordinate rows).")
    print(f"Wrote {RECONCILIATION.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
