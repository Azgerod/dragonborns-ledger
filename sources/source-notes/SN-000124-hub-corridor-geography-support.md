# Source Note: Hub and Corridor Geography Support

Status: needs review.

Source note ID: SN-000124

## Claim

The hub-and-corridor support table can use UESP Gamemap coordinates to compute nearest service candidates and broad corridor assignments, but straight-line distance must be paired with worldspace, transport, cold, and barrier flags before later route passes treat a location as practically nearby.

## Routing Relevance

Survival Mode disables ordinary fast travel and makes food, sleep, warmth, carry management, carriages, ferries, and bases route-shaping infrastructure. Later objective classification and route placement need a scalable table that says which major services and corridors are closest to each location without pretending that hold membership or raw Euclidean distance is a complete pathfinding model.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000423 | UESP Gamemap Skyrim marker endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_locs&db=sr&world=1 | 2026-05-12 | Marker x/y data used for all straight-line nearest-service calculations. |
| SRC-000424 | UESP Gamemap Skyrim world endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_worlds&db=sr | 2026-05-12 | Worldspace separation used to prevent cross-worldspace distance comparisons. |
| SRC-000420 | Skyrim:Transport | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Transport | 2026-05-12 | Carriage origins/destinations, ferry terminals, Solstheim carriage absence, Dead Man's Dread travel, and Survival fast-travel boundary. |
| SRC-000421 | Skyrim:Inns | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Inns | 2026-05-12 | Inn food/lodging locations, including the Retching Netch as Solstheim's only inn. |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival travel and infrastructure constraints. |
| SRC-000416 | Skyrim:Cold | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Cold | 2026-05-12 | Cold mechanics and source-listed cold interiors. |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | Candidate player-home/base categories and regional house context. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Hearthfire carriage and home-service context. |

## Evidence Summary

`data/locations/location-geography.csv` is generated from `data/locations/location-coordinates.csv`, which already separates UESP Gamemap coordinates by `coordinate_worldspace`. The generator therefore computes distances only within the same coordinate worldspace and leaves unmapped/no-marker rows as manual-validation cases.

The service-node model intentionally keeps separate nearest fields for corridor hub, major carriage origin, ferry terminal, inn/rest point, and candidate base. A location can be near an inn but far from a carriage origin, or near a ferry but not a useful storage base; combining those into one "nearest hub" would hide constraints that matter under Survival Mode.

The table includes `worldspace_access_model`, `transport_access_flags`, `cold_risk`, `barrier_flags`, and `geography_confidence`. These fields are derived from the coordinate status, UESP transport and inn boundaries, Survival/cold source notes, and high-level location categories. They are filters and warnings for later route placement, not final travel instructions.

## Confidence and Open Questions

Confidence is high for exact-marker straight-line nearest-service calculations inside one coordinate worldspace. Confidence is medium for multi-marker and proxy rows because the final route still needs to choose the actual entrance or access path. Confidence is low or none for no-marker and separate-worldspace exceptions until plugin-data extraction or manual validation supplies a route-comparable point.

Open questions for later route passes:

* road/path distance versus straight-line distance;
* mountain pass, water crossing, and enemy-pressure costs;
* exact timing for Hearthfire carriage services, Dead Man's Dread travel, and late dragon-riding cleanup;
* route-approved first base and long-term storage policy;
* per-location entry, clear, quest-state, and bug validations.

## Linked Records

`data/locations/location-geography.csv`; `data/locations/location-geography-reconciliation.md`; `data/locations/location-coordinates.csv`; `data/constraints/survival-mode-constraints.md`; `docs/task-board.md`; `tools/build_location_geography.py`; `tools/validate_location_geography.py`.
