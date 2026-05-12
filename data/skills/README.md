# Skill and Perk Data

Status: TB-009F completeness review complete; downstream constraint planning pending.

Skill and perk support tables live here when `objectives.csv` needs one row per completion objective but the source-list detail is better reviewed in a dedicated table.

Do not use this directory for final guide prose.

## Files

* `skill-perk-catalog.template.csv` defines the shared header for skill/perk support tables.
* `skill-perk-catalog.csv` records the 18 source-listed skill trees, their specializations, perk node counts, perk-rank counts, and objective cross-references.
* `perk-rank-catalog.template.csv` defines the shared header for individual perk-rank rows.
* `perk-rank-catalog.csv` records one source-listed row per perk rank, including perk node, rank, skill requirement, prerequisite text, form ID, and parent perk-tree objective cross-reference.
* `enchantment-learning-catalog.template.csv` defines the shared header for source-listed enchantment-learning rows.
* `enchantment-learning-catalog.csv` records source-listed apparel and weapon enchantment effects, source item families, unique-preservation exclusions, and objective cross-references.
* `alchemy-effect-catalog.template.csv` defines the shared header for source-listed alchemy ingredient-effect rows.
* `alchemy-effect-catalog.csv` records source-listed standard, Creation Club, and quest ingredient effect records, edge-case notes, and objective cross-references.
* `merchant-investment-catalog.template.csv` defines the shared header for source-listed merchant investment audit rows.
* `merchant-investment-catalog.csv` records source-listed available, bugged Unofficial Patch-only, and unknown AE Creation merchant investment rows with objective cross-references for available main-route investments.
* `practical-crafting-system-catalog.template.csv` defines the shared header for practical crafting-system reconciliation rows.
* `practical-crafting-system-catalog.csv` records source-listed crafting systems, whether existing objectives already represent them, and which system-level rows TB-009E added.
* `skill-crafting-completeness-review.md` records the TB-009F closeout review and downstream boundaries before TB-010.

## Current Boundaries

The current tables record source-listed skill trees, individual perk-rank requirements, enchantment-learning scope, alchemy ingredient-effect discovery scope, available merchant investments, and practical crafting-system coverage. They do not decide perk allocation order, trainer choices, grind methods, final Legendary reset recommendations, exact enchantment source items, ingredient collection copies, recipe sequences, quest-ingredient consumption policy, merchant route order, investment gold staging, recipe/output choices, or how all-perks/crafting progression fits the Legendary difficulty power curve. Those belong in TB-020 and later route/checklist passes.

Prerequisite text in `perk-rank-catalog.csv` is deliberately source-list text, not yet normalized route logic. If TB-020 needs machine-readable prerequisite graphs, add that as a derived planning artifact rather than replacing the source transcription.

`enchantment-learning-catalog.csv` keeps unique-only and unobtainable enchantments visible as excluded audit rows. Under the current specification, main-route enchantment learning covers non-unique, replaceable, or safely disposable source items only.

`alchemy-effect-catalog.csv` keeps one record per source-listed ingredient record, not one record per ingredient copy. Duplicate display names, such as the base-game and Creation Club Nightshade records, are separated by form ID and content source. Quest-gated and patch-added edge cases are flagged for later conflict, missability, PS4 AE scope, and crafting-route validation.

`merchant-investment-catalog.csv` keeps unavailable or uncertain rows visible as audit rows instead of routing them prematurely. Rows marked `available` have main-route objective IDs; rows marked `bugged_unofficial_patch_only` or `unknown_needs_validation` deliberately do not.

`practical-crafting-system-catalog.csv` is a reconciliation table, not a recipe list. It distinguishes systems already represented by existing objectives from systems that needed new access/use rows. Exact recipe knowledge, station timing, material sourcing, and checklist-driven outputs remain downstream work.
