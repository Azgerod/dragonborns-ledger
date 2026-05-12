# Location Route Validation

Status: TB-031G complete as a route-planning validation layer.

Scope: this file does not write final route prose or pathfinding. It records how location rows must be interpreted after TB-032 warnings and TB-033 validation, and before TB-034 route placement uses location counts.

Source support: SN-000128 plus the source notes named below.

## Output Summary

| Area | TB-031G decision | Later owner |
| --- | --- | --- |
| Delver / clearable rows | Source-listed clearable rows count for `Delver` when they increment `Dungeons Cleared`; Angarvunde and Mistwatch remain atypical non-counting clears. | TB-033 validated prototype handling; TB-034/TB-037 validate final counter totals. |
| Clear trigger wording | Normal clearables should be routed until the in-game `Cleared` tag appears, usually after boss defeat; active `Kill the Bandit Leader` targets may require report-back before the tag. | TB-032 warning placement; TB-034 final steps. |
| Explorer / discovery rows | Source-listed discoverable rows are independent discovery/checklist rows. Duplicate markers can count for Explorer but not as extra Delver clears. | TB-033 validated prototype handling; TB-034 places route order; TB-037 validates `Locations Discovered`. |
| Secondary cleared markers | Giant's Grove, Klimmek's House, Shalidor's Maze, and Sundered Towers are not independent Delver clears. | TB-034 may mention only where parent route naturally visits them. |
| The Chill checklist row | Explicitly excluded from required route/discovery coverage because official Skyrim has no map marker; the marker is USKP-only. | TB-036/TB-037 audit exclusion. |
| AE content locations | Remain parent-quest/property/content coverage, not independent Delver rows. Exact route use follows Creation, quest, branch, or property timing. | TB-032/TB-034/TB-037. |
| Coordinate exceptions | Multi-marker, proxy, no-marker, and separate-worldspace rows have route-use rules; do not treat straight-line corridor placement as final access. | TB-034 final placement. |

## Counter Rules

| Rule | Route-planning treatment | Source notes |
| --- | --- | --- |
| Normal clearable locations | Clear until the in-game map shows `Cleared`. If the row is being used for `Delver`, verify the `Dungeons Cleared` statistic increments unless the row is one of the documented exceptions. | SN-000077; SN-000128 |
| Boss/quest trigger | Boss defeat is the normal trigger class. If the location is a `Kill the Bandit Leader` radiant target, do not expect the `Cleared` tag until report-back. | SN-000077; SN-000128 |
| Angarvunde | Route as a clearable/completion location, but do not count it for `Delver`. Its clear state is tied to the related quest/word-wall state and has a no-Delver-count bug note. | SN-000077; SN-000128 |
| Mistwatch | Route as a clearable/completion location, but do not count it for `Delver`. Its clear state is tied to the related quest outcome and has a no-Delver-count bug note. | SN-000077; SN-000128 |
| Source-listed discoverable rows | Treat as map-marker discovery rows for `Locations Discovered` and `Explorer`, whether or not they are clearable. | SN-000078; SN-000128 |
| Duplicate map markers | Route as independent discovery markers when needed for Explorer/checklist proof, but tie clearance to the single primary clearable location. | SN-000079; SN-000128 |
| Secondary cleared markers | Do not route as independent clears and do not count for Delver; they inherit a visible cleared tag from the primary location. | SN-000079; SN-000128 |

## Exception Register

| Location row | Route validation | Primary / parent location | Route-block implication |
| --- | --- | --- | --- |
| Angarvunde | Atypical clear; does not increment `Dungeons Cleared` or count for Delver. | Angarvunde quest / word-wall state. | Route for dungeon, word wall, and checklist value, not Delver padding. |
| Mistwatch | Atypical clear; does not increment `Dungeons Cleared` or count for Delver. | Mistwatch quest outcome. | Route for quest/location value, not Delver padding. |
| Giant's Grove | Secondary clear; not an independent Delver clear. | Fallowstone Cave. | Route only through `The Cursed Tribe` / Fallowstone context. |
| Klimmek's House | Secondary cleared-marker caveat; not an independent clear/discovery target. | Shroud Hearth Barrow. | Do not route as map-marker or Delver objective. |
| Shalidor's Maze | Secondary clear; not an independent Delver clear. | Labyrinthian. | Route only when Labyrinthian/maze content is intentionally placed. |
| Sundered Towers | Secondary clear; not an independent Delver clear. | Red Eagle Redoubt. | Route only as part of Red Eagle/Reach handling. |
| North/South Brittleshin Pass | Duplicate markers; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Brittleshin Pass. | Choose entrance by route leg; do not double-count Delver. |
| North/South Cold Rock Pass | Duplicate markers; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Cold Rock Pass. | Choose entrance by route leg; do not double-count Delver. |
| North/South Shriekwind Bastion | Duplicate markers; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Shriekwind Bastion. | Choose entrance by route leg; do not double-count Delver. |
| North/South Skybound Watch | Duplicate markers; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Skybound Watch Pass. | Choose entrance by route leg; do not double-count Delver. |
| Lower Steepfall Burrow | Duplicate marker; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Steepfall Burrow. | Treat as an entrance/discovery marker, not a separate clear. |
| Reachcliff Secret Entrance | Duplicate marker; Explorer/discovery can count separately, but Delver/clear count is one parent dungeon. | Reachcliff Cave. | Treat as an entrance/discovery marker, not a separate clear. |
| Skuldafn | Separate quest worldspace with no normal route-comparable exterior marker. | Main quest Skuldafn access. | G13/manual expedition; do not route from Skyrim corridor distance. |
| Deadlands | Separate Creation worldspace reached through The Cause / Oblivion Gate access. | Red Scar Cavern / `The Consequences`. | G13/manual expedition; do not route from Skyrim corridor distance. |
| Crowstooth's Camp | Discoverable checklist/source row with no matching Gamemap coordinate. | Relative directions only. | Route from source directions if needed; no straight-line corridor calculation. |
| Mythic Dawn Camp | Unmarked, quest-stage-gated camp; no map marker even after it appears. | `The Cause` stage 60 / Rielle path. | Route only as The Cause quest content, not Explorer. |
| The Chill | Official unmarked Winterhold jail; USKP-only map marker. | Winterhold arrest/jail or manual visit. | Excluded from required discovery/clear coverage under official PS4 AE scope. |

