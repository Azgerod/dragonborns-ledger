# Activity and Favor Boundary Reconciliation

Status: TB-010A complete.

This reconciliation closes the no-journal activity/favor boundary before Phase 2 constraint research.

It does not choose exact route targets, resolve radiant boundaries, validate trophies, or create final guide instructions. Those remain downstream work.

## Boundary Rules

| Case | Treatment |
| --- | --- |
| Finite non-journal quest with a concrete location/outcome | Add or keep an objective row. It may later be routed alongside a location, unique item, word wall, or dungeon clear. |
| Repeatable/radiant no-journal activity or favor with relationship, trophy, economy, or representative-radiant value | Add one representative objective row for the type. Do not list every possible repeatable variant in Phase 1. |
| Reactive random event caused by NPC death, murder, theft, or other route-warping behavior | Add an excluded audit row if needed. Do not require triggering it for completion. |
| Roleplay-only interaction with no material reward or completion consequence | Exclude by default, with an audit row if the name could otherwise be confused with required content. |
| Material-processing action already covered by another system | Treat as support-only unless checklist mapping later proves it is externally tracked. |

## Added Objective Rows

| Objective ID | Objective | Treatment | Reason |
| --- | --- | --- | --- |
| OBJ-002756 | Coming of Age | Main-route finite non-journal quest | Concrete Ironbind Barrow encounter; not previously represented as a quest objective. |
| OBJ-002757 | Forgotten Names | Main-route finite non-journal quest | Concrete College/Midden quest; exact outcome choice remains downstream. |
| OBJ-002758 | Liar's Retreat Non-Journal Quest | Main-route finite non-journal quest | Concrete dungeon story and Longhammer synchronization; location clear alone was not explicit quest coverage. |
| OBJ-002759 | Rannveig's Fast Non-Journal Quest | Main-route finite non-journal quest | Concrete dungeon quest; location/word-wall rows alone were not explicit quest coverage. |
| OBJ-002760 | Robber's Gorge Non-Journal Quest | Main-route finite non-journal quest | Concrete dungeon/camp treasure sequence; location clear alone was not explicit quest coverage. |
| OBJ-002761 | Volskygge Non-Journal Quest | Main-route finite non-journal quest | Concrete dungeon/dragon-priest sequence; location clear and mask rows alone were not explicit quest coverage. |
| OBJ-002762 | Chop Wood Representative Activity | Representative no-journal activity radiant | Needed for activity-radiant boundary; `OBJ-002752` remains the Hard Worker trophy tracker. |
| OBJ-002763 | Gather Wheat Representative Activity | Representative no-journal activity radiant | Needed for activity-radiant boundary; exact crop/farmer selection remains downstream. |
| OBJ-002764 | Mine Ore Representative Activity | Representative no-journal activity radiant | Needed for activity-radiant boundary; `OBJ-002752` remains the Hard Worker trophy tracker. |
| OBJ-002765 | Fight! Fight! Representative Brawl | Representative no-journal brawl radiant | Keeps generic brawl type visible beyond the existing `Bloody Nose` row. |
| OBJ-002766 | Quest all Beggars Have Representative Favor | Representative no-journal favor radiant | Captures the beggar-disposition/Gift of Charity favor type without requiring every beggar variant. |
| OBJ-002767 | Quest all Drunks Have Representative Favor | Representative no-journal favor radiant | Captures the drunk-disposition favor type without requiring every drunk variant. |
| OBJ-002768 | Child Game: Hide and Seek | Excluded audit row | Roleplay/no-reward child game; not required unless a later checklist demands it. |
| OBJ-002769 | Child Game: Tag, You're It! | Excluded audit row | Roleplay/no-material-benefit child game; bug caveat is visible but the game is not required. |
| OBJ-002770 | Inheritance Random Courier Event | Excluded audit row | Reactive to NPC death; requiring it would create arbitrary NPC-death routing. |
| OBJ-002771 | Revenge, Hired Thugs Random Event | Excluded audit row | Reactive to murder; requiring it would create route-warping crime/NPC-death behavior. |
| OBJ-002772 | Steal, Thugs Hunt Player Random Event | Excluded audit row | Reactive to theft; requiring it would create route-warping crime behavior. |

## Existing Coverage Confirmed

| Source-listed no-journal page | Existing coverage | TB-010A result |
| --- | --- | --- |
| Drowned Sorrows | OBJ-000328 | Already represented as a Winterhold miscellaneous objective. |
| Falion's Secret | OBJ-000259 | Already represented as a Hjaalmarch miscellaneous objective. |
| Tolfdir the Absent-Minded | OBJ-000126 | Already represented as a College repeatable/radiant placeholder. TB-018 handles boundary. |
| Yngol's Barrow | OBJ-000347 | Already represented as a dungeon miscellaneous objective, with location, claw, and unique-item support rows. |

## Support-Only or Already-Owned Activities

| Activity | Treatment | Reason |
| --- | --- | --- |
| Cutting Lumber | Support-only for Hearthfire/log/property routing | Not a standalone completion objective unless checklist mapping later says otherwise. |
| Milling | Support-only for flour/food-processing routing | Not a standalone completion objective unless checklist mapping later says otherwise. |
| Fishing | Already owned by AE Fishing package, quest, item, ingredient, and species rows | No additional TB-010A row needed. |
| Child gifts/allowances | Support-only under adoption/relationship/default-choice work | Not a separate Phase 1 objective unless checklist mapping later says otherwise. |

## Downstream Handoff

| Task | Handoff |
| --- | --- |
| TB-010B | Include the new `OBJ-002756` through `OBJ-002772` rows in the Phase 2 research input index. |
| TB-015 | Validate Hard Worker, Hero of the People, and any PS4 trophy interactions before final routing. |
| TB-016 | Validate NPC disposition, thane-help, marriage/follower/training/investment/property implications for beggar, drunk, brawl, crop, wood, and ore targets. |
| TB-017 | Validate bugs, especially brawl crime conversion and child-game caveats. |
| TB-018 | Classify each representative no-journal activity/favor row as required, representative, finite, or excluded. |
| TB-019 | Account for Survival Mode travel, carry weight, food, cold, and rest implications when selecting exact activity/favor targets. |
| TB-030 | Reopen excluded/support-only activity decisions only if the external checklist explicitly tracks them. |

## Source Support

Primary support is in `sources/source-notes/SN-000089-activity-favor-boundary-reconciliation.md`.
