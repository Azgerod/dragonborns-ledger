# Skill and Crafting Completeness Review

Status: TB-009F complete; downstream constraint validation incorporated through TB-033, with final route-step verification still pending.

This review closes the TB-009 skill, perk, enchantment, alchemy, merchant investment, and practical crafting-system database layer before the broader objective database review in TB-010.

It does not choose perk allocation order, recipe sequences, ingredient sources, merchant route timing, grind loops, or final crafting power-curve policy.

## Reviewed Tables

| Area | Artifact | Coverage result | Remaining action |
| --- | --- | --- | --- |
| Skill trees and skill-100 objectives | `skill-perk-catalog.csv` | Complete for the 18 source-listed skill trees. | TB-027 set the block-level policy; TB-031E must choose exact training, natural leveling, Legendary reset distribution, and fallback execution. |
| Individual perk ranks | `perk-rank-catalog.csv` | Complete for 180 perk nodes and 251 perk ranks. | TB-031E/TB-033 used this table for source-selection and prototype validation; TB-034/TB-037 still verify final allocation in route order. A derived prerequisite graph is optional only if final route tooling needs it. |
| Enchantment learning | `enchantment-learning-catalog.csv` | Complete at source-list level for learnable effects, with unique-preservation and unobtainable exclusions visible. | TB-031E must select source items and checklist mapping without destroying preserved uniques. |
| Alchemy ingredient effects | `alchemy-effect-catalog.csv` | Complete at source-list level for 190 ingredient records. | TB-031E must choose acquisition copies, discovery recipes, and quest-ingredient policy. |
| Merchant investments | `merchant-investment-catalog.csv` | Complete at source-list audit level: available rows have objectives; bugged or unknown rows remain visible but unrouted. | TB-031D/TB-031E chose route timing, gold staging, and investment circuit policy; TB-034/TB-037 validate final NPC survival and replacement-merchant assumptions in route order. |
| Practical crafting systems | `practical-crafting-system-catalog.csv` | Complete for source-listed crafting systems from the Activities page. | TB-031E must choose representative recipes, outputs, and checklist-specific recipe knowledge. |

## Counts

| Check | Count |
| --- | ---: |
| Skill trees | 18 |
| Perk nodes | 180 |
| Perk ranks | 251 |
| Enchantment audit rows | 59 |
| Main-route enchantment-learning rows | 54 |
| Excluded enchantment audit rows | 5 |
| Alchemy ingredient records | 190 |
| Merchant investment audit rows | 50 |
| Available merchant investment objectives | 33 |
| Practical crafting-system rows | 13 |
| New practical crafting-system objectives | 3 |
| Crafting-adjacent trophy tracker rows | 2 |

## Boundary Decisions

The current skill/crafting layer is complete enough for TB-010. No known skill, perk, enchantment, alchemy, merchant investment, or practical crafting-system aggregate remains as a silent placeholder.

Some related activity entries are deliberately not represented as new skill/crafting-system objectives:

| Related entry | Current treatment | Follow-up |
| --- | --- | --- |
| Chop Wood | Covered for Hard Worker trophy action; work-radiant classification remains separate. | TB-018 should classify representative work/activity radiants. |
| Mine Ore | Covered for Hard Worker trophy action and mining system row; work-radiant classification remains separate. | TB-018 should classify representative work/activity radiants. |
| Gather Wheat | Not a crafting-system objective by itself. | TB-018 should classify whether work/activity radiants need representative route treatment. |
| Cutting Lumber | Hearthfire construction/material support exists in property data; not a separate finite completion objective unless checklist mapping requires it. | TB-031F should decide if a route action or checklist cue is needed. |
| Milling | Material/food-processing action only at this stage; not a separate finite completion objective unless checklist mapping requires it. | TB-031F should decide if a route action or checklist cue is needed. |
| Fishing | Already represented through AE package, quest, item, ingredient, and fishing-species data. | Fishing route mechanics remain downstream route/checklist work. |

## Downstream Dependencies

The following open questions are not TB-009F gaps:

* PS4 trophy behavior for Skill Master, Artificer, Hard Worker, and crafting-adjacent trophies was researched in TB-015 and was consumed by TB-033 prototype validation; final proof remains TB-034/TB-037 work.
* NPC survival and investment access was researched in TB-016 and remains a TB-031D/TB-031E route decision plus TB-034/TB-037 validation input.
* Work/activity radiant boundaries belong to TB-018.
* Survival Mode material, food, warmth, carry, and travel implications were researched in TB-019 and remain TB-031D/TB-031E route-decision inputs.
* Perk allocation, Legendary reset policy, ingredient/source-item selection, recipe choice, and crafting power curve were planned in TB-020/TB-027 and must be concretely selected in TB-031E.
* Checklist-specific recipe knowledge and external spreadsheet mapping belong to TB-031E/TB-031F.

## Source Support

Primary support is in `sources/source-notes/SN-000087-skill-crafting-completeness-review.md`, which cross-references SN-000081 through SN-000086 and the source-backed support tables.
