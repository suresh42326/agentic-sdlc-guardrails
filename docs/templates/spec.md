<!--
TEMPLATE: Feature spec
Copy to: docs/specs/<SPEC-ID>-<slug>/spec.md
Draft, grill, then approve. A small bugfix can be an issue with EARS criteria
instead of this file.
Ids: SPEC-<nnn> for the spec, SPEC-<nnn>/AC-<n> for a criterion.
Tests reference the criterion id.
-->

# SPEC-<nnn>: <Feature title>

| Field | Value |
|---|---|
| Status | Draft / Grilled / Approved / Superseded |
| Product owner | <name> |
| Tech lead | <name> |
| Risk | Low / Medium / **High** |
| Feature flag | `<flag-key>` (owner <name>, remove by <YYYY-MM-DD>) |
| Related ADRs | <ADR-NNNN> |

<!--
Low: docs or tests only.
Medium: application code.
High: auth, payments, personal data, migrations, infrastructure, permissions,
or a model/agent action that writes or sends.
High means a threat-model update, two approvals, and the security checklist.
-->

## 1. Problem and outcome

<What is wrong today, for whom, and which number will show that it is fixed.>

Success measure: <metric and target>

## 2. User stories

- **US-1** As a <role>, I want <capability>, so that <benefit>.
- **US-2** ...

## 3. Acceptance criteria (EARS)

<!--
Ubiquitous:   The <system> shall <response>.
Event:        When <trigger>, the <system> shall <response>.
State:        While <state>, the <system> shall <response>.
Unwanted:     If <condition>, then the <system> shall <response>.
Optional:     Where <feature>, the <system> shall <response>.
One behaviour per row. Each row maps to at least one automated test.
-->

| ID | Story | Criterion | Test layer |
|---|---|---|---|
| SPEC-<nnn>/AC-1 | US-1 | When <trigger>, the system shall <response>. | <unit/API/e2e/eval> |
| SPEC-<nnn>/AC-2 | US-1 | If <condition>, then the system shall <response>. | <layer> |

## 4. Out of scope

- <excluded behaviour>

## 5. Non-functional notes

<!-- Only deltas from the constitution. -->

- <note>

## 6. Data and privacy

- New personal data? <no / what, why, and how long you keep it>
- Shared with a third party, including a model provider? <no / what>

## 7. Model use

<!-- Required if the feature calls a model or runs an agent. Otherwise "Not applicable". -->

| Item | Answer |
|---|---|
| What the model does, and for whom | |
| Why a model, rather than ordinary code | |
| Risk | Low / Medium / High |
| Data sent to the model | <fields, classification, what you mask> |
| Retrieval sources | <sources and how permissions are applied> |
| Tools the model can call | <list; mark irreversible ones> |
| Where a human approves | |
| How the user is told a model is involved | |
| Model ids and fallback | |
| Eval metrics and thresholds | |
| Golden set | <path, size, who curates it> |
| Cost budget | <per task and per month> |
| Kill switch | flag `<flag-key>` |

## 8. Open questions

| # | Question | Owner | Answer |
|---|---|---|---|
| 1 | | | |

<!-- Status is Approved only when every question has an answer. -->

## 9. Approval

| Role | Name | Date |
|---|---|---|
| Product owner | | |
| Tech lead | | |
