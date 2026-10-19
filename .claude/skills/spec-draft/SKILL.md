---
name: spec-draft
description: Drafts a feature spec with user stories and EARS acceptance criteria from a short request, using docs/templates/spec.md. Use when a feature needs a spec, or when the human says "draft a spec".
---

# spec-draft

## Inputs

- A feature id and a short request from the person accountable for the product
- `docs/constitution.md` (principles, non-goals, budgets)
- `docs/templates/spec.md`

## Steps

1. Create `docs/specs/<ID>-<slug>/spec.md` from the template. Set status to `Draft`.
2. Write user stories as `As a <role>, I want <capability>, so that <outcome>`.
3. Write acceptance criteria in EARS, one behaviour each, with ids `<ID>/AC-n`:

| Pattern | Form |
|---|---|
| Ubiquitous | The system shall … |
| Event | **When** <trigger>, the system shall … |
| State | **While** <state>, the system shall … |
| Unwanted | **If** <condition>, **then** the system shall … |
| Optional | **Where** <feature>, the system shall … |

4. For every criterion, ask whether a test can prove it. If it cannot, rewrite it. Replace vague words ("fast", "friendly", "appropriate") with numbers.
5. Add criteria for authorization and, when the product is multi-tenant, for tenant isolation. Add unwanted-behaviour criteria for failures.
6. If the feature calls a model, fill in the AI intake section.
7. Put anything you are unsure about under **Open questions**. Do not guess. Grilling resolves them.

## Rules

- Write no code and no tests. A spec says what, not how.
- Anything that contradicts a non-goal goes under open questions, not into the spec body.
- The next step is `grill` on this spec.
