# Source Note: Quest, Trophy, and Property NPC Dependencies

Status: researched.

Source note ID: SN-000107

## Claim

Several route-critical quest, trophy, property, and reward paths depend on named NPCs staying alive, accessible, non-hostile, or in the correct quest state until the relevant objective is safely started or completed.

## Routing Relevance

TB-016 needs to promote these NPCs from generic objective notes into explicit constraint rows so later route drafts can place protection warnings, hard saves, or safe ordering before irreversible faction, Civil War, Daedric, Dragonborn, or property actions.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000388 | Skyrim:The Dainty Sload | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Dainty_Sload | 2026-05-12 | Erikur steps and Solitude Thieves Guild special-job dependency. |
| SRC-000389 | Skyrim:Essential NPCs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Essential_NPCs | 2026-05-12 | Erikur, Vittoria Vici, Ysolda, and other killability windows. |
| SRC-000368 | Skyrim:The Whispering Door | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Whispering_Door | 2026-05-12 | Ebony Blade start dependency through Hulda or Ysolda. |
| SRC-000040 | Skyrim:A New Source of Stalhrim | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_New_Source_of_Stalhrim | 2026-05-11 | Deor/Fanari dependency for stalhrim crafting unlock. |
| SRC-000379 | Skyrim:Boethiah's Calling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling | 2026-05-12 | Nonessential follower sacrifice requirement and follower-inventory risks. |
| SRC-000380 | Skyrim:The House of Horrors | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors | 2026-05-12 | Logrolf captive-state failure risk. |
| SRC-000381 | Skyrim:The Cursed Tribe | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Cursed_Tribe | 2026-05-12 | Largashbur first-visit giant attack and Orc NPC risk. |
| SRC-000374 | Skyrim:Kill Helvard | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_Helvard | 2026-05-12 | Falkreath Jarl disposition and property risk. |
| SRC-000375 | Skyrim:Lakeview Manor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lakeview_Manor | 2026-05-12 | Falkreath land purchase prerequisites and steward/Jarl handling. |
| SRC-000353 | Skyrim:Rare Gifts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Gifts | 2026-05-12 | Siddgeir letter caveat and Captain Aldis Civil War availability. |
| SRC-000373 | Skyrim:Unearthed | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unearthed | 2026-05-12 | Ralis outcome choice and follower preservation. |
| SRC-000038 | Skyrim:The Chief of Thirsk Hall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Chief_of_Thirsk_Hall | 2026-05-11 | Riekling-side Thirsk outcome and mutually exclusive NPC state. |
| SRC-000039 | Skyrim:Retaking Thirsk | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Retaking_Thirsk | 2026-05-11 | Nord-side Thirsk outcome and follow-on favor availability. |
| SRC-000370 | Skyrim:Promises to Keep | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Promises_to_Keep | 2026-05-12 | Frost ownership outcome and Louis/Sibbi/Maven interactions. |
| SRC-000363 | Skyrim:A Daedra's Best Friend | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Daedra%27s_Best_Friend | 2026-05-12 | Lod, Barbas, and Clavicus final outcome dependency. |
| SRC-000364 | Skyrim:Waking Nightmare | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Waking_Nightmare | 2026-05-12 | Erandur follower versus artifact outcome dependency. |
| SRC-000365 | Skyrim:Pieces of the Past | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pieces_of_the_Past | 2026-05-12 | Silus survival and final reward choice dependency. |
| SRC-000366 | Skyrim:The Taste of Death | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Taste_of_Death | 2026-05-12 | Eola/Verulus and Namira artifact outcome dependency. |

## Evidence Summary

UESP's `The Dainty Sload` page requires speaking to Erikur for the mission details and returning to Erikur after planting the Balmora Blue. The Essential NPCs page records Erikur as becoming killable after `Bound Until Death` on the Dark Brotherhood join path, so the route should complete the Solitude special job before advancing into any Erikur-risk window. The same page records Vittoria Vici's killability around `Bound Until Death`, so her Solitude favor row belongs before that Dark Brotherhood assassination.

Other named dependencies have direct objective consequences. `The Whispering Door` relies on the Bannered Mare rumor path through Hulda or Ysolda. `A New Source of Stalhrim` depends on Deor and Fanari surviving until the Skaal scene starts and stalhrim crafting can be unlocked. `The Cursed Tribe` begins with a Largashbur attack that can endanger Orc NPCs relevant to followers or training. `Boethiah's Calling` requires a sacrificeable nonessential follower and carries inventory/faction side effects. `The House of Horrors` fails if Logrolf is killed in the wrong captive state. The Daedric artifact rows for Barbas, Silus, Verulus/Eola, Sinding, and Erandur also need final-choice state protection until their artifact-safe or branch outcome is executed.

Property and branch rows also have NPC dependencies. `Kill Helvard` and `Lakeview Manor` sources support securing Falkreath property or thane progress before the Dark Brotherhood contract disrupts Jarl favor. `Rare Gifts` carries the Siddgeir level-letter caveat and Captain Aldis availability concern. Thirsk sources make the Riekling/Nord occupant state branch-dependent, and `Unearthed` creates a Ralis kill/spare choice that affects follower availability. `Promises to Keep` keeps Frost ownership tied to Louis, Sibbi, and Maven outcome handling.

## Confidence and Open Questions

Confidence is high that the named NPCs below need explicit constraint rows. Several exact route defaults remain unresolved by design: Thirsk side, Ralis outcome, Frost outcome, some Daedric alternate outcomes, and final spouse/steward/follower defaults belong to TB-028 or later writer-recommendation work. TB-017 still needs bug-specific mitigation for cases like Dainty Sload quest-state failure, Bards instrument bugs, adoption bugs, and Hjerim/Blood on the Ice interactions.

## Linked Records

`data/constraints/npc-dependencies.md`, OBJ-000047, OBJ-000050, OBJ-000060, OBJ-000159, OBJ-000166 through OBJ-000179, OBJ-000172, OBJ-000221, OBJ-000233, OBJ-000243, OBJ-000248, OBJ-000249, OBJ-000251, OBJ-000260, OBJ-000391, OBJ-000395, OBJ-000436, OBJ-000454 through OBJ-000459, OBJ-000465, OBJ-000476, OBJ-001919 through OBJ-001957, and OBJ-002717 through OBJ-002750.
