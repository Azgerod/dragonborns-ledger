# Location Completeness Review

Status: TB-008D complete; TB-031G route-validation layer complete; final route placement and validation pending.

This file closes the TB-008 source-list location database pass. It is a review artifact, not final guide prose.

## Review Inputs

| Input | Source note | Review role |
| --- | --- | --- |
| Clearable place category inventory | `SN-000077` | Confirms source-listed clearable locations are represented. |
| Discoverable place category inventory | `SN-000078` | Confirms source-listed map-marker discovery locations are represented. |
| Marker and AE location-gap reconciliation | `SN-000079` | Confirms duplicate markers, secondary markers, and AE place-page gaps are explicitly classified. |
| TB-008D completeness audit | `SN-000080` | Confirms live category membership and local objective/catalog crosswalk. |
| TB-031G route validation | `SN-000128` | Confirms Delver/Explorer mechanics, duplicate/secondary marker treatment, content-location handling, no-marker exclusions, and route-use rules for coordinate exceptions. |

## Source-List Coverage Result

The TB-008D audit found no missing Skyrim-title pages from the current UESP clearable, discoverable, or Creation Club place source categories.

| Source category | Current source-listed pages represented | Missing pages |
| --- | ---: | ---: |
| UESP clearable places | 241 | 0 |
| UESP discoverable places | 442 | 0 |
| UESP Creation Club places | 33 | 0 |

The union of those category inputs is 466 pages. `Klimmek's House` is retained as a 467th catalog row because UESP's dungeon-clearing notes identify it as a secondary cleared-marker caveat.

## Catalog Shape

| Location category | Rows | TB-008D interpretation |
| --- | ---: | --- |
| `clearable_location` | 238 | Independent clearable locations for later clear-trigger, Delver, bug, and route validation. |
| `discoverable_non_clearable` | 199 | Source-listed discoverable markers that are not independent clearable rows and are not duplicate marker rows. |
| `map_marker_duplicate` | 10 | Duplicate map markers tied to primary clearable locations; these remain discovery/checklist candidates, not separate clear objectives. |
| `secondary_marker` | 4 | Inherited cleared-marker caveats that should not be routed as independent Delver clears. |
| `content_location` | 16 | AE Creation place pages resolved as parent-quest/property/content route coverage, not independent Delver rows. Final placement remains with the parent content. |
| Total | 467 | One catalog row per current location objective row. |

## Status Distinctions Confirmed

| Distinction | Current handling |
| --- | --- |
| Discovery versus clearance | `discoverable_status` and `clearable_status` are separate fields in `location-catalog.csv`; source-listed clearable rows are not assumed to be route-ready discovery instructions. |
| Non-clearable markers | `discoverable_non_clearable` rows preserve map-marker discovery coverage without adding false clear objectives. |
| Duplicate markers | Duplicate entrance markers are `map_marker_duplicate` and use `clearable_status=inherited_from_primary`. |
| Secondary markers | Secondary cleared-marker caveats are `secondary_marker` and use `delver_count_status=does_not_count`. |
| AE content locations | AE place-page gaps are `content_location` rows with parent-content route treatment. They are not independent Delver rows, and only exact-marker content rows carry independent discoverable-marker treatment. |
| Checklist-only cases | Checklist-only location rows are handled by TB-031B/TB-031G reconciliation. `The Chill*` is explicitly excluded from required official route/discovery coverage because its marker is USKP-only. |

## Local Crosswalk Checks

The TB-008D local audit confirmed:

* 467 location objectives in `data/objectives/objectives.csv`;
* 467 support rows in `data/locations/location-catalog.csv`;
* no objective/catalog mismatches for objective ID, location name, location subcategory/category, or source content;
* no remaining `needs_reconciliation` location route statuses;
* location rows still carry source-note citations rather than uncited gameplay claims.

## Deferred Work

The database is complete for source-list coverage and TB-031G route-validation mechanics, but it is not final route prose. These downstream tasks remain intentionally open:

| Deferred question | Downstream task |
| --- | --- |
| PS4 Delver and Explorer trophy behavior | Counter and location mechanics complete in TB-031F/TB-031G; final route-state validation remains TB-033. |
| Exact clear triggers, primary-location links, and inherited clear-state handling | TB-031G complete at mechanics/exception level; TB-032 places warnings and TB-034 writes final steps. |
| Bug, missability, and cell-entry risks | TB-013 and TB-017 |
| Quest, faction, and world-state access timing | TB-014 and route prototype passes |
| Survival Mode travel, cold, shelter, sleep, food, carry, and route grouping | TB-019 and route prototype passes |
| Spreadsheet checklist mapping and checklist-only exceptions | TB-031B/TB-031G complete for location rows; TB-031J later resolved all remaining checklist source-readiness rows before TB-032. |