## AE Content Location Treatment

The 16 `content_location` rows are not independent Delver rows. They remain official AE place coverage tied to parent quest, property, or Creation content.

| Location | TB-031G route treatment |
| --- | --- |
| Blackbone Isle Grotto | Parented to Blackbone Isle / Dead Man's Dread quest access; not an independent map-marker or Delver row. |
| Dead Man's Dread | Parent property/ship content after acquisition; route through Blackbone Isle/Grotto access. |
| Deadlands | Separate worldspace reached through The Cause; manual high-risk expedition handling. |
| Fahlbtharz Forge | Solstheim sub-zone of Fahlbtharz opened by Ghosts of the Tribunal content; not a separate exterior marker. |
| Gallows Hall | AE home/property marker; route with acquisition and safe-storage validation, not Delver. |
| Goldenhills Farm Bunkhouse | Goldenhills Plantation sublocation; route with farm/property content. |
| The Guardian Vault | Ratway-linked content location; route with parent quest/item handling. |
| Iron Tusk Cave | Giant's Tooth sublocation; route with island/AE content handling. |
| Ironback Hideout Cellar | Ironback Hideout sublocation; route with parent camp/content. |
| Mythic Dawn Camp | Quest-stage-gated, unmarked; route only as The Cause content. |
| Nchuanthumz | Frostroot Cave/Nchuanthumz content; route with AE home acquisition and access validation. |
| Old Attius Farm Cellar | Old Attius Farm sublocation; route with Solstheim/Creation context. |
| The Pit | Bittercup Power branch-only location. |
| Rielle | The Cause/Rielle marker/content; route with level-gated The Cause handling. |
| Sightless Vault | Sightless Pit/Sunder and Wraithguard content; route with parent dungeon/item handling. |
| Solitude Sewers | Solitude/The Cause content; route with quest access and warning placement. |

## Coordinate and Access Rules

| Coordinate case | Route rule |
| --- | --- |
| `exact_marker` | Usable for broad corridor assignment, but still needs final road/path/quest-state placement. |
| `multi_marker` | Choose the entrance marker that matches the route leg. If the paired marker is a duplicate discovery row, route both only when Explorer/checklist proof needs them. |
| `proxy_marker` | Attach the row to the parent marker or sublocation named in `location-coordinates.csv`; do not treat the proxy as a distinct discovery. |
| `proxy_nearby_landmark` | Use only as approximate route support; final route needs explicit source-direction or parent-location wording. |
| `unmapped_no_marker` | No independent discovery marker. Route only if a quest/content/checklist objective requires the unmarked location. |
| `unmapped_worldspace` | Not distance-comparable to Skyrim/Solstheim exterior corridors. Route through the parent quest or portal/ferry/access model. |

## Catalog Updates

TB-031G updates `location-catalog.csv` so normal source-listed clearable rows have `delver_count_status=counts`, while Angarvunde and Mistwatch remain `atypical_does_not_count`. It also resolves content-location `needs_research` rows into parent-content treatment and corrects Fahlbtharz Forge to Solstheim/Fahlbtharz context.

## Handoffs

| Owner | Remaining work |
| --- | --- |
| TB-031H | Complete: `docs/source-objective-readiness-audit.md` records ownership for remaining broad metadata labels after TB-031G, especially rows that intentionally keep non-final access/path wording. |
| TB-032 | Place concise warnings for location-specific bug, quest-state, cell-entry, branch, and one-shot counter risks. |
| TB-033 | Validate final Delver, Explorer, Solstheim Explorer, and checklist location totals from observed route state. |
| TB-034 | Choose final path/entrance order and turn these validation rules into black-box route steps. |
