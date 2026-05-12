# NPC and Relationship Data

Status: in progress.

This directory holds source-list option tables for NPC, follower, pet, mount, spouse, child, steward, and household-role choices.

`relationship-options.csv` is not route prose. It is a candidate inventory used by later recommendation, checklist, NPC-dependency, and route-placement passes.

TB-031D route-affecting defaults are recorded in `data/route-planning/route-default-decisions.md`. Rows marked `route_treatment=route_default` identify the selected main-route recommendation inside the candidate inventory; other rows remain option-list candidates for TB-035.

Use these conventions:

* Keep one row per source-listed candidate or service option.
* Use objective rows for routed completion units and this table for large option lists.
* Treat `route_treatment=option_list` as non-default option-list coverage after TB-031D unless a later task explicitly reopens the default.
* Treat `route_treatment=route_default` as a planning default, not proof that the role is already available in-game.
* Keep exact route timing, NPC safety, prerequisite validation, and bug handling in the TB-032/TB-033 warning and validation layers, TB-034/TB-035 route/option passes, and the relevant constraint tables rather than this table.
