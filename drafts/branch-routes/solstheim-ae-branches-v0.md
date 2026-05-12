# Solstheim and AE Branch Prototypes v0

Status: TB-033 validated after TB-029 completion and TB-032 warning integration.

Scope: compact branch prototypes for Dragonborn/Solstheim and Anniversary Edition choice branches resolved by TB-028. These are not final guide prose and do not choose checklist defaults beyond the TB-028 matrix.

## Operating Rules

| Rule | Handling |
| --- | --- |
| Branch order | Create the named hard save, play each alternate branch first, verify branch-exclusive content, reload, then continue canonical main continuity. |
| Duplication boundary | Do not duplicate canonical Solstheim or AE quest progression unless the alternate state changes rewards, followers, services, powers, or checklist meaning. |
| Placement boundary | TB-029 records branch containers; TB-032 records warning and hard-save triggers; TB-033 validated branch safety at prototype level; TB-034 places final step order. |
| Branch verification | TB-033 validated the hard-save/reload/canonical-continuity structure. TB-034/TB-037 still verify step-level objective completion, branch-exclusive reward/state capture, reload point, and restoration of canonical continuity. |

## Branch Prototype Index

| Branch ID | Branch file section | Hard save | Canonical continuity | Alternate branch |
| --- | --- | --- | --- | --- |
| BR-006 | Thirsk Riekling branch | `HS-DRAGONBORN-THIRSK-CHOICE` | Nord-side `Retaking Thirsk` | Riekling-side `The Chief of Thirsk Hall` |
| BR-007 | Ghosts destroy-heretics branch | `HS-AE-GHOSTS-TEMPLE` | Join/infiltrate heretics | Destroy heretics |
| BR-008A | Bittercup Power branch | `HS-AE-BITTERCUP-ALTAR` | Fortune path | Power path / `The Pit` |
| BR-008B | Bittercup Nothing branch | `HS-AE-BITTERCUP-ALTAR` | Fortune path | Nothing path / Rulnik outcome |

## BR-006 - Thirsk Riekling Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-DRAGONBORN-THIRSK-CHOICE` before resolving Mead Hall control. |
| Canonical resume | Reload and complete `Retaking Thirsk` / Nord-side continuity. |
| Branch goal | Record Riekling-side quest and occupant/follower state without losing Nord-side favors, services, and spouse-candidate surface on the main save. |
| Source support | `SN-000034`, `SN-000099`, `SN-000107`, `SN-000111`. |

Alternate-only branch queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-000454` | `The Chief of Thirsk Hall` | Complete on branch as the Riekling-side outcome. |

Canonical-side rows to preserve for main continuity:

| Objective ID | Objective | Main-route handling |
| --- | --- | --- |
| `OBJ-000455` | `Retaking Thirsk` | Canonical Nord-side route after reload. |
| `OBJ-000456` | `Elmus Favor Quest (berries)` | Preserve for canonical Nord-side support surface. |
| `OBJ-000457` | `Elmus Favor Quest (mead)` | Preserve for canonical Nord-side support surface. |
| `OBJ-000458` | `Halbarn Favor Quest` | Preserve for canonical service/favor surface. |
| `OBJ-000459` | `Hilund Favor Quest` | Preserve for canonical favor surface. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Branch execution bug | Keep a save before hall assault. Let objective state settle before clearing too aggressively. |
| Riekling follower state | Verify branch-only follower/occupant access before reload. |
| Main-route duplicate risk | Do not complete Nord-side favors on the Riekling branch. TB-031C promoted Nord-side Thirsk and the Nord-side Elmus/Halbarn/Hilund favors to canonical main-route handling. |
| Reload point | After Riekling branch audit, reload `HS-DRAGONBORN-THIRSK-CHOICE` and continue Nord-side Thirsk. |

## BR-007 - Ghosts Destroy-Heretics Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-AE-GHOSTS-TEMPLE` before committing to heretic join/infiltrate versus destruction. |
| Canonical resume | Reload and continue the join/infiltrate path. |
| Branch goal | Record the destroy-heretics alternate state, including lost armory-key/Skullcrusher access and alternate Temple state, without losing main-route armory/crafting/follower coverage. |
| Source support | `SN-000099`; `SN-000129`. |

