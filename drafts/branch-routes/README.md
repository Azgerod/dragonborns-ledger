# Branch Routes

Status: TB-033 validated after TB-029 branch prototypes, TB-031C checklist escalation decisions, TB-031J source-readiness resolutions, and the TB-032 warning overlay.

Selective alternate-branch route drafts belong here. Branch drafts should stay sharply scoped to branch-exclusive content and should not duplicate objectives intended for the canonical main route.

This file preserves the TB-028 branch decision matrix and indexes the TB-029 branch prototype outputs. The prototype files are not final guide prose; they define branch containers, objective coverage, reload points, and later handoffs.

## TB-029 Prototype Outputs

| File | Coverage |
| --- | --- |
| `major-faction-branches-v0.md` | Civil War Stormcloak, Volkihar, Destroy the Dark Brotherhood, and compact Paarthurnax/Blades prototypes. |
| `solstheim-ae-branches-v0.md` | Thirsk Riekling, Ghosts destroy-heretics, and Bittercup Power/Nothing prototypes. |
| `reward-and-trophy-branches-v0.md` | Daedric reward branches, Aetherium Forge reward branches, Master Criminal trophy branch, and main-route-resolved optional outcome notes. |

## Boundaries

| Rule | TB-028 handling |
| --- | --- |
| Branch policy | Named hard save, play alternate branch first, reload, then continue canonical main route. |
| Scope | Classify branch treatment and defaults only. Do not write step-by-step branch routes. |
| Gameplay facts | Use existing objective, conflict, trophy, NPC, radiant, bug, and route-planning tables. New facts are limited to the Bittercup reward detail added to `SN-000099`. |
| Objective CSV | TB-031C promoted settled canonical defaults out of branch handling where checklist escalation required it: Nord-side Thirsk rows, Aetherial Crown, and Ring of Hircine are main-route rows; `The Pit` is a Bittercup Power branch row. |
| Branch depth | Include branch-exclusive content only. Do not repeat main-route objectives inside a branch unless the branch-only state changes their availability or reward. |
| Checklist escalation | TB-031C applied this rule. Future promotion of an alternate outcome requires a new task-board entry or source-readiness finding that proves checklist-relevant unique items, followers, services, powers, spells, locations, or persistent states are still unrepresented. |

## Inputs

| Input | Use |
| --- | --- |
| `docs/guide-specification.md` | Branch-save policy, main continuity defaults, completion scope, and option-list boundary. |
| `docs/decisions-log.md` | Resolved defaults: Imperial, Dawnguard, Dark Brotherhood join, Paarthurnax preserved, artifact-maximizing Daedric policy where supported. |
| `data/constraints/quest-conflicts-hard-saves.md` | Primary branch and hard-save register. |
| `data/constraints/trophy-dependencies.md` | Trophy-safe setup, Civil War/War Hero, Dawnguard, Oblivion Walker, Master Criminal, and counter risks. |
| `data/constraints/radiant-boundaries.md` | Branch-only Volkihar radiants and conversion-depth boundary. |
| `data/constraints/npc-dependencies.md` | NPC/follower/service consequences for Thirsk, Ralis, Frost, Daedric choices, and option lists. |
| `data/constraints/bug-prone-quests.md` | Branch execution warnings, especially Thirsk, Unearthed, family/service, and trophy branch saves. |
| `data/route-planning/objective-route-index.csv` | Current branch, option-list, and candidate-support counts. |
| `data/route-planning/prototype-objective-block-map.csv` | TB-026 per-objective dispositions and current branch deferrals. |
| `drafts/route-prototypes/main-route-prototype-v0.md` | Route-block frame `G00` through `G14` and branch-deferred handoffs. |

## Data Snapshot

| Slice | Rows | TB-028 interpretation |
| --- | ---: | --- |
| `branch_route` objectives | 43 | Alternate faction routes, branch-only radiants/rewards, mutually exclusive item outcomes, Master Criminal trophy branch, and TB-031F/TB-031J branch-source-readiness promotions after TB-031C canonical-default promotions. |
| `option_list` objectives | 11 | Household, spouse, child, steward, follower, pet, mount, and similar defaults. |
| `branch_only` objectives | 39 | Rows that should not enter the canonical main route unless a later reclassification explicitly promotes a chosen default. |
| `windowed` branch reward rows | 3 | Remaining Aetherial and Hircine alternate reward rows held for branch handling. |
| `held_branch_deferred` map rows | 43 | Expected generated status for branch-only or branch-default rows after TB-031C, TB-031F, and TB-031J promotions. |
| `held_option_list` map rows | 11 | Expected TB-026 status for option-list rows before default recommendation and checklist mapping. |

## TB-031C Escalation Results

