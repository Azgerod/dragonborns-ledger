# Quest Conflicts and Hard Saves

Status: TB-032 warning-layer placement added; TB-033 prototype validation complete.

Scope: this is a constraint table, not route prose. Use it to place hard saves, branch reloads, and warning-layer notes in later route drafts. Trophy timing, NPC protection, and bug mitigations still belong to the cited TB-015, TB-016, and TB-017 tables.

TB-028 decision details live in `drafts/branch-routes/README.md`. The table below records the selected defaults and branch classifications without rewriting `data/objectives/objectives.csv` route-placement counts.

TB-032 consumes this table into `drafts/route-prototypes/main-route-prototype-v0.md` as a concise warning overlay. TB-033 validated that the warning layer protects the sourced constraints. Final step numbers, pathing, and checklist cues remain TB-034/TB-037 work.

## TB-032 Hard-Save Placement Register

| Hard-save name | Place immediately before | Main continuity after branch/audit | Warning-layer note |
| --- | --- | --- | --- |
| `HS-CW-BEFORE-FACTION-OATH` | Civil War faction oath/commitment. | Reload and join Imperial. | Keep separate hard saves before Season Unending or any hold handoff that could skip War Hero. |
| `HS-DG-BLOODLINE` | Lord Harkon's faction choice in `Bloodline`. | Reload and refuse the gift for Dawnguard. | Volkihar branch must verify spouse state for `The Gift` or mark it conditional. |
| `HS-DB-ABANDONED-SHACK` | Abandoned Shack commitment. | Reload and join the Dark Brotherhood. | Complete or intentionally skip `Delayed Burial` before commitment. |
| `HS-MQ-PAARTHURNAX` | Killing Paarthurnax. | Reload with Paarthurnax alive. | Blades rebuilding and dragon hunt are branch-only checklist rows. |
| `HS-DRAGONBORN-THIRSK-CHOICE` | Thirsk Mead Hall side choice. | Reload and complete Nord-side `Retaking Thirsk`. | Save again before hall assault and let objective state settle. |
| `HS-AE-GHOSTS-TEMPLE` | Ghosts heretic join/infiltrate versus destruction commitment. | Reload and keep join/infiltrate continuity. | Destroy branch records altered Temple state and `Reclamation Priest's Journal (AE)`. |
| `HS-AE-BITTERCUP-ALTAR` | Bittercup altar path choice. | Reload after Power and Nothing audits; continue Fortune. | Main route keeps Fortune for Master Transmute coverage. |
| `HS-DAEDRIC-BLACK-STAR` | Final Black Star reward choice. | Reload and keep The Black Star. | Azura's Star/Aranea is reward-branch coverage. |
| `HS-DAEDRIC-CLAVICUS` | Final Barbas choice. | Reload, spare Barbas, and take Masque. | Rueful Axe does not carry Oblivion Walker-safe main continuity. |
| `HS-DAEDRIC-HIRCINE-GROTTO` | Hircine outcome after Bolar/grotto state is protected if needed. | Reload and keep Ring of Hircine. | Savior's Hide is reward branch; dual-artifact path is appendix/audit only. |
| `HS-DAEDRIC-MEHRUNES-SHRINE` | Silus shrine decision. | Reload and kill Silus/reforge Mehrunes' Razor. | Spare-Silus outcome is non-artifact branch coverage only. |
| `HS-DAEDRIC-NAMIRA-FEAST` | Verulus/Namira feast outcome. | Reload and complete Ring of Namira path. | Save-Verulus/kill-Eola outcomes are branch-only. |
| `HS-DAEDRIC-VAERMINA-SKULL` | Erandur final choice. | Reload and take Skull of Corruption. | Erandur follower outcome is branch-only. |
| `HS-DG-AETHERIUM-FORGE` | Forging the single Aetherial item. | Audit Staff and Shield, then reload and craft Crown. | Lost to the Ages trophy is separate from the kept reward. |
| `HS-TG-ARTICULATION-REWARD` | Brynjolf's Guild Master reward conversation for the Amulet of Articulation. | Reload until the selected strongest version is awarded, or record an explicit final-route tradeoff if accepting a random version. | Random reward version, not a level or cell-entry lock. |
| `HS-TROPHY-MASTER-CRIMINAL` | Deliberate all-holds bounty escalation. | Reload after trophy pop. | Use controlled nonessential crime escalation, avoid killing quest-critical NPCs, verify 1000 bounty in all nine holds and trophy pop. |
| `HS-RIFT-FROST-LETRUSH` | Frost handoff/outcome. | Keep Frost on the main save. | Alternate Louis/Maven handling remains optional unless TB-034/TB-037 find a final coverage gap. |
| `HS-DRAGONBORN-UNEARTHED-RALIS` | Ralis final outcome. | Spare Ralis on the main save. | Kill outcome remains optional unless TB-034/TB-037 find a final coverage gap. |
| `HS-COLLEGE-VELEHK-SAIN` | Velehk Sain outcome. | Release Velehk for hidden treasure path. | Kill outcome remains optional note. |
| `HS-AE-CIVIL-WAR-CHAMPIONS` | Battle of the Champions side/outcome if separated. | Keep Imperial-aligned handling. | TB-033 validated prototype-level handling; TB-034/TB-037 verify both equipment-set availability before final checklist closure. |

