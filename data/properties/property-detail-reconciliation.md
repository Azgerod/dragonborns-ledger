# Property Detail Reconciliation

Status: in progress.

This file summarizes the TB-007G3 property-detail expansion. It is a coordination artifact, not final guide prose.

## Coverage Added

| Area | Detail rows | Source notes | Notes |
| --- | ---: | --- | --- |
| City homes and Severin Manor | 49 | `SN-000074` | Covers five city-home purchase summaries, city-home furnishing/upgrades, child-bedroom tradeoffs, housecarl quarters, display/storage features, and Severin Manor facilities. |
| Hearthfire homesteads, construction, and services | 54 | `SN-000075` | Covers three land summaries, construction modules, exterior additions, wing choices, steward furnishing costs, materials, household services, livestock, horse service, and a downstream bug-warning row. |
| AE homes and Goldenhills Plantation | 24 | `SN-000076` | Covers AE home feature summaries plus Goldenhills ownership, interior upgrades, exterior farm construction, farmhand/livestock/horse services, crops, income, and pantry output. |

Total property-detail rows: 127.

## Current Interpretation

`data/objectives/objectives.csv` remains authoritative for completion objectives. `data/properties/property-details.csv` is supporting member-level data for later route placement, material planning, safe-storage validation, display/checklist audit, and service/default recommendations.

`source_lists_safe_home_storage` and related storage values are not final safe-storage recommendations. They mean the source describes the property as player housing or storage-bearing; route-safe storage still needs the later Survival Mode, bug, and warning passes.

## Deferred Follow-Up

| Deferred question | Downstream task |
| --- | --- |
| Exact purchase/acquisition timing and economy pacing | Route rigidity, economy/crafting, and route skeleton passes |
| Hjerim, Honeyside, Hearthfire, Goldenhills, and AE-home bug mitigations | TB-017 bug-prone quests and warning layer |
| Hearthfire wing defaults and child-bedroom/display tradeoffs | Role/default recommendation and route placement passes |
| Safe storage recommendations by property/container | TB-019 Survival Mode and warning/safe-storage validation |
| Collection display use and checklist synchronization | Checklist mapping and final coverage QA |
| Farm crop policy, farmhand/steward defaults, and income/pantry bounds | NPC dependency, Survival Mode, and radiant/repeatable-boundary passes |