| Area | Decision |
| --- | --- |
| Representative radiants | Do not escalate checklist variants into all-target coverage. Keep representative-type coverage; TB-031F chooses exact route actions. |
| Thieves Guild 125 jobs | Required completionist counter coverage through `OBJ-000048`; TB-031F handles job mix and counter mechanics. |
| Volkihar radiants and `New Allegiances` | Keep one representative branch instance and one successful `New Allegiances` conversion; no all-target escalation from checklist evidence. |
| `The Gift` | Branch-only and spouse-state conditional; TB-031D recommends the Ysolda spouse default, and TB-032 marks the `HS-DG-BLOODLINE` branch save as needing spouse-state verification or a conditional label. |
| Thirsk | Nord side and Nord-side favors are canonical main-route rows; Riekling side remains BR-006. |
| Bittercup | Fortune remains canonical; `The Pit` is BR-008A Power branch; Nothing/Rulnik remains compact branch/option coverage. |
| Daedric/Aetherial rewards | Ring of Hircine and Aetherial Crown are canonical main-route rows; alternate rewards remain compact reward branches. |
| Velehk/Frost/Ralis/Battle of the Champions | No new full branch. Keep current main defaults; TB-033 found no checklist-driven reason to promote them. Battle of the Champions equipment coverage remains a step-level TB-034/TB-037 check. |
| Option-list defaults | No checklist-driven branch escalation for personal/default choices; TB-031D chooses route defaults and TB-035 presents options. |

## Decision Vocabulary

| Treatment | Meaning |
| --- | --- |
| Full branch route | TB-029 should draft a branch prototype with branch-exclusive objectives and reload instruction. |
| Compact branch route | TB-029 should draft a short branch prototype for a substantial but narrow alternate state. |
| Reward branch | TB-029 should draft a compact save/reward branch at a single outcome point. |
| Trophy branch | Route a controlled trophy action on a hard save, then reload to preserve the clean final continuity. |
| Option list | No full branch. Later route/default pass recommends one choice and lists notable alternatives. |
| Main-route resolved | Main continuity choice is settled; no branch prototype unless checklist mapping later escalates it. |
| Appendix/audit only | Keep as a documented alternate or excluded/unsupported note, not route content. |

## Branch Decision Matrix