## Full Branch Routes

| Conflict or decision | Affected objectives | Canonical route | Branch route | Hard-save name | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Civil War faction commitment | OBJ-000072-OBJ-000101 | Imperial main route. Avoid finalizing route order until Season Unending and War Hero are validated. | Stormcloak Civil War branch from a pre-faction save; route only branch-exclusive sequence before reload. | HS-CW-BEFORE-FACTION-OATH | SN-000097 | TB-028 full branch route. |
| Dawnguard versus Volkihar at `Bloodline` | OBJ-000353, OBJ-000356, OBJ-000357, OBJ-000360, OBJ-000364, OBJ-000374-OBJ-000383 | Refuse Harkon's gift and continue Dawnguard. | Accept Harkon's gift and route Volkihar-exclusive quests, radiants, and rewards before reload. Baseline `New Allegiances` branch depth is one successful conversion unless TB-031C checklist escalation requires all three named conversions. | HS-DG-BLOODLINE | SN-000097 | TB-028 full branch route. |
| Dark Brotherhood join versus destroy | OBJ-000053-OBJ-000068 | Kill a captive in the Abandoned Shack and join the Dark Brotherhood. Complete `Delayed Burial` before entering the Sanctuary if it will be included. | Kill Astrid, complete `Destroy the Dark Brotherhood!`, record branch-exclusive outcome and unavailable join-route rewards, then reload. | HS-DB-ABANDONED-SHACK | SN-000097, SN-000100 | TB-028 full branch route. |
| Paarthurnax and Blades/Greybeards conflict | OBJ-000019, OBJ-000317 | Preserve Paarthurnax. Use Greybeards support and do not kill him on the canonical save. | Kill Paarthurnax only on the branch after any intended Blades-exclusive setup; record lost Greybeards support and restored Blades support, then reload. | HS-MQ-PAARTHURNAX | SN-000097 | TB-028 compact branch route. |
| Thirsk Mead Hall control | OBJ-000454-OBJ-000459 | Complete `Retaking Thirsk` on the canonical route to preserve the Nord-side favor/service/spouse-candidate surface. | Route `The Chief of Thirsk Hall`, the Riekling occupant state, and Riekling follower access from the same pre-choice save, then reload. | HS-DRAGONBORN-THIRSK-CHOICE | SN-000034, SN-000099 | TB-028 default selected; full branch route. |
| Ghosts of the Tribunal heretics | OBJ-000615-OBJ-000620, OBJ-000740 | Join/infiltrate path is the completionist default because it preserves armory access, crafting permissions, followers, companion tasks, and Skullcrusher access. | Destroy the heretics as the alternate substantial branch; record lost armory-key/Skullcrusher access and alternate Temple state, then reload. | HS-AE-GHOSTS-TEMPLE | SN-000099 | TB-028 default confirmed; full branch route. |
| Bittercup path choice | OBJ-000535, OBJ-000572-OBJ-000574, OBJ-000755 | Choose Fortune on the canonical route because Master Transmute is path-specific and spell/permanent-spell coverage is main-route scope. | From the altar save, branch Power for `The Pit`, Grand Champion's Sword, and Grand Champion's Helm; reload, then branch Nothing for Rulnik, Rulnik's Dagger, and Ironwood Soup support. Continue Fortune on the canonical save. | HS-AE-BITTERCUP-ALTAR | SN-000099 | TB-028 default selected; two compact alternate branches. |

## Artifact and Unique-Reward Outcome Saves

