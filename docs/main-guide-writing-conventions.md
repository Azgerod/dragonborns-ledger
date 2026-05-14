# Main Guide Writing Conventions

Status: active TB-035 drafting standard.

This file records the current player-facing writing conventions for `drafts/final-guide/main-guide-v1.md`. Update it whenever user feedback changes the standard.

## Core Shape

The final main guide is a linear player route, not an audit report. It should read like:

1. go here;
2. speak to this person;
3. accept or complete this quest;
4. collect this item/book/reward;
5. record non-obvious route bookkeeping only when needed;
6. stop here or return later.

Do not expose objective IDs, row counts, coverage ledgers, source-note mechanics, or database language in player-facing guide prose. Keep those details in `data/guide-coverage/main-guide-v1-coverage.csv` and source notes.

Use title case for chapter and section headings: capitalize major words, but leave minor connector words such as "and," "or," "the," "of," "in," "at," and "to" lowercase unless they begin the heading.

## Positive Route First

Write the guide around what the player should do. Do not build sections as lists of prohibited nearby content.

Use the global Route Discipline policy to absorb broad warnings. Local sections should not repeatedly say "do not detour," "do not clear nearby locations," "do not start side content," or similar broad prohibitions.

When the player is already in an area, route safe and efficient same-location objectives there. Do not defer an objective merely because it belongs to a different internal MR theme. If a quest, favor, service, pickup, or counter action is safe, sourced, and naturally colocated, place it where the player is already standing.

## Nearby Objective Audit

Every route-section pass must include a nearby-objective audit before guide prose is considered complete. This is not limited to locations. Check for all objective types that can naturally attach to the current place, road, dungeon, hub, or service stop:

* starting, advancing, or completing quests;
* discovering, entering, clearing, or deliberately avoiding locations;
* collecting finite items, treasure maps, claws, masks, stones, paragons, notes, books, spell tomes, powers, shouts, pets, mounts, and unique rewards;
* buying property, services, homes, mounts, maps, pets, upgrades, or Creation items;
* completing representative favors, work actions, radiants, counters, trophies, crafting outputs, investments, skill actions, or relationship prerequisites.

Use both the compiled project data and the relevant wiki/source pages. A normal section audit should inspect:

1. `data/route-planning/objective-route-index.csv` by route corridor, nearest hub, location name, support location, and text terms for obvious nearby places.
2. `data/route-planning/objective-constraints.csv` for every nearby objective that might be moved earlier or held back.
3. Domain support tables under `data/books/`, `data/items/`, `data/locations/`, `data/properties/`, `data/npc/`, and `data/skills/` for same-place candidates not obvious from the route index.
4. `data/checklist-mapping/coverage-matrix.csv` for place-specific checklist rows that share a generic objective parent, such as individual crop-sale, firewood-sale, ore-sale, and other representative activity variants.
5. The cited source notes and primary wiki pages when route timing depends on exact quest stage, cell state, reward state, ownership, bug-sensitive route order, or placed-object details.

The default answer should be "route it now" when an objective is safe, sourced, efficient, and naturally colocated. Hold it only for a concrete reason such as a level gate, cell-entry or clear-state risk, branch state, quest conflict, NPC dependency, trophy/counter boundary, skill-book read timing, ownership/theft risk, Survival/logistics issue, or missing source validation.

Do not preserve stale lower-level gates after the route has already passed a higher threshold. If the player has already been held for level 40, a later level-25 or level-36 checkpoint should either be removed from player-facing prose or the sequence should be reordered so the lower gate appears before the higher one. Once a threshold is safely exceeded, write the reward or quest handoff as a normal routed acquisition and record the gate satisfaction internally.

When a first-entry, actor-state, or start-window issue can close off a quest or service, use it as an internal route-order reason: route the minimum stabilizing action before optional same-city work. Do not write player-facing "if the script fails" recovery instructions; assume normal game behavior once the route has chosen the safer order.

