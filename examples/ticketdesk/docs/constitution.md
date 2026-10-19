<!--
WORKED EXAMPLE for the fictional TicketDesk app.
Numbers are illustrative targets, not measurements from a running system.
Copy docs/templates/constitution.md and replace this file's contents when you start a real project.
-->

# TicketDesk — Constitution (example)

| Field | Value |
|---|---|
| Owning team | TicketDesk maintainers (example) |
| Tech lead | <name> |
| Product owner | <name> |
| Release manager | <name> |
| QA | <names> |
| Last amended | 2026-10-18 |

## 1. Purpose

TicketDesk is a multi-tenant support desk for software teams. Staff file tickets, assign them, and reply to the person who wrote in. A model suggests a category, a priority, and a draft reply. A staff member reviews that draft and is the only one who can send it.

## 2. Principles

1. Tenant data never crosses a tenant boundary, including in search, logs, and model prompts.
2. A human sends every customer-facing message. The model drafts; it does not send.
3. Ticket text is confidential. It is masked before it leaves the trust boundary.
4. Suggested replies that are not grounded in the ticket and the knowledge base are not shown.
5. Correctness of who can see a ticket beats speed of delivery.
6. These principles may tighten the baseline agent rules. They do not loosen them.

## 3. Non-goals

- TicketDesk does not replace a full IT service-management suite.
- The model does not close tickets, change assignees, or issue refunds.
- There is no mobile app in this example.
- This folder does not contain a running web app. It is documentation only.

## 4. Stack

| Layer | This project | ADR if this was a close call |
|---|---|---|
| Backend | Python, FastAPI | |
| Database | PostgreSQL | |
| Web | Next.js | |
| Mobile | Not in scope | |
| Hosting | Decided per deployment; no vendor is required by this example | |
| Model access | Through one gateway; model ids pinned per environment | |

## 5. Data sensitivity

| Category | Examples | Classification | Personal data? | Regulation |
|---|---|---|---|---|
| Account | staff name, email, role, tenant id | Confidential | Yes | GDPR, where EU residents are involved |
| Ticket | subject, body, attachments, requester email | Confidential | Yes | GDPR, where EU residents are involved |
| Model trace | masked prompt, suggestion, staff accept/reject | Confidential | Yes, until masked | Same as the ticket |

- Residency: the region named for that tenant. Logs, backups, embeddings, and model calls stay in that region.
- Processing outside the region: no.
- Retention: application logs 30 days, model traces 14 days, backups 30 days, closed tickets 2 years and then deleted, including embeddings.

## 6. Quality targets

| Characteristic | Requirement | Measured by |
|---|---|---|
| Correctness | Every acceptance criterion has an automated test | traceability report |
| Performance | See §7 | load test on release |
| Accessibility | WCAG 2.2 AA on create, assign, and reply | scanner, no serious violations |
| Reliability | See §8 | SLO dashboards |
| Security | ASVS L2 | review plus automated checks |
| Maintainability | Line coverage at least 80% on changed code; mutation score at least 60 on changed code | pull-request checks |

## 7. Performance budgets

| Flow | p95 latency | Error rate | Throughput | Notes |
|---|---|---|---|---|
| GET /api/tickets | 300 ms | 0.5% | 50 rps | excludes the model |
| POST /api/tickets | 400 ms | 0.5% | 20 rps | |
| Suggest reply, end to end | 4 s | 1% | 5 rps | includes the model call |
| Web LCP, queue and ticket page | 2.5 s | — | — | |

## 8. Service level objectives

| SLO | SLI | Target | Window |
|---|---|---|---|
| API availability | non-5xx / all responses | 99.5% | 28d |
| API latency | requests faster than 300 ms / all, model routes excluded | 95% | 28d |
| Suggestion success | suggestions a staff member can accept or edit / attempts | 90% | 28d |

When an error budget is spent, feature work pauses until reliability work restores it.

## 9. Security level

- ASVS level: L2 (accounts and personal data).
- Mobile: not applicable.
- Penetration test before first launch: yes.
- Vulnerability contact: the address published in the deployment's `security.txt`.

## 10. Recovery

| Objective | Target |
|---|---|
| RPO | 15 min |
| RTO | 4 h |
| Backups | Point-in-time recovery on the database, plus a monthly restore test |

## 11. Operating model

- Who runs production: the team that adopts this example.
- On-call: business hours in the team's timezone, unless that team writes a different rule here.
- Escalation: on-call, then tech lead.
- Support window after launch: 30 days, named contact in the handover pack.
- Telemetry: one backend per environment. Ticket bodies are not labels or log fields.

## 12. Model features

| Feature | Purpose | Risk | Personal data | Human approval | Monthly cost budget |
|---|---|---|---|---|---|
| Triage | Suggest category and priority from the ticket text | Medium | Ticket text, masked | Staff can override before save | Set per deployment |
| Suggested reply | Draft a reply from the ticket and the knowledge base | High | Ticket text, masked | Staff must edit or accept, then send | Set per deployment |

## 13. Approval

| Role | Name | Date |
|---|---|---|
| Tech lead | Example — not signed | |
| Product owner | Example — not signed | |

## Amendment log

| Date | Change | Pull request |
|---|---|---|
| 2026-10-18 | Illustrative initial constitution | |
