# Source Note: Black Book Power Choice Sets

Status: researched; TB-031D defaults added.

Source note ID: SN-000048

## Claim

The seven Dragonborn Black Books award powers, abilities, or a perk-reset system that need source-list objective coverage separate from the quest rows that find or complete the Black Books.

## Routing Relevance

The specification requires Black Books and all permanent spells, powers, and abilities. Existing Dragonborn quest rows already track Black Book quests; this source note adds the reward-system layer so later passes can recommend defaults, handle switchable choices, and synchronize Hidden Knowledge and all-perks planning without writing route content now.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000045 | Skyrim:Black Book (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book_(book) | 2026-05-11 | Identifies the seven Black Books as a complete book-series inventory. |
| SRC-000167 | Skyrim:Powers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Powers | 2026-05-11 | Cross-checks Black Book powers and abilities in the powers inventory. |
| SRC-000050 | Skyrim:Black Book: The Hidden Twilight (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Hidden_Twilight_(quest) | 2026-05-11 | Supports Hidden Twilight reward choice handling. |
| SRC-000051 | Skyrim:Black Book: The Sallow Regent (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Sallow_Regent_(quest) | 2026-05-11 | Supports Sallow Regent reward choice handling. |
| SRC-000052 | Skyrim:Black Book: Untold Legends (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Untold_Legends_(quest) | 2026-05-11 | Supports Untold Legends reward choice handling. |
| SRC-000053 | Skyrim:Apocrypha (The Winds of Change) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Apocrypha_(The_Winds_of_Change) | 2026-05-11 | Supports Winds of Change location and reward context. |
| SRC-000329 | Skyrim:At the Summit of Apocrypha | 2 - UESP | https://en.uesp.net/wiki/Skyrim:At_the_Summit_of_Apocrypha | 2026-05-12 | Supports Waking Dreams skill-tree reset service after the Dragonborn finale. |
| SRC-000426 | Skyrim:The Gardener of Men | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Gardener_of_Men | 2026-05-12 | Supports Epistolary Acumen reward choices and effects. |
| SRC-000427 | Skyrim:Black Book: Filament and Filigree (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Filament_and_Filigree_(quest) | 2026-05-12 | Supports Filament and Filigree reward choices, effects, and reward-change note. |

## Evidence Summary

The seven Black Books are already represented as quest or book objectives in existing Dragonborn rows. Their reward layer still needs separate tracking because several books offer selectable powers or abilities, and Waking Dreams adds a perk-reset system that can matter to the all-perks plan.

TB-031D sets route defaults without making those choices irreversible. The relevant Black Book rewards can be changed by rereading the book on Solstheim where the source page states that behavior; Waking Dreams' post-finale skill-tree reset is a late progression service rather than a routine travel or leveling assumption.

| Black Book system | Source-backed effect set | TB-031D route default |
| --- | --- | --- |
| Waking Dreams | After `At the Summit of Apocrypha`, reading Waking Dreams gives access to skill-tree portals that clear and refund a single tree at the cost of one dragon soul. | Do not use routine perk resets during normal routing; reserve for controlled late progression/final validation. |
| Epistolary Acumen | Dragonborn Flame, Dragonborn Force, or Dragonborn Frost modify Fire Breath, Unrelenting Force, or Frost Breath respectively. | Dragonborn Force. |
| Filament and Filigree | Secret of Strength removes power-attack stamina cost for 30 seconds; Secret of Arcana removes spell magicka cost for 30 seconds; Secret of Protection halves damage for 30 seconds. | Secret of Arcana, with explicit temporary switches only if later route passes need them. |
| The Hidden Twilight | Mora's Agony, Mora's Grasp, or Mora's Boon; Mora's Boon fully restores health, magicka, and stamina. | Mora's Boon. |
| The Sallow Regent | Seeker of Might improves Combat skills; Seeker of Sorcery reduces spell cost and strengthens enchantments; Seeker of Shadows improves Stealth skills and potion strength. | Seeker of Sorcery as standing default; TB-031E may temporarily switch for potion, Smithing, or combat windows. |
| Untold Legends | Bardic Knowledge, Black Market, or Secret Servant; Secret Servant summons a Dremora butler for carry support. | Secret Servant. |
| The Winds of Change | Companion's Insight prevents player combat damage to followers in combat, Lover's Insight improves damage/prices by sex pairing, and Scholar's Insight adds a skill point from skill books. | Scholar's Insight until the skill-book plan is complete, then Companion's Insight as final default. |

## Confidence and Open Questions

Confidence is high that all seven reward systems need coverage and that the TB-031D defaults are safe route recommendations. Exact switch timing, Waking Dreams dragon-soul economy, skill-book read timing, and final validation remain deferred to TB-031E/TB-033.

## Linked Records

OBJ-000795 through OBJ-000801.
