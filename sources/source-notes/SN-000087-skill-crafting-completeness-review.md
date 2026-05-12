# Source Note: Skill and Crafting Completeness Review

Status: needs review.

Source note ID: SN-000087

## Claim

The TB-009 skill/crafting layer is complete enough for the broader objective database review. Current support tables represent the source-listed skill trees, perk ranks, enchantment-learning effects, alchemy ingredient effects, available merchant investments, and practical crafting systems. No known finite skill/crafting aggregate remains silently unresolved, but route timing, exact recipes, source-item choices, perk allocation, work-radiant treatment, and checklist-specific recipe knowledge remain downstream work.

## Routing Relevance

The specification requires all skills to 100, all perks, non-destructive enchantment learning, all alchemy ingredient effects, available merchant investments, and practical crafting-system knowledge tracked by the chosen checklist. This note supports closing TB-009F without beginning final route construction.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Skill tree, perk count, perk point, Legendary reset, and Skill Master context. |
| SRC-000287 | Skyrim:Enchanting Effects | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting_Effects | 2026-05-12 | Enchantment-effect source list used for learnable and excluded enchantment audit rows. |
| SRC-000294 | Skyrim:Ingredients | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ingredients | 2026-05-12 | Standard, Creation Club, and quest ingredient effect tables. |
| SRC-000296 | Skyrim:Merchants | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Merchants | 2026-05-12 | Merchant investment audit source and available/bugged/unknown investment treatment. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Practical crafting-system list, activity-adjacent trophy actions, and non-crafting work/task boundary check. |
| SRC-000298 | Skyrim:Atronach Forge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Atronach_Forge | 2026-05-12 | Atronach Forge practical system support. |
| SRC-000119 | Skyrim:Staff Enchanter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_Enchanter | 2026-05-12 | Staff Enchanter practical system support. |
| SRC-000299 | Skyrim:Imbuing Chamber | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Imbuing_Chamber | 2026-05-12 | Imbuing Chamber practical system support. |

## Evidence Summary

Detailed source capture remains in SN-000081 through SN-000086. This review checks that those slices now cover the full TB-009 scope:

| Area | Current support | Review result |
| --- | --- | --- |
| Skills and perks | `skill-perk-catalog.csv`; `perk-rank-catalog.csv`; SN-000081; SN-000082 | 18 skill trees, 180 perk nodes, and 251 perk ranks are represented. |
| Enchantment learning | `enchantment-learning-catalog.csv`; SN-000083 | 54 main-route non-destructive learning rows plus five excluded audit rows are represented. |
| Alchemy effects | `alchemy-effect-catalog.csv`; SN-000084 | 190 source-listed ingredient records are represented. |
| Merchant investments | `merchant-investment-catalog.csv`; SN-000085 | 33 available investment objective rows are represented; 13 bugged and four unknown rows stay visible as audit rows. |
| Practical crafting systems | `practical-crafting-system-catalog.csv`; SN-000086 | 13 source-listed crafting systems are represented, either by existing objectives or by TB-009E system rows. |

The Activities page also lists non-crafting work/task entries such as Chop Wood, Gather Wheat, Mine Ore, Cutting Lumber, Milling, and Fishing. These do not require additional practical crafting-system objective rows in TB-009F. Chop Wood and Mine Ore are represented where needed for the Hard Worker trophy action row; Fishing already has AE package, quest, item, ingredient, and species coverage; Cutting Lumber and Milling are material or food-processing actions unless checklist mapping later treats them as explicit checklist rows. Gather Wheat and any representative work/activity radiant boundary should be handled in TB-018 rather than hidden inside the skill/crafting layer.

## Confidence and Open Questions

Confidence is high that TB-009 has no known source-list category gap for skills, perks, enchantment learning, alchemy effects, merchant investments, or practical crafting systems.

Open questions for later work:

* exact perk allocation order, training plan, and Legendary reset policy;
* source item selection for enchantment learning;
* ingredient acquisition copies and recipe sequences;
* NPC survival and practical route timing for merchant investments;
* representative work/activity radiant treatment for Chop Wood, Gather Wheat, and Mine Ore;
* recipe/output selection for Atronach Forge, Staff Enchanter, Imbuing Chamber, cooking, baking, smelting, tanning, and checklist-specific crafting knowledge;
* PS4 trophy behavior for skill and crafting-adjacent trophies.

## Linked Records

`data/skills/skill-crafting-completeness-review.md`; `data/skills/`; `data/objectives/objectives.csv`; `docs/task-board.md`.