Before accepting an assassination contract, hostile-faction contract, or any quest that will turn an NPC into a target, audit that target's normal services, favor dialogue, work-action rows, relationship options, merchant state, and quest dependencies. If any safe required row depends on the target's normal dialogue or alive state, route that row before accepting or advancing the hostile objective.

Before completing a quest that grants a broad access or status reward, audit whether that reward can close off an earlier favor, introductory quest, service gate, or relationship path. Examples include Blood-Kin, faction membership, thane state, guild-master state, ownership state, and post-finale faction outcomes. If the status can make a required objective unavailable, route the vulnerable objective before the status-granting turn-in, and record that ordering reason in the source note or coverage tracker.

Before curing, replacing, or otherwise changing a transformation state, audit every downstream objective that depends on that state. Treat Beast Blood, Vampire Lord, normal vampirism, and final mortal state like route-critical access states. Do not cure lycanthropy, ask Serana/Harkon for Vampire Lord conversion, cure Serana, or perform a final mortal-state restoration until state-dependent quests, services, powers, perks, merchants, and unique item purchases are complete or explicitly staged around the change.

Do not force a transformation mastery grind into the first section where the form becomes available if substantial fresh hostile content remains ahead. Open and close transformation windows deliberately: confirm the outgoing state is complete before replacing it, start explicit perk/counter tracking when the new state begins, let natural routed combat carry the tree where practical, and route the cure or final-state restoration only after the required perks are complete. Use a dedicated grind only when the route has no better natural content left or the user explicitly approves that approach.

Not every nearby source-listed candidate is itself a required stop. For objectives satisfied by one selected source from several duplicates, such as most skill books and some spell tomes, audit the nearby candidate and route it only if it is the best coherent source or safely completes the actual objective now. Do not add an unmarked detour merely to carry an unread duplicate book or a fallback source for many sections; record the candidate decision in the source note or coverage tracker.

When the guide chooses a different deterministic source than the current source-selection table, update `data/constraints/progression-source-selections.csv` in the same pass. Examples include switching a spell tome from a vendor stock plan to a fixed quest reward, or changing the selected copy of a skill-book title because the routed dungeon contains a safer container copy.

When a checklist row names a specific local variant of a representative activity, treat that row as a real nearby objective even if the generic parent objective has already been represented elsewhere. If the player is already at that farm, sawmill, mine, inn, or service stop and the action is safe, route the specific variant in normal prose. Do not add a routine bracket cue for it.

When a broad source inventory creates a book/document row whose individual page has no in-world location and the related quest/location walkthrough does not name it as an obtainable pickup, do not invent a player action. Record it as an explicit internal exclusion or data-reconciliation item in the coverage tracker/source note, and keep it out of the player-facing route unless a later source pass finds an executable location.

For the opening game and other fragile Survival segments, "safe and nearby" is not enough by itself. Optional combat-forward detours should usually wait until the player has reached the next settlement, sold or dropped excess Helgen loot, stocked food, rested if needed, and made a stable save. The opening route may still pull a nearby objective forward when it is truly low-risk or tightly bundled with the current action, but early stabilization beats harvesting every colocated item before the first support stop.

Do not assume early money that the route has not actually created. Property, mount, pet, armor, spell, crafting, training, and furnishing purchases should be routed at the first coherent point where normal routed loot, rewards, and selling can plausibly fund them. Do not use grinding, merchant exploits, free-purchase glitches, or "if you happen to have enough gold" as a hidden bridge unless the guide explicitly routes that economy plan and the user has approved the exploit/grind policy. For early homes in particular, unlocking purchase permission is not the same as buying and verifying storage.

Keep related objectives together where doing so helps the player's actual route, but do not treat "coherent bundle later" as a standalone deferral reason. The default remains: route safe nearby objectives now. A later bundle is justified only when it protects a concrete constraint or clearly improves execution, such as avoiding a shallow discovery-only pass, keeping a randomized target pool intact, preserving a level/reward gate, waiting for a branch save, preventing an NPC/service conflict, grouping a quest start with its next soon progress point, or avoiding Survival/economy strain. If none of those reasons apply, pull the objective forward.

