# Survival Geography Pass v0

Status: TB-025 complete; downstream route-default, checklist, location-validation, source-readiness, and warning-layer updates refreshed through TB-032.

This is a Phase 6 planning artifact. It reshapes the TB-024 level-gated skeleton around Survival Mode travel, cold, rest, food, carry, storage, and transport pressure. It is not route prose, not a final objective order, and not a flexible-objective insertion pass.

No new gameplay research was performed for this pass. Gameplay facts are carried from the source-backed Survival Mode constraint table, the TB-024 level-gated skeleton, and the hub/corridor geography support layer.

## Inputs

| Input | Use |
| --- | --- |
| `drafts/route-prototypes/level-gated-skeleton-v0.md` | Mandatory level bands `S00` through `S15`, reward gates, branch-gate placement, and TB-025 handoff rules. |
| `drafts/route-prototypes/route-anchors-v0.md` | Structural anchors `A00` through `A21`, especially early Survival stabilization, property infrastructure, Dawnguard, Solstheim, and late cleanup anchors. |
| `data/constraints/survival-mode-constraints.md` | Source-backed Survival rules for hunger, fatigue, cold, sleep-gated level-ups, carry limits, fast-travel restrictions, carriages, ferries, horses, inns, homes, camps, and regional sequencing. |
| `data/locations/location-geography.csv` | Hub/corridor support fields: route cluster, route corridor, nearest corridor hub, carriage origin, ferry terminal, inn/rest point, candidate base, access model, transport flags, cold risk, barrier flags, and confidence. |
| `data/locations/location-geography-reconciliation.md` | Generation notes, counts, and distance policy for the geography layer. |
| `data/route-planning/objective-route-index.csv` | Generated objective workbench for later TB-026 insertion by corridor and constraint state. |
| `data/route-planning/objective-constraints.csv` | Objective-to-constraint links for later route validation before turning any corridor placement into instructions. |

## Boundaries

| Boundary | Rule for later route passes |
| --- | --- |
| This pass groups corridors, not steps. | Do not convert a block below directly into black-box guide instructions. |
| Geography is not hold membership. | Use hub/corridor, worldspace, access model, transport, cold risk, and rest/base fields. Do not group by hold alone. |
| Straight-line support is not pathfinding. | Validate roads, passes, water, quest access, enemy pressure, weather, and exact entrances before route prose. |
| Level gates still win. | Survival convenience cannot cross the TB-024 mandatory gates at levels 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, or 252. |
| Branch defaults are external to this geography pass. | Use TB-028 defaults, TB-029 branch prototypes, and TB-031C checklist escalation decisions rather than choosing branch policy here. |
| Flexible objective insertion is complete at prototype level. | TB-026 inserted safe nearby objective queues into the corridor frame; TB-034 still chooses final step order. |
| Skill/perk/grind detail is block-level only. | TB-027 supplies progression blocks, underleveled fallbacks, and the Legendary reset baseline; TB-031E supplies exact source choices; TB-032 supplies warning triggers; checklist cues and final validation remain later work. |
| Checklist synchronization is complete at prototype/audit level. | TB-030 mapped the raw checklist; TB-031A through TB-031J resolved review buckets, defaults, counters, location validation, source/index readiness, source-readiness rows, and route-affecting checklist decisions before TB-032 warning prose. |

## Terms

| Term | Meaning |
| --- | --- |
| Corridor | Broad geography/travel grouping from `location-geography.csv`; not a route step or proof of practical pathing. |
| Rest point | Inn, home, faction bed, or other support endpoint to validate before the block becomes route prose. |
| Candidate base | Possible future logistics node after acquisition, ownership, safety, and storage validation; not assumed available at block start. |
| Prepared sweep | Remote, cold, mountain, coastal, Solstheim, or separate-worldspace block that needs preflight support before objective insertion. |
| Transport support | Carriage, ferry, horse, stable, road, or gateway context; not automatic fast travel and not proof that the listed service is local. |

## Data Snapshot

| Snapshot | Value |
| --- | ---: |
| Geography support rows | 472 |
| Unique location records covered by geography rows | 467 |
| Unique objective IDs covered by geography rows | 467 |
| Route clusters | 9 |
| Route corridors | 23 |
| Same-worldspace overland rows | 390 |
| Solstheim ferry-gateway rows | 56 |
| Ferry or island access rows | 6 |
| Local or interior subarea rows | 10 |
| Manual/not-comparable rows | 4 |
| Standard cold-risk rows | 278 |
| Regional cold rows | 102 |
| Solstheim cold-region rows | 51 |
| Source-listed cold interior rows | 23 |
| High-elevation or mountain rows | 14 |

