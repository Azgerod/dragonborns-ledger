# Source Note: City Home and Severin Manor Detail Expansion

Status: needs review.

Source note ID: SN-000074

## Claim

The property detail table now carries source-backed purchase, furnishing, upgrade, display, family-support, and safe-storage review rows for the five purchasable city homes and Severin Manor.

## Routing Relevance

City homes affect early and midgame storage, sleep access, collection displays, family/adoption support, regional routing, economy gates, and checklist synchronization. Severin Manor affects the Dragonborn/Raven Rock route as the Solstheim player home and Raven Rock Owner property reward. These details remain supporting data; the objective rows remain the routed completion units.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | City-house purchase costs, steward names, furnishing/upgrades, storage/display summary, child-bedroom tradeoffs, and overall house safe-storage framing. |
| SRC-000043 | Skyrim:Severin Manor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Severin_Manor | 2026-05-12 | Severin Manor acquisition and facility details. |

## Evidence Summary

UESP's Houses page states that Skyrim houses are places where the player may sleep and safely store items in non-respawning containers, and it summarizes the five purchasable city homes: Breezehome, Honeyside, Vlindrel Hall, Hjerim, and Proudspire Manor. Its city-house table gives each city's housecarl, purchase cost range, full upgrade cost range, display counts, storage spaces, and major crafting features.

The same page's individual city-home sections list city stewards, individual furnishing/upgrade names, costs, housecarl-quarter unlocks, and Hearthfire child-bedroom tradeoffs. The detail table preserves those as supporting rows so later route passes can choose timing, family defaults, storage bases, collection-display usage, and bug mitigations without turning the data layer into guide prose.

UESP's Houses and Severin Manor pages identify Severin Manor as the Raven Rock/Solstheim player home obtained through Served Cold, with no purchasable upgrades, no spouse/steward/adopted-child/housecarl support, and stocked crafting, storage, and display facilities.

## Confidence and Open Questions

Confidence is high for source-listed city-home and Severin Manor details. Later passes must still validate exact acquisition prerequisites, Civil War steward/Jarl state, Hjerim and Honeyside bugs, final safe-storage recommendations, child-bedroom defaults, city-home economy timing, and checklist mapping.

## Linked Records

`data/properties/property-details.csv`, `OBJ-001919` through `OBJ-001925`.
