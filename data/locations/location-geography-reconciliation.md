# Location Geography Reconciliation

Status: TB-021B complete.

This file summarizes the generated hub-and-corridor support table. It is not route prose.

## Model Review

* Kept raw `x`/`y` coordinates out of `location-geography.csv`; `location-coordinates.csv` remains the coordinate source of truth.
* Split the old generic nearest-hub idea into separate nearest corridor hub, major carriage origin, ferry terminal, inn/rest point, and candidate base fields because those answer different Survival Mode questions.
* Added `worldspace_access_model`, `transport_access_flags`, `cold_risk`, `barrier_flags`, and `geography_confidence` so later route passes can filter straight-line candidates instead of treating distance as a complete pathfinding answer.
* Kept road adjacency, exact path cost, enemy danger, weather state, and quest-state gating out of this table; those require later route-specific validation.

## Generation

* Input coordinate rows: 472.
* Comparable rows with service distances: 468.
* Not-comparable rows: 4.
* Source note: `SN-000124-hub-corridor-geography-support.md`.
* Generator: `tools/build_location_geography.py`.

## Seed Node Counts

| Node group | Rows |
| --- | ---: |
| Corridor hubs | 22 |
| Major carriage origins | 5 |
| Ferry terminals | 6 |
| Inn/rest nodes | 17 |
| Candidate bases | 18 |

## Route Cluster Counts

| Value | Rows |
| --- | ---: |
| central_skyrim | 65 |
| eastern_skyrim | 47 |
| manual_validation_required | 4 |
| northern_skyrim | 66 |
| northwest_skyrim | 87 |
| solstheim | 56 |
| southeast_skyrim | 44 |
| southern_skyrim | 64 |
| western_skyrim | 39 |

## Route Corridor Counts

| Value | Rows |
| --- | ---: |
| dawnstar_pale_coast | 19 |
| dayspring_canyon | 3 |
| dragon_bridge_haafingar_road | 23 |
| falkreath_pine_forest | 35 |
| icewater_volkihar_ferry | 15 |
| ivarstead_rift_pass | 29 |
| kynesgrove_eastmarch_road | 29 |
| manual_validation_required | 4 |
| markarth_reach | 19 |
| morthal_marsh | 29 |
| nightgate_pale_pass | 28 |
| old_hroldan_reach_road | 20 |
| raven_rock_west | 22 |
| riften_rift | 41 |
| riverwood_helgen_road | 17 |
| rorikstead_western_road | 20 |
| skaal_north | 14 |
| solitude_haafingar | 20 |
| tel_mithryn_east | 4 |
| thirsk_central | 16 |
| whiterun_central_plains | 28 |
| windhelm_eastmarch | 18 |
| winterhold_coast | 19 |

## Worldspace Access Model Counts

| Value | Rows |
| --- | ---: |
| dungeon_lift_or_interior_transition | 4 |
| ferry_gateway_then_local_overland | 56 |
| ferry_or_island_access | 6 |
| local_or_interior_subarea | 10 |
| no_marker_manual_validation | 2 |
| portal_or_quest_transition | 2 |
| same_worldspace_overland | 390 |
| separate_worldspace_not_comparable | 2 |

## Cold Risk Counts

| Value | Rows |
| --- | ---: |
| high_elevation_or_mountain | 14 |
| not_comparable | 4 |
| regional_cold | 102 |
| solstheim_cold_region | 51 |
| source_listed_cold_interior | 23 |
| standard | 278 |

## Confidence Counts

| Value | Rows |
| --- | ---: |
| high | 381 |
| low | 2 |
| medium | 85 |
| none | 4 |

## Distance Policy

Distances are straight-line UESP Gamemap coordinate distances. They are useful for clustering and nearest-service candidate selection, but not sufficient for final route steps.

Do not compare rows across `coordinate_worldspace`. Solstheim rows use Raven Rock as the ferry gateway before local overland clustering. Rows with no comparable coordinate remain manual-validation cases.

## Not-Comparable Rows

| coordinate_record_id | location_record_id | location_name | coordinate_status | worldspace_access_model | Notes |
| --- | --- | --- | --- | --- | --- |
| COORD-000197 | LOC-000193 | Skuldafn | unmapped_worldspace | separate_worldspace_not_comparable | Straight-line support data; validate roads, passes, water, quest state, and exact access before route prose. No comparable x/y coordinate is available for automated service distance. Access model: separate_worldspace_not_comparable. |
| COORD-000271 | LOC-000266 | Crowstooth's Camp | unmapped_no_marker | no_marker_manual_validation | Straight-line support data; validate roads, passes, water, quest state, and exact access before route prose. No comparable x/y coordinate is available for automated service distance. Access model: no_marker_manual_validation. |
| COORD-000459 | LOC-000454 | Deadlands | unmapped_worldspace | separate_worldspace_not_comparable | Straight-line support data; validate roads, passes, water, quest state, and exact access before route prose. No comparable x/y coordinate is available for automated service distance. Access model: separate_worldspace_not_comparable. |
| COORD-000466 | LOC-000461 | Mythic Dawn Camp | unmapped_no_marker | no_marker_manual_validation | Straight-line support data; validate roads, passes, water, quest state, and exact access before route prose. No comparable x/y coordinate is available for automated service distance. Access model: no_marker_manual_validation. |
