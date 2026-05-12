# Source Note: Location Marker and Gap Reconciliation

Status: needs review.

Source note ID: SN-000079

## Claim

UESP identifies several location marker cases that need reconciliation rather than normal clearable/discoverable treatment: secondary cleared markers, duplicate map-marker entrances, clearable rows without separate discoverable category membership, and AE Creation place pages outside the current clearable/discoverable category union.

## Routing Relevance

The specification requires all map-marked locations discovered, all clearable locations cleared where possible, and official AE Creation locations covered. Without this reconciliation, the database could double-count duplicate entrance markers, treat inherited cleared tags as independent Delver clears, or omit AE Creation place pages that are neither source-listed as clearable nor discoverable.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Secondary cleared markers, duplicate map-marker cases, Angarvunde/Mistwatch caveat, and Delver/Explorer context. |
| SRC-000264 | Category:Skyrim-Places-Clearable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Clearable | 2026-05-12 | Clearable category membership used to find clearable rows requiring marker reconciliation. |
| SRC-000265 | Category:Skyrim-Places-Discoverable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Discoverable | 2026-05-12 | Discoverable category membership used to find duplicate marker rows and unresolved clearable rows. |
| SRC-000266 | Category:Skyrim-Creation Club-Places | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Places | 2026-05-12 | AE Creation place pages used to find location pages not covered by clearable/discoverable category rows. |
| SRC-000267 | Skyrim:Klimmek's House | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Klimmek%27s_House | 2026-05-12 | Place-page categories for the secondary cleared-marker row. |

## Evidence Summary

The UESP Dungeons page distinguishes normal dungeon clearing from special marker cases. It states that some secondary locations can display a cleared tag when an associated primary location is cleared, but those secondary locations do not increment the Dungeons Cleared statistic or count toward Delver. The page lists Giant's Grove, Klimmek's House, Shalidor's Maze, and Sundered Towers as examples.

The same Dungeons page states that several locations have two map markers and can count twice toward Explorer while still counting only once toward the Dungeons Cleared statistic. The listed cases are North/South Brittleshin Pass, North/South Cold Rock Pass, North/South Shriekwind Bastion, North/South Skybound Watch Pass, Lower Steepfall Burrow, and Reachcliff Secret Entrance.

The TB-008C harvest compared UESP clearable, discoverable, and Creation Club place category membership. It reclassified existing duplicate marker rows instead of adding new clear objectives, marked the remaining clearable rows lacking discoverable-category membership as source-listed not discoverable for this stage, and added 16 AE Creation place rows that were present in the Creation Club places category but absent from the current clearable/discoverable catalog.

## Confidence and Open Questions

Confidence is high for category membership and named marker special cases as fetched on 2026-05-12. This note does not settle PS4 trophy behavior, exact quest-state access, bug mitigation, or route order.

Open questions for later validation:

* exact Delver and Explorer trophy behavior on PS4 AE;
* whether any AE Creation place page should become a routed discovery/clearance objective after per-page validation;
* whether checklist mapping expects unmarked AE interiors as checklist rows or appendix-only coverage;
* exact primary-location linkage for inherited cleared-marker rows;
* route-safe timing for Skuldafn, Civil War camps, and quest/faction-dependent markers.

## Linked Records

`data/locations/location-catalog.csv`; `data/locations/location-reconciliation.md`; updated marker rows plus `OBJ-002408` through `OBJ-002424`.
