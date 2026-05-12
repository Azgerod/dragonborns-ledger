# Checklist Escalation Decisions

Status: TB-031C complete.

Input: `data/checklist-mapping/coverage-matrix.csv`

Raw checklist snapshot: `data/checklist-mapping/raw/Skyrim Checklist.xlsx`

This pass decides whether checklist evidence promotes representative, branch, option-list, or counter handling. It does not add unsourced objectives merely because the spreadsheet names something, and it does not write final route prose.

## Coverage Impact

| Area | Decision |
| --- | --- |
| Total checklist rows | Unchanged at 3,697. |
| Branch prototype checklist rows | Reduced from 37 to 30 after canonical defaults were promoted out of branch handling. |
| Main-route prototype checklist rows | Increased from 3,069 to 3,076 after canonical defaults were promoted. |
| Source-readiness holds | Unchanged at 90 in TB-031C; TB-031J later resolved the remaining source-readiness rows before TB-032. |
| Objective route placement | Canonical Thirsk Nord-side rows, Aetherial Crown, and Ring of Hircine are main-route rows. `The Pit` is a Bittercup Power branch row. |

## Decisions

| Topic | TB-031C decision | Follow-up owner |
| --- | --- | --- |
| Representative radiants and no-journal activities | Do not escalate checklist variants into all-NPC/all-location requirements. Keep the existing representative-type policy; the 65 no-journal activity/favor checklist variants remain mapped to representative activity rows. | TB-031F chooses exact route actions and counter mechanics. TB-031D may choose targets where defaults affect logistics or relationships. |
| Thieves Guild 125 side jobs | Treat the source-backed 125-job Guild display/safe boundary as required completionist counter coverage through `OBJ-000048`, not as an optional appendix. | TB-031F chooses job mix, rejection policy, Raven Rock/Riften handling, and counter tracking. |
| Volkihar representative radiants | Keep one representative branch instance for ordinary Volkihar hunt/framing radiants. Do not escalate all targets unless a later concrete checklist/source contradiction proves a named row is still not covered. | TB-032 records warnings; TB-033 validated prototype-level branch handling; TB-034/TB-037 verify final step coverage. |
| `New Allegiances` | Keep one successful conversion in the Volkihar branch. The checklist has one quest row, not member-level rows for all named conversion targets. | TB-032 records branch setup and known radiant-hazard warnings. |
| `The Gift` | Keep as Volkihar branch-only conditional coverage. It does not decide the canonical spouse default. | TB-031D chooses spouse/default logistics; TB-032 marks the branch save as needing a valid spouse setup or conditional label. |
| Thirsk Mead Hall | Canonical main continuity is the Nord side: `Retaking Thirsk` plus Nord-side Elmus/Halbarn/Hilund favors. The Riekling side remains the branch. | TB-032 records the hard-save/reload warning; TB-034 routes canonical Solstheim steps. |
| Ghosts of the Tribunal | Keep join/infiltrate as main continuity and destroy-heretics as the branch audit. TB-031J later source-checked the remaining Ghosts book/document rows: ordinary Ashfall's Tear or carried journals map to main Ghosts handling, while `Reclamation Priest's Journal (AE)` maps to BR-007 branch coverage. | TB-033 validated prototype-level branch/checklist coverage; TB-034/TB-037 verify final step coverage. |
| Bittercup | Keep Fortune/Fortunate Son as canonical main continuity. Promote `The Pit` to the Power branch. Keep the Nothing/Rulnik path as compact branch/option coverage without promoting extra checklist rows from unsupported item names. | TB-031E handles Master Transmute/progression source timing; TB-035 handles Rulnik option-list presentation. |
| Daedric and Aetherial branch rewards | Keep existing reward branches. Promote canonical Ring of Hircine and Aetherial Crown rows to main-route handling; Savior's Hide, Rueful Axe, Azura's Star, Aetherial Staff, and Aetherial Shield remain branch rewards. | TB-032 records reward hard-save warnings; TB-033 validated prototype-level branch coverage; TB-034/TB-037 verify branch reward capture and reloads. |
| Velehk, Frost, and Ralis | Do not promote new full branches. Current main defaults remain: release Velehk, keep Frost, and spare Ralis. Checklist rows for Velehk's map, Frost, Ralis, and Hoarfrost are covered by existing main-route or option/default handling. | TB-035 handles option-list rows; TB-033 validated prototype-level coverage; TB-037 validates final coverage. |
| Battle of the Champions | Do not create a separate branch from checklist evidence alone. Keep Imperial-aligned handling with Civil War context; side-equipment availability remains source-note dependent. | TB-032 records the side-selection save trigger; TB-033 validated prototype-level handling; TB-034/TB-037 verify both equipment-set availability before final checklist closure. |
| Personal/default choices | Do not branch spouse, children, stewards, followers, pets, mounts, Black Book powers, or similar personal choices from checklist presence alone. | TB-031D chooses route-affecting defaults; TB-035 writes option-list presentation. |
| TB-031B quest source-readiness rows | Do not promote `Rebuilding the Blades`, `Dragon Hunting`, `Archery Practice`, or `Scare My Enemy` without source validation. TB-031F resolved the Blades rows as BR-004 branch content and the Angi/Hired Muscle rows as source-backed main-route handling. | TB-031F complete; TB-031H audited owner labels. |

## Updated Objective Dispositions

| Objective | New treatment | Reason |
| --- | --- | --- |
| `OBJ-000048` Thieves Guild City Influence and Side Job Counter | Main-route dependency-flexible counter. | The 125-job boundary is required completionist counter coverage; TB-031F resolved the mechanics. |
| `OBJ-000455` Retaking Thirsk | Main-route windowed row. | Nord side is canonical after branch hard-save/reload handling. |
| `OBJ-000456` through `OBJ-000459` Thirsk favors | Main-route dependency-flexible rows. | Nord-side favor/service coverage belongs to canonical continuity. |
| `OBJ-000574` The Pit | Branch-route branch-only row. | Power path is a Bittercup alternate branch; Fortune remains canonical. |
| `OBJ-001607` Aetherial Crown | Main-route windowed row. | Crown is the canonical Aetherium Forge reward. |
| `OBJ-001608` Ring of Hircine | Main-route windowed row. | Single-artifact Ring outcome is canonical; Savior's Hide remains a reward branch. |

## Non-Decisions

| Area | Why not resolved here |
| --- | --- |
| Exact route steps for radiants/counters | TB-031C decides escalation only. TB-031F handles counter mechanics and TB-034/TB-035 write route prose. |
| Exact spouse/family/steward/default choices | These choices affect logistics and final continuity, so TB-031D owns them. |
| Exact source-readiness validation | TB-031H completed the source/objective/support readiness audit after TB-031D through TB-031G touched their rows; TB-031J then completed the row-level source-readiness mappings and exclusions. |
| Final checklist proof | TB-033 validated branch restoration and coverage at the prototype level; TB-037 validates objective completion and final coverage after route/default/progression decisions are fully integrated. |
