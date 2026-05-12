#!/usr/bin/env python3
"""Build hub/corridor geography support from generated location coordinates."""

from __future__ import annotations

from collections import Counter
import csv
from dataclasses import dataclass
from math import hypot
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCATIONS_DIR = REPO_ROOT / "data" / "locations"
COORDINATES = LOCATIONS_DIR / "location-coordinates.csv"
CATALOG = LOCATIONS_DIR / "location-catalog.csv"
OUTPUT = LOCATIONS_DIR / "location-geography.csv"
RECONCILIATION = LOCATIONS_DIR / "location-geography-reconciliation.md"

SOURCE_NOTE = "SN-000124-hub-corridor-geography-support.md"

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


@dataclass(frozen=True)
class Node:
    name: str
    lookup_name: str
    node_type: str
    worldspace: str
    route_cluster: str
    route_corridor: str


@dataclass(frozen=True)
class ResolvedNode:
    node: Node
    x: float
    y: float


CORRIDOR_NODES = [
    Node("Whiterun", "Whiterun", "major_city", "Skyrim", "central_skyrim", "whiterun_central_plains"),
    Node("Riverwood", "Riverwood", "village", "Skyrim", "central_skyrim", "riverwood_helgen_road"),
    Node("Rorikstead", "Rorikstead", "village", "Skyrim", "central_skyrim", "rorikstead_western_road"),
    Node("Falkreath", "Falkreath", "minor_capital", "Skyrim", "southern_skyrim", "falkreath_pine_forest"),
    Node("Ivarstead", "Ivarstead", "village", "Skyrim", "southern_skyrim", "ivarstead_rift_pass"),
    Node("Riften", "Riften", "major_city", "Skyrim", "southeast_skyrim", "riften_rift"),
    Node("Fort Dawnguard", "Fort Dawnguard", "faction_hub", "Skyrim", "southeast_skyrim", "dayspring_canyon"),
    Node("Windhelm", "Windhelm", "major_city", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Kynesgrove", "Kynesgrove", "village", "Skyrim", "eastern_skyrim", "kynesgrove_eastmarch_road"),
    Node("Dawnstar", "Dawnstar", "minor_capital", "Skyrim", "northern_skyrim", "dawnstar_pale_coast"),
    Node("Nightgate Inn", "Nightgate Inn", "road_inn", "Skyrim", "northern_skyrim", "nightgate_pale_pass"),
    Node("Winterhold", "Winterhold", "minor_capital", "Skyrim", "northern_skyrim", "winterhold_coast"),
    Node("Morthal", "Morthal", "minor_capital", "Skyrim", "northwest_skyrim", "morthal_marsh"),
    Node("Solitude", "Solitude", "major_city", "Skyrim", "northwest_skyrim", "solitude_haafingar"),
    Node("Dragon Bridge", "Dragon Bridge", "village", "Skyrim", "northwest_skyrim", "dragon_bridge_haafingar_road"),
    Node("Icewater Jetty", "Icewater Jetty", "ferry_terminal", "Skyrim", "northwest_skyrim", "icewater_volkihar_ferry"),
    Node("Markarth", "Markarth", "major_city", "Skyrim", "western_skyrim", "markarth_reach"),
    Node("Old Hroldan Inn", "Old Hroldan Inn", "road_inn", "Skyrim", "western_skyrim", "old_hroldan_reach_road"),
    Node("Raven Rock", "Raven Rock", "solstheim_gateway", "Solstheim", "solstheim", "raven_rock_west"),
    Node("Skaal Village", "Skaal Village", "village", "Solstheim", "solstheim", "skaal_north"),
    Node("Tel Mithryn", "Tel Mithryn (settlement)", "settlement", "Solstheim", "solstheim", "tel_mithryn_east"),
    Node("Thirsk Mead Hall", "Thirsk Mead Hall", "settlement", "Solstheim", "solstheim", "thirsk_central"),
]

MAJOR_CARRIAGE_ORIGINS = [
    Node("Markarth Stables", "Markarth Stables", "major_carriage_origin", "Skyrim", "western_skyrim", "markarth_reach"),
    Node("Riften Stables", "Riften Stables", "major_carriage_origin", "Skyrim", "southeast_skyrim", "riften_rift"),
    Node("Solitude carriage origin", "Solitude", "major_carriage_origin", "Skyrim", "northwest_skyrim", "solitude_haafingar"),
    Node("Whiterun Stables", "Whiterun Stables", "major_carriage_origin", "Skyrim", "central_skyrim", "whiterun_central_plains"),
    Node("Windhelm Stables", "Windhelm Stables", "major_carriage_origin", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
]

FERRY_TERMINALS = [
    Node("Dawnstar ferry", "Dawnstar", "ferry_terminal", "Skyrim", "northern_skyrim", "dawnstar_pale_coast"),
    Node("Solitude ferry", "Solitude", "ferry_terminal", "Skyrim", "northwest_skyrim", "solitude_haafingar"),
    Node("Windhelm ferry", "Windhelm", "ferry_terminal", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Icewater Jetty", "Icewater Jetty", "ferry_terminal", "Skyrim", "northwest_skyrim", "icewater_volkihar_ferry"),
    Node("Castle Volkihar ferry", "Castle Volkihar", "ferry_terminal", "Skyrim", "northwest_skyrim", "icewater_volkihar_ferry"),
    Node("Raven Rock ferry", "Raven Rock", "ferry_terminal", "Solstheim", "solstheim", "raven_rock_west"),
]

INN_OR_REST_NODES = [
    Node("Braidwood Inn", "Kynesgrove", "inn", "Skyrim", "eastern_skyrim", "kynesgrove_eastmarch_road"),
    Node("Candlehearth Hall", "Windhelm", "inn", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Dead Man's Drink", "Falkreath", "inn", "Skyrim", "southern_skyrim", "falkreath_pine_forest"),
    Node("Four Shields Tavern", "Dragon Bridge", "inn", "Skyrim", "northwest_skyrim", "dragon_bridge_haafingar_road"),
    Node("The Winking Skeever", "Solitude", "inn", "Skyrim", "northwest_skyrim", "solitude_haafingar"),
    Node("Moorside Inn", "Morthal", "inn", "Skyrim", "northwest_skyrim", "morthal_marsh"),
    Node("Nightgate Inn", "Nightgate Inn", "inn", "Skyrim", "northern_skyrim", "nightgate_pale_pass"),
    Node("Windpeak Inn", "Dawnstar", "inn", "Skyrim", "northern_skyrim", "dawnstar_pale_coast"),
    Node("Silver-Blood Inn", "Markarth", "inn", "Skyrim", "western_skyrim", "markarth_reach"),
    Node("Old Hroldan Inn", "Old Hroldan Inn", "inn", "Skyrim", "western_skyrim", "old_hroldan_reach_road"),
    Node("The Bee and Barb", "Riften", "inn", "Skyrim", "southeast_skyrim", "riften_rift"),
    Node("Vilemyr Inn", "Ivarstead", "inn", "Skyrim", "southern_skyrim", "ivarstead_rift_pass"),
    Node("Frostfruit Inn", "Rorikstead", "inn", "Skyrim", "central_skyrim", "rorikstead_western_road"),
    Node("Sleeping Giant Inn", "Riverwood", "inn", "Skyrim", "central_skyrim", "riverwood_helgen_road"),
    Node("The Bannered Mare", "Whiterun", "inn", "Skyrim", "central_skyrim", "whiterun_central_plains"),
    Node("The Frozen Hearth", "Winterhold", "inn", "Skyrim", "northern_skyrim", "winterhold_coast"),
    Node("The Retching Netch", "Raven Rock", "inn", "Solstheim", "solstheim", "raven_rock_west"),
]

CANDIDATE_BASES = [
    Node("Breezehome", "Whiterun", "city_home", "Skyrim", "central_skyrim", "whiterun_central_plains"),
    Node("Tundra Homestead", "Tundra Homestead", "ae_home", "Skyrim", "central_skyrim", "whiterun_central_plains"),
    Node("Goldenhills Plantation", "Goldenhills Plantation", "ae_farm_home", "Skyrim", "central_skyrim", "rorikstead_western_road"),
    Node("Lakeview Manor", "Lakeview Manor", "hearthfire_homestead", "Skyrim", "southern_skyrim", "falkreath_pine_forest"),
    Node("Heljarchen Hall", "Heljarchen Hall", "hearthfire_homestead", "Skyrim", "northern_skyrim", "nightgate_pale_pass"),
    Node("Windstad Manor", "Windstad Manor", "hearthfire_homestead", "Skyrim", "northwest_skyrim", "morthal_marsh"),
    Node("Honeyside", "Riften", "city_home", "Skyrim", "southeast_skyrim", "riften_rift"),
    Node("Shadowfoot Sanctum", "Shadowfoot Sanctum", "ae_home", "Skyrim", "southeast_skyrim", "riften_rift"),
    Node("Vlindrel Hall", "Markarth", "city_home", "Skyrim", "western_skyrim", "markarth_reach"),
    Node("Proudspire Manor", "Solitude", "city_home", "Skyrim", "northwest_skyrim", "solitude_haafingar"),
    Node("Hjerim", "Windhelm", "city_home", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Myrwatch", "Myrwatch", "ae_home", "Skyrim", "northwest_skyrim", "morthal_marsh"),
    Node("Hendraheim", "Hendraheim", "ae_home", "Skyrim", "western_skyrim", "old_hroldan_reach_road"),
    Node("Gallows Hall", "Gallows Hall", "ae_home", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Bloodchill Manor", "Bloodchill Cavern", "ae_home", "Skyrim", "northern_skyrim", "nightgate_pale_pass"),
    Node("Nchuanthumz", "Nchuanthumz", "ae_home", "Skyrim", "eastern_skyrim", "windhelm_eastmarch"),
    Node("Dead Man's Dread", "Dead Man's Dread", "ae_home", "Skyrim", "northwest_skyrim", "icewater_volkihar_ferry"),
    Node("Severin Manor", "Raven Rock", "dragonborn_home", "Solstheim", "solstheim", "raven_rock_west"),
]

COLD_LOCATION_NAMES = {
    "Alftand",
    "Altar of Thrond",
    "Benkongerike",
    "Bleakcoast Cave",
    "Bonechill Passage",
    "Bristleback Cave",
    "Cold Rock Pass",
    "Duskglow Crevice",
    "Forsaken Cave",
    "Frossel",
    "Frostflow Lighthouse",
    "Glacial Cave",
    "Greywater Grotto",
    "Haemar's Shame",
    "Hob's Fall Cave",
    "Septimus Signus's Outpost",
    "Sightless Pit",
    "Sightless Vault",
    "Southfringe Sanctum",
    "Steepfall Burrow",
    "Stillborn Cave",
    "Yngvild",
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().lower()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def coordinate_index(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        for value in (row["location_name"], row["map_marker_name"], row["map_marker_page"]):
            key = normalize(value)
            if key and row["x"] and row["y"]:
                index.setdefault(key, []).append(row)
    return index


def resolve_nodes(nodes: list[Node], index: dict[str, list[dict[str, str]]]) -> list[ResolvedNode]:
    resolved: list[ResolvedNode] = []
    for node in nodes:
        candidates = [
            row for row in index.get(normalize(node.lookup_name), [])
            if row["coordinate_worldspace"] == node.worldspace and row["x"] and row["y"]
        ]
        if not candidates:
            raise RuntimeError(f"Could not resolve service node {node.name!r} using {node.lookup_name!r}")
        candidates.sort(key=lambda row: (row["coordinate_status"] != "exact_marker", row["coordinate_record_id"]))
        chosen = candidates[0]
        resolved.append(ResolvedNode(node=node, x=float(chosen["x"]), y=float(chosen["y"])))
    return resolved


def comparable(row: dict[str, str]) -> bool:
    return bool(row["x"] and row["y"] and row["distance_scope"] != "not_comparable")


def nearest(row: dict[str, str], nodes: list[ResolvedNode]) -> tuple[ResolvedNode | None, int | None]:
    if not comparable(row):
        return None, None
    x = float(row["x"])
    y = float(row["y"])
    candidates = [
        (round(hypot(x - node.x, y - node.y)), node)
        for node in nodes
        if node.node.worldspace == row["coordinate_worldspace"]
    ]
    if not candidates:
        return None, None
    candidates.sort(key=lambda item: (item[0], item[1].node.name))
    distance, node = candidates[0]
    return node, distance


def bucket(distance: int | None) -> str:
    if distance is None:
        return "unavailable"
    if distance <= 12000:
        return "adjacent"
    if distance <= 35000:
        return "near"
    if distance <= 70000:
        return "regional"
    return "remote"


def z_value(row: dict[str, str]) -> float | None:
    if not row["z"]:
        return None
    try:
        return float(row["z"])
    except ValueError:
        return None


def cold_risk(row: dict[str, str], catalog_row: dict[str, str]) -> str:
    if not comparable(row):
        return "not_comparable"
    name = row["location_name"]
    categories = catalog_row["uesp_categories"]
    hold = catalog_row["hold"]
    z = z_value(row)
    if name in COLD_LOCATION_NAMES or "Ice Caves" in categories:
        return "source_listed_cold_interior"
    if row["coordinate_worldspace"] == "Solstheim":
        return "solstheim_cold_region"
    if hold in {"The Pale", "Winterhold"} or (row["y"] and float(row["y"]) >= 85000):
        return "regional_cold"
    if z is not None and z >= 14000:
        return "high_elevation_or_mountain"
    return "standard"


def worldspace_access_model(row: dict[str, str], catalog_row: dict[str, str]) -> str:
    if row["coordinate_status"] == "unmapped_worldspace":
        return "separate_worldspace_not_comparable"
    if row["coordinate_status"] == "unmapped_no_marker":
        return "no_marker_manual_validation"
    categories = catalog_row["uesp_categories"]
    name = row["location_name"]
    if row["coordinate_worldspace"] == "Solstheim":
        return "ferry_gateway_then_local_overland"
    if catalog_row["worldspace"] == "Blackreach" or "Blackreach" in categories:
        return "dungeon_lift_or_interior_transition"
    if name in {"Forgotten Vale", "Darkfall Cave", "Skuldafn"}:
        return "portal_or_quest_transition"
    if name in {"Castle Volkihar", "Castle Volkihar Balcony", "Icewater Jetty", "Blackbone Isle", "Blackbone Isle Grotto", "Dead Man's Dread"}:
        return "ferry_or_island_access"
    if row["coordinate_status"].startswith("proxy"):
        return "local_or_interior_subarea"
    return "same_worldspace_overland"


def barrier_flags(row: dict[str, str], catalog_row: dict[str, str], risk: str, access_model: str) -> str:
    flags: list[str] = []
    categories = catalog_row["uesp_categories"]
    name = row["location_name"]
    if row["coordinate_status"] == "multi_marker":
        flags.append("choose_route_entrance")
    elif row["coordinate_status"].startswith("proxy"):
        flags.append("proxy_coordinate")
    elif row["coordinate_status"] == "unmapped_no_marker":
        flags.append("no_marker")
    elif row["coordinate_status"] == "unmapped_worldspace":
        flags.append("separate_worldspace")
    if access_model in {"ferry_gateway_then_local_overland", "ferry_or_island_access"}:
        flags.append("water_or_ferry_access")
    if access_model == "dungeon_lift_or_interior_transition":
        flags.append("dungeon_lift_or_interior_transition")
    if access_model == "portal_or_quest_transition":
        flags.append("quest_or_portal_transition")
    if "Passes" in categories or "Pass" in name or name in {"High Hrothgar", "Throat of the World"}:
        flags.append("mountain_or_pass")
    if risk != "standard":
        flags.append(risk)
    z = z_value(row)
    if z is not None and z >= 16000:
        flags.append("high_elevation_marker")
    if "Shipwrecks" in categories or name in {"Blackbone Isle", "Blackbone Isle Grotto", "Dead Man's Dread", "Castle Volkihar", "Castle Volkihar Balcony", "Icewater Jetty"}:
        flags.append("coastal_or_island_marker")
    if not flags:
        flags.append("none_flagged")
    return " | ".join(dict.fromkeys(flags))


def confidence(row: dict[str, str], flags: str) -> str:
    if row["distance_scope"] == "not_comparable":
        return "none"
    if row["coordinate_status"] == "proxy_nearby_landmark":
        return "low"
    if row["coordinate_status"] in {"proxy_marker", "multi_marker"}:
        return "medium"
    if any(flag in flags for flag in ("quest_or_portal_transition", "dungeon_lift_or_interior_transition", "water_or_ferry_access")):
        return "medium"
    return "high"


def transport_flags(row: dict[str, str], carriage_distance: int | None, ferry_distance: int | None) -> str:
    flags = [
        f"major_carriage_origin_{bucket(carriage_distance)}",
        f"ferry_terminal_{bucket(ferry_distance)}",
    ]
    if row["coordinate_worldspace"] == "Solstheim":
        flags.extend(["solstheim_no_carriages", "raven_rock_ferry_gateway"])
    if row["distance_scope"] == "not_comparable":
        flags.append("manual_transport_validation")
    return " | ".join(flags)


def nearest_values(row: dict[str, str], nodes: list[ResolvedNode]) -> tuple[str, str, str, str, str, str]:
    node, distance = nearest(row, nodes)
    if node is None or distance is None:
        return "", "", "", "", "", ""
    return (
        node.node.name,
        node.node.node_type,
        str(distance),
        node.node.route_cluster,
        node.node.route_corridor,
        bucket(distance),
    )


def build_rows() -> tuple[list[dict[str, str]], dict[str, Counter[str]]]:
    coordinates = read_csv(COORDINATES)
    catalog = {row["location_record_id"]: row for row in read_csv(CATALOG)}
    index = coordinate_index(coordinates)

    corridor_nodes = resolve_nodes(CORRIDOR_NODES, index)
    carriage_nodes = resolve_nodes(MAJOR_CARRIAGE_ORIGINS, index)
    ferry_nodes = resolve_nodes(FERRY_TERMINALS, index)
    inn_nodes = resolve_nodes(INN_OR_REST_NODES, index)
    base_nodes = resolve_nodes(CANDIDATE_BASES, index)

    rows: list[dict[str, str]] = []
    counts: dict[str, Counter[str]] = {
        "route_cluster": Counter(),
        "route_corridor": Counter(),
        "coordinate_worldspace": Counter(),
        "worldspace_access_model": Counter(),
        "cold_risk": Counter(),
        "geography_confidence": Counter(),
    }

    for sequence, coordinate in enumerate(coordinates, start=1):
        catalog_row = catalog[coordinate["location_record_id"]]
        hub_name, hub_type, hub_distance, cluster, corridor, _ = nearest_values(coordinate, corridor_nodes)
        carriage_name, _, carriage_distance, _, _, _ = nearest_values(coordinate, carriage_nodes)
        ferry_name, _, ferry_distance, _, _, _ = nearest_values(coordinate, ferry_nodes)
        inn_name, inn_type, inn_distance, _, _, _ = nearest_values(coordinate, inn_nodes)
        base_name, base_type, base_distance, _, _, _ = nearest_values(coordinate, base_nodes)
        risk = cold_risk(coordinate, catalog_row)
        access_model = worldspace_access_model(coordinate, catalog_row)
        flags = barrier_flags(coordinate, catalog_row, risk, access_model)
        row_confidence = confidence(coordinate, flags)

        if not cluster:
            cluster = "manual_validation_required"
        if not corridor:
            corridor = "manual_validation_required"

        row = {
            "geography_record_id": f"GEOG-{sequence:06d}",
            "coordinate_record_id": coordinate["coordinate_record_id"],
            "location_record_id": coordinate["location_record_id"],
            "objective_id": coordinate["objective_id"],
            "location_name": coordinate["location_name"],
            "location_category": coordinate["location_category"],
            "source_content": coordinate["source_content"],
            "coordinate_worldspace": coordinate["coordinate_worldspace"],
            "coordinate_status": coordinate["coordinate_status"],
            "distance_scope": coordinate["distance_scope"],
            "route_cluster": cluster,
            "route_corridor": corridor,
            "nearest_corridor_hub": hub_name,
            "nearest_corridor_hub_type": hub_type,
            "nearest_corridor_hub_distance": hub_distance,
            "nearest_major_carriage_origin": carriage_name,
            "nearest_major_carriage_origin_distance": carriage_distance,
            "nearest_ferry_terminal": ferry_name,
            "nearest_ferry_terminal_distance": ferry_distance,
            "nearest_inn_or_rest": inn_name,
            "nearest_inn_or_rest_type": inn_type,
            "nearest_inn_or_rest_distance": inn_distance,
            "nearest_candidate_base": base_name,
            "nearest_candidate_base_type": base_type,
            "nearest_candidate_base_distance": base_distance,
            "worldspace_access_model": access_model,
            "transport_access_flags": transport_flags(
                coordinate,
                int(carriage_distance) if carriage_distance else None,
                int(ferry_distance) if ferry_distance else None,
            ),
            "cold_risk": risk,
            "barrier_flags": flags,
            "geography_confidence": row_confidence,
            "citations": SOURCE_NOTE,
            "notes": geography_notes(coordinate, access_model),
        }
        rows.append(row)
        for key in counts:
            counts[key][row[key] or "blank"] += 1

    return rows, counts


def geography_notes(row: dict[str, str], access_model: str) -> str:
    notes = ["Straight-line support data; validate roads, passes, water, quest state, and exact access before route prose."]
    if row["coordinate_status"] == "multi_marker":
        notes.append("Multiple coordinate rows exist for this location; choose the entrance that matches the planned route leg.")
    elif row["coordinate_status"].startswith("proxy"):
        notes.append("Coordinate is a proxy marker, not a confirmed exact endpoint.")
    elif row["distance_scope"] == "not_comparable":
        notes.append("No comparable x/y coordinate is available for automated service distance.")
    if access_model != "same_worldspace_overland":
        notes.append(f"Access model: {access_model}.")
    return " ".join(notes)


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def table_from_counter(counter: Counter[str]) -> list[str]:
    lines = ["| Value | Rows |", "| --- | ---: |"]
    for value, count in sorted(counter.items()):
        lines.append(f"| {value} | {count} |")
    return lines


def node_summary() -> list[str]:
    groups = [
        ("Corridor hubs", CORRIDOR_NODES),
        ("Major carriage origins", MAJOR_CARRIAGE_ORIGINS),
        ("Ferry terminals", FERRY_TERMINALS),
        ("Inn/rest nodes", INN_OR_REST_NODES),
        ("Candidate bases", CANDIDATE_BASES),
    ]
    lines = ["| Node group | Rows |", "| --- | ---: |"]
    for label, nodes in groups:
        lines.append(f"| {label} | {len(nodes)} |")
    return lines


def write_reconciliation(rows: list[dict[str, str]], counts: dict[str, Counter[str]]) -> None:
    noncomparable = [row for row in rows if row["distance_scope"] == "not_comparable"]
    lines = [
        "# Location Geography Reconciliation",
        "",
        "Status: TB-021B complete.",
        "",
        "This file summarizes the generated hub-and-corridor support table. It is not route prose.",
        "",
        "## Model Review",
        "",
        "* Kept raw `x`/`y` coordinates out of `location-geography.csv`; `location-coordinates.csv` remains the coordinate source of truth.",
        "* Split the old generic nearest-hub idea into separate nearest corridor hub, major carriage origin, ferry terminal, inn/rest point, and candidate base fields because those answer different Survival Mode questions.",
        "* Added `worldspace_access_model`, `transport_access_flags`, `cold_risk`, `barrier_flags`, and `geography_confidence` so later route passes can filter straight-line candidates instead of treating distance as a complete pathfinding answer.",
        "* Kept road adjacency, exact path cost, enemy danger, weather state, and quest-state gating out of this table; those require later route-specific validation.",
        "",
        "## Generation",
        "",
        f"* Input coordinate rows: {len(rows)}.",
        f"* Comparable rows with service distances: {len([row for row in rows if row['distance_scope'] != 'not_comparable'])}.",
        f"* Not-comparable rows: {len(noncomparable)}.",
        f"* Source note: `{SOURCE_NOTE}`.",
        f"* Generator: `tools/build_location_geography.py`.",
        "",
        "## Seed Node Counts",
        "",
        *node_summary(),
        "",
        "## Route Cluster Counts",
        "",
        *table_from_counter(counts["route_cluster"]),
        "",
        "## Route Corridor Counts",
        "",
        *table_from_counter(counts["route_corridor"]),
        "",
        "## Worldspace Access Model Counts",
        "",
        *table_from_counter(counts["worldspace_access_model"]),
        "",
        "## Cold Risk Counts",
        "",
        *table_from_counter(counts["cold_risk"]),
        "",
        "## Confidence Counts",
        "",
        *table_from_counter(counts["geography_confidence"]),
        "",
        "## Distance Policy",
        "",
        "Distances are straight-line UESP Gamemap coordinate distances. They are useful for clustering and nearest-service candidate selection, but not sufficient for final route steps.",
        "",
        "Do not compare rows across `coordinate_worldspace`. Solstheim rows use Raven Rock as the ferry gateway before local overland clustering. Rows with no comparable coordinate remain manual-validation cases.",
        "",
        "## Not-Comparable Rows",
        "",
        "| coordinate_record_id | location_record_id | location_name | coordinate_status | worldspace_access_model | Notes |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in noncomparable:
        lines.append(
            "| {coordinate_record_id} | {location_record_id} | {location_name} | {coordinate_status} | {worldspace_access_model} | {notes} |".format(
                coordinate_record_id=row["coordinate_record_id"],
                location_record_id=row["location_record_id"],
                location_name=row["location_name"].replace("|", "\\|"),
                coordinate_status=row["coordinate_status"],
                worldspace_access_model=row["worldspace_access_model"],
                notes=row["notes"].replace("|", "\\|"),
            )
        )
    RECONCILIATION.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows, counts = build_rows()
    write_csv(rows)
    write_reconciliation(rows, counts)
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)} ({len(rows)} geography rows).")
    print(f"Wrote {RECONCILIATION.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
