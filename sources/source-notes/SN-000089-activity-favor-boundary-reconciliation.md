# Source Note: Activity and Favor Boundary Reconciliation

Status: researched; TB-031D representative targets added.

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

The same category also contains repeatable or radiant no-journal activity/favor pages. TB-010A adds representative rows for `Chop Wood`, `Gather Wheat`, `Mine Ore`, `Fight! Fight!`, `Quest all Beggars Have`, and `Quest all Drunks Have`. These rows are not exhaustive variant lists.

TB-031D chooses representative targets for route-default planning:

| Representative row | Target default | Source-backed basis |
| --- | --- | --- |
| Chop Wood | Hulda at the Bannered Mare. | TB-035 revised the default from Hod to Hulda after the geographic-route audit: `Chop Wood` lists Hulda as a Whiterun buyer, and the first Whiterun city loop can pair Hulda's firewood turn-in with crime-safe `Argonian Ale Extraction`. SN-000132 records the later source-backed route correction. |
| Gather Wheat / crop sale | Alfhild Battle-Born at Battle-Born Farm. | `Gather Wheat` lists Alfhild Battle-Born at Battle-Born Farm in Whiterun Hold as a crop buyer and says these crop-sale favors count toward hold help. |
| Mine Ore | Grogmar gro-Burzag at Redbelly Mine. | `Mine Ore` lists Grogmar at Redbelly Mine, says the activity is repeatable and counts toward hold help, and notes Redbelly Mine completion raises favor enough to make the player blood-kin to the Orcs. |
| Fight! Fight! | Uthgerd the Unbroken in Whiterun. | `Fight! Fight!` lists Uthgerd in Whiterun and records follower, marriage, Blades, and Hearthfire steward option value; the page also records brawl assault risks that need controlled execution. |
| Quest all Beggars Have | Brenuin in Whiterun. | The beggar favor page lists Brenuin in Whiterun and records Gift of Charity, disposition, repeatability, and thane-help relevance. |
| Quest all Drunks Have | Embry in Riverwood. | The drunk favor page lists Embry at Riverwood's Sleeping Giant Inn and records disposition, repeatability, and thane-help relevance, while noting this unmarked quest does not count for `Hero of the People`. |

`Inheritance`, `Revenge, Hired Thugs`, and `Steal, Thugs hunt player` are reactive events caused by NPC death, murder, or theft. The guide should not require causing arbitrary NPC deaths, murder-triggered retaliation, or theft-triggered retaliation purely for completion. TB-010A adds excluded audit rows so they remain visible without becoming required objectives.

The Activities page also links child games. `Hide and Seek (game)` states that it is for roleplaying and gives no rewards. `Tag, you're it!` describes a timed child game with no material benefit and notes a bug caveat involving Fjotra during `The Heart of Dibella`. TB-010A adds excluded audit rows for both child games so checklist mapping can revisit them later only if an external checklist explicitly tracks them.

Cutting lumber and milling remain support-only material/food-processing actions, and fishing remains covered by existing AE Fishing package, quest, item, ingredient, and species rows. They do not need additional TB-010A objective rows.

## Confidence and Open Questions

Confidence is high for category membership, the boundary decision, and the TB-031D representative target defaults. Confidence remains intentionally lower for exact action timing, counter tracking, trophy fallback treatment, and warning placement, because TB-031F and TB-032 still need to route the actual mechanics.

Open questions deferred to later tasks:

* Whether any external checklist row explicitly tracks a child game, cutting lumber, milling, inheritance, or hired-thug event despite the current exclusion/default-support policy.

## Linked Records

`data/objectives/activity-favor-reconciliation.md`; `data/objectives/objectives.csv`; `docs/task-board.md`.
