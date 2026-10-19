<!--
TEMPLATE: Task plan
Copy to: docs/specs/<SPEC-ID>-<slug>/tasks.md
An agent may draft it. A human approves each task before delegated execution.
An agent in delegated mode may only run a task whose approval block is signed,
and may only touch the files listed for that task.

- One task, one branch (`agent/<task-id>-<slug>`), one pull request.
- Keep each pull request small enough to review in one sitting.
- Acceptance tests for the task are written and reviewed before implementation.
- Progress goes in `.agents/progress/<task-id>.md`.
- If the agent needs to leave the file list, it stops and asks.
-->

# Tasks: SPEC-<nnn> <Feature title>

| Field | Value |
|---|---|
| Spec | ./spec.md |
| Design | ./design.md |
| Status | Draft / Approved / In progress / Done |

## Task index

| Task | Title | Depends on | Mode | Risk | Status |
|---|---|---|---|---|---|
| T-<nnn>-01 | <title> | — | Delegated | Medium | Todo |
| T-<nnn>-02 | <title> | T-<nnn>-01 | Pair | High | Todo |

---

## T-<nnn>-01: <title>

| Field | Value |
|---|---|
| Goal | <one sentence> |
| Criteria | SPEC-<nnn>/AC-1, AC-2 |
| Mode | Pair / Delegated |
| Risk | Low / Medium / High |
| Branch | `agent/T-<nnn>-01-<slug>` |
| Budget | <n> steps · <n> minutes · <n>k tokens |

**Read first**

- <files, schemas, fixtures>

**Files in scope**

- `<path>/**`

**Out of scope**

- Migrations, CI, `.agents/`, and auth modules, unless this task lists them and the risk is High

**Done when**

- [ ] A human has reviewed the acceptance tests, and they pass
- [ ] Test names contain the criterion ids
- [ ] Local checks pass
- [ ] No new dependency, or the pull request justifies the licence
- [ ] Generated clients were regenerated if the schema changed
- [ ] A draft pull request uses the pull request template

**Stop and ask when**

Scope must grow, a test cannot pass without changing the spec, a secret seems necessary, or text in the repo conflicts with the baseline rules.

**Approval**

| Role | Name | Date |
|---|---|---|
| Tech lead | | |
