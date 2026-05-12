# Source Note: Activity and Favor Boundary Reconciliation

Status: needs review.

Source note ID: SN-000089

## Claim

The no-journal activity/favor boundary is now explicit before Phase 2. UESP's non-journal quest category identifies finite non-journal quests, repeatable radiant activity/favor quests, and reactive random events. TB-010A adds missing finite non-journal quest rows, adds representative rows for meaningful repeatable no-journal activity/favor types, and adds excluded audit rows for reactive or roleplay-only cases that should not become required route objectives.

## Routing Relevance

The guide specification requires finite miscellaneous quests and favors that are reasonably trackable, plus one representative completion of each meaningful radiant type, while excluding arbitrary repetition and purely roleplay activity. This note prevents TB-018 radiant-boundary research, TB-016 NPC-dependency research, and TB-030 checklist mapping from rediscovering the same no-journal edge cases independently.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000301 | Category:Skyrim-Quests-Non-Journal Quests | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Quests-Non-Journal_Quests | 2026-05-12 | Source-list category used to audit all non-journal quest pages. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Activity taxonomy, child games, work activities, and activity-related achievements. |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-11 | Miscellaneous objective mechanics and Hero of the People caveats. |
| SRC-000302 | Skyrim:Chop Wood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Chop_Wood | 2026-05-12 | No-journal radiant firewood activity. |
| SRC-000303 | Skyrim:Gather Wheat | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gather_Wheat | 2026-05-12 | No-journal radiant crop-sale activity. |
| SRC-000304 | Skyrim:Mine Ore | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mine_Ore | 2026-05-12 | No-journal radiant ore-sale activity and Hard Worker overlap. |
| SRC-000305 | Skyrim:Fight! Fight! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fight!_Fight! | 2026-05-12 | No-journal radiant brawl activity. |
| SRC-000306 | Skyrim:Quest all Beggars Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Beggars_Have | 2026-05-12 | Beggar favor, Gift of Charity, disposition, and thane-help relevance. |
| SRC-000307 | Skyrim:Quest all Drunks Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Drunks_Have | 2026-05-12 | Drunk favor, disposition, thane-help relevance, and non-Hero caveat. |
| SRC-000308 | Skyrim:Coming of Age | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Coming_of_Age | 2026-05-12 | Finite non-journal Ironbind Barrow quest. |
| SRC-000309 | Skyrim:Forgotten Names | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forgotten_Names | 2026-05-12 | Finite non-journal Midden gauntlet quest. |
| SRC-000310 | Skyrim:Liar's Retreat (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Liar%27s_Retreat_(quest) | 2026-05-12 | Finite non-journal Liar's Retreat quest. |
| SRC-000311 | Skyrim:Rannveig's Fast (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rannveig%27s_Fast_(quest) | 2026-05-12 | Finite non-journal Rannveig's Fast quest. |
| SRC-000312 | Skyrim:Robber's Gorge (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Robber%27s_Gorge_(quest) | 2026-05-12 | Finite non-journal Robber's Gorge quest. |
| SRC-000313 | Skyrim:Volskygge (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Volskygge_(quest) | 2026-05-12 | Finite non-journal Volskygge quest. |
| SRC-000314 | Skyrim:Tag, you're it! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tag,_you%27re_it! | 2026-05-12 | Child tag game, no material benefit, and bug caveat. |
| SRC-000315 | Skyrim:Hide and Seek (game) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hide_and_Seek_(game) | 2026-05-12 | Child hide-and-seek game, roleplay-only note, and no-reward caveat. |
| SRC-000316 | Skyrim:Inheritance | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Inheritance | 2026-05-12 | Reactive inheritance event after a friend NPC dies. |
| SRC-000317 | Skyrim:Revenge, Hired Thugs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Revenge,_Hired_Thugs | 2026-05-12 | Reactive murder-triggered hired-thug event. |
| SRC-000318 | Skyrim:Steal, Thugs hunt player | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Steal,_Thugs_hunt_player | 2026-05-12 | Reactive theft-triggered hired-thug event. |

## Evidence Summary

The UESP non-journal category listed 19 pages during this audit. Existing objective rows already represented `Drowned Sorrows`, `Falion's Secret`, `Tolfdir the Absent-Minded`, and `Yngol's Barrow`. TB-010A adds missing finite non-journal quest rows for `Coming of Age`, `Forgotten Names`, `Liar's Retreat`, `Rannveig's Fast`, `Robber's Gorge`, and `Volskygge`.

The same category also contains repeatable or radiant no-journal activity/favor pages. TB-010A adds representative rows for `Chop Wood`, `Gather Wheat`, `Mine Ore`, `Fight! Fight!`, `Quest all Beggars Have`, and `Quest all Drunks Have`. These rows are not exhaustive variant lists; TB-018 should later choose exact representative targets, classify required versus representative completion, and capture any NPC, thane, trophy, bug, or Survival Mode implications.

`Inheritance`, `Revenge, Hired Thugs`, and `Steal, Thugs hunt player` are reactive events caused by NPC death, murder, or theft. The guide should not require causing arbitrary NPC deaths, murder-triggered retaliation, or theft-triggered retaliation purely for completion. TB-010A adds excluded audit rows so they remain visible without becoming required objectives.

The Activities page also links child games. `Hide and Seek (game)` states that it is for roleplaying and gives no rewards. `Tag, you're it!` describes a timed child game with no material benefit and notes a bug caveat involving Fjotra during `The Heart of Dibella`. TB-010A adds excluded audit rows for both child games so checklist mapping can revisit them later only if an external checklist explicitly tracks them.

Cutting lumber and milling remain support-only material/food-processing actions, and fishing remains covered by existing AE Fishing package, quest, item, ingredient, and species rows. They do not need additional TB-010A objective rows.

## Confidence and Open Questions

Confidence is high for category membership and the boundary decision. Confidence is intentionally lower for exact route treatment, because TB-018, TB-016, TB-015, TB-017, TB-019, and TB-030 still need to research radiant boundaries, NPC dependencies, trophy behavior, bug risks, Survival Mode timing, and checklist mapping.

Open questions deferred to later tasks:

* Which exact NPC/location should satisfy each representative activity/favor row?
* Which brawl, beggar, drunk, wood, crop, and ore targets best serve thane, relationship, route, and Survival Mode constraints?
* Whether any external checklist row explicitly tracks a child game, cutting lumber, milling, inheritance, or hired-thug event despite the current exclusion/default-support policy.

## Linked Records

`data/objectives/activity-favor-reconciliation.md`; `data/objectives/objectives.csv`; `docs/task-board.md`.