Distinguish quest-chain integrity from theme bucketing. It is good route design to keep a tightly linked quest or dungeon chain intact when splitting it would create artificial partial clears, odd return trips, or route-fragile states; for example, do not run most of a dungeon now and return much later just to take one gated quest item. It is bad route design to hold unrelated safe objectives merely because they share a hold, faction, theme, or later chapter label with another objective that is genuinely gated. If one Falkreath, Dawnstar, Whiterun, or faction objective must wait, audit the neighboring objectives independently and route the safe ones now.

Prefer a complete same-place action such as "start quest, enter location, collect the local book, clear the location, turn in the reward" over a shallow early action such as "discover but do not clear" unless that partial action has an independent route reason. Discovery-only, pickup-only, or "start now, ignore until much later" steps should be deliberate exceptions, not the default output of the nearby-objective audit.

When a nearby objective is held for later, the source note or coverage tracker must name the concrete route reason rather than merely saying that it belongs to a later bundle. It usually should be absent from the player-facing prose rather than written as "discover but do not clear" or "do not start this yet." Add player-facing text only when the player is being sent to the exact trigger, item, room, or dialogue and the accidental action would matter.

When a quest or faction assignment forces a major-city or service-hub visit, audit that hub as if it were a normal route section, not merely a stop inside the quest theme. Pull forward safe same-visit favors, documents, collectibles, services, and quest starts/progress where their next step is local or soon. Then narrow or remove stale later "city prerequisite" buckets so the same work is not duplicated.

For quests whose start, progress, and completion happen in different places, choose timing deliberately:

* Do not wait until the completion location if the player was just at the quest-start location and the next stage is soon.
* Do not start a quest at the earliest possible moment if it will sit untouched for a long time and there is a later efficient start-location visit before the next stage.
* Prefer the most recent efficient visit to the quest-start location before the next routed progress or completion step.
* Make exceptions for fragile first-visit starts, branch setup, missable dialogue, leveled reward gates, radiant target control, or objectives that must remain active for later route control.
* Revisit these decisions as later route sections are expanded. A quest start that looked good in an early pass may need to move earlier or later once the next progress point is known.

Do not ask the player to manipulate RNG or reroll ordinary radiant assignments as part of normal guide execution. If a target is randomized, respect the target the save actually gives and write a concise conditional route branch for each possible outcome. Reserve save/reload language for explicit branch saves, route-choice correction, or source-backed reward/state protection.

When a random assignment creates a temporary route divergence, isolate it from the main route. Tell the player to complete the assigned job, retrieval, delivery, or target directly, handle only objectives at the assignment site itself, return to the starting hub or named route point, and then continue the main route. Do not build the surrounding itinerary around one preferred random outcome, and do not detour for nearby objectives just because the assignment temporarily sends the player through an area.

If a required collectible or unique item depends on an uncontrolled random encounter, name the natural acquisition window in the guide, route the action to take if the encounter appears, and record a `NEEDS ROUTE RESOLUTION` row in the internal coverage tracker until a deterministic or explicitly approved random-encounter policy exists. Do not hide the row under generic cleanup language and do not ask the player to roam or reload purely to force the encounter.

For repeatable counter systems with random assignment, city targeting, or known pre-state bugs, do not opportunistically sprinkle jobs through city visits just because the player is nearby. First confirm the safe quest state, the assignment controls, the failure/rejection consequences, and the exact counter target. If scattering early jobs could create failed-entry clutter, permanent target items, inventory side effects, or blocked improvements, hold the system for a controlled block and document the route reason in the source note and coverage tracker.

If two route constraints conflict, prefer a narrow controlled exception over weakening either constraint globally. Example: if a later assassination would threaten an NPC required for a repeatable-counter special job, route only the minimum required counter work to protect that NPC-dependent quest, then return the rest of the counter system to its normal controlled block.

If a source-backed objective requires temporarily disabling Survival Mode and the user approves that exception, write it as a named one-action exception in the player guide: save first, turn Survival Mode off only at the required place, perform the required action, then turn Survival Mode back on immediately before travel, combat, sleep, crafting, or unrelated interaction. Record the source-backed reason and affected objective rows in the source note and coverage tracker. Do not treat the exception as permission to relax the mandatory Survival Mode rule globally.

