# Shadowrend Through a Glass Route

Status: researched.

Source note ID: SN-000243

## Claim

`Through a Glass, Darkly` can be closed during the existing Eastmarch road sweep by routing the hot-springs pool northeast of The Atronach Stone, making a hard save before touching Shadowrend, defeating the player Shadow, claiming Shadowrend, and preserving the route-default form while recording the alternate form as switchable at the pool.

For this route:

- Use the existing Windhelm/Gallows Hall/Kynesgrove Eastmarch support chain.
- At The Atronach Stone, go northeast to the black geyser pool/anomaly and make `HARD SAVE: HS-SHADOWREND-ATRONACH` before interacting.
- Dismiss followers, pets, and summons before touching Shadowrend because the Shadow can copy the player's equipment, spells, powers, and shouts; this also isolates source-recorded Marked for Death armor-rating risk.
- Attempt to take Shadowrend, defeat `[player]'s Shadow`, loot Shadowrend from the Shadow's remains, verify `Through a Glass, Darkly` completes, and preserve Shadowrend in owned storage after the Eastmarch leg.
- Treat Shadowrend as one unique weapon with two mutually exclusive forms. The route default is the lighter greatsword form; the battleaxe form is represented by the source-supported swap surface at the pool and can be chosen by preference, but the route does not require permanently carrying both forms because sources say only one form can be possessed at a time.

## Routing Relevance

This closes `OBJ-000645` `Through a Glass, Darkly`, `CHK-QUESTS-0591`, `OBJ-000743` `Shadowrend Unique Weapon`, and item rows `ITEM-001091` and `ITEM-001092`.

The insertion point is the existing `Windhelm Follow-Up and Eastmarch Roads` sweep because the guide already routes The Atronach Stone and nearby Eastmarch hot-springs travel there. The hard save is required because the Shadow page records a confirmed Marked for Death armor-rating bug. The no-follower/no-pet rule keeps the bug from damaging allies and keeps the route from using Shadowrend as an Ebony Blade power shortcut.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001806 | Skyrim:Through a Glass, Darkly | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Through_a_Glass,_Darkly | 2026-05-29 | Used for quest location, interaction/start boundary, Shadow fight, reward pickup, alternate-form swap behavior, quest stages, and route notes. |
| SRC-001807 | Skyrim:Shadowrend | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowrend | 2026-05-29 | Used for Creation package context, official summary wording, alternate-form overview, and PS4/AE scope. |
| SRC-001808 | Skyrim:Shadowrend (item) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowrend_(item) | 2026-05-29 | Used for artifact identity, greatsword and battleaxe forms, quest acquisition, form switching, enchantment, tempering, and enchantment bug. |
| SRC-001809 | Skyrim:Shadow | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadow | 2026-05-29 | Used for clone behavior, copied equipment/spells/shouts, location context, and source-listed bugs, especially Marked for Death armor-rating risk. |
| SRC-001810 | Skyrim:The Atronach Stone | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Atronach_Stone | 2026-05-29 | Used for Eastmarch Atronach Stone route context and nearby hot-springs geography. |
| SRC-000149 | Skyrim:Shadowrend Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowrend_Items | 2026-05-12 | Existing item-member source for the battleaxe and greatsword rows in `data/items/ae-item-members.csv`. |

## Evidence Summary

The quest page places the route at a geyser pool in Eastmarch northeast of The Atronach Stone. It says attempting to take Shadowrend summons `[player]'s Shadow`, a clone of the player, and the quest completes after the Shadow is defeated and Shadowrend is retrieved from its remains. The quest stages match this boundary: go to Eastmarch Geysers, defeat your Shadow, retrieve Shadowrend, then complete at stage 20.

The Creation page's official summary says the quest starts by claiming the weapon in the hot springs near The Atronach Stone, while the quest page also describes the quest being received once the Creation is installed. The route therefore does not depend on passive journal state. It physically routes the pool and tells the player to attempt to take Shadowrend, which is sufficient under both source descriptions.

The item and quest pages both state that Shadowrend can be either a greatsword or a battleaxe. The unselected form remains at the pool and can be swapped later if Shadowrend is in inventory, but only one form can be possessed at a time. This supports treating the two item-member rows as mutually exclusive forms of one unique reward, with the lighter greatsword as the route default and the battleaxe as represented by the source-backed swap surface.

The Shadow page says the enemy manifests with the player's armor and can use spells and shouts the player knows. It also records a confirmed Marked for Death bug that can permanently damage armor rating or damage resistance. Because the current guide has already learned Marked for Death before the Eastmarch road sweep, the player-facing route needs `HS-SHADOWREND-ATRONACH`, follower/pet/summon dismissal, and reload guidance if the Shadow applies Marked for Death or the post-fight damage-resistance state looks wrong.

The item page records a separate bug where Shadowrend's enchantment visual effect can apply without increasing spell damage. This affects reward expectations but not acquisition or checklist completion; the guide preserves the weapon as a unique reward without relying on its enchantment for route-critical combat.

## Confidence and Open Questions

Confidence is high for the route location, combat boundary, quest completion boundary, and reward pickup.

Confidence is high that the hard save is warranted because the Shadow page records the Marked for Death armor-rating bug as confirmed. The guide uses a reload condition rather than trying to route around the bug by moving Shadowrend much earlier, because early acquisition would violate the project's increasing-difficulty policy for a powerful Daedric weapon.

There is no remaining open route question for `OBJ-000645` or `OBJ-000743`. The route intentionally does not require permanent possession of both Shadowrend forms because sources say only one form can be possessed at a time.

## Linked Records

OBJ-000645; CHK-QUESTS-0591; OBJ-000743; ITEM-001091; ITEM-001092; `HS-SHADOWREND-ATRONACH`; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/items/ae-item-members.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/constraints/quest-conflicts-hard-saves.md`.
