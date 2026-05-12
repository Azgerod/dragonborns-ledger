# Source Note: Location Route Validation

Status: researched; TB-031G location route-validation layer added.

Source note ID: SN-000128

## Claim

TB-031G can resolve the route-planning mechanics for location discovery, dungeon clearing, duplicate markers, secondary cleared markers, unmarked checklist locations, and separate/proxy worldspace location rows without writing final pathfinding prose.

## Routing Relevance

The route must not infer `Delver`, `Explorer`, or checklist location completion from broad corridor membership alone. Later route prose needs to know which rows count as independent discoveries, which rows count toward Delver, which markers are duplicate or inherited, which content locations follow parent quests, and which rows remain manual access cases.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Clearing rule, Delver relation, Angarvunde/Mistwatch caveat, duplicate marker and secondary marker caveats. |
| SRC-000264 | Category:Skyrim-Places-Clearable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Clearable | 2026-05-12 | Source-listed clearable locations. |
| SRC-000265 | Category:Skyrim-Places-Discoverable | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Places-Discoverable | 2026-05-12 | Source-listed discoverable map-marker locations and Explorer relation. |
| SRC-000423 | UESP Gamemap Skyrim marker endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_locs&db=sr&world=1 | 2026-05-12 | Marker coordinates and exact/proxy/multi-marker route support. |
| SRC-000424 | UESP Gamemap Skyrim world endpoint | 2 - UESP | https://gamemap.uesp.net/db/gamemap.php?action=get_worlds&db=sr | 2026-05-12 | Worldspace separation for non-comparable route coordinates. |
| SRC-000433 | Skyrim:The Chill | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Chill | 2026-05-12 | Official unmarked Winterhold jail and USKP-only marker note. |
| SRC-000434 | Skyrim:Giant's Grove | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Giant%27s_Grove | 2026-05-12 | Secondary clear inherited from Fallowstone Cave. |
| SRC-000435 | Skyrim:Shalidor's Maze | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shalidor%27s_Maze | 2026-05-12 | Secondary clear inherited from Labyrinthian. |
| SRC-000436 | Skyrim:Sundered Towers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sundered_Towers | 2026-05-12 | Secondary clear inherited from Red Eagle Redoubt. |
| SRC-000437 | Skyrim:Angarvunde | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Angarvunde | 2026-05-12 | Atypical clear and no Delver-count bug. |
| SRC-000438 | Skyrim:Mistwatch | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mistwatch | 2026-05-12 | Atypical clear and no Delver-count bug. |
| SRC-000439 | Skyrim:Mythic Dawn Camp | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mythic_Dawn_Camp | 2026-05-12 | Stage-gated camp, mountain-path access, and no map marker. |
| SRC-000440 | Skyrim:The Pit (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pit_(place) | 2026-05-12 | Bittercup Power-only access. |
| SRC-000441 | Skyrim:Deadlands | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Deadlands | 2026-05-12 | Separate worldspace, Oblivion Gate access, and post-quest return. |
| SRC-000442 | Skyrim:Fahlbtharz | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fahlbtharz | 2026-05-12 | Solstheim Fahlbtharz placement and Fahlbtharz Forge sub-zone. |

## Evidence Summary

UESP's dungeon-clearing rule says most clearable dungeons receive the in-game `Cleared` tag after the location boss is defeated. It also states that a cleared dungeon can still contain enemies or loot, so final route validation must watch for the `Cleared` tag and, when using a location for `Delver`, the `Dungeons Cleared` statistic rather than assuming a sweep is complete from room traversal alone.

UESP identifies two atypical clearable locations, Angarvunde and Mistwatch. Angarvunde is marked cleared through the related quest/word-wall state rather than a normal boss kill and does not increment `Dungeons Cleared` or count for `Delver`. Mistwatch is marked cleared when its related quest is completed, either through the boss-kill path or the dialogue resolution path, and likewise does not increment `Dungeons Cleared` or count for `Delver`.

UESP also identifies two marker classes that must not be treated as independent Delver clears. Duplicate map-marker entrances can count separately for `Explorer`/locations discovered while still counting only once for the Dungeons Cleared statistic. Secondary cleared markers, including Giant's Grove, Klimmek's House, Shalidor's Maze, and Sundered Towers, can show a `Cleared` tag inherited from a primary location but do not increment `Dungeons Cleared` or count for `Delver`.

The discoverable-place category states that discoverable places are separate in-game map markers that count toward `Locations Discovered` and the `Explorer` achievement. TB-031G therefore treats source-listed discoverable rows as discovery/checklist rows, not necessarily clear rows.

The Chill is an official unmarked Winterhold jail. UESP notes that a map marker was added by the Unofficial Skyrim Patch, but the project scope is official PS4 Anniversary Edition content, not USKP. TB-031G therefore excludes the checklist-only `The Chill*` row from required route/discovery coverage while preserving the source note for audit.

UESP Gamemap coordinates remain route-support data rather than pathfinding. Exact markers may be used for broad corridor placement; multi-marker rows require choosing an entrance based on the route leg; proxy rows follow their parent marker or nearby landmark; no-marker rows do not count as independent map-marker discoveries; and separate-worldspace rows such as Skuldafn and Deadlands require parent-quest access rather than Skyrim/Solstheim straight-line routing.

## Confidence and Open Questions

Confidence is high for Delver-count class handling, duplicate/secondary marker treatment, The Chill exclusion, and worldspace/proxy route-use policy.

Remaining work is final route placement and validation, not source readiness:

* TB-032 places concise warnings where location entry, quest state, or bug risks matter.
* TB-033 validates final Delver/Explorer/Solstheim Explorer counters against observed in-game/stat behavior.
* TB-034 chooses final entrance/path order and exact route steps.
* TB-031H records remaining metadata-label ownership in `docs/source-objective-readiness-audit.md`; location route placement remains TB-034 work.

## Linked Records

`data/locations/location-route-validation.md`; `data/locations/location-catalog.csv`; `data/locations/location-coordinates.csv`; `data/locations/location-geography.csv`; `data/checklist-mapping/coverage-matrix.csv`; `drafts/route-prototypes/main-route-prototype-v0.md`.
