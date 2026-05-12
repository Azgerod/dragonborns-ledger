# Location Coordinate Reconciliation

Status: TB-021A complete.

This file summarizes the generated coordinate support table. It is not route prose.

## Generation

* Input catalog rows: 467.
* Coordinate rows: 472.
* Rows with numeric x/y coordinates: 468.
* Source note: `SN-000123-location-coordinate-dataset.md`.
* Generator: `tools/build_location_coordinates.py`.

## Coordinate Status Counts

| coordinate_status | Rows |
| --- | ---: |
| exact_marker | 445 |
| multi_marker | 9 |
| proxy_marker | 12 |
| proxy_nearby_landmark | 2 |
| unmapped_no_marker | 2 |
| unmapped_worldspace | 2 |

## Distance Policy

Compute straight-line distance only between rows with numeric `x` and `y` values and the same `coordinate_worldspace`.

Rows marked `proxy_marker` or `proxy_nearby_landmark` are useful for coarse routing, but later route passes should validate the actual entrance or access path before treating them as precise travel endpoints.

Rows marked `multi_marker` intentionally preserve multiple entrance markers for one catalog row. Use the matching entrance marker for the planned route leg instead of averaging the points.

Rows marked `unmapped_no_marker` or `unmapped_worldspace` are not distance-comparable until a later plugin-data extraction or manual route validation supplies a defensible point.

## Manual Proxy and Unmapped Rows

| location_record_id | location_name | coordinate_status | proxy_marker | confidence | Notes |
| --- | --- | --- | --- | --- | --- |
| LOC-000146 | Nchuand-Zel | proxy_marker | Understone Keep | medium | UESP locates Nchuand-Zel inside Understone Keep; no separate Gamemap marker was found. |
| LOC-000193 | Skuldafn | unmapped_worldspace | N/A | none | Skuldafn exists as a separate Gamemap worldspace and has no normal route-comparable exterior location marker. |
| LOC-000266 | Crowstooth's Camp | unmapped_no_marker | N/A | none | Crowstooth's Camp has no matching Gamemap marker; the UESP page gives relative directions only. |
| LOC-000389 | Shadowfoot Sanctum | proxy_marker | Riften Docks (CC) | high | UESP names the exterior map marker for Shadowfoot Sanctum as Riften Docks. |
| LOC-000432 | Varlais Cavern | proxy_marker | Rielle (CC) | high | UESP says Varlais Cavern is not a separate location and forms part of Rielle's first zone. |
| LOC-000452 | Blackbone Isle Grotto | proxy_marker | Blackbone Isle (CC) | high | Blackbone Isle Grotto is routed through the Blackbone Isle map marker. |
| LOC-000453 | Dead Man's Dread | proxy_marker | Blackbone Isle (CC) | medium | Dead Man's Dread is accessed through Blackbone Isle Grotto/Blackbone Isle; no separate ship marker was found. |
| LOC-000454 | Deadlands | unmapped_worldspace | N/A | none | Deadlands is a separate Creation worldspace with no comparable exterior Gamemap coordinate in the Skyrim route graph. |
| LOC-000455 | Fahlbtharz Forge | proxy_marker | Fahlbtharz | high | Fahlbtharz Forge is treated as part of the Fahlbtharz route point. |
| LOC-000457 | Goldenhills Farm Bunkhouse | proxy_marker | Goldenhills Plantation (CC) | high | Goldenhills Farm Bunkhouse is a sublocation at Goldenhills Plantation. |
| LOC-000458 | The Guardian Vault | proxy_marker | The Ratway | medium | The Guardian Vault has no map marker and is located in the Ratway. |
| LOC-000459 | Iron Tusk Cave | proxy_marker | Giant's Tooth (CC) | high | Iron Tusk Cave is inside Giant's Tooth; use the island's map marker for exterior distance. |
| LOC-000460 | Ironback Hideout Cellar | proxy_marker | Ironback Hideout | high | Ironback Hideout Cellar is a sublocation at Ironback Hideout. |
| LOC-000461 | Mythic Dawn Camp | unmapped_no_marker | N/A | none | UESP explicitly says Mythic Dawn Camp has no map marker even after it appears. |
| LOC-000462 | Nchuanthumz | proxy_nearby_landmark | Kagrenzel | low | Nchuanthumz is north of Kagrenzel within Frostroot Cave; no Frostroot/Nchuanthumz Gamemap marker was found. |
| LOC-000463 | Old Attius Farm Cellar | proxy_marker | Old Attius Farm | high | Old Attius Farm Cellar is a sublocation at Old Attius Farm. |
| LOC-000464 | The Pit | proxy_nearby_landmark | Falkreath Watchtower | low | The Pit is described as northeast of Falkreath Watchtower and lacks its own Gamemap marker. |
| LOC-000466 | Sightless Vault | proxy_marker | Sightless Pit | high | Sightless Vault redirects to the broader Sightless Pit subject. |
