# Counter Coverage Plan

Status: TB-031F complete as a route-planning counter/action layer.

Scope: this is not final route prose. It records how later route passes must satisfy checklist and trophy counters without inferring mechanics from broad objective rows.

Source support: SN-000127 plus the source notes named in each row below.

## Output Summary

| Area | TB-031F decision | Later owner |
| --- | --- | --- |
| Trophy counters | Track exact counter checkpoints for side quests, misc objectives, locks/pockets, speech checks, dungeon clears, map discoveries, skill books, dragon souls/rides, Black Books, Solstheim discoveries, and trophy pop saves. | TB-033 final validation. |
| Thieves Guild side jobs | Route 20 restoration jobs with city tallies, then continue Delvin/Vex jobs to the 125-job display/safe boundary. | TB-034 route placement; TB-033 validation. |
| Dawnguard `Lost Relic` | Complete all three relic versions; record every filler radiant used because filler count is semi-random. | TB-034 Dawnguard route; TB-033 validation. |
| Fishing | Treat Fishing as a structured quest/species/biome/rod/weather sweep, not incidental travel fishing. | TB-034 route placement; TB-037 checklist proof. |
| Work activities | Pair Hard Worker station actions with representative activity defaults where possible. | TB-034 route placement. |
| Cutting lumber and milling | Keep as support-only property/material actions, not standalone required counters. | TB-034/TB-037 if checklist proof needs a cue. |
| Source-readiness rows | Promote/map six TB-031F-owned rows: Rebuilding the Blades, Dragon Hunting, Archery Practice, Scare My Enemy, Firebrand Wine Case, and Map of Dragon Burials. | TB-031H metadata audit complete; TB-033 validation. |

## Counter Checkpoints

| Counter/action | Route treatment | Checkpoint rule | Source notes |
| --- | --- | --- | --- |
| `Sideways` | Use only source-qualified side quests. | Mark a trophy checkpoint when 10 qualifying side quests have completed; do not count `Blood on the Ice`, Black Book side quests, or `Lost to the Ages` for this trophy. Continue maximalist side-quest routing afterward. | SN-000020; SN-000103; SN-000127 |
| `Hero of the People` | Count distinct finite miscellaneous objectives, not arbitrary repeats. | Maintain a running misc-objective count and check the trophy at 50. Do not rely on drunk favors or repeated no-journal activities for the count. | SN-000022; SN-000103; SN-000113; SN-000127 |
| `Delver` | Count observed clear-state completions only. | Route more than 50 source-listed clearable locations, but mark the trophy checkpoint only after 50 clear messages/counter increments are observed. TB-031G validates the clear-trigger class and exceptions. | SN-000077; SN-000103; SN-000127; SN-000128 |
| `Explorer` | Count observed map-marker discoveries only. | Route at least 100 source-listed discoverable/clearable markers and verify the counter at 100. TB-031G validates duplicate markers, secondary markers, no-marker rows, and separate-worldspace treatment. | SN-000078; SN-000103; SN-000127; SN-000128 |
| `Reader` | Read title-level skill books, not duplicate copies. | TB-031E selects copies. Read after Scholar's Insight unless a documented tradeoff is chosen; check trophy after 50 different titles and continue to all 90 skill-book objectives. | SN-000051; SN-000103; SN-000126; SN-000127 |
| `Thief` | Track lock and pocket halves separately. | Maintain `locks_picked` and `pockets_picked` counters. Natural lockpicking can carry the lock half; schedule controlled G04/G14 pickpocket actions for the pocket half instead of assuming 50 pockets happen naturally. | SN-000103; SN-000119; SN-000127 |
| `Snake Tongue` | Reserve one successful persuade, one bribe, and one intimidate action. | Do not leave this to incidental dialogue. Final route must label three Speech-check slots, save before each if failure matters, and record the trophy only after all three action types succeed. | SN-000103; SN-000127 |
| `Hard Worker` | Perform all three player station actions explicitly. | Chop wood at Riverwood/Hod support, mine ore at Redbelly/Grogmar support, and cook one food item at a route-supported cooking station. Paid turn-ins are representative favor coverage; the trophy needs the player actions. | SN-000089; SN-000103; SN-000113; SN-000126; SN-000127 |
| `Artificer` | Use TB-031E representative crafting outputs. | Craft one smithed item, one enchanted disposable item, and one potion; verify trophy before treating later crafting as cleanup. | SN-000103; SN-000126; SN-000127 |
| `Golden Touch` | Add an economy checkpoint before final high-spend cleanup. | Verify 100,000 gold before expensive final home/material/perk cleanup if the route's normal economy has not already popped the trophy. | SN-000103; SN-000127 |
| `Dragon Hunter` | Track absorbed souls separately from dragons killed and souls spent. | Check the trophy at 20 absorbed dragon souls; avoid counting souls stolen during the Miraak window. | SN-000033; SN-000103; SN-000127 |
| `Soul Tear` | Teach all three words through Durnehviir. | After Soul Cairn access, route three Durnehviir summon/listen cycles and record each word before marking the trophy complete. | SN-000105; SN-000127 |
| `Dragon Aspect` | Learn all three source words. | Check the trophy only after all three Dragon Aspect words are learned, even though all-shouts scope continues beyond this trophy. | SN-000105; SN-000127 |
| `Hidden Knowledge` | Use Black Book completions. | Project scope routes all seven Black Books; check trophy after the fifth completed/rewarded Black Book. | SN-000105; SN-000127 |
| `Dragonrider` | Use completed Bend Will on rideable dragons only. | After all three Bend Will words, route five successful dragon mounts with saves and post-dismount camera/state checks. | SN-000105; SN-000111; SN-000127 |
| `Solstheim Explorer` | Count Solstheim map discoveries. | Track 30 Solstheim location discoveries during island sweeps; TB-031G validates marker/discovery case handling. | SN-000105; SN-000127; SN-000128 |
| `Standing Stones` | Track each stone discovery separately from final power choice. | Route all 13 Standing Stones; final power default remains a separate route/default decision. | SN-000103; SN-000127 |
| `Master Criminal` | Keep as trophy branch. | Use `HS-TROPHY-MASTER-CRIMINAL`, stage controlled 1000-gold bounties in all nine holds, avoid quest-critical NPC deaths, verify trophy pop, and reload. TB-034 chooses final step locations. | SN-000103; SN-000127 |
| Trophy-pop fallback | Use manual saves before one-shot or long-counter completions. | If a trophy does not pop after a sourced completion action, reload the latest pre-action save and repeat the verified action rather than continuing silently. | SN-000101; SN-000103; SN-000105; SN-000127 |

