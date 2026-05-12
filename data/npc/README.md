# NPC and Relationship Data

Status: in progress.

This directory holds source-list option tables for NPC, follower, pet, mount, spouse, child, steward, and household-role choices.

`relationship-options.csv` is not route prose. It is a candidate inventory used by later recommendation, checklist, NPC-dependency, and route-placement passes.

Use these conventions:

* Keep one row per source-listed candidate or service option.
* Use objective rows for routed completion units and this table for large option lists.
* Treat `route_treatment=option_list` as unresolved until TB-031D chooses defaults or records an explicit option-list handoff.
* Keep exact route timing, NPC safety, prerequisite validation, and bug handling in TB-031D, TB-032, TB-033, and the relevant constraint tables rather than this table.