Source support: `data/locations/location-geography-reconciliation.md`; `location-geography.csv` rows cite `SN-000124-hub-corridor-geography-support.md`.

## Survival Operating Rules

These rules are the route-shaping assumptions consumed by every geography block below.

| Rule | Route consequence | Source support |
| --- | --- | --- |
| Survival Mode is a main-route baseline after `Unbound`; do not disable/re-enable it or rely on ordinary fast travel. | Every phase needs real travel, rest, food, and recovery planning. | `survival-mode-constraints.md` (`SN-000115`, `SN-000116`) |
| Food, hunger, and hot soups matter before long trips, cold trips, and dungeon chains. | Pair travel blocks with inn, home, farm, campsite, or settlement restock points. Hot soup planning means Fire Salts plus cookable soup ingredients, not generic food alone. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`) |
| Fatigue and level-ups require verified bed planning; outdoor camps are emergency support, not a planning substitute. | Place planned level-ups, crafting, major fights, shrine use, and potion-supported work at a verified proper bed, preferably an inn/home/faction bed. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`) |
| Cold, freezing water, northern weather, mountain routes, and cold interiors can be lethal or route-breaking. | Treat northern, coastal, mountain, cold-interior, and Solstheim blocks as prepared expeditions. | `survival-mode-constraints.md` (`SN-000115`, `SN-000118`) |
| Carry capacity is reduced and AE arrows/lockpicks have weight. | Early storage, sell-off loops, backpacks, horses, followers/pets, and material staging are route infrastructure, not optional flavor. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`) |
| Disease and no natural health regeneration increase expedition recovery pressure. | Add healing and disease-removal support before long dungeons, remote loops, and cold trips where exposure is likely. | `survival-mode-constraints.md` (`SN-000115`) |
| Carriages and boats remain usable, but only major hold capitals are normal carriage origins and minor capitals are not return hubs. | Use carriages for access and cold avoidance, but plan return legs from minor holds by road, horse, ferry, or another verified service. | `survival-mode-constraints.md` (`SN-000116`) |
| Ferries shape the coast and Solstheim; Solstheim has no carriage network. | Coastal and island routes must be ferry-centered, with Raven Rock as the first Solstheim anchor. | `survival-mode-constraints.md` (`SN-000116`, `SN-000118`) |
| Homes, farms, and Hearthfire services are logistics nodes. | Property timing should support safe storage, beds, cooking, crafting, carriages, horses, and heavy material movement. | `survival-mode-constraints.md` (`SN-000116`, `SN-000117`) |

## Corridor Support Register

This table is the geography backbone for TB-026. It is a support register only. Corridors with cold-risk rows need preparation even if their nearest service point looks close in straight-line data. Candidate bases are possible later nodes after acquisition and storage validation, not guaranteed current rest/storage.

| Cluster | Corridor | Rows | Primary hub | Rest point | Candidate base | Transport support | Cold profile |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| central_skyrim | `riverwood_helgen_road` | 17 | Riverwood | Sleeping Giant Inn | Lakeview Manor | Whiterun carriage/stable access; no local ferry support. | Mostly standard; one mountain/high row. |
| central_skyrim | `rorikstead_western_road` | 20 | Rorikstead | Frostfruit Inn | Goldenhills Plantation | Carriage-backed from Whiterun; no local ferry support. | Standard. |
| central_skyrim | `whiterun_central_plains` | 28 | Whiterun | The Bannered Mare | Breezehome | Whiterun carriage/stable access; no local ferry support. | Mostly standard; three regional-cold rows. |
| southern_skyrim | `falkreath_pine_forest` | 35 | Falkreath | Dead Man's Drink | Lakeview Manor | Whiterun carriage origin to Falkreath; no local ferry support. | Mostly standard; some mountain/high and cold-interior rows. |
| southern_skyrim | `ivarstead_rift_pass` | 29 | Ivarstead | Vilemyr Inn | Shadowfoot Sanctum | Riften/Whiterun road access; no local ferry support. | Standard core with mountain/pass and cold-interior rows. |
| southeast_skyrim | `riften_rift` | 41 | Riften | The Bee and Barb | Shadowfoot Sanctum | Riften carriage/stable access; no local ferry support. | Mostly standard; several mountain/high rows. |
| southeast_skyrim | `dayspring_canyon` | 3 | Fort Dawnguard | The Bee and Barb | Honeyside | Riften carriage/stable access, then canyon approach. | Small Dawnguard corridor; includes one mountain/high row. |
| western_skyrim | `markarth_reach` | 19 | Markarth | Silver-Blood Inn | Vlindrel Hall | Markarth carriage/stable access; ferry only if an objective explicitly requires Icewater validation. | Standard, but road/pass validation still required. |
| western_skyrim | `old_hroldan_reach_road` | 20 | Old Hroldan Inn | Old Hroldan Inn | Vlindrel Hall | Markarth carriage/stable access, then road-inn loop. | Standard, road-inn expedition corridor. |
| eastern_skyrim | `kynesgrove_eastmarch_road` | 29 | Kynesgrove | Braidwood Inn | Gallows Hall | Windhelm carriage/stable support; ferry only for specific coastal/Solstheim objectives. | Standard. |
| eastern_skyrim | `windhelm_eastmarch` | 18 | Windhelm | Candlehearth Hall | Hjerim | Windhelm carriage/stable and ferry hub. | Mixed standard/regional cold plus one cold interior. |
| northwest_skyrim | `solitude_haafingar` | 20 | Solitude | The Winking Skeever | Proudspire Manor | Solitude carriage and ferry hub. | Mostly regional cold. |
| northwest_skyrim | `dragon_bridge_haafingar_road` | 23 | Dragon Bridge | Four Shields Tavern | Proudspire Manor | Solitude carriage origin, then road loop; ferry only for specific coastal objectives. | Mixed standard/regional cold. |
| northwest_skyrim | `morthal_marsh` | 29 | Morthal | Moorside Inn | Myrwatch | Solitude carriage origin to Morthal; ferry only for specific coastal objectives. | Mostly standard with regional-cold and cold-interior rows. |
| northwest_skyrim | `icewater_volkihar_ferry` | 15 | Icewater Jetty | Four Shields Tavern | Dead Man's Dread | Ferry/coast corridor: Icewater Jetty, Castle Volkihar, and related coastal access. | Ferry/coast corridor with regional cold and cold-interior risk. |
| northern_skyrim | `dawnstar_pale_coast` | 19 | Dawnstar | Windpeak Inn | Bloodchill Manor | Carriage destination and Dawnstar ferry support; validate return leg. | Regional cold plus cold interiors. |
| northern_skyrim | `nightgate_pale_pass` | 28 | Nightgate Inn | Nightgate Inn | Bloodchill Manor | Road-inn pass; carriage/ferry support is regional, not local. | Regional cold plus cold interiors. |
| northern_skyrim | `winterhold_coast` | 19 | Winterhold | The Frozen Hearth | Bloodchill Manor | Carriage destination; no local ferry origin and return leg needs validation. | Regional cold plus cold interiors. |
| solstheim | `raven_rock_west` | 22 | Raven Rock | The Retching Netch | Severin Manor | Raven Rock ferry; no carriages | Solstheim cold plus one cold interior. |
| solstheim | `thirsk_central` | 16 | Thirsk Mead Hall | The Retching Netch | Severin Manor | Raven Rock ferry; no carriages | Solstheim cold plus one cold interior. |
| solstheim | `skaal_north` | 14 | Skaal Village | The Retching Netch | Severin Manor | Raven Rock ferry; no carriages | Solstheim cold plus cold interiors. |
| solstheim | `tel_mithryn_east` | 4 | Tel Mithryn | The Retching Netch | Severin Manor | Raven Rock ferry; no carriages | Solstheim cold. |
| manual_validation_required | `manual_validation_required` | 4 | Not comparable | Not comparable | Not comparable | Manual transport validation | Not comparable; do not auto-place by distance. |

## Level-Band Geography Reshape

The TB-024 skeleton remains the level/reward law. This table adds Survival geography pressure to each band.

| Skeleton band | Survival geography role | Preferred corridor pressure | Required support before expansion | Gates preserved |
| --- | --- | --- | --- | --- |
| S00 | Setup only. Establish official AE, trophy-safe scope, Legendary, and Survival baseline. | None. | No travel assumptions. | Setup gate and Survival baseline. |
| S01 | Opening warm-core stabilization. Convert Riverwood/Whiterun from story openers into bed, food, sell-off, craft, and first-storage planning hubs. | `riverwood_helgen_road`, `whiterun_central_plains`. | Verified bed, cooked food, early storage candidate, basic warmth, sell-off route, and first Whiterun protected-entry handling. | First Whiterun entry; no broad cold, mountain, Solstheim, or heavy collection sweeps. |
| S02 | Early transport and carry scaffolding. Use nearby central roads to stabilize without chasing every courier or map marker. | `whiterun_central_plains`, `rorikstead_western_road`, limited `riverwood_helgen_road`. | Mount/carry plan, inn gold, food loop, safe storage, and first vendor/sell-off pattern. | Do not force level-5 AE courier content immediately; do not approach/loot Silent Moons before level 8. |
| S03 | First low-level gate band. Add only tightly supported nearby travel; do not let new warnings turn into broad route spread. | Central corridors plus carefully staged `falkreath_pine_forest` or `rorikstead_western_road` if needed. | Same as S02 plus explicit return bed/rest point and NPC-risk check. | Level 8 Silent Moons gate; level-9 Largashbur and Falkreath caveats remain warnings, not automatic actions. |
| S04 | Early-mid regional expansion. Start using warm/southern/southeast spokes, but keep cold and high-risk AE/Daedric content prepared rather than automatic. | `falkreath_pine_forest`, `riften_rift`, `ivarstead_rift_pass`, `kynesgrove_eastmarch_road`, `markarth_reach` only when power and support allow. | Reliable storage, horse or equivalent carry relief, cooked food and hot soup ingredients, inn endpoints, and sell-off loops. | Eligible Daedric/AE gates do not override branch, power, geography, or warning validation. |
| S05 | Controlled faction and Septimus staging window. Treat any north or Dwemer-linked travel as expedition planning, not casual map cleanup. | City/faction hubs plus prepared `nightgate_pale_pass` or other cold/mountain corridors only if the quest state demands it. | Verified bed before major dungeon chains, carry space, food and hot soup ingredients, return bed, and no long dangling Oghma/cube state. | Bards instruments uncollected before assignment; Oghma read/use timing follows the late TB-027 progression policy and exact TB-031E source/checklist timing. |
| S06 | Property/artifact infrastructure band. Favor property, storage, carriage, horse, and food systems that reduce later route cost. | Central/southern/southeast/western corridors, with Dawnstar/Heljarchen pressure only after its gate is valid. | Safe-storage validation, material-staging plan, property bug checks, and steward/carriage evaluation before heavy construction loops. | Level 20/22 gates; Helvard/Lakeview and Whiterun/Dawnstar NPC dependencies preserved. |
| S07 | First major reward-threshold band. Route geography can deepen factions, but it cannot open level-36 linked dungeons early. | Warm and city-backed corridors; College/Winterhold depth remains constrained until the linked-dungeon gate is safe. | Verified proper bed for level-ups/crafting, cold kit before any Winterhold/Pale travel, carry emptying before reward dungeons. | Level 25 Mage's Circlet; level 27 Pale Blade; no `Trinity Restored` before 32; no `Lost Legends` or linked-dungeon approach before 36, including Saarthal under the current Phase 2 constraint. |
| S08 | Nightingale armor-safe band. Use this as a midgame corridor consolidation point, not a signal to finish all Thieves rewards. | Riften/southeast and central/warm loops; cold corridors only in prepared sweeps. | Return base, food and hot soup ingredients, sell-off, and sleep-before-level checks. | Level 32 starts `Trinity Restored` eligibility only; Nightingale Blade/Bow and other source-tier rewards still wait for 46 if conservative policy is kept. |
| S09 | Level-36 linked-dungeon band. Now geography may group Forbidden Legend-linked travel, but it must still respect cold, mountain, and corridor endpoints. | `morthal_marsh`, `ivarstead_rift_pass`, `western_skyrim`, `winterhold_coast` only as prepared loops tied to beds. | Warmth kit, verified bed before and after long dungeons, carry space, and verified exit/rest path. | Do not take Shield of Solitude before 40; do not enter Sky Haven or Riftweald before 46. |
| S10 | Shield of Solitude-safe preparation band. Build city, Civil War, main-quest, ferry, and late-faction logistics without crossing 46 gates. | `solitude_haafingar`, `dragon_bridge_haafingar_road`, `morthal_marsh`, `windhelm_eastmarch`, plus warm support loops. | Carriage/ferry cash, coastal cold kit, bed endpoint, storage/sell-off before faction chains. | Level 40 Shield of Solitude; Sky Haven, Riftweald, Chillrend, Dragonbane, and source-tier Nightingale rewards remain closed until 46. |
| S11 | Maximum-tier classic reward and major expedition band. Open late classic reward corridors and begin Dawnguard/Solstheim only with logistics established. | `markarth_reach`/Sky Haven access, `riften_rift`/Riftweald access, `dayspring_canyon`, `icewater_volkihar_ferry`, `windhelm_eastmarch`, initial `raven_rock_west` if supported. | Full expedition kit: verified bed, hot soup ingredients, healing/cure resources, carry relief, ferry planning, storage return, and hard-save branch anchors. | Level 46 gates opened; final Miraak remains locked until 60; branch saves stay anchors, not branch prose. |
| S12 | Solstheim and late mythic consolidation. Treat Raven Rock/Severin as the island logistics spine, not ordinary Skyrim backtracking. | `raven_rock_west`, `thirsk_central`, `skaal_north`, `tel_mithryn_east`, plus separate-worldspace/AE expedition blocks. | Raven Rock restock, Severin storage only after validation, hot soup ingredients/warmth kit, ferry return plan, cold-interior handling, and Black Book/Dragonborn progression checks. | Final Miraak safe at 60+; Legendary Dragon still waits for 78 and Ebony Warrior for 80. |
| S13 | Legendary Dragon checkpoint. Geography should serve combat readiness, not checklist cleanup sprawl. | Prepared dragon-hunt block in a supportable exterior region. | Verified bed, food and hot soup ingredients if cold, healing, carry space, and recovery endpoint. | Level 78 only; Ebony Warrior remains locked until 80. |
| S14 | Late high-risk and progression tail. Use established bases, transport, and known corridors to finish remaining hard content without unstable backtracking. | Any corridor, but each block must have a rest/base/transport endpoint and avoid unnecessary cold exposure. | Final combat kit, storage, sell-off, sleep-before-level checks, and bounded reset recovery planning. | Level 80 Ebony Warrior; all-perks grind still not final until 252. |
| S15 | All-perks and final reconciliation. Geography becomes cleanup validation, not discovery by wandering. | Corridor-by-corridor final audit after TB-031A-TB-031J reconciliation. | Stable checklist map, final storage/display policy, all skills restored to 100 after resets, and explicit remaining travel loops. | Level 252 all-perks finalization and complete route/checklist validation. |

## Route Block Frame for TB-026

The route prototype uses these blocks as insertion containers. A block can contain quests, locations, books, stones, word walls, favors, radiants, property work, and local AE objectives only after the relevant objective row and constraint rows have been checked.

| Block | Working role | Eligible corridors | Earliest skeleton pressure | Must attach before use | Do not use for |
| --- | --- | --- | --- | --- | --- |
| G00 | Setup and run rules. | None. | S00 | Official AE scope, Survival baseline, trophy-safe setup. | Gameplay objective insertion. |
| G01 | Opening warm core. | `riverwood_helgen_road`, `whiterun_central_plains`. | S01 | Bed, food, sell-off, first storage candidate, first Whiterun protected-entry handling. | Cold sweeps, heavy collection, broad Daedric/AE routing. |
| G02 | Central carry/storage loop. | `whiterun_central_plains`, `rorikstead_western_road`. | S02-S04 | TB-031D defaults: Whiterun Stable Horse, Breezehome as first-storage bridge, Tundra Homestead as main base, Goldenhills as food/income support after validation. | Using any candidate base before purchase/acquisition, ownership, safety, and storage validation. |
| G03 | Southern warm expansion. | `falkreath_pine_forest`, `riverwood_helgen_road`, `ivarstead_rift_pass`. | S03-S06 | Inn endpoint, mountain/cold-interior screening, Lakeview/Helvard checks where relevant. | Level-locked reward dungeons or unvalidated Hircine/grotto branch state. |
| G04 | Riften and southeast support. | `riften_rift`, `dayspring_canyon` when Dawnguard-ready. | S04-S11 | Riften bed/storage/sell-off plan, mountain-row screening, and later Dawnguard branch readiness. | Dawnguard or Aetherium branch content in main continuity; use TB-028/TB-029 branch prototypes. |
| G05 | Western Reach and road-inn expeditions. | `markarth_reach`, `old_hroldan_reach_road`. | S04-S11 | Horse, food, bed endpoint, pass/path validation, carry emptying. | Sky Haven/Dragonbane before level 46. |
| G06 | Eastmarch and Windhelm ferry hub. | `kynesgrove_eastmarch_road`, `windhelm_eastmarch`. | S04-S12 | Windhelm bed/ferry plan, cold kit for Windhelm-adjacent cold rows, sell-off/storage. | Solstheim broad cleanup before Raven Rock support exists. |
| G07 | Solitude and northwest city/coast prep. | `solitude_haafingar`, `dragon_bridge_haafingar_road`, `morthal_marsh`. | S06-S11 | Solitude carriage/ferry access, inn endpoint, coastal cold kit, Bards and Civil War state checks. | Bards instrument pickup before assignment or 46-gated rewards. |
| G08 | Pale/Winterhold prepared sweep. | `dawnstar_pale_coast`, `nightgate_pale_pass`, `winterhold_coast`. | S07-S12 | Hot soup ingredients, warm gear, daylight travel where possible, verified beds, return transport, cold-interior exit plan. | Pre-36 Saarthal/Forbidden Legend-linked placement or casual detours. |
| G09 | Level-36 linked-dungeon loop. | Folgunthur/Saarthal/Geirmund/Reachwater corridors as validated by objective rows. | S09 | Level 36 reached, warm/carry/rest support, exact linked-dungeon access validation. | Any pre-36 linked-dungeon approach, read, loot, or entry state. |
| G10 | Level-46 classic reward loop. | Riftweald/Riften, Sky Haven/Reach, late Thieves reward handoffs. | S11 | Level 46 reached, reward-source checks, hard saves where constraint rows require them. | Practical-tier tradeoffs not explicitly accepted by a later pass. |
| G11 | Dawnguard expedition. | `dayspring_canyon`, `icewater_volkihar_ferry`, related separate interiors/worldspaces after validation. | S11-S12 | `Bloodline` hard save, ferry/cold kit, transformation/trophy planning, food/rest/carry plan, and TB-028/TB-029 branch/default handling. | Volkihar branch objectives in main continuity or Aetherium reward branches without the hard-save/reload structure. |
| G12 | Solstheim/Raven Rock spine. | `raven_rock_west`, then `thirsk_central`, `skaal_north`, `tel_mithryn_east`. | S11-S12 | Raven Rock inn/restock, ferry return, Severin validation before storage, cold kit, camps as backup only. | Broad island cleanup before support is established or final Miraak before 60. |
| G13 | Separate-worldspace and AE high-risk expeditions. | Manual/not-comparable rows, Black Books/Apocrypha, Skuldafn, Deadlands, and similar route-specific spaces after validation. | S11-S14 | Parent quest access, explicit exit/recovery path, inventory/carry plan, and source-row validation. | Automated placement from straight-line geography. |
| G14 | Late cleanup by corridor. | All corridors, one supportable loop at a time. | S14-S15 | Checklist map, final storage/display policy, bed/food/carry endpoints, TB-031J source-readiness resolutions, and remaining objective validation. | Replacing TB-031A-TB-031J reconciliation, TB-032 warnings, or TB-033 constraint validation. |

## Prepared Sweep Requirements

Use this as a preflight checklist before TB-026 places objectives into a cold, coastal, mountain, remote, or separate-worldspace block.

| Sweep type | Minimum support before placement | Source support |
| --- | --- | --- |
| Northern or coastal sweep | Verified bed endpoint, warm gear/clothing, hot soup ingredients, torches/heat plan, ferry/carriage cash if relevant, return route, and daylight/weather caution. | `survival-mode-constraints.md` (`SN-000116`, `SN-000118`) |
| Mountain or pass sweep | Food, warmth kit, horse/path plan, campsite backup, planned descent or inn endpoint, and no heavy-carry burden. | `survival-mode-constraints.md` (`SN-000117`, `SN-000118`) |
| Cold-interior dungeon | Treat as cold travel, not shelter: hot soup ingredients, torches, healing, empty carry space, sleep before entry, and nearest rest point after exit. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`, `SN-000118`) |
| Long dungeon or enclosed worldspace | Food, healing, disease-removal plan where exposure is likely, carry space, verified bed before entry, and storage/sell-off plan after exit. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`) |
| Solstheim loop | Arrive rested/fed through Windhelm/Raven Rock ferry, use Raven Rock as hub, validate Severin before storage, carry camps as backup only, and keep ferry return available. | `survival-mode-constraints.md` (`SN-000116`, `SN-000117`, `SN-000118`) |
| Heavy collection/material loop | Safe storage or sell-off endpoint, horse/follower/pet/backpack plan where available, and no unique-item loss/disenchant assumption. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`) |
| Planned level-up or crafting block | Verified proper bed before level-up or potion-sensitive crafting, nearby storage/material access, and shrine/blessing support if used. | `survival-mode-constraints.md` (`SN-000115`, `SN-000117`); `skill-perk-leveling-plan.md` (`SN-000119`, `SN-000121`) |
| Disease-prone expedition | Cure Disease potion, Hawk Feathers, shrine access, or another disease-removal plan before route prose assumes recovery. | `survival-mode-constraints.md` (`SN-000115`) |