When several active objectives draw from overlapping randomized target pools, start every vulnerable objective before clearing any shared target location, then build the player's actual target list from the quest log. Route each unique target once, and tell the player to handle every active objective at that location before leaving. This is especially important when pre-clearing a location can block a later retrieval or when a single Forsworn camp/dungeon can satisfy a Daedric, miscellaneous, unique-item, location, and book objective together. Keep the player-facing branch concise, but record the full target-pool reasoning in the source note and coverage tracker.

If a nearby location belongs to a randomized retrieval or favor target pool but the relevant quest giver cannot be safely started yet, do not pre-clear that location merely because the road passes it. Hold it for a target-aware block unless there is a stronger route reason to consume it now, and record the hold in coverage/source notes rather than in player-facing prose.

Intentional quest failure is allowed only when it is source-backed and route-protective. When a failed objective is the intended route, write it as a clear player action in guide prose, cite the source behavior in the source note, and record the protected downstream state in the coverage tracker. Do not use failure as a shortcut unless it preserves a required NPC, item, reward, trophy, or clean continuity state better than normal completion.

If the player-facing guide warns the player away from a nearby objective, the internal coverage tracker must say why that objective is not routed now. If no source-backed reason survives the audit, remove the warning and replace it with a positive route instruction.

When a route naturally passes an option-list NPC, pet, follower, spouse, child, mount, or household candidate, represent the option in one concise player-facing sentence if it is useful for later choice awareness. Do not expand it into a table or internal rationale in the route body; keep the objective/checklist/option IDs and default-vs-non-default status in the coverage tracker.

Useful helper:

```bash
python3 tools/query_nearby_objectives.py --corridor riverwood_helgen_road
python3 tools/query_nearby_objectives.py --text "Guardian Stones"
```

This helper is only a first-pass index query. It does not replace support-table checks or source-page reading.

## Local Warnings

Keep local warnings rare and concrete. Use them only for:

* leveled reward or cell-entry gates;
* branch decisions and irreversible choices;
* source-backed actions whose route order prevents fragile state;
* trophy/counter boundaries;
* dialogue options adjacent to a routed dialogue when a misclick would matter;
* skill books or quest-starting documents only when the route sends the player to interact with that exact object, shelf, table, container, or room.

Do not repeat generic book, note, dungeon, rumor, property, or Creation warnings that are already covered by Route Discipline.

## Detail Level

Be explicit about route-critical facts: NPC names, quest names, locations, puzzle solutions, item names, save points, branch reloads, gates, counters, and non-obvious route bookkeeping.

Do not micromanage ordinary Skyrim play. Avoid routine combat advice, ordinary looting advice, and excessive carry-weight commentary unless it protects a route-critical objective or Survival Mode constraint.

Good:

`Before leaving, carry food, healing, lockpicks, enough empty carry space, and a ranged option.`

Too much:

`Loot only light valuables, use the wall for cover, attack only when the dragon is focused elsewhere, and avoid every nearby roadside marker.`

## Checklist Logging

The player-facing guide should not use routine bracket checklist cues. The global guide conventions tell the player to update the matching checklist row whenever the route tells them to complete a quest, discover or clear a location, learn a spell or shout, read or take a tracked book, acquire a unique item or set, gain a power, unlock a follower, buy property, obtain a pet or mount, finish a favor, or perform another tracked completion action.

Do not write bracketed checklist callouts or phrases such as "mark the row" or "record the spell tome cue" for obvious acquisitions and completions. If the player would plainly know from normal play that the named thing happened, route the action in prose and let the global policy handle checklist logging.

Use explicit route bookkeeping only for non-obvious state: counter totals, branch-experienced rows, randomized radiant results, option-list/default handling, hidden prerequisites, and conditional availability that the game does not cleanly expose. Counters should state the target and current count, for example: `Record the Sideways counter at 1 of 10 qualifying side quests.`

