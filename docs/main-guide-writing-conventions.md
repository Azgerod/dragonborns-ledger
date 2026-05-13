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
4. The cited source notes and primary wiki pages when route timing depends on exact quest stage, cell state, reward state, ownership, bugs, or placed-object details.

The default answer should be "route it now" when an objective is safe, sourced, efficient, and naturally colocated. Hold it only for a concrete reason such as a level gate, cell-entry or clear-state risk, branch state, quest conflict, NPC dependency, trophy/counter boundary, skill-book read timing, ownership/theft risk, Survival/logistics issue, or missing source validation.

For the opening game and other fragile Survival segments, "safe and nearby" is not enough by itself. Optional combat-forward detours should usually wait until the player has reached the next settlement, sold or dropped excess Helgen loot, stocked food, rested if needed, and made a stable save. The opening route may still pull a nearby objective forward when it is truly low-risk or tightly bundled with the current action, but early stabilization beats harvesting every colocated item before the first support stop.

Do not assume early money that the route has not actually created. Property, mount, pet, armor, spell, crafting, training, and furnishing purchases should be routed at the first coherent point where normal routed loot, rewards, and selling can plausibly fund them. Do not use grinding, merchant exploits, free-purchase glitches, or "if you happen to have enough gold" as a hidden bridge unless the guide explicitly routes that economy plan and the user has approved the exploit/grind policy. For early homes in particular, unlocking purchase permission is not the same as buying and verifying storage.

Keep related objectives together where possible. Prefer a coherent bundle such as "start quest, enter location, collect the local book, clear the location, turn in the reward" over a shallow early action such as "discover but do not clear" unless that partial action has an independent route reason. Discovery-only, pickup-only, or "start now, ignore until much later" steps should be deliberate exceptions, not the default output of the nearby-objective audit.

For quests whose start, progress, and completion happen in different places, choose timing deliberately:

* Do not wait until the completion location if the player was just at the quest-start location and the next stage is soon.
* Do not start a quest at the earliest possible moment if it will sit untouched for a long time and there is a later efficient start-location visit before the next stage.
* Prefer the most recent efficient visit to the quest-start location before the next routed progress or completion step.
* Make exceptions for fragile first-visit starts, branch setup, missable dialogue, leveled reward gates, radiant seeding, or objectives that must remain active for later route control.
* Revisit these decisions as later route sections are expanded. A quest start that looked good in an early pass may need to move earlier or later once the next progress point is known.

If the player-facing guide warns the player away from a nearby objective, the internal coverage tracker must say why that objective is not routed now. If no source-backed reason survives the audit, remove the warning and replace it with a positive route instruction.

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

Ordinary state checks such as "carry weight is controlled," "food is stocked," "Survival Mode is still on," and "a rotating manual save has been made" belong in prose or end-state bullets, not checklist cues.

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

## End-State Blocks

End-state blocks should summarize route state clearly, not repeat every global prohibition. Include completed objectives, active quest state, important staged objectives, counters, gated returns, Survival readiness, and save state.

Avoid giant bullets beginning "You have not started..." unless a specific unstarted state is unusually important and not already covered by Route Discipline.

## Internal Audit Layer

The guide must remain internally auditable, but audit machinery belongs outside the player-facing prose.

Use `data/guide-coverage/main-guide-v1-coverage.csv` for objective IDs, staged/completed status, checklist cue mapping, option/default rows, exclusions, and unresolved status. If the guide moves an objective earlier or later, update the coverage tracker in the same pass.

Use source notes for sourced gameplay facts that affect route order, gates, bugs, rewards, counters, or completion boundaries. Do not invent route facts to make a section read more cleanly.
