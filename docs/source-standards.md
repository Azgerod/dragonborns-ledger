# Source Standards

These are the gameplay-research sourcing rules for the project. They are reflected in `AGENTS.md` and support the verification requirements in `docs/guide-specification.md`.

Do not perform gameplay research for repository-structure, documentation-normalization, or other infrastructure-only tasks.

## Source Priority

Use current online sources. Prioritize:

1. Bethesda official support and official Anniversary Edition information.
2. UESP.
3. Reliable trophy or achievement guides.
4. Well-maintained community checklists.
5. Community discussion only as secondary evidence.

## Citation Rule

Every factual gameplay claim that affects routing must include a citation in the relevant source notes under `sources/source-notes/`.

## Research Workflow

Before a gameplay fact enters `data/objectives/`, `data/constraints/`, route prototypes, branch routes, or final guide prose:

1. Add or update a source inventory row in `sources/bibliography.md`.
2. Create or update a source note under `sources/source-notes/`.
3. Record the claim, routing relevance, sources, confidence, and open questions in the source note.
4. Reference the source note from the relevant data row or route note.

Use one source note for one tight claim or a small cluster of tightly related claims. Do not use one large source note as a catch-all for an entire questline, faction, or Creation.

## Conflict Handling

If sources disagree:

1. Prefer the higher-priority source category when it directly answers the claim.
2. Record the disagreement in the source note.
3. Mark the related data row as unresolved or needing review.
4. Do not route the fact as settled until the conflict is resolved or explicitly carried as an uncertainty.

## Do Not Rely On Memory For

Do not rely on memory for:

* AE Creation start triggers.
* Leveled item thresholds.
* Quest conflicts.
* PS4 trophy behavior.
* Bug risks.
* Cell-entry locking.
* Missable rewards.
