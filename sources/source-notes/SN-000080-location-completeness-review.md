# Source Note: Location Completeness Review

Status: needs review.

Source note ID: SN-000080

## Claim

The TB-008 location catalog represents the current UESP source-list inputs used for this stage: clearable places, discoverable places, and Creation Club place pages, with the known Klimmek's House secondary-marker caveat retained as an additional reconciled row.

## Routing Relevance

The specification requires all map-marked locations discovered, all clearable locations cleared where possible, and official AE Creation locations covered. This review checks whether the source-list location database is complete enough to close TB-008 before moving to skill, perk, alchemy, enchantment, and crafting-system objectives. It does not decide route order, exact clear triggers, PS4 trophy behavior, bug mitigation, or checklist mapping.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Secondary marker and duplicate marker caveats used by TB-008C and carried into this review. |
| SRC-000264 | Category:Skyrim-Places-Clearable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Clearable | 2026-05-12 | Clearable place category membership rechecked during TB-008D. |
| SRC-000265 | Category:Skyrim-Places-Discoverable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Discoverable | 2026-05-12 | Discoverable place category membership rechecked during TB-008D. |
| SRC-000266 | Category:Skyrim-Creation Club-Places | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Places | 2026-05-12 | Creation Club place category membership rechecked during TB-008D. |
| SRC-000267 | Skyrim:Klimmek's House | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Klimmek%27s_House | 2026-05-12 | Additional secondary-marker place page retained because UESP Dungeons lists it as a cleared-marker caveat. |

## Evidence Summary

The TB-008D live category audit queried the UESP MediaWiki API on 2026-05-12 and compared current category members against `data/locations/location-catalog.csv`.

| Source category | Total members | Skyrim-title members represented in catalog | Missing Skyrim-title members |
| --- | ---: | ---: | ---: |
| `Category:Skyrim-Places-Clearable` | 249 | 241 | 0 |
| `Category:Skyrim-Places-Discoverable` | 456 | 442 | 0 |
| `Category:Skyrim-Creation Club-Places` | 33 | 33 | 0 |

The union of the three current category title sets contains 466 pages, all represented in the location catalog. The catalog has 467 rows because Klimmek's House is retained as an additional secondary-marker caveat documented by the UESP Dungeons page and its own place page.

The TB-008D local crosswalk audit found 467 location objective rows, 467 location catalog rows, and no objective/catalog mismatches for objective ID, location name, location subcategory/category, or source content.

## Confidence and Open Questions

Confidence is high that the location catalog is complete for the current TB-008 source-list scope. It is not route-ready.

Open questions for later work:

* PS4 Delver and Explorer trophy behavior;
* exact per-location clear triggers and primary-location linkage;
* quest, faction, or world-state access constraints for unusual markers;
* bug, missability, and cell-entry risks;
* Survival Mode route clustering and travel preparation;
* external checklist rows that may require checklist-only location additions or explicit exclusions.

## Linked Records

`data/locations/location-catalog.csv`; `data/locations/location-completeness-review.md`; `docs/task-board.md`.