| Conflict or decision | Affected objectives | Canonical route | Branch route | Hard-save name | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `The Black Star` reward | OBJ-000165 | Take the Black Star for the utility default. | Branch Azura's Star and Aranea follower outcome as a compact reward branch. | HS-DAEDRIC-BLACK-STAR | SN-000098 | TB-028 default confirmed; reward branch. |
| `A Daedra's Best Friend` reward | OBJ-000167 | Spare Barbas and take the Masque of Clavicus Vile for Oblivion Walker-safe completion. | Kill Barbas and take the Rueful Axe only on an alternate outcome branch. | HS-DAEDRIC-CLAVICUS | SN-000098 | Canonical artifact-safe. |
| `Ill Met By Moonlight` outcome | OBJ-000169 | Take the Ring of Hircine single-artifact outcome on the main route. Do not rely on the dual-artifact outcome for Oblivion Walker. Preserve Bolar's Oathblade and the non-quest grotto clear state before the quest if the route keeps Sinding alive. | Branch Savior's Hide as the alternate single-artifact outcome. Document the UESP-listed dual-artifact route only as appendix/audit material unless the user later accepts it explicitly. | HS-DAEDRIC-HIRCINE-GROTTO | SN-000095, SN-000098 | TB-028 default selected; reward branch plus appendix-only dual-artifact note. |
| `Pieces of the Past` final choice | OBJ-000171 | Kill Silus and reforge Mehrunes' Razor for artifact-safe completion. | Spare Silus and accept the non-artifact gold outcome only on branch. | HS-DAEDRIC-MEHRUNES-SHRINE | SN-000098 | Canonical artifact-safe. |
| `The Taste of Death` final outcome | OBJ-000175 | Complete Namira's feast outcome for Ring of Namira and artifact-safe completion. | Save Verulus or kill Eola only on branch. | HS-DAEDRIC-NAMIRA-FEAST | SN-000098 | Canonical artifact-safe. |
| `Waking Nightmare` final choice | OBJ-000179 | Kill Erandur before he destroys the Skull of Corruption for artifact-safe completion. | Spare Erandur and record follower outcome only on branch. | HS-DAEDRIC-VAERMINA-SKULL | SN-000098 | Canonical artifact-safe; bug pass still needed. |
| `Lost to the Ages` Aetherial reward | OBJ-000385, OBJ-001565, OBJ-001585, OBJ-001607 | Craft the Aetherial Crown on the canonical route. | Branch Aetherial Staff and Aetherial Shield craft rewards from the forge save. | HS-DG-AETHERIUM-FORGE | SN-000099 | TB-028 default selected; reward branch. |
| `Promises to Keep` / Frost ownership | OBJ-001955, NPCOPT-000238 | Keep Frost on the main route. Prefer a save before meeting Louis with Frost. | Branch handing Frost to Louis or alternate Louis/Maven outcomes only if later checklist policy requires it. | HS-RIFT-FROST-LETRUSH | SN-000099 | TB-028 main-route resolved; optional outcome note. |
| `Unearthed` Ralis outcome | OBJ-000465, NPCOPT-000164 | Spare Ralis to preserve follower availability; remove/collect Hoarfrost without killing him if route permits. | Kill Ralis only if later checklist policy requires the alternate outcome. | HS-DRAGONBORN-UNEARTHED-RALIS | SN-000099 | TB-028 main-route resolved; optional outcome note. |
| `Forgotten Names` Velehk Sain outcome | OBJ-000764 | Release Velehk Sain for the hidden treasure map/reward path. | Branch the kill outcome only if final checklist treats corpse loot as required. | HS-COLLEGE-VELEHK-SAIN | SN-000099 | TB-028 main-route resolved; optional outcome note. |
| `Battle of the Champions` side selection | OBJ-000579, OBJ-001350 | Use Imperial-aligned handling with the Civil War main route. Loot all equipment from the assigned chest and fallen champion. | Stormcloak-aligned staging belongs with the Stormcloak branch only if it materially differs after TB-029 review. | HS-AE-CIVIL-WAR-CHAMPIONS | SN-000099 | TB-028 main-route resolved; TB-033 kept the prototype-level assumption; TB-034/TB-037 verify final equipment coverage. |

## Option-List Decisions

