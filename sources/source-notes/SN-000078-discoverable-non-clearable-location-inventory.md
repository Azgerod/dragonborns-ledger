# Source Note: Discoverable Non-Clearable Location Inventory

Status: needs review.

Source note ID: SN-000078

## Claim

UESP's discoverable-place category identifies map-marker locations that should be represented for discovery/checklist coverage even when they are not source-listed as clearable places.

## Routing Relevance

The specification requires all map-marked locations discovered. TB-008A already entered source-listed clearable locations. This TB-008B pass adds discoverable rows that were not already represented by the clearable-location catalog, without deciding final route order, duplicate-marker treatment, Explorer trophy behavior, location bugs, or Survival Mode geography.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000265 | Category:Skyrim-Places-Discoverable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Discoverable | 2026-05-12 | Category description and source-listed discoverable place membership. |
| SRC-000264 | Category:Skyrim-Places-Clearable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Clearable | 2026-05-12 | Used as the subtraction set so clearable locations are not duplicated as discovery-only rows. |

## Evidence Summary

The UESP discoverable-place category describes discoverable places as separate in-game map markers that count toward the Locations Discovered statistic and Explorer achievement. The TB-008B harvest queried the category through the MediaWiki API on 2026-05-12. The API returned 456 category members; 14 were User-namespace pages and were excluded. Of the 442 Skyrim-namespace discoverable place pages, 233 were already represented by existing location catalog rows or by matching source-listed clearable names from TB-008A. This pass updated 14 existing clearable catalog rows whose discoverable status was not exposed during the first harvest. The remaining 209 pages were added as discoverable non-clearable location rows.

Exact page-category classification for the 209 added rows produced 179 base-game rows, nine Dawnguard rows, two Dragonborn rows, three Hearthfire rows, and 16 AE Creation rows.

## Confidence and Open Questions

Confidence is high that the rows reflect UESP discoverable-category membership as fetched on 2026-05-12 and that they do not intentionally duplicate current clearable-location rows. They are not final route-ready location instructions.

Open questions for later TB-008/TB-015/TB-017/TB-019 work:

* duplicate entrances, secondary markers, hidden markers, and locations whose map state is inherited from another place;
* Explorer trophy behavior on PS4 AE and whether every source-listed discoverable marker is relevant to the trophy/checklist;
* quest or faction state needed to reveal or reach specific markers;
* bug risks, missability, and any marker state affected by Civil War or AE content installation;
* Survival Mode route clustering, shelter, cold, carry, rest, and transport implications.

## Linked Records

OBJ-002199 through OBJ-002407; 14 existing clearable catalog rows updated in `data/locations/location-catalog.csv`.
