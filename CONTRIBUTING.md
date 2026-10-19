# Contributing

This repository is a template for agent guardrails. Changes should stay vendor-neutral: no employer names, client names, internal document numbers, or private URLs.

## What to change

- Baseline rules live in `.agents/org/org-rules.md`.
- Skills have one canonical copy in `.agents/skills/`. After you edit them, run `sh scripts/sync-skills.sh` so `.claude/skills/` matches.
- Permission lists live in `.claude/settings.json` (Claude Code) and `.vscode/settings.json` (Copilot). Keep the deny lists aligned.
- Blank forms live in `docs/templates/`. The TicketDesk documents under `examples/ticketdesk/` are a labelled sample. Do not turn that sample into a real application in this repository.

## Checks

```sh
python3 -m unittest discover -s tests -v
sh scripts/doctor.sh
```

The unit tests cover secret redaction, hook wiring, and a ban on known employer-specific strings.

## Pull requests

- One concern per pull request.
- Fill in `.github/pull_request_template.md`, including who prompted any agent that wrote the change.
- Do not commit `.agents/audit/`, `.env` files, or real personal data.
- A human reviews changes to the guardrail paths listed in `CODEOWNERS`. Replace `YOUR_GITHUB_USER` before you rely on that file.

## Publishing a copy

If this history ever contained private material, publish from a fresh repository with a single initial commit. Do not push the old history to a public remote.
