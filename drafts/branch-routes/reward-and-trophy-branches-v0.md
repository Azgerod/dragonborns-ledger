# Reward and Trophy Branch Prototypes v0

Status: TB-033 validated after TB-029 completion and TB-032 warning integration.

Scope: compact outcome branches for Daedric rewards, Aetherium Forge rewards, and the Master Criminal trophy branch. These are branch prototypes, not final black-box guide steps. TB-032 records warning and hard-save trigger placement; TB-033 validated the prototype-level structure; final step/checklist validation remains TB-034/TB-037.

## Operating Rules

| Rule | Handling |
| --- | --- |
| Branch order | Create the named hard save, play the alternate reward/trophy branch, verify branch-exclusive reward or trophy state, reload, then continue canonical main continuity. |
| Artifact policy | Canonical route keeps artifact-safe choices for Oblivion Walker unless TB-028 explicitly marks a different supported default. |
| Exploit policy | Hircine dual-artifact acquisition remains appendix/audit only, not a baseline branch route. |
| Trophy branch policy | Master Criminal uses a clean-save branch because permanent all-holds bounty state is not desired in final continuity. |
| Branch verification | TB-033 validated the hard-save/reload/canonical-continuity structure. TB-034/TB-037 still verify step-level objective completion, alternate reward acquisition/state, trophy pop where relevant, and restoration of canonical continuity. |

## Branch Prototype Index

| Branch ID | Branch file section | Hard save | Canonical continuity | Alternate branch |
| --- | --- | --- | --- | --- |
| BR-009 | Black Star reward | `HS-DAEDRIC-BLACK-STAR` | The Black Star | Azura's Star / Aranea outcome |
| BR-010 | Clavicus reward | `HS-DAEDRIC-CLAVICUS` | Masque of Clavicus Vile | Rueful Axe |
| BR-011 | Hircine reward | `HS-DAEDRIC-HIRCINE-GROTTO` | Ring of Hircine single-artifact outcome | Savior's Hide single-artifact outcome |
| BR-012 | Mehrunes reward | `HS-DAEDRIC-MEHRUNES-SHRINE` | Mehrunes' Razor | Spare Silus / non-artifact outcome |
| BR-013 | Namira reward | `HS-DAEDRIC-NAMIRA-FEAST` | Ring of Namira | Save Verulus / kill Eola outcome |
| BR-014 | Vaermina reward | `HS-DAEDRIC-VAERMINA-SKULL` | Skull of Corruption | Spare Erandur follower outcome |
| BR-015 | Aetherium Forge reward | `HS-DG-AETHERIUM-FORGE` | Aetherial Crown | Aetherial Staff and Aetherial Shield |
| BR-005 | Master Criminal trophy | `HS-TROPHY-MASTER-CRIMINAL` | Clean final continuity | All-holds bounty trophy branch |

## Daedric Reward Branches

| Branch | Hard save | Canonical reward | Alternate branch reward/outcome | Prototype handling | Source support |
| --- | --- | --- | --- | --- | --- |
| BR-009 `The Black Star` | `HS-DAEDRIC-BLACK-STAR` | `OBJ-001613` Artifact: The Black Star | `OBJ-001612` Artifact: Azura's Star and Aranea outcome | Branch Azura's Star only; reload and take The Black Star on main save. | `SN-000098`, `SN-000104` |
| BR-010 `A Daedra's Best Friend` | `HS-DAEDRIC-CLAVICUS` | `OBJ-001584` Artifact: Masque of Clavicus Vile | `OBJ-001555` Artifact: The Rueful Axe | Branch Rueful Axe only; reload and choose Masque on main save. Do not count Rueful Axe for Oblivion Walker. | `SN-000098`, `SN-000104`, `SN-000107` |
| BR-011 `Ill Met By Moonlight` | `HS-DAEDRIC-HIRCINE-GROTTO` | `OBJ-001608` Artifact: Ring of Hircine | `OBJ-001581` Artifact: Savior's Hide | Branch Savior's Hide single-artifact outcome only; reload and keep Ring of Hircine on main save. | `SN-000095`, `SN-000098`, `SN-000104`, `SN-000107` |
| BR-012 `Pieces of the Past` | `HS-DAEDRIC-MEHRUNES-SHRINE` | `OBJ-001561` Artifact: Mehrunes' Razor | Spare Silus / gold non-artifact outcome | Branch spare-Silus outcome only; reload and kill Silus/reforge Razor on main save. | `SN-000098`, `SN-000104`, `SN-000107` |
| BR-013 `The Taste of Death` | `HS-DAEDRIC-NAMIRA-FEAST` | `OBJ-001609` Artifact: Ring of Namira | Save Verulus or kill Eola non-artifact outcome | Branch non-artifact moral outcome only; reload and complete Namira feast on main save. | `SN-000098`, `SN-000104`, `SN-000107` |
| BR-014 `Waking Nightmare` | `HS-DAEDRIC-VAERMINA-SKULL` | `OBJ-001569` Artifact: Skull of Corruption | Spare Erandur follower outcome | Branch Erandur-spared outcome only; reload and take Skull on main save. | `SN-000098`, `SN-000104`, `SN-000107` |

