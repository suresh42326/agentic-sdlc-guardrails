<!--
TEMPLATE: Architecture Decision Record (MADR-style)
Copy to: docs/adr/NNNN-short-title.md
Write one when a decision is hard to reverse, adds a core dependency, or
chooses a datastore, auth approach, or model provider.
The person accountable for the architecture approves it. Once Accepted, an
ADR is immutable. To change it, write a new ADR that supersedes it.
Delete this comment after you fill the record in.
-->

# ADR-NNNN: <Short title>

| Field | Value |
|---|---|
| Status | Proposed / Accepted / Rejected / Deprecated / Superseded by ADR-XXXX |
| Date | <YYYY-MM-DD> |
| Deciders | <names or roles> |
| Consulted | <names or roles> |
| Related spec(s) | <SPEC-nnn> |

## Context and problem statement

<!-- What forces the decision, and what question are you answering? -->

## Decision drivers

- <driver, for example "p95 under 300 ms at the stated load">
- <driver, for example "must run on more than one cloud">

## Considered options

1. <Option A>
2. <Option B>
3. <Option C>

## Decision outcome

Chosen option: **<Option X>**, because <justification tied to the drivers>.

### Consequences

- Good: <...>
- Accepted trade-off: <...>
- Follow-up: <issue links>

### Confirmation

<!-- How you will notice if the decision is ignored later: a test, a CI check, a metric. -->
- <example: an architecture test that features do not import each other>

## Pros and cons of the options

### <Option A>

- Good: <...>
- Bad: <...>

### <Option B>

- Good: <...>
- Bad: <...>

## More information

<!-- Links to specs and in-repo benchmarks. A reader should not need a private wiki. -->
