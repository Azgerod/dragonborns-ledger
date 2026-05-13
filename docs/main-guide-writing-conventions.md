# Main Guide Writing Conventions

Status: active TB-035 drafting standard.

This file records the current player-facing writing conventions for `drafts/final-guide/main-guide-v1.md`. Update it whenever user feedback changes the standard.

## Core Shape

The final main guide is a linear player route, not an audit report. It should read like:

1. go here;
2. speak to this person;
3. accept or complete this quest;
4. collect this item/book/reward;
5. mark this checklist cue;
6. stop here or return later.

Do not expose objective IDs, row counts, coverage ledgers, source-note mechanics, or database language in player-facing guide prose. Keep those details in `data/guide-coverage/main-guide-v1-coverage.csv` and source notes.

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
5. The cited source notes and primary wiki pages when route timing depends on exact quest stage, cell state, reward state, ownership, bugs, or placed-object details.

The default answer should be "route it now" when an objective is safe, sourced, efficient, and naturally colocated. Hold it only for a concrete reason such as a level gate, cell-entry or clear-state risk, branch state, quest conflict, NPC dependency, trophy/counter boundary, skill-book read timing, ownership/theft risk, Survival/logistics issue, or missing source validation.

When a first-entry, actor-state, or start-window bug can close off a quest or service, route the minimum stabilizing action before optional same-city work. After the fragile state is protected, resume the normal nearby-objective audit for safe colocated objectives.

Not every nearby source-listed candidate is itself a required stop. For objectives satisfied by one selected source from several duplicates, such as most skill books and some spell tomes, audit the nearby candidate and route it only if it is the best coherent source or safely completes the actual objective now. Do not add an unmarked detour merely to carry an unread duplicate book or a fallback source for many sections; record the candidate decision in the source note or coverage tracker.

When the guide chooses a different deterministic source than the current source-selection table, update `data/constraints/progression-source-selections.csv` in the same pass. Examples include switching a spell tome from a vendor stock plan to a fixed quest reward, or changing the selected copy of a skill-book title because the routed dungeon contains a safer container copy.

When a checklist row names a specific local variant of a representative activity, treat that row as a real nearby objective even if the generic parent objective has already been represented elsewhere. If the player is already at that farm, sawmill, mine, inn, or service stop and the action is safe, route the specific variant and mark the specific checklist cue.

When a broad source inventory creates a book/document row whose individual page has no in-world location and the related quest/location walkthrough does not name it as an obtainable pickup, do not invent a player action. Record it as an explicit internal exclusion or data-reconciliation item in the coverage tracker/source note, and keep it out of the player-facing route unless a later source pass finds an executable location.

For the opening game and other fragile Survival segments, "safe and nearby" is not enough by itself. Optional combat-forward detours should usually wait until the player has reached the next settlement, sold or dropped excess Helgen loot, stocked food, rested if needed, and made a stable save. The opening route may still pull a nearby objective forward when it is truly low-risk or tightly bundled with the current action, but early stabilization beats harvesting every colocated item before the first support stop.

Do not assume early money that the route has not actually created. Property, mount, pet, armor, spell, crafting, training, and furnishing purchases should be routed at the first coherent point where normal routed loot, rewards, and selling can plausibly fund them. Do not use grinding, merchant exploits, free-purchase glitches, or "if you happen to have enough gold" as a hidden bridge unless the guide explicitly routes that economy plan and the user has approved the exploit/grind policy. For early homes in particular, unlocking purchase permission is not the same as buying and verifying storage.

Keep related objectives together where possible. Prefer a coherent bundle such as "start quest, enter location, collect the local book, clear the location, turn in the reward" over a shallow early action such as "discover but do not clear" unless that partial action has an independent route reason. Discovery-only, pickup-only, or "start now, ignore until much later" steps should be deliberate exceptions, not the default output of the nearby-objective audit.

When a nearby objective is held for a later coherent bundle, it usually should be absent from the player-facing prose rather than written as "discover but do not clear" or "do not start this yet." Record the route judgment in the source note or internal coverage tracker instead. Add player-facing text only when the player is being sent to the exact trigger, item, room, or dialogue and the accidental action would matter.

When a quest or faction assignment forces a major-city or service-hub visit, audit that hub as if it were a normal route section, not merely a stop inside the quest theme. Pull forward safe same-visit favors, documents, collectibles, services, and quest starts/progress where their next step is local or soon. Then narrow or remove stale later "city prerequisite" buckets so the same work is not duplicated.

For quests whose start, progress, and completion happen in different places, choose timing deliberately:

