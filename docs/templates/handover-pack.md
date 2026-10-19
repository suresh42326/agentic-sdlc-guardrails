<!--
TEMPLATE: Handover pack
Copy to: docs/handover/README.md
Use this when a different team will operate production.
Deliver it before go-live, then keep a short support window with a named contact.
Everything listed lives in the repository or is exported into it.
-->

# Handover — <Project name>

| Field | Value |
|---|---|
| Receiving team | <team and contact> |
| Delivered by | <name> |
| Delivery date | <YYYY-MM-DD> |
| Support window | <start> to <end>, contact <channel> |
| Release at handover | <vX.Y.Z> |

## 1. System overview

- Constitution: docs/constitution.md
- Architecture: docs/architecture/
- ADRs: docs/adr/
- Threat model: docs/security/threat-model.md

## 2. Environments and access

| Environment | Purpose | How to get access | Owner after handover |
|---|---|---|---|
| Staging | Release testing | <group> | |
| Production | Live | time-boxed | |

- Infrastructure as code: <path>. State: <backend>. Who can apply: <role>.
- Secrets: <vault name>. An inventory of secret *names* (never values) is in docs/handover/secrets-inventory.md.
- Credentials to rotate at handover: <list>

## 3. Build, release, deploy

- How to cut a release: <steps>
- Where the release evidence appears: <...>
- Deploy and rollback: docs/runbooks/deploy-and-rollback.md
- Mobile store accounts and update channels, if any: <...>

## 4. Operations

| Item | Where |
|---|---|
| Dashboards | <names> |
| SLOs | docs/constitution.md and the alert rules |
| Alerts | docs/runbooks/ |
| Errors | <project> |
| Model traces | <project> |
| Backup and the last restore test | docs/runbooks/restore.md |
| Disaster recovery | docs/runbooks/disaster-recovery.md |
| Incidents | docs/postmortems/ |
| Cost alerts | <...> |

## 5. Security

- Open waivers and their expiry: docs/waivers/
- Vulnerability policy in force: <summary>
- Last penetration test or dynamic scan: <reference>
- Security contact: <...>

## 6. Model features

- Inventory of features, models, and fallbacks: <...>
- Prompt files and golden sets: <paths>
- How to run evals: <command>
- Kill-switch flags: <...>
- Budgets and rate limits: <...>

## 7. Known issues

| Item | Severity | Issue |
|---|---|---|
| | | |

## 8. Acceptance

| Check | Done |
|---|---|
| Receiving team walked through deploy, rollback, and restore | ☐ |
| Their on-call can open dashboards, alerts, and runbooks | ☐ |
| Credentials rotated; standing access for the previous operators removed when the support window ends | ☐ |

| Role | Name | Date |
|---|---|---|
| Delivering tech lead | | |
| Receiving operator | | |
