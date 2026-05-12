# Property Data

Status: active.

Property detail tables live here when a home, farm, upgrade, furnishing, service, display, or safe-storage question needs member-level tracking beyond a single objective row.

Use this directory for source-backed inventories of purchasable upgrades, Hearthfire construction or furnishing details, AE home features, Goldenhills Plantation operations, service options, and storage/display validation.

The objective database remains authoritative for routed completion units. Tables in this directory should support later route placement, material planning, Survival Mode logistics, checklist mapping, and safe-storage decisions.

Do not use this directory for final guide prose.

## Files

| File | Purpose |
| --- | --- |
| `property-details.template.csv` | Header template for property detail rows. |
| `property-details.csv` | Source-backed member/detail rows for city homes, Severin Manor, Hearthfire homesteads, AE homes, and Goldenhills Plantation. |
| `property-detail-reconciliation.md` | Coverage summary and deferred follow-up notes for the property-detail pass. |

## Table Semantics

Each row is a supporting detail, not a new routed completion objective. Use `parent_objective_id` to link the detail back to the authoritative objective row in `data/objectives/objectives.csv`.

Use `route_treatment` to distinguish purchasable upgrades, mutually exclusive room choices, material-planning rows, services, and details that need later validation before route placement.

Safe-storage fields are intentionally conservative. A `source_lists_*` value means the source describes home/storage behavior, not that the final route has already approved the container as a safe storage recommendation.
