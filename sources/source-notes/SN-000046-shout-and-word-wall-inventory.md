# Source Note: Shout and Word Wall Inventory

Status: needs review.

Source note ID: SN-000046

## Claim

The completion scope needs source-list coverage for every official dragon shout, the word-wall or quest sources that teach those shouts, and the dragon soul unlock pool needed to unlock all shout words.

## Routing Relevance

The specification requires all dragon shouts and word walls, plus enough dragon souls to unlock all shouts. This pass records one objective row for each shout and one parent row for the dragon soul unlock pool without deciding exact dungeon order, dragon-farming route, one-way-location handling, or word-wall cleanup timing.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000165 | Skyrim:Dragon Shouts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Shouts | 2026-05-11 | Identifies the official shout list, word sources, quest-taught shouts, and the additional dragon souls needed for all unlocks. |
| SRC-000166 | Skyrim:Word Wall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Word_Wall | 2026-05-11 | Supports word-wall mechanics and source-list tracking for shout words learned from walls. |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-11 | Supports base-game shout trophy context. |
| SRC-000044 | Skyrim:Dragon Riding | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Riding | 2026-05-11 | Supports Bend Will and Dragonrider trophy context. |

## Evidence Summary

UESP identifies 27 total shouts when official add-ons are included and notes the additional dragon souls required after quest-taught words. It also distinguishes words learned from word walls from words taught through quest progression. This is enough to create source-list objective rows, but exact location ordering, dungeon clear synchronization, one-way-location checks, and bug mitigation still need later constraint validation.

## Confidence and Open Questions

Confidence is high that every shout and a dragon-soul unlock pool need objective coverage. Open questions include exact route order, word-wall location clear synchronization, any missable one-way word source, Drain Vitality duplicate-shout behavior, and how the final guide should count dragon soul acquisition without prescribing unnecessary grinding.

## Linked Records

OBJ-000760 through OBJ-000787.
