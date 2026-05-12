# Source Note: Practical Crafting System Reconciliation

Status: needs review.

Source note ID: SN-000086

## Claim

UESP's Activities page identifies the major Skyrim crafting activities. Most are already represented by skill/perk rows, tutorial rows, property rows, AE item-member rows, alchemy/enchantment rows, or trophy tracker rows. TB-009E adds missing source-list coverage for crafting-adjacent trophies and three distinct practical systems that were not already represented as objective rows: the Atronach Forge, Staff Enchanter access, and the Imbuing Chamber.

## Routing Relevance

The specification requires practical crafting-system unlocks and recipe/system knowledge tracked by the chosen checklist, while also requiring a gradual difficulty curve. This note supports system-level objective rows and `data/skills/practical-crafting-system-catalog.csv` without selecting recipes, crafting outputs, grind loops, or high-power gear timing.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Crafting activity list and Artificer / Hard Worker achievement summaries. |
| SRC-000298 | Skyrim:Atronach Forge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Atronach_Forge | 2026-05-12 | Atronach Forge use, recipe mechanics, Sigil Stone gating, and output categories. |
| SRC-000119 | Skyrim:Staff Enchanter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_Enchanter | 2026-05-12 | Staff Enchanter requirements, Dragonborn/AE station access notes, and craftable staff context. |
| SRC-000299 | Skyrim:Imbuing Chamber | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Imbuing_Chamber | 2026-05-12 | Imbuing Chamber and spider-crafting context. |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-11 | Trophy names, values, and achievement descriptions. |

## Evidence Summary

The Activities page lists skill-controlled crafting systems: Alchemy, Enchanting, Staff Enchanting, and Smithing. It also lists other crafting activities: Atronach Forge, Baking, Bone Forge, Construction, Cooking, Imbuing Chamber, Mining, Smelting, and Tanning. The same page lists two relevant base-game achievements: Artificer and Hard Worker.

TB-009E adds these missing objective rows:

| Added row type | Rows |
| --- | ---: |
| Crafting-adjacent trophy rows | 2 |
| Practical crafting-system rows | 3 |

The practical crafting-system catalog records whether each source-listed system is:

* already represented by existing objectives;
* newly represented by TB-009E;
* deferred to checklist mapping or later route planning because it is a common station action rather than a finite completion target.

The Atronach Forge page says recipes can create staves, spell tomes, scrolls, Daedric items, and other outputs, and notes that finding a recipe copy is not required if the player supplies the correct ingredients. This pass therefore treats Atronach Forge recipe notes as checklist-dependent recipe knowledge rather than required book/document objectives.

The Staff Enchanter page says staff enchanting does not require the Enchanting skill, but still increases it when used; it also records Dragonborn and AE station-access context. This pass adds a system-access row and leaves exact staff choices to TB-020 and checklist mapping.

The Imbuing Chamber page is used as source support for the Dragonborn spider-crafting system. This pass adds a system-access row and leaves exact spider recipe/output handling to TB-020 and checklist mapping.

## Confidence and Open Questions

Confidence is high that the broad crafting-system coverage is now visible enough for TB-009F and TB-010. Confidence is lower for final route readiness because exact recipe choices, ingredient/material sources, power-curve timing, station access, and PS4 trophy validation remain later work.

Open questions for later work:

* exact recipes or representative crafts needed for checklist synchronization;
* whether Atronach Forge recipe notes, baking recipes, spider recipes, or staff recipes appear in the external checklist;
* when to use high-power systems without flattening the Legendary difficulty curve;
* whether AE homes or Dragonborn locations provide the safest staff-enchanter access in the final route;
* PS4 trophy behavior for Artificer and Hard Worker in TB-015.

## Linked Records

`data/objectives/objectives.csv` rows `OBJ-002751` through `OBJ-002755`; `data/skills/practical-crafting-system-catalog.csv`; `data/objectives/aggregate-reconciliation.md`; `docs/task-board.md`.
