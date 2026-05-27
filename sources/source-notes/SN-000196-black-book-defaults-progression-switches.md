# SN-000196 - Black Book Defaults and Progression Switches

Status: researched for TB-035-MR-062.

This note supports the `Black Book Defaults and Progression Switches` section in `drafts/final-guide/main-guide-v1.md`.

## Sources

| source_id | Priority | Source | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001427 | 2 - UESP | Skyrim:Black Book (book) | https://en.uesp.net/wiki/Skyrim:Black_Book_(book) | 2026-05-13 | Seven Black Book title inventory. |
| SRC-001428 | 2 - UESP | Skyrim:Black Book: The Winds of Change (quest) | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Winds_of_Change_(quest) | 2026-05-13 | Companion's Insight, Lover's Insight, Scholar's Insight, Solstheim reward switching, and Scholar's Insight skill-book effect. |
| SRC-001429 | 2 - UESP | Skyrim:Black Book: The Sallow Regent (quest) | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Sallow_Regent_(quest) | 2026-05-13 | Seeker of Might, Seeker of Shadows, Seeker of Sorcery, and related crafting/combat effects. |
| SRC-001430 | 2 - UESP | Skyrim:At the Summit of Apocrypha | https://en.uesp.net/wiki/Skyrim:At_the_Summit_of_Apocrypha | 2026-05-13 | Waking Dreams post-finale skill-tree reset service, one-dragon-soul reset cost, Solstheim reading requirement, and permanent Black Book quest-item state. |
| SRC-001431 | 2 - UESP | Skyrim:The Gardener of Men | https://en.uesp.net/wiki/Skyrim:The_Gardener_of_Men | 2026-05-13 | Epistolary Acumen reward choices and Dragonborn Force effect. |
| SRC-001432 | 2 - UESP | Skyrim:Black Book: Filament and Filigree (quest) | https://en.uesp.net/wiki/Skyrim:Black_Book:_Filament_and_Filigree_(quest) | 2026-05-13 | Secret of Arcana, Secret of Strength, and Secret of Protection reward choices. |
| SRC-001433 | 2 - UESP | Skyrim:Black Book: The Hidden Twilight (quest) | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Hidden_Twilight_(quest) | 2026-05-13 | Mora's Boon, Mora's Agony, and Mora's Grasp reward choices. |
| SRC-001434 | 2 - UESP | Skyrim:Black Book: Untold Legends (quest) | https://en.uesp.net/wiki/Skyrim:Black_Book:_Untold_Legends_(quest) | 2026-05-13 | Untold Legends reward route and Secret Servant choice. |
| SN-000048 | Internal source note | Black Book Power Choice Sets | sources/source-notes/SN-000048-black-book-power-choice-sets.md | 2026-05-11 | TB-031D default register for the Black Book power systems. |

## Route Placement

The section is a controlled Solstheim maintenance stop after the high-risk AE pass. All seven Black Books have already been acquired and read by this point. The player has the main route's major combat, Vampire Lord, main quest, Dragonborn finale, and AE reward states stabilized, so rerouting back to Solstheim for power reconciliation is low-risk and avoids carrying ambiguous Black Book defaults into the final cleanup layers.

The guide actively reselects the changeable standing defaults instead of merely asking the player to remember prior choices. For Epistolary Acumen, the route keeps the already-selected `Dragonborn Force` default from the earlier `The Gardener of Men` pass.

- `Dragonborn Force` from Epistolary Acumen is retained as the standing shout modifier.
- `Secret of Arcana` from Filament and Filigree.
- `Mora's Boon` from The Hidden Twilight.
- `Seeker of Sorcery` from The Sallow Regent.
- `Secret Servant` from Untold Legends.
- `Scholar's Insight` from The Winds of Change, retained until the selected skill-book route is complete.

This is intentionally isolated from nearby Raven Rock or Tel Mithryn work. It is a state-maintenance pass, not a geography sweep. Nearby physical objectives remain controlled by the later location, collectible, book, crafting, and property passes.

## Scholar's Insight Timing

The section does not switch to `Companion's Insight` yet. Several selected skill-book sources remain in the pending G14 book/document pass, and `Scholar's Insight` is still the route-critical skill-book default. The player-facing guide states that Companion's Insight will become the final Winds of Change default only after the planned skill-book route is complete.

## Waking Dreams Reset Handling

Waking Dreams' reset service is available after `At the Summit of Apocrypha`, but each tree reset costs one dragon soul. The guide therefore records the service and preserves dragon souls for named reset windows rather than spending resets in this maintenance section. The all-perks and level-252 work remains in the later all-perks loop.

## Unresolved Rows

No new `NEEDS ROUTE RESOLUTION` rows are introduced by this pass. Existing unresolved rows remain inherited: `Note from Mogrul`, Potion of Blood, Ironwood Soup Elixir, and Mysterious Potion. `Filial Bonds`/Torkild is now closed earlier by the pre-Storn search circuit. `Weakened Sigil Stone` is excluded from this route.

## Linked Records

OBJ-000795; OBJ-000796; OBJ-000797; OBJ-000798; OBJ-000799; OBJ-000800; OBJ-000801; PROGSEL-000593.