| Conflict or decision | Affected objectives | Canonical route | Branch route | Hard-save name | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `In My Time Of Need` | OBJ-000199 | Isolated moral/outcome choice; default not yet selected. | Do not full-branch unless checklist or later roleplay policy requires showing both endings. | Optional save before Saadia/Kematu handoff | SN-000099 | TB-028 option list; default later. |
| `The Blessings of Nature` | OBJ-000201 | Isolated Gildergreen outcome choice; default not yet selected. | Do not full-branch unless visual city-state or NPC preservation policy requires both. | Optional save before Eldergleam final choice | SN-000099 | TB-028 option list; default later. |
| Black Book power choices | OBJ-000418, OBJ-000420, OBJ-000441, OBJ-000460-OBJ-000462 | Pick practical defaults during skill/perk planning after changeability and usefulness are verified. | No full branch unless a power is proven irreversible for the route. | No hard save by default until a later pass proves an irreversible choice. | SN-000032, SN-000033 | TB-028 option list; TB-031C/TB-033 default and validation. |
| Household and role assignments | OBJ-000408, OBJ-001945-OBJ-001954, NPC option rows | Use option lists with a recommended default for spouse, children, stewards, bards, carriage drivers, farmhands, followers, pets, and stable horses. | Do not full-branch isolated personal preference choices. | No hard save by default | SN-000067, SN-000099 | TB-028 option list; TB-031D default mapping. |
| Unique-only enchantment exclusions | OBJ-002498, OBJ-002521-OBJ-002523, OBJ-002525 | Preserve unique items; do not disenchant unique-only effects merely for enchantment learning. | No branch required unless final checklist explicitly asks for destructive audit proof. | No hard save by default | SN-000083 | Already excluded from main. |
| Optional child games/random events | OBJ-002768-OBJ-002772 | Treat as excluded unbounded or optional flavor, not true route constraints. | No branch. | No hard save | SN-000089 | No TB-014 action. |

## Trophy and Cleanup Hard-Save Branches

| Trophy or action | Affected objectives | Canonical route | Branch route | Hard-save name | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Master Criminal trophy | OBJ-002777 | Preserve a clean final continuity without permanent all-holds bounty disruption. | Stage controlled 1000-gold bounties in all nine holds on the trophy branch, avoid quest-critical NPC deaths, verify the trophy pop, then reload. Final step locations remain TB-034 route prose. | HS-TROPHY-MASTER-CRIMINAL | SN-000103 | TB-032 warning/action layer placed; TB-033 validated prototype-level treatment. |

## Sequencing and Missability Warnings

