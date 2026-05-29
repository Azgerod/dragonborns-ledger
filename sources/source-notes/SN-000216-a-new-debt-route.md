# SN-000216 - A New Debt Route

Status: researched.

Source note ID: SN-000216

## Claim

`A New Debt` can be closed as a controlled Raven Rock follow-up immediately after the Tel Mithryn steward route. The guide should let Mogrul's nonpayment state create the debt-collector encounter, take and read `Mogrul's Orders` from the thugs, then return to Mogrul and pay the full 1,000-gold debt. `Note from Mogrul` remains unresolved because its source page has no fixed location field and the checked quest/NPC pages do not provide a deterministic normal-play pickup path for the note itself.

## Routing Relevance

TB-038R carried `OBJ-000423` and `OBJ-001324` forward because the original Solstheim route left `A New Debt` open across several Raven Rock sections while waiting for `Mogrul's Orders`. The high-risk part is the quest state, not the later Solstheim geography: after `Reluctant Steward`, Mogrul confronts the player in Raven Rock, the nonpayment dialogue enables collectors, the collectors carry `Mogrul's Orders`, and the quest can then be completed by paying Mogrul. Closing the sequence in the same Raven Rock return avoids indefinite conditional carryforward into Kolbjorn, Fahlbtharz, and later Solstheim sections.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001541 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_New_Debt | 2026-05-29 | Quest prerequisite, Raven Rock confrontation, nonpayment collector state, 1,000-gold payment, kill alternative, Intimidate option, Drovas contribution, and bug notes. |
| SRC-001542 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mogrul%27s_Orders | 2026-05-29 | Quest-document identity and Mogrul's thug carrier source. |
| SRC-001543 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Note_from_Mogrul | 2026-05-29 | Quest-document identity and blank location field, supporting unresolved treatment. |
| SRC-001544 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mogrul%27s_Thug | 2026-05-29 | Debt-collector encounter context, hostile leveled thugs, approach line, and `Mogrul's Orders` inventory. |
| SRC-001545 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mogrul_(Dragonborn) | 2026-05-29 | Mogrul's Raven Rock location, post-`Reluctant Steward` collection role, payment/kill choices, and permanent-hostility bug caveat. |
| SRC-001546 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reluctant_Steward | 2026-05-29 | Drovas steward route, reward/access context, next quest link, and warning to expect Mogrul on the next Raven Rock return. |

## Evidence Summary

UESP lists `A New Debt` as a Dragonborn side quest given by Mogrul in Raven Rock after `Reluctant Steward`. The quick walkthrough is to be informed of the inherited debt and then pay the debt or kill Mogrul. The detailed walkthrough states that once Drovas is under Neloth's protection, Mogrul expects the player to pay Drovas's 1,000-gold debt, and that he will send thugs until the debt is paid.

The Mogrul dialogue gives several outcomes. Paying 1,000 gold completes the debt. Choosing the nonpayment line leaves the debt active and warns that collectors will be sent. The Intimidate option can reduce the payment to 500 gold only on a successful check; a failed check makes no progress. Killing Mogrul is a quest-completion alternative, but the quest page warns that Redoran Guard intervention can create a bounty risk, and the Mogrul NPC page records a possible permanent-hostility issue.

UESP's `Mogrul's Orders` page lists the document as quest-related to `A New Debt` and carried by Mogrul's thugs. The Mogrul's Thug page says the thugs can be encountered during `A New Debt` depending on gameplay choices, approach with a debt-collection line, and carry `Mogrul's Orders`. The checked sources therefore support a route that chooses nonpayment once, handles the debt collectors, loots/reads `Mogrul's Orders`, and then removes the debt state by paying Mogrul.

The `Note from Mogrul` page is also quest-related to `A New Debt`, but its location field is blank. The checked quest, Mogrul, and thug pages do not identify a fixed carrier, container, or repeatable pickup path for that note. The route should not pretend this row is solved by the thug encounter for `Mogrul's Orders`.

## Route Decision

Replace the long conditional carryforward with a closed Raven Rock debt sequence in `Tel Mithryn, Nchardak, And Kagrumez`: make `HARD SAVE: HS-DRAGONBORN-A-NEW-DEBT`, choose Mogrul's nonpayment dialogue once, leave Raven Rock on foot until the debt collectors approach, kill the thugs, loot and read `Mogrul's Orders`, then return to Raven Rock and pay Mogrul the full 1,000 gold. If Mogrul or Slitter enters an unstable hostile state before the payment path is available, reload the hard save.

This closes `OBJ-000423`, `CHK-QUESTS-0548`, and `OBJ-001324`. Keep `OBJ-001325` as an explicit `NEEDS ROUTE RESOLUTION` row.

## Confidence and Open Questions

Confidence is medium-high for closing `A New Debt` safely after collecting `Mogrul's Orders`: the source-backed quest mechanics are straightforward, but the debt-collector encounter is still a world interaction rather than a named fixed location. The route mitigates this with a local hard save and immediate quest-state cleanup. Confidence is low for `Note from Mogrul`; no deterministic normal-play acquisition path has been identified.

## Linked Records

`OBJ-000423`; `CHK-QUESTS-0548`; `OBJ-001324`; `OBJ-001325`; `BOOKLOC-001567`; `BOOKLOC-001568`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv`.