| ID | Decision point | Canonical main continuity | Treatment | Hard save | TB-029 branch-exclusive scope | Source support | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BR-001 | Civil War faction commitment | Imperial. | Full branch route. | `HS-CW-BEFORE-FACTION-OATH` | Stormcloak-only sequence `OBJ-000087` through `OBJ-000101`; protect War Hero logic and Solitude/Captain Aldis warnings. | `SN-000097`, `SN-000100`, `SN-000102` | Do not duplicate Imperial objectives. The Stormcloak branch should be played first from the oath save, then reload for Imperial. |
| BR-002 | Dawnguard versus Volkihar at `Bloodline` | Dawnguard; refuse Harkon's gift. | Full branch route. | `HS-DG-BLOODLINE` | Volkihar quest/radiant/reward rows `OBJ-000356`, `OBJ-000357`, `OBJ-000374` through `OBJ-000383`, plus branch-only amulets/rings. | `SN-000097`, `SN-000105`, `SN-000114` | `New Allegiances` baseline is one successful conversion. TB-031C found no checklist evidence requiring all three named conversions. |
| BR-003 | Dark Brotherhood join versus destroy | Join the Dark Brotherhood. | Full branch route. | `HS-DB-ABANDONED-SHACK` | `Destroy the Dark Brotherhood!` branch-exclusive outcome and unavailable join-route comparison; reload before join route. | `SN-000097`, `SN-000100`, `SN-000102` | Complete or intentionally skip `Delayed Burial` before either commitment according to the main route. |
| BR-004 | Paarthurnax / Blades conflict | Preserve Paarthurnax. | Compact branch route. | `HS-MQ-PAARTHURNAX` | Kill-Paarthurnax outcome and Blades support state only; reload to preserve Greybeards support. | `SN-000097` | Do not move main-route shout/word-wall support into the branch unless it is Blades-exclusive. |
| BR-005 | Master Criminal trophy | Clean final continuity, no permanent all-holds bounty state. | Trophy branch. | `HS-TROPHY-MASTER-CRIMINAL` | TB-029 drafts a compact trophy branch: controlled 1000-gold bounty in all nine holds, trophy verification, then reload. | `SN-000103` | This is not mutually exclusive story content, but it is branch-routed because the final-state disruption is large. TB-032 now records warning/action limits; TB-034 places final step locations. |
| BR-006 | Thirsk Mead Hall control | Retaking Thirsk / Nord side. | Full branch route. | `HS-DRAGONBORN-THIRSK-CHOICE` | Riekling-side `The Chief of Thirsk Hall`, Riekling occupant/follower state, and Riekling-only post-state checks. | `SN-000034`, `SN-000099`, `SN-000107`, `SN-000111` | TB-031C promoted Nord-side Thirsk rows to main-route handling because the canonical default preserves the source-listed Thirsk favor/service/spouse-candidate surface around Halbarn, Hilund, and Elmus. |
| BR-007 | Ghosts of the Tribunal heretics | Join/infiltrate heretic path. | Full branch route. | `HS-AE-GHOSTS-TEMPLE` | Destroy-heretics outcome and alternate Temple state, including TB-031J branch coverage for `Reclamation Priest's Journal (AE)`. | `SN-000099`, `SN-000129` | Main default preserves armory access, crafting permissions, followers, companion tasks, and Skullcrusher access. |
| BR-008 | Bittercup altar path | Fortune path. | Two compact alternate branches. | `HS-AE-BITTERCUP-ALTAR` | From the altar save, route Power -> `The Pit`, Grand Champion's Sword, and Grand Champion's Helm; then Nothing -> Rulnik, Rulnik's Dagger, and Ironwood Soup support. Reload after each branch and continue Fortune on the main save. | `SN-000099` | TB-031C made `The Pit` branch-only in the objective map. Fortune remains the main default because the sourced reward table makes Master Transmute path-specific, and spell/permanent-spell coverage is main-route scope. |
| BR-009 | `The Black Star` reward | The Black Star. | Reward branch. | `HS-DAEDRIC-BLACK-STAR` | Azura's Star and Aranea outcome only. | `SN-000098`, `SN-000104` | Both star outcomes are qualifying artifacts. The Black Star remains the utility default; Azura's Star is branch-exclusive. |
| BR-010 | `A Daedra's Best Friend` reward | Masque of Clavicus Vile. | Reward branch. | `HS-DAEDRIC-CLAVICUS` | Rueful Axe outcome only. | `SN-000098`, `SN-000104`, `SN-000107` | Main route must not use Rueful Axe for Oblivion Walker. |
| BR-011 | `Ill Met By Moonlight` outcome | Ring of Hircine single-artifact outcome. | Reward branch plus appendix-only exploit note. | `HS-DAEDRIC-HIRCINE-GROTTO` | Savior's Hide single-artifact outcome. Document dual-artifact route only as appendix/audit, not baseline. | `SN-000095`, `SN-000098`, `SN-000104`, `SN-000107` | TB-031C promoted Ring of Hircine to main-route handling. Do not rely on the dual-artifact outcome for Oblivion Walker. Preserve Bolar's Oathblade and the non-quest grotto clear state before the quest if the route keeps Sinding alive on the main save. |
| BR-012 | `Pieces of the Past` final choice | Kill Silus and reforge Mehrunes' Razor. | Reward branch. | `HS-DAEDRIC-MEHRUNES-SHRINE` | Spare-Silus gold/non-artifact outcome only. | `SN-000098`, `SN-000104`, `SN-000107` | Main route is artifact-safe. |
| BR-013 | `The Taste of Death` final outcome | Namira feast outcome and Ring of Namira. | Reward branch. | `HS-DAEDRIC-NAMIRA-FEAST` | Save Verulus / kill Eola alternate outcome only. | `SN-000098`, `SN-000104`, `SN-000107` | Main route is artifact-safe. |
| BR-014 | `Waking Nightmare` final choice | Kill Erandur and take Skull of Corruption. | Reward branch. | `HS-DAEDRIC-VAERMINA-SKULL` | Spare Erandur follower outcome only. | `SN-000098`, `SN-000104`, `SN-000107` | Main route is artifact-safe; Erandur follower access is branch-only. |
| BR-015 | `Lost to the Ages` Aetherial reward | Aetherial Crown. | Reward branch. | `HS-DG-AETHERIUM-FORGE` | Aetherial Staff and Aetherial Shield forge outcomes. | `SN-000099`, `SN-000105` | TB-031C promoted Aetherial Crown to main-route handling. Trophy only requires quest completion, but unique reward branches are substantial enough to route from the forge save. |
| BR-016 | `Forgotten Names` / Velehk Sain | Release Velehk for hidden treasure map/reward path. | Main-route resolved with optional outcome note. | `HS-COLLEGE-VELEHK-SAIN` | No full branch; TB-031C found no checklist evidence requiring kill-outcome corpse loot. | `SN-000099` | Keep the hard save because the reward sets differ, but treat the kill path as too small for a full branch by default. |
| BR-017 | `Promises to Keep` / Frost | Keep Frost. | Main-route resolved with optional outcome note. | `HS-RIFT-FROST-LETRUSH` | No TB-029 full branch unless checklist mapping requires handing Frost to Louis or another alternate state. | `SN-000099`, `SN-000107` | Main continuity preserves the unique mount. |
| BR-018 | `Unearthed` / Ralis | Spare Ralis. | Main-route resolved with optional outcome note. | `HS-DRAGONBORN-UNEARTHED-RALIS` | No TB-029 full branch unless checklist mapping requires the kill outcome. | `SN-000099`, `SN-000107`, `SN-000111` | Main continuity preserves follower availability; collect Hoarfrost without killing him if the final route validates that handling. |
| BR-019 | `Battle of the Champions` side selection | Imperial-aligned handling. | Main-route resolved; branch placement piggybacks on Civil War branch if needed. | `HS-AE-CIVIL-WAR-CHAMPIONS` | Stormcloak-aligned staging only if TB-034/TB-037 finds branch-exclusive equipment/state not covered by Civil War branch. | `SN-000099` | TB-031C and TB-033 found no checklist evidence for a separate branch. Keep source-note dependent; final step/checklist validation should verify both equipment-set availability before final guide release. Do not create a separate full branch for side flavor alone. |

