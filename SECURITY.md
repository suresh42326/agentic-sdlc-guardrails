# Security

## Reporting a vulnerability

If you find a vulnerability in these guardrail files — a permission gap, a redaction bypass, or a hook that fails open in a dangerous way — report it through GitHub private vulnerability reporting on this repository. Please do not open a public issue that includes a working bypass.

## What this template does not promise

The permission lists and the audit hook reduce the chance that an agent takes a destructive or leaky action. They do not sandbox the process, and they do not replace human review. Redaction looks for common secret shapes and sensitive key names. A novel secret format can still land in `.agents/audit/audit.jsonl`. That file is gitignored. Do not commit it, and do not paste it into an issue.

## Secrets in history

Before you publish a fork, scan the full git history with a secrets scanner. If anything is found, publish a new repository whose first commit is the cleaned tree. Rewriting a branch is not enough if the old objects remain reachable.
