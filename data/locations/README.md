# Location Data

Status: source-list coverage review complete; downstream validation pending.

Location discovery and clearance tables live here when the objective database needs one row per routed completion unit but the source details need more room than `objectives.csv` should carry.

Use this directory for source-backed map-marker, discoverable-location, clearable-location, duplicate-marker, and location-reconciliation data before route placement chooses when each area is visited.

Do not use this directory for final guide prose.

## Row Policy

Use one objective row for each location completion unit that the guide may need to discover, clear, validate, or exclude. Use the location catalog to preserve source-page categories, clearability/discoverability status, Delver-count uncertainty, and later route-validation notes.

Map-marker discovery and location clearing are related but not identical:

* A clearable location can require later per-page validation for the exact clear trigger.
* A discoverable or map-marked location can be non-clearable and still belong in the location checklist.
* Duplicate entrances, secondary markers, and places whose cleared tag is inherited from a primary location need explicit reconciliation instead of silent duplicate rows.

## Files

* `location-catalog.template.csv` defines the shared header for location catalog tables.
* `location-catalog.csv` records source-listed location rows and their current discovery/clearance status.
* `location-coordinates.template.csv` defines the generated coordinate table header.
* `location-coordinates.csv` records UESP Gamemap numeric marker coordinates, proxy markers, multi-marker cases, and no-marker/worldspace exceptions for catalog locations.
* `location-coordinate-reconciliation.md` summarizes coordinate coverage and distance-use policy.
* `location-geography.template.csv` defines the generated hub/corridor geography table header.
* `location-geography.csv` records derived nearest service candidates, corridor assignments, worldspace access models, cold risk, and barrier flags for coordinate rows.
* `location-geography-reconciliation.md` summarizes the hub/corridor model, seed-node counts, coverage, and distance-use limits.
* `clearable-location-reconciliation.md` summarizes current clearable-location source-list coverage and downstream reconciliation boundaries.
* `discoverable-location-reconciliation.md` summarizes current discoverable non-clearable location coverage and downstream reconciliation boundaries.
* `location-reconciliation.md` summarizes duplicate marker, secondary marker, and AE location-gap reconciliation.
* `location-completeness-review.md` closes the TB-008 source-list coverage review and records remaining downstream validation work.
