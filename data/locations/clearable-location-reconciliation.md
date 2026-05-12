# Clearable Location Reconciliation

Status: TB-008A complete; TB-008C marker reconciliation complete; TB-008D completeness review complete; downstream per-location validation pending.

This file summarizes the first TB-008 location pass. It is a coordination artifact, not final guide prose.

## Coverage Added

| Area | Rows | Source notes | Notes |
| --- | ---: | --- | --- |
| Source-listed clearable location objectives | 241 | `SN-000077` | Added `OBJ-001958` through `OBJ-002198` from UESP clearable-place category membership after excluding User-namespace category members. TB-008C later reclassified three of these as secondary marker caveats. |
| Location catalog support rows | 241 | `SN-000077` | Added `LOC-000001` through `LOC-000241` in `data/locations/location-catalog.csv`. |

## Current Counts

| Field | Count |
| --- | ---: |
| Independent clearable rows after TB-008C | 238 |
| Base-game source content among independent clearable rows | 216 |
| Dawnguard source content | 4 |
| Dragonborn source content | 18 |
| Also source-listed as discoverable by UESP category after TB-008B cross-check | 233 |
| Clearable rows not separately source-listed as discoverable after TB-008C | 7 |
| Reclassified secondary marker caveats | 3 |
| Atypical non-counting Delver status from UESP Dungeons note | 2 |
| Delver count still needing validation among independent clearable rows | 236 |

## Rows Needing Discoverable/Map-Marker Reconciliation

These source-listed clearable rows did not carry UESP's discoverable-place category during the TB-008A harvest. They may still matter for route clearance, but their map-marker/discovery treatment needs a later TB-008 pass:

After TB-008C, the remaining independent clearable rows not separately source-listed as discoverable are:

Brittleshin Pass; Cold Rock Pass; Coldcinder Cave; Mara's Eye Den; Nchuand-Zel; Skuldafn; Skybound Watch Pass.

Brittleshin Pass, Cold Rock Pass, and Skybound Watch Pass now have separate duplicate marker rows for their north/south markers. Shalidor's Maze was reclassified as a secondary marker caveat.

## Current Interpretation

`data/objectives/objectives.csv` remains authoritative for routed completion objectives. `data/locations/location-catalog.csv` preserves source-page categories, discoverable status, clearable status, Delver-count uncertainty, and route-validation notes.

The TB-008A rows are source-list inventory rows. They are not final route instructions and do not settle exact clear triggers, duplicate marker behavior, trophy counting, bug risk, or Survival Mode timing.

## Deferred Follow-Up

| Deferred question | Downstream task |
| --- | --- |
| Non-clearable discoverable/map-marked locations | TB-008B |
| Duplicate entrances, inherited cleared tags, and secondary map markers | Complete in TB-008C |
| Exact boss/quest clear triggers per location | Downstream per-location validation; TB-017 where bug or warning handling is needed |
| Delver/Explorer PS4 trophy behavior and count validation | TB-015 |
| Survival Mode geography, shelter, cold, carry, rest, and route clustering | TB-019 and route prototype passes |
| Checklist row mapping for location discovery and clearance | TB-030 |