Affected objective queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-000615` | `Ashen Heart` | Record only branch-specific availability/state differences; do not duplicate canonical quest handling. |
| `OBJ-000616` | `Buyer Beware` | Record branch-specific access differences if affected by destroyed-heretic state. |
| `OBJ-000617` | `Careless Curation` | Record branch-specific access differences if affected by destroyed-heretic state. |
| `OBJ-000618` | `Ghosts of the Tribunal` | Execute destroy-heretics outcome on branch. |
| `OBJ-000619` | `Her Word Against Theirs` | Record branch-specific propaganda/Temple-state consequences if available. |
| `OBJ-000620` | `Trueflame` | Record branch-specific access differences if affected by destroyed-heretic state. |
| `OBJ-000740` | `Ghosts of the Tribunal Equipment Parent Set` | Record unavailable or altered equipment access, especially armory-key and Skullcrusher consequences. |
| Checklist cue | `Reclamation Priest's Journal (AE)` | TB-031J maps this to BR-007 because the source ties it to giving propaganda to the Reclamation Priest and his later Ashfall's Tear attack state. TB-033 kept it as branch-only checklist coverage. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Main default | Join/infiltrate remains canonical because it preserves armory access, crafting permissions, followers, companion tasks, and Skullcrusher access. |
| Equipment and document coverage | TB-031C found no equipment evidence requiring a larger destroy-only or join-only branch. TB-031J resolves the Ghosts source-readiness document rows: ordinary Ashfall's Tear or carried journals map to main Ghosts handling, while `Reclamation Priest's Journal (AE)` maps to this branch. TB-033 validated the prototype-level branch/checklist split; final step cues remain TB-034/TB-037. |
| Route granularity | This branch should be an alternate-state audit, not a second copy of every Ghosts quest step. |
| Reload point | After destroy-heretics audit, reload `HS-AE-GHOSTS-TEMPLE` and continue join/infiltrate continuity. |

## BR-008A - Bittercup Power Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-AE-BITTERCUP-ALTAR` before choosing a Bittercup path. |
| Canonical resume | Reload and choose Fortune on the main save. |
| Branch goal | Complete the Power path and record `The Pit` rewards, then reload before trying the Nothing branch or continuing the Fortune main save. |
| Source support | `SN-000099`. |

Branch objective and reward queue:

| ID | Objective / reward | Branch handling |
| --- | --- | --- |
| `OBJ-000535` | `Bittercup` | Parent Creation branch context. |
| `OBJ-000572` | `A Dying Wish` | Choose Power only on this branch attempt. |
| `OBJ-000574` | `The Pit` | Complete Power follow-on branch quest. |
| `OBJ-000755` | `Bittercup Reward Parent Set` | Record Power-path reward members. |
| `ITEM-001137` | `Grand Champion's Helm` | Power-path reward member. |
| `ITEM-001139` | `Grand Champion's Sword` | Power-path reward member. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Main-route spell coverage | Do not keep Power on the canonical save because Fortune carries `Spell Tome: Master Transmute` coverage. |
| Sequential branch handling | After Power audit, reload `HS-AE-BITTERCUP-ALTAR` before attempting Nothing or continuing Fortune. |
| Checklist mapping | TB-031C promoted `The Pit` to BR-008A branch handling and found no extra supported checklist item rows to promote from the Power path. |

## BR-008B - Bittercup Nothing Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-AE-BITTERCUP-ALTAR` before choosing a Bittercup path. |
| Canonical resume | Reload and choose Fortune on the main save. |
| Branch goal | Complete the Nothing path and record Rulnik/follower, Rulnik's Dagger, and Ironwood Soup support, then reload to preserve Fortune continuity. |
| Source support | `SN-000099`. |

Branch objective and reward queue:

| ID | Objective / reward | Branch handling |
| --- | --- | --- |
| `OBJ-000535` | `Bittercup` | Parent Creation branch context. |
| `OBJ-000572` | `A Dying Wish` | Choose Nothing only on this branch attempt. |
| `OBJ-000755` | `Bittercup Reward Parent Set` | Record Nothing-path reward members. |
| `ITEM-001140` | `Rulnik's Dagger` | Nothing-path reward member. |
| `ITEM-001141` | `Ironwood Soup` | Nothing-path food/support member. |
| `ITEM-001142` | `Ironwood Soup` | Duplicate/source-listed soup member; TB-031C did not promote a separate checklist row. |
| `ITEM-001143` | `Hot Ironwood Soup` | Survival-relevant variant; TB-031C did not promote a separate checklist row, and TB-032 does not add a separate checklist cue for it. TB-034 may use it only as branch-local food support. |
| `NPCOPT-000058` | `Rulnik Wind-Strider` spouse candidate | Branch-only option surface. |
| `NPCOPT-000130` | `Rulnik Wind-Strider` steward candidate | Branch-only option surface. |
| `NPCOPT-000215` | `Rulnik Wind-Strider` follower candidate | Branch-only option surface. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Main-route spell coverage | Do not keep Nothing on the canonical save because Fortune carries `Spell Tome: Master Transmute` coverage. |
| Sequential branch handling | If Power branch was also audited, reload the same altar save before choosing Nothing. |
| Checklist mapping | TB-031C left Rulnik role options in option-list handling and did not promote Ironwood food variants into separate checklist rows. TB-035 presents Rulnik options if needed. |
| Reload point | After Nothing audit, reload `HS-AE-BITTERCUP-ALTAR` and continue Fortune. |
