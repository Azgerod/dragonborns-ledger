# Checklist Coverage Strategy

Status: TB-031C escalation decisions complete.

Use this file to document how spreadsheet-tracked objectives will be mapped to the guide.

Allowed mapping outcomes:

* Main-route prototype block.
* Branch-route prototype.
* Option-list note.
* Appendix-only checklist.
* Explicit exclusion with justification.
* Source-readiness hold with a named owner.

TB-030 maps the raw spreadsheet rows to the current route-planning layer. It does not assign final black-box guide step numbers, because those do not exist yet.

Rows marked `scope_review_required` are not allowed to persist past TB-031A. TB-031A resolved the broad regular-book library rows as explicit exclusions from required route and appendix coverage; audit them in the matrix with `match_source=book_scope_review`.

Rows marked `manual_review_required` are not allowed to persist past TB-031B. TB-031B resolved the generic manual-review bucket by mapping source-supported rows to existing objectives/support tables and converting unpromoted checklist-only rows into typed `source_readiness_required` holds.

Rows marked `source_readiness_required` are not route-ready. They are explicit checklist-source reconciliation inputs whose `guide_location` names the earliest follow-up task that must validate, promote, or exclude the row before final checklist synchronization.

TB-031C resolved checklist-driven branch/radiant/counter escalation decisions. TB-031D resolved route-affecting defaults in `data/route-planning/route-default-decisions.md`. TB-031E through TB-031I remain the explicit follow-up tasks for progression source selection, counter mechanics, location route validation, source/objective/support-table/generated-index readiness, and final deferral-audit closure. Do not defer these reviews into final QA unless the task board is updated with a narrower unresolved-risk entry.

No checklist objective should remain unmapped in the final guide unless explicitly excluded and justified.
