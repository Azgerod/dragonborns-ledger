# Source Note: City Homes and Severin Manor Property Inventory

Status: needs review.

Source note ID: SN-000065

## Claim

Non-AE property coverage needs source-list rows for the five purchasable city homes and a separate Dragonborn property row for Severin Manor. Hearthfire homesteads and AE Creation homes are already represented by earlier property passes.

## Routing Relevance

The specification requires full property/home/upgrade coverage, safe-storage awareness, Survival Mode geography planning, and later checklist synchronization. These rows let later route and constraint passes choose exact acquisition timing, furnishing policy, family-home use, storage bases, and bug mitigations without turning the source-list inventory into final guide instructions.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | Lists city houses, Dragonborn houses, Hearthfire houses, Creation Club houses, purchase/award summaries, upgrade context, storage/crafting features, and housecarls. |
| SRC-000042 | Skyrim:Served Cold | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Served_Cold | 2026-05-11 | Existing quest source for the Severin Manor reward and Raven Rock Owner context. |
| SRC-000043 | Skyrim:Severin Manor | 2 - UESP | https://en.uesp.net/wiki/Dragonborn:Severin_Manor | 2026-05-11 | Existing property source for Severin Manor ownership, storage, and trophy context. |

## Evidence Summary

UESP's Houses page lists five city houses: Breezehome in Whiterun, Honeyside in Riften, Vlindrel Hall in Markarth, Hjerim in Windhelm, and Proudspire Manor in Solitude. The city-house table identifies each home's city, associated housecarl, purchase price range, upgrade/furnishing cost range, storage/display feature categories, and crafting features. The individual house sections identify the relevant city steward purchase source and furnishing/upgrade categories.

The same Houses page lists Severin Manor under Dragonborn houses and describes it as the only ownable house on Solstheim, awarded by Councilor Morvayn as a reward for `Served Cold`. It also distinguishes Severin Manor from most other homes by noting no spouse, steward, adopted-child, housecarl, or upgrade support, while still providing storage and crafting facilities.

## Confidence and Open Questions

Confidence is high for source-list property membership. TB-031D selects Breezehome as first-storage bridge, Tundra Homestead as main base, Goldenhills as farm support, and Severin Manor as Solstheim base after verification. Exact acquisition prerequisites, Civil War steward/Jarl state, gold timing, storage safety, furnishing tradeoffs, child-bedroom implementation, bug mitigations, and route timing remain deferred to property, conflict, NPC, bug, economy, and route passes.

## Linked Records

OBJ-001919 through OBJ-001925.
