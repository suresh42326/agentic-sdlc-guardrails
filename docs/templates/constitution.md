<!--
TEMPLATE: Project constitution
Copy to: docs/constitution.md
Written when the project starts. Changed only by pull request.
Owners: the person accountable for the architecture and the person accountable for the product.
Agents read this file as durable context. Keep it short. Replace every placeholder.
A filled example lives in examples/ticketdesk/docs/constitution.md.
-->

# <Project name> — Constitution

| Field | Value |
|---|---|
| Owning team | <team> |
| Tech lead | <name> |
| Product owner | <name> |
| Release manager | <name> |
| QA | <names> |
| Last amended | <YYYY-MM-DD> |

## 1. Purpose

<!-- Two or three sentences: who uses this system and what outcome it delivers. -->

<purpose>

## 2. Principles

<!-- Five to eight principles. A principle may tighten the baseline agent rules. It may not loosen them. -->

1. <example: "A human sends every customer-facing message.">
2. <example: "Every user-visible model output names its source.">
3. <...>

## 3. Non-goals

<!-- What this project will not do. Stops scope creep and agent over-reach. -->

- <non-goal>
- <non-goal>

## 4. Stack

| Layer | This project | ADR if this was a close call |
|---|---|---|
| Backend | <language and framework> | |
| Database | <engine> | |
| Web | <framework, or "none"> | |
| Mobile | <framework, or "not in scope"> | |
| Hosting | <provider, or "undecided"> | |
| Model access | <gateway and pinned models, or "none"> | |

## 5. Data sensitivity

| Category | Examples | Classification (Public / Internal / Confidential / Restricted) | Personal data? | Regulation |
|---|---|---|---|---|
| <category> | <examples> | <class> | <yes/no> | <GDPR, HIPAA, PCI, none> |

- Residency: <regions where data, logs, backups, embeddings, and model calls may run>
- Processing outside those regions: <no / yes, with approval from …>
- Retention: logs <n days>, model traces <n days>, backups <n days>

## 6. Quality targets

<!-- Only rows with a number. "N/A" needs a reason. -->

| Characteristic | Requirement | Measured by |
|---|---|---|
| Correctness | <every acceptance criterion has an automated test> | traceability report |
| Performance | See §7 | load test on release |
| Accessibility | <WCAG level on the key flows> | scanner, no serious violations |
| Reliability | See §8 | SLO dashboards |
| Security | <ASVS level> | review plus automated checks |
| Maintainability | <coverage and mutation targets you actually enforce> | pull-request checks |

## 7. Performance budgets

| Flow | p95 latency | Error rate | Throughput | Notes |
|---|---|---|---|---|
| <GET /api/...> | <300 ms> | <0.5%> | <50 rps> | |
| Web LCP, key pages | <2.5 s> | — | — | |
| Model feature, end to end | <4 s> | <1%> | | includes the model call |

## 8. Service level objectives

<!-- Window is 28 days unless you say otherwise. -->

| SLO | SLI | Target | Window |
|---|---|---|---|
| API availability | non-5xx / all responses | <99.5%> | 28d |
| API latency | requests faster than <300 ms> / all | <95%> | 28d |
| Model task success | successful completions / attempts on a labelled sample | <90%> | 28d |

When an error budget is spent, feature work pauses until reliability work restores it.

## 9. Security level

- ASVS level: <L1, or L2 when the product handles accounts, personal data, or payments>
- Mobile (MASVS): <L1 / L2 / not applicable>
- Penetration test before first launch: <yes if L2 / no>
- Vulnerability contact: <security.txt URL or mailbox>

## 10. Recovery

| Objective | Target |
|---|---|
| RPO (maximum data loss) | <for example 15 min> |
| RTO (maximum time to restore) | <for example 4 h> |
| Backups | <method, plus a restore test on a schedule> |

## 11. Operating model

- Who runs production: <team>
- On-call hours and timezone: <...>
- Escalation: <roles>
- Support window after launch: <dates and who is on point>
- Where telemetry lives: <system; keep it separate per environment>

## 12. Model features

<!-- One row per feature that calls a model. Write "None" if there are none. -->

| Feature | Purpose | Risk | Personal data | Human approval | Monthly cost budget |
|---|---|---|---|---|---|
| <feature> | <purpose> | <low/medium/high> | <class> | <where a human decides> | <amount> |

## 13. Approval

| Role | Name | Date |
|---|---|---|
| Tech lead | | |
| Product owner | | |

## Amendment log

| Date | Change | Pull request |
|---|---|---|
| <date> | Initial | <#> |
