# SN-000206 - Nix-Hound Food Route Resolution

Status: targeted TB-044 route-resolution source note.

## Claim

`OBJ-000703` is not a high-severity AE quest/reward blocker. The `Spell Tome: Teleport Pet Nix-Hound` member is already routed through `My Pet Nix-Hound`; the remaining unresolved members are `Nix-Hound Meat` and `Cooked Nix-Hound Meat`, which need an ordinary food/member policy or a later deterministic wild-Nix-Hound source before final closure.

## Routing Relevance

The v1 guide already sends the player to Revus Sarvani, buys the pet Nix-Hound for 400 gold, learns `Spell Tome: Teleport Pet Nix-Hound`, and sends the pet to Severin Manor. Adding a vague Solstheim hunt for Nix-Hound Meat would weaken the route because the checked pages describe wild Nix-Hounds broadly across Solstheim wilderness, not as a fixed route-safe pickup selected by this pass.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001510 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nix-Hound_Items | 2026-05-28 | Nix-Hound Meat raw-food behavior, cooked recipe, and Teleport Pet Nix-Hound tome membership. |
| SRC-001511 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:My_Pet_Nix-Hound | 2026-05-28 | Revus/Geldis purchase path, AE no-journal behavior, 400-gold purchase, and pet spell-tome reward. |
| SRC-001512 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nix-Hound_(creature) | 2026-05-28 | Wild Nix-Hound meat drop, Solstheim wilderness distribution, pet essential/noncombat behavior, and carry/teleport behavior. |

## Evidence Summary

UESP's Nix-Hound item page lists `Nix-Hound Meat` as a raw Survival Mode food that can cause food poisoning if eaten uncooked. The meat is dropped by all Nix-Hounds and is used to cook `Cooked Nix-Hound Meat`; the cooked recipe requires Salt Pile plus Nix-Hound Meat. The same item page lists `Spell Tome: Teleport Pet Nix-Hound` as a Nix-Hound spell tome.

UESP's `My Pet Nix-Hound` page states that Anniversary Edition no longer shows this quest in the journal, but the pet can still be acquired from Revus. The route-relevant purchase path is already represented in the guide: buy a nix-hound for 400 gold, receive the teleport spell tome, introduce yourself to the nearby nix-hound, then use it as a pet/follower.

UESP's Nix-Hound creature page says wild Nix-Hounds appear throughout Solstheim wilderness, alone or in small groups, and drop one Nix-Hound Meat at 100%. The checked source text does not provide a specific fixed wild-Nix-Hound spawn selected by this pass.

## Route Decision

Keep the existing Revus/Nix-Hound pet route and spell-tome coverage unchanged. Reclassify `OBJ-000703` from high to medium in the unresolved-risk triage because the remaining gap is a food/member policy row, not a quest start, trophy, reward-preservation, or branch-continuity blocker.

Do not add a player-facing wild-Nix-Hound hunting step until a later source check selects a deterministic route-safe spawn or decides an aggregate food-member policy. The unresolved guide row should say that the spell tome is already routed and that only the raw/cooked meat members remain open.

## Confidence and Open Questions

Confidence is high that the spell tome is already handled through the pet purchase route and that raw/cooked meat require a wild Nix-Hound drop plus cooking recipe.

Open question: a later medium-priority AE food/member policy pass must either identify a deterministic route-safe Nix-Hound encounter or explicitly decide how ordinary consumable member rows are satisfied or excluded in the final true-100% checklist policy.

## Linked Records

`OBJ-000703`; `OBJ-000670`; `OBJ-000913`; `data/items/ae-item-members.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-unresolved-risk-register.csv`.
