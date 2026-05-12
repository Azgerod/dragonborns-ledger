# Location Reconciliation

Status: TB-008C complete; TB-008D completeness review complete; downstream route/checklist validation pending.

This file summarizes the TB-008C reconciliation pass. It is a coordination artifact, not final guide prose.

## Coverage Reconciled

| Area | Rows | Source notes | Treatment |
| --- | ---: | --- | --- |
| Secondary cleared-marker rows | 4 | `SN-000079` | Giant's Grove, Shalidor's Maze, Sundered Towers, and Klimmek's House are treated as secondary marker caveats, not independent Delver clear objectives. |
| Duplicate map-marker rows | 10 | `SN-000079` | North/South Brittleshin Pass, North/South Cold Rock Pass, North/South Shriekwind Bastion, North/South Skybound Watch, Lower Steepfall Burrow, and Reachcliff Secret Entrance are discovery markers tied to primary clearable locations. |
| AE Creation place-page gaps | 16 | `SN-000079` | Added appendix-stage content-location rows for AE place pages that were in UESP's Creation Club places category but absent from the clearable/discoverable catalog union. |
| Clearable rows without separate discoverable category membership | 7 | `SN-000079` | Retained as clearable/access objectives and marked not separately source-listed as discoverable at this stage. |

## Current Location Catalog Shape

| Location category | Rows | Meaning |
| --- | ---: | --- |
| `clearable_location` | 238 | Independent clearable/source-listed dungeon or place rows after secondary-marker reconciliation. |
| `discoverable_non_clearable` | 199 | Source-listed discoverable map markers that are not independent clearable rows and are not duplicate marker rows. |
| `map_marker_duplicate` | 10 | Source-listed duplicate map markers that count as discovery markers but inherit clear state from a primary clearable location. |
| `secondary_marker` | 4 | Places with inherited cleared-marker behavior that should not be routed as independent clear objectives. |
| `content_location` | 16 | Official AE Creation place pages needing later route/checklist validation. |

Total location catalog rows: 467.

## TB-008D Review Outcome

The TB-008D completeness review found no missing pages from the current UESP clearable, discoverable, or Creation Club place source categories. The location database now has a one-to-one crosswalk between 467 location objective rows and 467 location catalog rows.

Detailed review notes live in `data/locations/location-completeness-review.md`; the supporting source note is `SN-000080`.

## Remaining Location Review Questions

TB-008D closes the source-list completeness review. The following are intentionally left for later constraint/checklist passes:

* PS4 Delver and Explorer trophy validation;
* exact per-location clear triggers and primary-location linkage;
* bug and missability review;
* quest/faction access timing for isolated or state-dependent markers;
* Survival Mode route grouping;
* checklist-row mapping.
