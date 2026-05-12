# Route Rigidity Classification Notes

Status: TB-022 complete.

These notes document how TB-022 classified `routing_rigidity` and filled remaining `route_placement` gaps in `data/objectives/objectives.csv`. They are not route prose and do not add new gameplay facts.

## Boundaries

* The classification is a planning layer, not final route order.
* Source-backed Phase 2 constraint tables override broad category defaults.
* Rows with unresolved branch defaults are classified for branch-matrix handling now; TB-028 may later promote one outcome to `main_route` after choosing the default.
* Rows that only aggregate child/member coverage are classified as tracking rows, not new route steps.
* No new online gameplay research was performed for this pass.

## Direct Constraint Rules

| Pressure | Classification rule |
| --- | --- |
| Confirmed leveled reward, cell-entry, location-spawn, quest-start, or corpse-appearance lock | `fixed_late`, unless the row is a random reward or unresolved choice window. |
| Civil War, Dawnguard, Dark Brotherhood, Paarthurnax, Daedric, Aetherial, Thirsk, AE outcome, or other hard-save branch matrix | `windowed` for canonical/main rows; `branch_only` for known alternate-only branch rows. |
| Source-backed failure-state repair quest or forced random event | `excluded_unbounded`. |
| Source-backed representative or required radiant | `dependency_flexible`, `region_flexible`, or `windowed` according to the constraint table boundary. |
| Trophy/counter parent row that does not itself create early route order | `cleanup_safe`, except Daedric artifact trophy tracking remains `windowed`. |

## Category Defaults

| Row type | Default used when no tighter constraint applied |
| --- | --- |
| Quest/document and AE document title rows | `main_route` / `dependency_flexible`, because the current scope includes quest and AE books while exact copy/location choice is later work. |
| Collectible member rows | `main_route` / `region_flexible`, because route insertion should occur when the regional route is nearby. |
| Collectible set parent rows | `main_route` / `cleanup_safe`, because the parent row verifies member completion rather than creating a separate route step. |
| Standard location rows | Kept as already classified by the location/geography support layer. |
| Ordinary unique item rows without a known level, branch, cell, or bug constraint | `main_route` / `dependency_flexible`, because exact acquisition source and preservation handling remain later route work. |
| AE package rows | Classified from `data/constraints/ae-creation-start-triggers.md`: hard/prerequisite gates become `fixed_late`, outcome-sensitive packages become `windowed`, vendor/crafting/Solstheim/infrastructure packages become `dependency_flexible`, and region-only packages become `region_flexible`. |
| AE child quest/item/system rows | Inherit only hard gate or branch pressure from the parent package; otherwise use `dependency_flexible` until child-level route insertion. |
| Local miscellaneous/favor rows without special constraints | `region_flexible`. |
| Skill, perk, crafting, property, NPC/service, pet, mount, and relationship rows | Kept as already classified unless they were still unclassified; remaining unclassified support-set rows use `dependency_flexible`. |

## Explicit Conservative Placements

| Objective | Placement | Reason |
| --- | --- | --- |
| `OBJ-000439` Skaal Village Dialogue | `appendix` / `cleanup_safe` | Source-list dialogue tracker with no independent route boundary until checklist mapping. |
| `OBJ-000466` Black Book miscellaneous tracker | `appendix` / `cleanup_safe` | Duplicate tracker for individual Black Book rows. |
| `OBJ-000692` Plague of the Dead Zombie System | `appendix` / `cleanup_safe` | System-awareness row; arbitrary zombie encounters are not finite objectives. |
| `OBJ-000125` Rejoining the College | `excluded` / `excluded_unbounded` | Failure-state repair quest. |
| `OBJ-000161` Honor Thy Family | `excluded` / `excluded_unbounded` | Failure-state repair quest. |
| `OBJ-000412` Bandit Attack | `excluded` / `excluded_unbounded` | Forced Hearthfire random event is not required; resolve only if it occurs naturally. |

## Handoffs

* TB-023 and TB-024 should use fixed early, fixed late, and windowed rows as anchor candidates, not as final sequence.
* TB-025 should use `region_flexible` rows with `data/locations/location-geography.csv` rather than hold-level grouping.
* TB-026 should insert flexible rows only after route anchors and Survival geography exist.
* TB-028 should revisit unresolved branch-matrix reward rows and promote exactly the chosen canonical rewards/objectives to `main_route`.
