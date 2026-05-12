# Source Note: Progression Source Selection and Grind Policy

Status: researched; TB-031E source-selection policy added.

Source note ID: SN-000126

## Claim

TB-031E can resolve the progression source-selection layer without final route step numbering: skill-book copy defaults, spell-tome source defaults, enchantment-learning source families, alchemy ingredient acquisition methods, merchant investment circuit rules, representative crafting outputs, trainer blocks, Legendary reset distribution, Oghma timing, and exploit exclusions can be chosen as planning defaults while final numeric reset counts remain a TB-033 validation artifact.

## Routing Relevance

These decisions remove hidden progression assumptions before TB-031F counter mechanics, TB-032 warning placement, and final route drafting. They also resolve the TB-031E-owned source-readiness rows in the checklist coverage matrix: the raw checklist's `Damage Stamina` enchantment row maps to the existing `Stamina Damage` objective, and the raw checklist's `Kesh Fiber (AE)` alchemy rows map to source-listed `Kresh Fiber`.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000183 | Skyrim:Skill Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skill_Books | 2026-05-11 | Skill-book title and copy-location foundation. |
| SRC-000190 | Skyrim:Oghma Infinium | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Oghma_Infinium | 2026-05-11 | Oghma reward group choice, one-use behavior, above-100 limit, and bug note. |
| SRC-000287 | Skyrim:Enchanting Effects | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting_Effects | 2026-05-12 | Enchantment effects and source-item families. |
| SRC-000294 | Skyrim:Ingredients | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ingredients | 2026-05-12 | Ingredient names, effects, and source notes, including Creation Club ingredients. |
| SRC-000106 | Skyrim:Rare Curios Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Curios_Items | 2026-05-12 | Rare Curios ingredient acquisition through Khajiit caravan traders. |
| SRC-000391 | Skyrim:Trainers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trainers | 2026-05-12 | Trainer list, trainer caps, five-session limit, no-carryover rule, and exploit notes. |
| SRC-000422 | Skyrim:Leveling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveling | 2026-05-12 | Character XP, training interaction, and Legendary reset support. |
| SRC-000298 | Skyrim:Atronach Forge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Atronach_Forge | 2026-05-12 | Atronach Forge access, recipes, and material-recovery exploit note. |
| SRC-000119 | Skyrim:Staff Enchanter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_Enchanter | 2026-05-12 | Staff Enchanter access, inputs, Staff of Flames recipe row, and station bugs. |
| SRC-000299 | Skyrim:Imbuing Chamber | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Imbuing_Chamber | 2026-05-12 | Imbuing Chamber/spider scroll recipe patterns. |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival travel, carry, food, and sleep constraints. |
| SRC-000418 | Skyrim:Fatigue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fatigue | 2026-05-12 | Fatigue and potion-effect reliability constraints. |

## Evidence Summary

The raw checklist's `Damage Stamina` enchantment entry is a naming alias for the existing source-backed weapon enchantment objective `OBJ-002515`, recorded in the catalog as `Stamina Damage`. The checklist detail lists the same generic weapon source families already present in the enchantment catalog, and UESP's Enchanting Effects page associates the damage-stamina effect with those source families.

The raw checklist's `Kesh Fiber (AE)` rows are spelling aliases for source-listed `Kresh Fiber`. UESP's Ingredients and Rare Curios item pages list `Kresh Fiber`; Rare Curios acquisition is through Khajiit caravan traders. The existing catalog row `ALCHEMY-000152`/`OBJ-002678` already carries the four effects named by the checklist.

The Oghma Infinium supports one late skill-group boost choice among Combat, Magic, and Stealth, cannot raise skills above 100, is removed after use, and has a bug note that can require retrying from an older save if the full five-point gain does not apply. TB-031E therefore treats Oghma as a late gap closer with hard-save verification rather than an early progression convenience.

UESP's Trainers page supports the paid-training policy used here: five sessions per character level, no saved unused sessions, trainer caps at 90, and warnings around follower-trainer and pickpocket recovery exploits. TB-031E therefore selects trainer blocks by skill but keeps training as a smoothing tool, not as the full all-skills route.

UESP's crafting pages support the representative system outputs chosen for planning: Atronach Forge Fire Salts use an always-available recipe pattern with salt, a ruby-family item, and a soul gem; the Staff Enchanter can make Staff of Flames from an unenchanted Destruction staff, the Flames spell, and one Heart Stone after normal access; White Ridge Barrow's Imbuing Chamber supports Mind Control Spider output from an albino spider pod and soul gem. The same sources record exploit or station caveats, so TB-031E keeps material-recovery and abnormal XP behavior out of the baseline.

## Confidence and Open Questions

Confidence is high for the alias fixes, selected source-table counts, training limits, Oghma timing constraints, and representative crafting outputs because they are source-backed and do not depend on final route order.

Remaining validation is intentionally narrower:

* TB-033/TB-034 may swap a selected skill-book copy only if final route access, crime, or cell-state validation proves the selected copy unsafe.
* TB-033 must verify the final physical nonunique source item used for each learnable enchantment because vendor/random availability cannot be fabricated at this layer.
* TB-033 must produce final numeric reset counts after route order, natural skill gain, training purchases, skill-book reading, Oghma use, and crafting batches are known.
* TB-031H records source-note/readiness metadata ownership in `docs/source-objective-readiness-audit.md`; remaining progression validation belongs to TB-033/TB-034.

## Linked Records

`data/constraints/progression-source-selection.md`; `data/constraints/progression-source-selections.csv`; `data/constraints/skill-perk-leveling-plan.md`; `tools/build_progression_source_selection.py`; `tools/build_checklist_coverage.py`; `data/checklist-mapping/coverage-matrix.csv`; `docs/task-board.md`.
