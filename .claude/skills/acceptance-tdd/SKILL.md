---
name: acceptance-tdd
description: Implements one approved task acceptance-test-first. Writes API or end-to-end tests from the EARS criteria, stops for human review, then implements in thin vertical slices. Use for an approved task, or when the human says "implement T<n>".
---

# acceptance-tdd

## Inputs

- One task from `docs/specs/<ID>/tasks.md` whose status is `Approved`
- The acceptance criteria that task names
- `AGENTS.md` and the relevant ADRs

## Phase A — tests, then stop

1. For each named criterion, write an acceptance test through the public interface (HTTP or browser). Name it so the criterion id is in the test name, for example `test_td007_ac2_breach_notifies_assignee`.
2. For every new endpoint in a multi-tenant product, add a cross-tenant test: a caller from another tenant receives a not-found (or the project's equivalent), and never the first tenant's data.
3. Run the tests. Confirm they fail because the behaviour is missing, not because a fixture is broken.
4. Write `.agents/progress/<task-id>.md`. **Stop and ask a human to review the tests.** Do not implement until they say so.

## Phase B — one slice at a time

5. Pick one failing acceptance test. Write the smallest code that makes it pass. Add unit tests only where the logic is easy to get wrong. Repeat. Do not write every test and then all of the code in two lumps.
6. After each green step, run the affected tests and update the progress file.
7. Refactor only while the tests are green.
8. Finish by running the project's local checks. Fix failures. Do not suppress them.

## Rules

- Change only the task's **Files in scope**. If you need another file, stop and ask.
- Do not edit, skip, or weaken an approved acceptance test to make it pass. If the test looks wrong, stop and ask.
- A bug fix starts with a regression test that fails without the fix.
- In delegated mode: branch `agent/<task-id>-<slug>`, open a draft pull request, and add the `Agent-*` trailers from the baseline rules.
