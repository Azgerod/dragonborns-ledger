# Source Note: Location Coordinate Dataset

Status: needs review.

Source note ID: SN-000123

## Claim

UESP Gamemap exposes numeric marker coordinates for Skyrim map locations. `data/locations/location-coordinates.csv` uses those marker `x` and `y` coordinates, with worldspace separation, as the first computation-ready geography layer for later hub, corridor, and nearest-service work.

## Routing Relevance

Survival Mode routing cannot treat every location in a hold as equally close to every carriage, ferry, inn, or hub. The route needs numeric points before it can choose nearest services or form corridor clusters. Coordinates are route-planning inputs only; they do not replace later road, mountain, water, cold, access-state, or portal validation.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000423 | UESP Gamemap Skyrim marker endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_locs&db=sr&world=1 | 2026-05-12 | Marker dataset fetched for every enabled Skyrim Gamemap worldspace, not only world 1. |
| SRC-000424 | UESP Gamemap Skyrim world endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_worlds&db=sr | 2026-05-12 | Worldspace IDs and names used to keep distance comparisons within one coordinate frame. |

## Evidence Summary

The Gamemap world endpoint currently lists eight enabled Skyrim map worldspaces: Skyrim, Solstheim, Day Spring Canyon, Soul Cairn, Skuldafn, Japhet's Folly, Forgotten Vale, and Apocrypha.

The marker endpoint provides location rows per worldspace. Rows include marker/world IDs, display name, wiki page, icon type, `x` and `y`, and usually form/editor/z details in the description field. `tools/build_location_coordinates.py` fetched those rows, matched them against `data/locations/location-catalog.csv`, and generated:

| Result bucket | Coordinate rows |
| --- | ---: |
| exact UESP Gamemap marker match | 445 |
| multiple valid marker rows preserved | 9 |
| manual proxy marker | 12 |
| nearby landmark proxy marker | 2 |
| no Gamemap marker | 2 |
| separate or unmapped worldspace | 2 |

There are 467 input catalog rows and 472 coordinate rows because several catalog parent rows have multiple valid entrance markers. The route must choose the entrance that matches the planned approach instead of averaging them.

Distance computations should use straight-line `sqrt((x2 - x1)^2 + (y2 - y1)^2)` only when both rows have numeric coordinates and the same `coordinate_worldspace`. Rows marked as proxy coordinates are acceptable for coarse regional planning, but route steps still need access-path validation before relying on them as precise endpoints.

## Confidence and Open Questions

Confidence is high for exact Gamemap marker rows because they come directly from UESP's map data endpoint.

Confidence is medium or low for proxy rows depending on how directly UESP ties the catalog location to the proxy marker. Proxy rows are flagged in `coordinate_status`, `match_confidence`, and `notes`.

Open questions for later geography work:

* exact road/path distance versus straight-line distance;
* cold, water, mountain, and one-way transition costs;
* portal/transport modeling for Solstheim, Blackreach lifts, Forgotten Vale, Soul Cairn, Skuldafn, Apocrypha, Deadlands, and Dead Man's Dread map travel;
* whether official plugin-data extraction can supply exact points for the remaining no-marker or low-confidence proxy cases.

## Linked Records

`data/locations/location-catalog.csv`; `data/locations/location-coordinates.csv`; `data/locations/location-coordinate-reconciliation.md`; `data/constraints/survival-mode-constraints.md`; `docs/task-board.md`; `tools/fetch_uesp_gamemap.py`; `tools/build_location_coordinates.py`; `tools/validate_location_coordinates.py`.
