# Checklist Coverage Strategy

Status: TB-032 warning overlay complete after TB-031J source-readiness review.

Use this file to document how spreadsheet-tracked objectives will be mapped to the guide.

Allowed mapping outcomes:

* Main-route prototype block.
* Branch-route prototype.
* Option-list note.
* Appendix-only checklist.
* Explicit exclusion with justification.
* Source-readiness hold with a named owner, only as a temporary review state before TB-031J.

TB-030 maps the raw spreadsheet rows to the current route-planning layer. It does not assign final black-box guide step numbers, because those do not exist yet.

Rows marked `scope_review_required` are not allowed to persist past TB-031A. TB-031A resolved the broad regular-book library rows as explicit exclusions from required route and appendix coverage; audit them in the matrix with `match_source=book_scope_review`.

Rows marked `manual_review_required` are not allowed to persist past TB-031B. TB-031B resolved the generic manual-review bucket by mapping source-supported rows to existing objectives/support tables and converting unpromoted checklist-only rows into typed `source_readiness_required` holds.

Rows marked `source_readiness_required` are not route-ready. They are explicit checklist-source reconciliation inputs whose `guide_location` names the earliest follow-up task that must validate, promote, or exclude the row before final checklist synchronization. After TB-031J, no generated checklist row should still use this status.

TB-031C resolved checklist-driven branch/radiant/counter escalation decisions. TB-031D resolved route-affecting defaults in `data/route-planning/route-default-decisions.md`. TB-031E resolved progression source selection in `data/constraints/progression-source-selection.md` and `data/constraints/progression-source-selections.csv`, including the TB-031E-owned source-readiness aliases. TB-031F resolved counter mechanics in `data/checklist-mapping/counter-coverage-plan.md`, including the TB-031F-owned source-readiness rows. TB-031G resolved location route validation in `data/locations/location-route-validation.md`, including the remaining location source-readiness row. TB-031H resolved source/objective/support-table/generated-index readiness ownership. TB-031I closed the deferred-work audit before warning prose. TB-031J then pulled the remaining 78 source-readiness rows forward, resolving them as source-backed main-route mappings, one branch-prototype mapping, or explicit exclusions before TB-032. TB-031K refreshed downstream planning artifacts so those decisions were current inputs to the warning layer. TB-032 then recorded the warning/hard-save triggers, which TB-033 validated.

No checklist objective should remain unmapped in the final guide unless explicitly excluded and justified.