| Constraint | Affected objectives | Route rule | Hard-save or warning placement | Source notes | Handoff |
| --- | --- | --- | --- | --- | --- |
| Civil War / Season Unending / War Hero | OBJ-000072-OBJ-000101 and trophy rows | Do not allow Season Unending to skip the War Hero fort requirement unless TB-015 proves an alternate safe trophy path. | Hard save before Season Unending and before any Civil War hold handoff that could alter fort battles. | SN-000010, SN-000097 | TB-015 trophy validation. |
| `Delayed Burial` window | OBJ-000053, OBJ-000207 | Complete or intentionally skip `Delayed Burial` before entering the Dark Brotherhood Sanctuary or starting the destroy route. | Warning before `Innocence Lost`/Abandoned Shack continuation. | SN-000097, SN-000100 | TB-017 bug/side-quest cleanup. |
| Companions post-Silver Hand radiants | OBJ-000109-OBJ-000111 | Complete representative windowed radiants after `The Silver Hand` and before starting `Blood's Honor` if TB-018 keeps them required. | Warning at Companions progression gate. | SN-000011, SN-000100 | TB-018 radiant boundary. |
| Bards College ordering | OBJ-000182-OBJ-000186 | Avoid late investigation start and avoid early instrument pickup unless the bug pass approves it. | Warning before Bards College join and before entering instrument locations. | SN-000018, SN-000100 | TB-017 bug mitigation. |
| Falkreath land and `Kill Helvard` | OBJ-000159, OBJ-000391, OBJ-000395 | Buy Lakeview Manor and clear Falkreath land prerequisites before killing Helvard on the Dark Brotherhood route. | Hard save before accepting/executing the Helvard contract if property is not secured. | SN-000100 | TB-016 property/NPC pass. |
| Falkreath `Rare Gifts` and level-9 Jarl letter | OBJ-000249, OBJ-000391 | If Siddgeir's Black-Briar Mead favor is needed, do it before the Hearthfire Jarl letter can block it. | Warning before character level 9 or before accepting Falkreath land chain. | SN-000100 | TB-016 property pass. |
| Captain Aldis `Rare Gifts` | OBJ-000260 | Complete Aldis's `The Mirror` favor before Stormcloak Battle for Solitude branch if the favor is needed. | Branch warning in Stormcloak Civil War route. | SN-000100 | TB-016 NPC/favor pass. |
| `A New Source of Stalhrim` | OBJ-000436 | Let Deor/Fanari finish their scene; protect Deor and Fanari until the quest starts and stalhrim crafting is unlocked. | Warning on return to Skaal Village after `The Fate of the Skaal`. | SN-000100 | TB-016 and TB-017. |
| `The Whispering Door` start dependency | OBJ-000172 | Keep Hulda and Ysolda alive until the rumor/start path is secured. | NPC warning before risky Whiterun violence or hostile quest states. | SN-000100 | TB-016 NPC pass. |
| `Discerning the Transmundane` cube/outpost lock | OBJ-000168 | After opening the cube, take/resolve the Oghma Infinium before allowing the outpost cell to respawn; do not kill Septimus prematurely. | Hard save before opening the cube and before leaving the opened outpost for long-term delay. | SN-000100 | TB-017 bug/lock pass. |
| `Boethiah's Calling` sacrifice | OBJ-000166 | Use a deliberately chosen nonessential, non-unique follower and strip borrowed inventory before sacrifice. Avoid Companion leaders. | Hard save at Sacellum before ordering the follower to use the pillar. | SN-000100 | TB-016 follower dependency. |
| `The House of Horrors` Logrolf state | OBJ-000174 | Do not kill Logrolf while captive; escort/rescue path must remain intact until the Mace is obtained. | Hard save before freeing Logrolf and before re-entering the Abandoned House. | SN-000100 | TB-017 bug pass. |
| `The Cursed Tribe` first visit | OBJ-000170 | Intervene quickly at Largashbur to protect potential Orc followers during the opening giant attack. | Warning before first approach to Largashbur at level 9+. | SN-000100 | TB-016 NPC pass. |
| Kharjo's Amulet of the Moon targets | OBJ-000221 and related favor rows | Avoid clearing nonrespawning possible target locations before the Amulet target is assigned, or verify the target list before first visit. | Carry forward TB-013 first-visit warning. | SN-000096 | TB-016/TB-017. |

## Candidate Queue Disposition

| Candidate group | Disposition | Source notes |
| --- | --- | --- |
| Full/compact branches with resolved canonical defaults | Civil War, Dawnguard, Dark Brotherhood, compact Paarthurnax, Thirsk, Ghosts of the Tribunal, and Bittercup have TB-029 branch prototypes and TB-032 warning placement. | SN-000097, SN-000099 |
| Reward branches with resolved defaults | Black Star, Clavicus, Hircine, Mehrunes, Namira, Vaermina, and Aetherium have compact reward-branch prototypes and TB-032 warning placement. | SN-000098, SN-000099 |
| Main-route resolved outcome notes | Frost, Ralis, Velehk Sain, and Battle of the Champions have main-continuity defaults; TB-033 found no prototype-level reason to reopen them. TB-034/TB-037 may still reject an assumption if final checklist validation proves alternate-outcome coverage is missing. | SN-000099 |
| Isolated moral/preference choices | Keep as option-list defaults unless a later checklist/trophy/NPC pass upgrades them to branch routes. | SN-000099 |
| Branch checklist escalation | TB-031C applied current checklist escalation decisions and TB-033 validated the prototype-level result. Future escalation requires a new concrete contradiction or final-QA finding. | SN-000099 |
| Radiant/bounty/work activity candidates | TB-018 and TB-031F set repetition boundaries and representative/counter handling; final placement remains TB-034. | SN-000011, SN-000013, SN-000089, SN-000127 |
| Bug-only candidates | Keep the warning pointer here only when route order is affected; detailed mitigations are in `data/constraints/bug-prone-quests.md` and the TB-032 overlay. | SN-000100 |
| NPC/property/family/service dependencies | Keep the branch/option classification here; TB-031D selected route defaults and TB-032 records warning triggers, while final step order remains TB-034. | SN-000067, SN-000100 |
| Duplicate or excluded rows | No hard-save row needed for duplicate cross-references, unique-only enchantment exclusions, or unbounded child/random events unless later checklist mapping reopens them. | SN-000083, SN-000089 |
