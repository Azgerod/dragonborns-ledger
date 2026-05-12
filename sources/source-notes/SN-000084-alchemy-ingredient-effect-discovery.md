# Source Note: Alchemy Ingredient Effect Discovery

Status: needs review.

Source note ID: SN-000084

## Claim

The source-listed alchemy ingredient effect inventory contains 190 ingredient records: 110 standard ingredient records, 74 Creation Club ingredient records, and 6 quest ingredient records. Under the project specification, each record is a main-route discovery target at this database stage, but this pass does not choose collection locations, recipe order, perk timing, or route placement.

## Routing Relevance

The specification requires all alchemy ingredient effects to be discovered. This note supports TB-009D objective rows and `data/skills/alchemy-effect-catalog.csv` by capturing ingredient/effect coverage without prematurely deciding how the final route will obtain or consume each ingredient.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000281 | Skyrim:Alchemy | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alchemy | 2026-05-12 | Alchemy lab use and ingredient-effect discovery mechanics. |
| SRC-000294 | Skyrim:Ingredients | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ingredients | 2026-05-12 | Standard, Creation Club, and quest ingredient effect tables. |
| SRC-000295 | Skyrim:Special Edition Patch | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Special_Edition_Patch | 2026-05-12 | Patch 1.6.1130 note for Aloe Vera Leaves. |
| SRC-000106 | Skyrim:Rare Curios Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Curios_Items | 2026-05-12 | Supporting AE item context for Rare Curios ingredient rows already expanded in item support data. |
| SRC-000108 | Skyrim:Fishing Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Items | 2026-05-12 | Supporting AE item context for Fishing ingredient rows already expanded in item support data. |
| SRC-000137 | Skyrim:Spell Knight Armor Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Spell_Knight_Armor_Items | 2026-05-12 | Supporting AE item context for Spell Knight Armor quest-ingredient rows already expanded in item support data. |

## Evidence Summary

The Alchemy page describes alchemy labs as the workbench for combining ingredients and explains that ingredient effects can be discovered through eating ingredients and, with the Experimenter perk, revealing additional effects when consuming an ingredient. Final recipe planning belongs to TB-020 because the route still needs to balance all-perks progression, unique/quest item handling, and crafting power growth.

The Ingredients page supplies the effect table captured in `data/skills/alchemy-effect-catalog.csv`:

| Ingredient section | Source-listed rows |
| --- | ---: |
| Standard Ingredients | 110 |
| Creation Club Ingredients | 74 |
| Quest Ingredients | 6 |
| **Total** | **190** |

Content-source classification in the catalog follows the source markers and table placement:

| Source content | Rows |
| --- | ---: |
| base_game | 98 |
| dawnguard | 5 |
| dragonborn | 11 |
| ae_creation | 76 |
| **Total** | **190** |

Two edge cases are intentionally retained:

| Ingredient | Treatment |
| --- | --- |
| Aloe Vera Leaves | Listed by UESP in Standard Ingredients, but noted as added by Special Edition Patch 1.6.1130. It is treated as `base_game` for now and flagged for later PS4 AE scope validation. |
| Nightshade | Appears twice with different form IDs: the base-game ingredient and a Creation Club variant. Both are kept as separate discovery records because the source table presents separate ingredient records, even though the effect profile matches. |

Quest ingredients are kept as main-route discovery targets at this stage because the specification requires all ingredient effects. Their exact acquisition windows, one-time consumption risks, and any branch implications are deferred to the conflict, missability, and crafting-planning passes.

## Confidence and Open Questions

Confidence is high for the source-listed effect inventory and record counts. Confidence is lower for route readiness because this pass does not choose recipes, ingredient copies, Experimenter timing, quest-ingredient handling, or Survival Mode storage and travel timing.

Open questions for later work:

* recipe or eating sequence for discovering all effects without wasting scarce ingredients;
* handling of one-time or quest-gated ingredients such as Jarrin Root and Spell Knight Armor hearts;
* PS4 AE validation for Aloe Vera Leaves after Patch 1.6.1130;
* route collection candidates and storage policy for high-volume ingredient work;
* integration with all-perks progression and a gradually increasing crafting power curve.

## Linked Records

`data/objectives/objectives.csv` rows `OBJ-002526` through `OBJ-002716`; `data/skills/alchemy-effect-catalog.csv`; `docs/task-board.md`.
