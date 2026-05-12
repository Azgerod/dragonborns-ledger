# Source Note: Clearable Location Inventory

Status: needs review.

Source note ID: SN-000077

## Claim

UESP provides a clearable-place category and dungeon-clearing rules that are sufficient to seed a source-listed clearable-location catalog before per-location route validation.

## Routing Relevance

The specification requires all map-marked locations discovered and all clearable locations cleared where clearing is possible. This pass creates source-list objective rows and a location catalog for clearable places without deciding route order, exact boss or quest clear triggers, duplicate marker handling, Survival Mode geography, bug mitigation, or final trophy/checklist validation.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Dungeon clearing rules, clearable count caveats, Angarvunde/Mistwatch atypical behavior, and Delver context. |
| SRC-000264 | Category:Skyrim-Places-Clearable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Clearable | 2026-05-12 | Category description and source-listed clearable place membership. |

## Evidence Summary

The UESP Dungeons page describes clearing as a dungeon state normally produced after defeating a location boss; it also notes that Angarvunde and Mistwatch are atypical because they are marked cleared by related quest completion rather than a boss kill. The same page ties clearable places to Delver progress while warning that official add-ons can change totals.

The UESP clearable-place category describes itself as the list of clearable places in Skyrim. The TB-008A harvest queried the category through the MediaWiki API on 2026-05-12. The API returned 249 category members; eight were User-namespace pages and were excluded. The resulting first-pass catalog contains 241 Skyrim-namespace place pages. Exact place-category classification produced 219 base-game rows, four Dawnguard rows, and 18 Dragonborn rows. Of those, 219 also carried UESP's discoverable-place category during the harvest; the remaining 22 need later discoverable/map-marker reconciliation.

Because the Dungeons page text and current category membership do not present one simple final count for the AE/DLC project scope, this pass treats category membership as source-listed inventory and marks Delver count status for most rows as needing validation. Angarvunde and Mistwatch are marked with the atypical non-counting status described by UESP.

## Confidence and Open Questions

Confidence is high that the catalog reflects UESP clearable-category membership as fetched on 2026-05-12. It is not yet final route-ready location logic.

Open questions for later TB-008/TB-015/TB-017/TB-019 work:

* which source-listed rows are discoverable map markers, duplicate entrances, or secondary markers;
* exact per-location clear triggers and whether any require quest completion rather than boss death;
* Delver/Explorer trophy behavior on PS4 AE;
* location bugs, respawn quirks, and clear-state inconsistencies;
* Survival Mode timing, weather, shelter, sleep, carry, and regional clustering.

## Linked Records

OBJ-001958 through OBJ-002198; `data/locations/location-catalog.csv`.