* Do not wait until the completion location if the player was just at the quest-start location and the next stage is soon.
* Do not start a quest at the earliest possible moment if it will sit untouched for a long time and there is a later efficient start-location visit before the next stage.
* Prefer the most recent efficient visit to the quest-start location before the next routed progress or completion step.
* Make exceptions for fragile first-visit starts, branch setup, missable dialogue, leveled reward gates, radiant target control, or objectives that must remain active for later route control.
* Revisit these decisions as later route sections are expanded. A quest start that looked good in an early pass may need to move earlier or later once the next progress point is known.

Do not ask the player to manipulate RNG or reroll ordinary radiant assignments as part of normal guide execution. If a target is randomized, respect the target the save actually gives and write a conditional route branch. Reserve save/reload language for explicit branch saves, trophy-pop fallback, bug recovery, or source-backed reward/state protection.

When several active objectives draw from overlapping randomized target pools, start every vulnerable objective before clearing any shared target location, then build the player's actual target list from the quest log. Route each unique target once, and tell the player to handle every active objective at that location before leaving. This is especially important when pre-clearing a location can block a later retrieval or when a single Forsworn camp/dungeon can satisfy a Daedric, miscellaneous, unique-item, location, and book objective together. Keep the player-facing branch concise, but record the full target-pool reasoning in the source note and coverage tracker.

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
* bug-prone actions;
* trophy/counter boundaries;
* dialogue options adjacent to a routed dialogue when a misclick would matter;
* skill books or quest-starting documents only when the route sends the player to interact with that exact object, shelf, table, container, or room.

Do not repeat generic book, note, dungeon, rumor, property, or Creation warnings that are already covered by Route Discipline.

## Detail Level

Be explicit about route-critical facts: NPC names, quest names, locations, puzzle solutions, item names, save points, branch reloads, gates, counters, and checklist cues.

Do not micromanage ordinary Skyrim play. Avoid routine combat advice, ordinary looting advice, and excessive carry-weight commentary unless it protects a route-critical objective or Survival Mode constraint.

Good:

`Before leaving, carry food, healing, lockpicks, enough empty carry space, and a ranged option.`

Too much:

`Loot only light valuables, use the wall for cover, attack only when the dragon is focused elsewhere, and avoid every nearby roadside marker.`

## Checklist Cues

Use `[CHECKLIST: ...]` only when an objective, reward, location, power, counter, branch outcome, or other checklist-relevant item is actually completed, acquired, discovered, or recorded.

Ordinary state checks such as "carry weight is controlled," "food is stocked," "Survival Mode is still on," and "a rotating manual save has been made" belong in route prose, not checklist cues.

Counters should state the target and current count, for example: `Record the Sideways counter at 1 of 10 qualifying side quests.`

## Section Boundaries

Player-facing route sections are area-and-state based, not rigid MR buckets. Internal MR labels are coordination handles only and should not appear in player-facing headings.

If detailed routing shows that a safe objective belongs earlier or later than the scaffold implied, move it and update:

* `drafts/final-guide/main-guide-v1.md`;
* `data/guide-coverage/main-guide-v1-coverage.csv`;
* any relevant source note;
* `docs/main-guide-v1-expansion-plan.md`, `docs/task-board.md`, or `docs/session-handoff.md` if the coordination state changes.

The internal section list itself is allowed to change. When nearby-objective audits move meaningful work earlier, remove that work from later theme buckets instead of leaving duplicate or stale instructions. When a newly unlocked quest is best handled in the next coherent geographic block, note that handoff and reshape the next block around the start/progress/completion bundle.

Apply new routing conventions retrospectively to already-expanded sections when they reveal a systemic issue. Do not wait for manual user audits to catch every missed same-location objective.

## No Section-End State Lists

Do not end guide chapters or sections with "End state before..." lists. They make the player-facing guide feel like a planning artifact and duplicate information already carried by route instructions, checklist cues, source notes, and the internal coverage tracker.

If continuity state matters for play, state it at the route point where it matters: for example, tell the player to keep a quest active before leaving town, preserve an item when it is acquired, or make a named hard save before the risky handoff. Keep broader state summaries in `data/guide-coverage/main-guide-v1-coverage.csv`, source notes, task-board notes, or handoff docs rather than in the player-facing route body.

## Internal Audit Layer

The guide must remain internally auditable, but audit machinery belongs outside the player-facing prose.

Use `data/guide-coverage/main-guide-v1-coverage.csv` for objective IDs, staged/completed status, checklist cue mapping, option/default rows, exclusions, and unresolved status. If the guide moves an objective earlier or later, update the coverage tracker in the same pass.

Use source notes for sourced gameplay facts that affect route order, gates, bugs, rewards, counters, or completion boundaries. Do not invent route facts to make a section read more cleanly.

## User-Facing Handoff

After each guide-expansion pass, the assistant response to the user should include a short routing-decision summary. Explain which nearby objectives were routed now, which were deliberately held, and why. Keep that explanation out of the player-facing guide body unless the player needs the information to execute the route safely.
