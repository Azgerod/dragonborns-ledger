# Source Note: AE Fishing Species Collectible Set

Status: needs review.

Source note ID: SN-000064

## Claim

UESP's Fishing Creation page identifies AE Fishing creatures and special creatures that should be represented as a finite fishing species/special-catch collectible set before route placement.

## Routing Relevance

The specification includes all official AE Creation Club systems, Fishing species and fishing objectives, checklist synchronization, and Survival Mode routing concerns. This pass creates species/special-catch objective rows without deciding fishing-spot route order, weather handling, quest gating, bait/restock assumptions, or final checklist mapping.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000241 | Skyrim:Fishing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing | 2026-05-12 | Fishing Creation overview, 69 fishing-spot note, creature list, special creatures, and quest context. |
| SRC-000108 | Skyrim:Fishing Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Items | 2026-05-11 | Existing Fishing item-page support for fish ingredients, food, rods, unique rewards, and related Fishing items. |

## Evidence Summary

The Fishing Creation page lists 22 regular Fishing creatures and three special creatures: Emperor Crab Guardian Spirit, Fangtusk, and Snippy. This pass adds one parent row plus 25 member rows.

Fishing quest rows already exist from the AE quest-bearing Creation pass. This pass does not duplicate those quest rows; it records the species/special-catch checklist surface that later route and checklist work must synchronize with Fishing quests, weather-sensitive catches, spot geography, and reward items.

## Confidence and Open Questions

Confidence is high for the source-list creature names. Exact catch method, weather or water-type restrictions, quest gating, special-creature handling, fishing-spot geography, bait/restock needs, and Survival Mode implications remain deferred to constraint and route passes.

## Linked Records

OBJ-001893 through OBJ-001918.
