# Source Note: Enchantment Learning Scope

Status: needs review.

Source note ID: SN-000083

## Claim

Skyrim's source-listed enchantment effects include 40 apparel effects and 19 weapon effects. Under this project's unique-item preservation policy, 54 effects are main-route enchantment-learning targets, four unique-only effects are excluded from main-route learning, and one source-listed effect is excluded because its source item is not obtainable in normal gameplay.

## Routing Relevance

The specification requires all enchantments learned except where learning an enchantment would destroy an irreplaceable unique item. This note supports TB-009C objective rows and `data/skills/enchantment-learning-catalog.csv` without selecting the final item source, arcane enchanter stop, or crafting power-curve timing.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000272 | Skyrim:Enchanting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting | 2026-05-12 | Arcane enchanter and disenchanting mechanics. |
| SRC-000287 | Skyrim:Enchanting Effects | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting_Effects | 2026-05-12 | Source-listed apparel and weapon effects, valid item slots, base values, and disenchant source items. |
| SRC-000288 | Skyrim:Gloves of the Pugilist | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gloves_of_the_Pugilist | 2026-05-12 | Unique source item for Fortify Unarmed. |
| SRC-000289 | Skyrim:Steel Battleaxe of Fiery Souls | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Steel_Battleaxe_of_Fiery_Souls | 2026-05-12 | Unique source item for Fiery Soul Trap. |
| SRC-000290 | Skyrim:Poacher's Axe | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Poacher%27s_Axe | 2026-05-12 | Unique source item for Huntsman's Prowess. |
| SRC-000291 | Skyrim:Notched Pickaxe | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Notched_Pickaxe | 2026-05-12 | Unique source item for Smithing Expertise. |
| SRC-000292 | Skyrim:Unobtainable Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unobtainable_Items | 2026-05-12 | Briarheart Geis source item availability. |
| SRC-000293 | Skyrim:Necromantic Grimoire Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Necromantic_Grimoire_Items | 2026-05-12 | AE Necromantic Grimoire item sources for Dark Moon and Empower Necromancy. |

## Evidence Summary

The Enchanting page explains that arcane enchanters are used to disenchant items and learn their enchantments, and that disenchanting destroys the item. It also notes that many artifacts and most unique items cannot be disenchanted at all.

The Enchanting Effects page lists the source effects captured in `data/skills/enchantment-learning-catalog.csv`:

| Effect table | Source-listed effects | Main-route learnable | Excluded for preservation | Excluded as unobtainable |
| --- | ---: | ---: | ---: | ---: |
| Apparel effects | 40 | 39 | 1 | 0 |
| Weapon effects | 19 | 15 | 3 | 1 |
| **Total** | **59** | **54** | **4** | **1** |

Excluded preservation rows:

| Enchantment | Source item | Reason |
| --- | --- | --- |
| Fortify Unarmed | Gloves of the Pugilist | Source item page categorizes the gloves as a unique item. |
| Fiery Soul Trap | Steel Battleaxe of Fiery Souls | Source item page categorizes the battleaxe as a unique item. |
| Huntsman's Prowess | Poacher's Axe | Source item page describes it as a special axe with a unique enchantment and categorizes it as a unique item. |
| Smithing Expertise | Notched Pickaxe | Source item page describes it as a special pickaxe and categorizes it as a unique item. |

Briarheart Geis is kept as an excluded audit row because the Enchanting Effects page lists it as a disenchant source effect, while the Unobtainable Items page says the Briarheart Geis weapon cannot be found in game.

Dark Moon and Empower Necromancy are treated as main-route AE Creation enchantment targets at this stage because the Enchanting Effects page lists Elite and Ascendant Necromancer hoods/robes as the source items and the Necromantic Grimoire item page documents those items as Creation content. Exact acquisition timing remains deferred.

## Confidence and Open Questions

Confidence is high for the source-listed effect inventory and for excluding the four unique-only source items under the project policy. Confidence is lower for route readiness because this pass does not choose a specific non-unique source item, vendor, loot source, dungeon source, or arcane enchanter stop for each learnable effect.

Open questions for later work:

* source item selection for each learnable enchantment;
* whether any checklist requires a separate optional destructive branch for unique-only learnable effects;
* whether AE Necromantic Grimoire source items need level, vendor, enemy, or quest-state validation before routing;
* how enchantment learning should be staged so crafting power increases gradually;
* crafting trophy interactions and PS4 validation in TB-015.

## Linked Records

`data/objectives/objectives.csv` rows `OBJ-002466` through `OBJ-002525`; `data/skills/enchantment-learning-catalog.csv`; `docs/task-board.md`.