## Gate Preservation Notes for Geography

| Gate | Geography-specific routing risk | TB-026 rule |
| --- | --- | --- |
| Level 8 Silent Moons | Central Whiterun travel can naturally pass near Silent Moons. | Do not place Silent Moons first loot/clear into G01/G02 before level 8. |
| Level 25 Mage's Circlet | College depth can be tempting when visiting Winterhold. | Do not report the `Good Intentions` reward before level 25 even if a northern sweep is efficient. |
| Level 27 Pale Blade | Pale/Nightgate sweeps can collide with Frostmere timing. | Do not claim/resolve The Pale Blade before level 27; check Kharjo target risk separately. |
| Level 32 Nightingale armor | Riften/Thieves routing is geography-efficient early. | Do not start `Trinity Restored` before level 32. |
| Level 36 Forbidden Legend linked dungeons | Winterhold/Saarthal, Folgunthur, Geirmund, and Reachwater are spread across useful corridors. | Current Phase 2 constraints include Saarthal in the linked-dungeon spawn lock: do not read `Lost Legends` or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before level 36 unless a later source review explicitly reopens ordinary College/Saarthal routing. |
| Level 40 Shield of Solitude | Solitude is a natural Bards/Civil War/coastal hub. | Do not take Falk's final Shield of Solitude reward before level 40. |
| Level 46 classic rewards | Riften, Reach, and Thieves/Main Quest corridors can become efficient before 46. | Do not enter Riftweald Manor or Sky Haven Temple, or accept source-tier Nightingale Blade/Bow rewards, before level 46 unless a later explicit tradeoff allows it. |
| Level 60 Miraak | Solstheim route efficiency can pull Dragonborn finalization early. | Build Raven Rock/Solstheim support earlier if needed, but do not finish final Miraak before level 60. |
| Levels 78, 80, 252 | Late combat/progression checks are not geography cleanup. | Keep Legendary Dragon, Ebony Warrior, and all-perks finalization as late progression gates with their own readiness checks. |

## TB-026 Handoff

TB-026 has built `drafts/route-prototypes/main-route-prototype-v0.md` by inserting flexible objectives into the `G00` through `G14` route-block frame. For later route edits, continue to:

* start from `data/route-planning/objective-route-index.csv` corridor, access, cold, candidate, and constraint summaries;
* inspect `data/route-planning/objective-constraints.csv` and the canonical constraint source when `constraint_count` is nonzero;
* validate the canonical objective row in `data/objectives/objectives.csv` before changing route placement or adding prototype route text;
* keep level and reward gates from `level-gated-skeleton-v0.md` intact;
* attach rest, food, carry, storage, and transport support to every remote/cold/coastal/mountain/Solstheim block;
* treat candidate bases as unavailable until acquisition, ownership, safety, and storage validation are confirmed;
* use the now-resolved TB-028/TB-029 branch defaults/prototypes, TB-031D route defaults, TB-031E skill/reset distribution, TB-031F counter mechanics, TB-031G location-validation rules, and TB-031J source-readiness resolutions; keep warning copy, final step order, and final validation in their assigned later tasks.