Daedric warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Oblivion Walker | Canonical route must use artifact-awarding outcomes and must not rely on the Hircine dual-artifact route. |
| Hircine cell state | TB-032 records the Bloated Man's Grotto / Bolar's Oathblade warning before final Hircine route prose. |
| NPC dependencies | Silus, Eola/Verulus, Sinding, Erandur, Lod/Barbas, and other branch NPC warnings are recorded in TB-016/TB-032 source-backed tables. |
| Reload point | After each alternate reward audit, reload the named hard save and execute the canonical artifact-safe choice. |

## BR-015 - Aetherium Forge Reward Branches

| Field | Prototype |
| --- | --- |
| Hard save | `HS-DG-AETHERIUM-FORGE` before crafting the one Aetherial item. |
| Canonical resume | Reload and craft the Aetherial Crown on the main save. |
| Branch goal | Record the two non-canonical Aetherial reward outcomes without losing the Crown default. |
| Source support | `SN-000099`, `SN-000105`. |

Reward branch queue:

| Objective ID | Reward | Branch handling |
| --- | --- | --- |
| `OBJ-001565` | Artifact: Aetherial Staff | Craft on one branch attempt, record reward, reload. |
| `OBJ-001585` | Artifact: Aetherial Shield | Craft on a second branch attempt, record reward, reload. |
| `OBJ-001607` | Artifact: Aetherial Crown | Canonical reward after branch audits; keep on main save. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Single craft limit | The branch point exists because only one Aetherial item can be forged in one continuity. |
| Trophy | `Lost to the Ages` trophy completion is separate from which reward is kept. |
| Reload point | After Staff and Shield branch audits, reload `HS-DG-AETHERIUM-FORGE` and craft Crown. |

## BR-005 - Master Criminal Trophy Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-TROPHY-MASTER-CRIMINAL` before deliberate crime escalation. |
| Canonical resume | Reload after trophy verification to preserve clean final continuity. |
| Branch goal | Get the `Master Criminal` trophy by holding 1000 gold bounty in all nine holds, then reload. |
| Source support | `SN-000103`. |

Trophy branch queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-002777` | `Master Criminal Trophy Set` | TB-029 uses placeholder crime method only: stage controlled 1000-gold bounties in all nine holds, verify trophy pop, reload. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Exact crime actions | TB-032 records the action limits: controlled 1000-gold bounties in all nine holds, avoid quest-critical NPC deaths, verify trophy, reload. TB-034 chooses final step locations. |
| Trophy-pop fallback | Keep recent manual save; if trophy does not pop, reload and repeat the verified action according to the TB-032 warning layer. |
| Final state | Reload after trophy verification; do not carry all-holds bounty into final continuity. |

## Main-Route Resolved Outcome Notes

These rows keep their TB-028 main-route defaults. TB-031C found no checklist evidence requiring new full branches.

| Decision | Hard save | Main continuity | Branch escalation rule | Source support |
| --- | --- | --- | --- | --- |
| `Forgotten Names` / Velehk Sain | `HS-COLLEGE-VELEHK-SAIN` | Release Velehk for hidden treasure map/reward path. | Branch kill outcome only if final checklist treats corpse loot as required. | `SN-000099` |
| `Promises to Keep` / Frost | `HS-RIFT-FROST-LETRUSH` | Keep Frost. | Branch handoff/alternate Louis/Maven outcomes only if checklist mapping requires them. | `SN-000099`, `SN-000107` |
| `Unearthed` / Ralis | `HS-DRAGONBORN-UNEARTHED-RALIS` | Spare Ralis; preserve follower availability. | Branch kill outcome only if checklist mapping requires it. | `SN-000099`, `SN-000107`, `SN-000111` |
| `Battle of the Champions` side selection | `HS-AE-CIVIL-WAR-CHAMPIONS` | Imperial-aligned handling with Civil War main route. | Piggyback Stormcloak staging on Civil War branch only if TB-034/TB-037 verifies checklist-relevant side differences. | `SN-000099` |

Handoff note: TB-031C and TB-033 did not create a separate `Battle of the Champions` branch. Equipment coverage remains source-note dependent until TB-034/TB-037 verifies both equipment-set availability for final checklist mapping.
