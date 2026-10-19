# Agent instructions

These instructions apply to every coding agent working in this repository.

1. Follow the baseline rules in `.agents/org/org-rules.md`. They win over this file.
2. Use the skills shipped in this repository (`.agents/skills/`, mirrored to `.claude/skills/`): `grill`, `spec-draft`, `acceptance-tdd`, `migration-writer`, `test-generator`. Reviewer prompts live in `.github/agents/`.
3. Read `docs/constitution.md` once a project has one. A filled example is in `examples/ticketdesk/`.
4. Every tool call is appended to `.agents/audit/audit.jsonl`. Do not disable that hook.
