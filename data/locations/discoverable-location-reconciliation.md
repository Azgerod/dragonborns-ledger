# Discoverable Location Reconciliation

Status: TB-008B complete; TB-008C duplicate-marker reconciliation complete; TB-008D completeness review complete; downstream location validation pending.

This file summarizes the TB-008B discoverable non-clearable location pass. It is a coordination artifact, not final guide prose.

## Coverage Added

| Area | Rows | Source notes | Notes |
| --- | ---: | --- | --- |
| Discoverable non-clearable location objectives | 209 | `SN-000078` | Added `OBJ-002199` through `OBJ-002407` from UESP discoverable-place category membership after subtracting current clearable-location coverage. TB-008C later reclassified ten of these as duplicate marker rows. |
| Location catalog support rows | 209 | `SN-000078` | Added `LOC-000242` through `LOC-000450` in `data/locations/location-catalog.csv`; 199 remain `discoverable_non_clearable` after TB-008C. |
| Existing clearable rows updated as discoverable-confirmed | 14 | `SN-000078` | Updated clearable catalog rows that were present in the discoverable category but were still marked `needs_research` from the TB-008A page-category harvest. |

## Current Counts

| Field | Count |
| --- | ---: |
| Discoverable non-clearable rows after TB-008C | 199 |
| Duplicate marker rows after TB-008C | 10 |
| Base-game source content among original TB-008B rows | 179 |
| Dawnguard source content | 9 |
| Dragonborn source content | 2 |
| Hearthfire source content | 3 |
| AE Creation source content | 16 |
| Current clearable status among remaining discoverable non-clearable rows | 199 source-listed not clearable |
| Current discoverable status among remaining discoverable non-clearable rows | 199 source-listed discoverable |

## Current Interpretation

`data/objectives/objectives.csv` remains authoritative for routed completion objectives. `data/locations/location-catalog.csv` preserves source-page categories, discovery/clearance status, and later route-validation notes.

The TB-008B rows are source-list inventory rows. They do not settle exact route timing, quest-state access, duplicate marker behavior, Explorer trophy validation, bug risk, or Survival Mode timing.

## Deferred Follow-Up

| Deferred question | Downstream task |
| --- | --- |
| Duplicate entrances, inherited cleared tags, and secondary map markers | Complete in TB-008C |
| Clearable rows lacking discoverable category and discoverable rows with unusual marker behavior | Complete in TB-008C |
| Official DLC/AE location gaps outside current UESP clearable/discoverable category coverage | Complete in TB-008C for AE Creation Club place category gaps; TB-008D reviews remaining location completeness. |
| Explorer and Delver PS4 trophy behavior | TB-015 |
| Location bugs, marker state issues, and quest/faction access caveats | TB-017 |
| Survival Mode geography, shelter, cold, carry, rest, and route clustering | TB-019 and route prototype passes |
| Checklist row mapping for location discovery and clearance | TB-031B/TB-031F |