## Thieves Guild 125-Job Plan

| Layer | Decision |
| --- | --- |
| Restoration city tally | Track Markarth, Solitude, Whiterun, and Windhelm separately. Complete five Delvin/Vex jobs in each city, then complete that city's special reputation quest. |
| Assignment filtering | Make a save before requesting jobs. For restoration, accept only jobs in cities still below five; reload/re-roll rather than creating failed journal entries. |
| Riften handling | Riften jobs do not help restoration. After all four reputation cities are restored, Riften jobs may count toward total Delvin/Vex side-job progress if the final route wants safer nearby repeats. |
| Raven Rock handling | Reject or reload Raven Rock Bedlam. Do not count Raven Rock toward restoration because Solstheim has no reputation quest. |
| Job-type coverage | Ensure at least one completion of each job type: Numbers, Fishing, Bedlam, Burglary, Shill, Sweep, and Heist. |
| 125-job completionist boundary | After restoration, continue source-valid Delvin/Vex jobs to total 125. Track total jobs separately from restoration city tallies and stop at the 125-job safe/display boundary. |
| Final validation | TB-033 verifies four special jobs, Under New Management access, display thresholds, and the 125-job safe. |

## Lost Relic and Dawnguard Filler

| Rule | Treatment |
| --- | --- |
| Relic boundary | Complete all three `Lost Relic` versions for the Dawnguard Rune Hammer, Rune Shield, and Rune Axe. |
| Unlock precondition | Complete the first `Ancient Technology` before expecting `Lost Relic` availability. |
| Filler policy | Complete one representative Dawnguard side radiant of each type where offered, then continue required fillers until all three relics are obtained. Record actual filler titles and targets because the filler count is not deterministic. |
| Target cautions | Avoid `Cleansing Light` at Movarth's Lair if possible. Treat `A Jarl's Justice` as a slow recurrence source, not a reliable immediate filler loop. |

## Fishing and Support Actions

| System | Route treatment |
| --- | --- |
| Fishing questline | Route Fishing Creation quests as the parent structure for rods, maps, fishing spots, species, and special catches. |
| Species set | Treat the fish species checklist as a biome/rod/weather table. Do not expect all catches from one spot or one weather state. |
| Fishing alchemy ingredients | Preserve at least one ingredient copy for the TB-031E Experimenter pass when a fish is also an alchemy ingredient. |
| Cutting lumber | Support-only Hearthfire/material action. Use when buying/cutting logs for construction; do not add a standalone objective unless TB-037 checklist proof later requires a cue. |
| Milling | Support-only food/material processing action. Use where Hearthfire kitchen/farm/cooking support needs it; do not add a standalone counter. |

## Source-Readiness Resolutions

| Checklist row | TB-031F resolution | Route implication |
| --- | --- | --- |
| `Rebuilding the Blades` | Promoted to `OBJ-002785` branch-route objective. | Add to BR-004 Paarthurnax/Blades branch only; canonical save preserves Paarthurnax. |
| `Dragon Hunting` | Promoted to `OBJ-002786` branch-route representative radiant. | Add one Blades dragon hunt to BR-004 branch after Blades support is restored; reload after branch audit. |
| `Archery Practice` | Promoted to `OBJ-002787` main-route training/activity objective. | Route Angi's six practice tasks when Angi's Camp access and progression timing are safe. |
| `Scare My Enemy` | Mapped to existing `OBJ-000104` Hired Muscle. | Accept if the Companions radiant seed offers it; do not require a restart solely to force it. |
| `Firebrand Wine Case` | Promoted to `OBJ-002788` parent-quest quest-item checklist cue. | Cue acquisition/use during `Scoundrel's Folly`; final QA verifies retention or turn-in state. |
| `Map of Dragon Burials` | Promoted to `OBJ-002789` parent-quest quest-item checklist cue. | Cue inspection/acquisition during `A Blade in the Dark`; final QA verifies retention or quest-use state. |

After regeneration, no TB-031F-owned `source_readiness_required` row should remain. TB-031J later pulled the remaining non-TB-031F source-readiness rows forward and resolved them before TB-032.

## Handoffs

| Owner | Remaining work |
| --- | --- |
| TB-031G | Complete: validates clear/discovery mechanics, duplicate and secondary markers, location access classes, no-marker rows, and separate-worldspace cases before counter rows become final route steps. |
| TB-031H/TB-031J | Complete: audit metadata/readiness labels after TB-031F promotions, then resolve remaining source-readiness rows before warning placement. |
| TB-032 | Complete: warning triggers for trophy-pop saves, crime branches, Hired Muscle target bugs, Blades/Paarthurnax branch setup, and one-shot counter actions are recorded in the main prototype warning overlay. |
| TB-033 | Validate final trophy pops, counter totals, branch reload state, and checklist proof against the finished route. |
| TB-034/TB-037 | Convert these checkpoint policies into final route instructions and checklist cues. |
