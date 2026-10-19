## Summary

<!-- What changed and why, in a few sentences. -->

## Links

- Spec or issue: <SPEC-nnn or issue>
- Task: <T-nnn-nn or n/a>
- Criteria: <SPEC-nnn/AC-1>
- ADRs: <ADR-NNNN or none>

## Risk

- [ ] Low — docs or tests only
- [ ] Medium — application code
- [ ] **High** — auth, payments, personal data, migrations, infrastructure, permissions, or a model/agent action that writes or sends

## Who wrote this

- [ ] A human
- [ ] An agent in pair mode
- [ ] An agent executing an approved task (branch `agent/*`)
- [ ] An unattended agent (needs two approvals)

Harness and model: <name>
Human who prompted the agent (accountable, and not the only approver): @<handle>

- [ ] Commits include `Agent-Model`, `Agent-Mode`, `Agent-Session`, and `Agent-Operator` (no agent `Co-Authored-By`)
- [ ] The agent stayed inside the task's file list. Guardrail files were not edited, or the repository owner is requested.

## Author checklist

- [ ] Tests were written first, and their names contain the criterion ids
- [ ] A bug fix includes a regression test that fails without the fix
- [ ] Local checks passed
- [ ] No new dependency, or the licence is justified in this pull request
- [ ] If the API schema changed, the generated client was regenerated
- [ ] Docs were updated where behaviour changed

## Database migration

- [ ] Not applicable
- [ ] This pull request is only the expand, migrate, or contract step
- [ ] The migration linter passes; indexes on existing tables are created concurrently
- [ ] Downgrade was tested (up, down, up) or the pull request explains why it cannot be

## Feature flag

- [ ] Not applicable
- [ ] Flag `<key>` defaults off; owner `<name>`; remove by `<YYYY-MM-DD>`

## Model changes

- [ ] Not applicable
- [ ] Prompts live in files, not inline in code
- [ ] Evals passed, and thresholds were unchanged or tightened
- [ ] New tools are allow-listed, typed, and wait for a human when the action is irreversible

## Security checklist (required for High)

- [ ] Threat model updated: <link>
- [ ] Authorization is enforced on the server, with ownership checks
- [ ] Input is validated; output is encoded; queries are parameterized
- [ ] No secrets in code, config, prompts, or logs
- [ ] Personal data is minimised, masked in logs and prompts, and deleted on schedule
- [ ] New outbound calls have timeouts
- [ ] Security reviewer: @<handle>

## Reviewer checklist

- [ ] Solves the spec and does not sneak in unrelated changes
- [ ] Tests assert behaviour
- [ ] Matches the constitution and the ADRs
- [ ] For agent pull requests: no expansion of scope or permissions