For source-listed documents or rewards tied to conditional/random encounters, do not silently choose the cleaner quest ending if it makes the item unavailable. Route the encounter trigger when it is safe, keep the player instruction concise, and isolate the random wait from normal geography routing. If a source page has no deterministic pickup path, record the exact missing fact in source notes and coverage rather than pretending the row is handled.

Do not add player-facing trophy-pop fallbacks, autosave fallbacks, crash workarounds, console-style recovery notes, "if the quest does not start" instructions, or similar technical contingency prose. The guide assumes the game functions properly throughout. Source notes and coverage trackers may record bug-sensitive route reasons, but the route body should present the intended normal path.

Ordinary state checks such as "carry weight is controlled," "food is stocked," "Survival Mode is still on," and "a rotating manual save has been made" belong in route prose, not checklist callouts.

## Section Boundaries

Player-facing route sections are area-and-state based, not rigid MR buckets. Internal MR labels are coordination handles only and should not appear in player-facing headings.

If detailed routing shows that a safe objective belongs earlier or later than the scaffold implied, move it and update:

* `drafts/final-guide/main-guide-v1.md`;
* `data/guide-coverage/main-guide-v1-coverage.csv`;
* any relevant source note;
* `docs/main-guide-v1-expansion-plan.md`, `docs/task-board.md`, or `docs/session-handoff.md` if the coordination state changes.

The internal section list itself is allowed to change. When nearby-objective audits move meaningful work earlier, remove that work from later theme buckets instead of leaving duplicate or stale instructions. When a newly unlocked quest is best handled in the next coherent geographic block, note that handoff and reshape the next block around the start/progress/completion bundle.

Apply new routing conventions retrospectively to already-expanded sections when they reveal a systemic issue. Do not wait for manual user audits to catch every missed same-location objective.

Do not let late reconciliation sections become dumping grounds for ordinary unfinished objectives. If a remaining location, quest, book, unique item, property, pet, mount, spell, crafting unlock, counter action, or other objective was safe earlier, retrospectively insert it into the earliest natural route point that can handle it coherently. Late cleanup sections are only for objectives that are genuinely gated until that point, unresolved random-encounter policy, final cross-checks, final crafting/reconciliation systems, or deliberately approved final grinds.

## Branch Continuity

Branch routes exist to record branch-exclusive quests, outcomes, trophies, and meaningful alternate content before returning to the canonical main save. Do not treat temporary branch loot as main-route checklist completion unless the branch itself is the only required record for that item or outcome.

When a branch visits a location that the main route will also enter, keep main-continuity collectibles, books, shouts, and preserved gear on the main route after reload. This avoids duplicate player-facing instructions and prevents the guide from marking an item that disappears with the branch save.

## No Section-End State Lists

Do not end guide chapters or sections with "End state before..." lists. They make the player-facing guide feel like a planning artifact and duplicate information already carried by route instructions, global checklist logging, source notes, and the internal coverage tracker.

If continuity state matters for play, state it at the route point where it matters: for example, tell the player to keep a quest active before leaving town, preserve an item when it is acquired, or make a named hard save before the risky handoff. Keep broader state summaries in `data/guide-coverage/main-guide-v1-coverage.csv`, source notes, task-board notes, or handoff docs rather than in the player-facing route body.

## Internal Audit Layer

The guide must remain internally auditable, but audit machinery belongs outside the player-facing prose.

Use `data/guide-coverage/main-guide-v1-coverage.csv` for objective IDs, staged/completed status, checklist cue mapping, option/default rows, exclusions, and unresolved status. If the guide moves an objective earlier or later, update the coverage tracker in the same pass.

Use source notes for sourced gameplay facts that affect route order, gates, bugs, rewards, counters, or completion boundaries. Do not invent route facts to make a section read more cleanly.

## User-Facing Handoff

After each guide-expansion pass, the assistant response to the user should include a short routing-decision summary. Explain which nearby objectives were routed now, which were deliberately held, and why. Keep that explanation out of the player-facing guide body unless the player needs the information to execute the route safely.