## Option-List Matrix

| ID | Option point | Treatment | Default owner | Source support | Notes |
| --- | --- | --- | --- | --- | --- |
| OPT-001 | `In My Time Of Need` | Option list. | TB-035 route/default pass after checklist review. | `SN-000099` | Isolated moral/outcome choice. No full branch unless external checklist mapping escalates both endings. |
| OPT-002 | `The Blessings of Nature` | Option list. | TB-035 route/default pass after NPC/checklist review. | `SN-000099` | Isolated city-state/NPC outcome choice. No full branch by default. |
| OPT-003 | Black Book power choices | Option list / progression default. | TB-031D/TB-035. | `SN-000032`, `SN-000033` | TB-031C and TB-033 found no checklist-driven hard-save branch need; TB-031D chooses route defaults unless later step-level validation proves an irreversible route-critical power selection. |
| OPT-004 | Spouse, adopted children, stewards, household roles, followers, pets, mounts, farmhands, bards, and carriage services | Option list. | TB-031D checklist/default mapping. | `SN-000067`, `SN-000068`, `SN-000099`, `SN-000106`, `SN-000110` | Recommend defaults later. Do not branch personal preference assignments. |
| OPT-005 | Unique-only enchantment exclusions | Appendix/exclusion, not branch. | TB-031E complete; TB-036 appendix audit. | `SN-000083` | TB-031C found no branch escalation. Preserve unique items; do not disenchant them merely to learn enchantments. |
| OPT-006 | Optional child games/random events | Excluded/unbounded appendix only. | None unless checklist reopens. | `SN-000089`, `SN-000110` | Do not route arbitrary random/reactive child events. |

## TB-029 Branch Prototype Queue

| Priority | Prototype bundle | Includes |
| --- | --- | --- |
| 1 | Major faction branches | Civil War Stormcloak, Volkihar, Destroy the Dark Brotherhood, compact Paarthurnax/Blades. |
| 2 | Solstheim and AE branches | Thirsk Riekling branch, Ghosts destroy-heretics branch, Bittercup Power and Nothing branches. |
| 3 | Reward branches | Daedric outcome branches and Aetherium Forge reward branches. |
| 4 | Trophy branch | Master Criminal compact trophy branch; TB-032 records warning/action limits and TB-034 places final step locations. |
| 5 | Optional outcome notes | Velehk, Frost, Ralis, Battle of the Champions side staging, and isolated moral choices only if checklist mapping escalates them. |

## Handoffs

| Owner | Handoff |
| --- | --- |
| TB-029 | Complete. Prototype files listed above include branch-exclusive objectives only, plus explicit reload/resume points. |
| TB-031C | Complete. `data/checklist-mapping/checklist-escalation-decisions.md` records no all-target radiant escalation, required Thieves Guild 125-job counter coverage, canonical/default promotions, and branch-only holds. |
| TB-031J | Complete. `data/checklist-mapping/source-readiness-resolutions.csv` maps `Reclamation Priest's Journal (AE)` to BR-007 and leaves no unresolved source-readiness branch bucket. |
| TB-032 | Complete. Warning and hard-save trigger placement is recorded in `drafts/route-prototypes/main-route-prototype-v0.md` and `data/constraints/quest-conflicts-hard-saves.md`. |
| TB-033 | Complete in `drafts/route-prototypes/validation-report-v0.md`: prototype-level branch save/reload and canonical-continuity validation passed. TB-034/TB-037 still verify step-level reward/state capture and trophy pops. |
