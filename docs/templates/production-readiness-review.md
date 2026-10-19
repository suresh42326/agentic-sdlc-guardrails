<!--
TEMPLATE: Production readiness review
Copy to: docs/release/prr.md
Do this once, before the first production launch, and again after a major
architecture change (new datastore, new model capability, new deployable).
Participants: tech lead, release manager, QA, a security reviewer, and the
person who will operate production.
Every "No" is either fixed before launch or covered by a waiver with an expiry.
-->

# Production readiness — <Project name>

| Field | Value |
|---|---|
| Date | <YYYY-MM-DD> |
| Release | <vX.Y.Z> |
| Participants | <names and roles> |
| Decision | Go / Go with waivers / No-go |

## 1. Architecture

| Check | Yes/No | Evidence |
|---|---|---|
| Constitution approved (targets, SLOs, RPO/RTO) | | docs/constitution.md |
| Context and container diagrams are current | | docs/architecture/ |
| ADRs exist for hard-to-reverse decisions | | docs/adr/ |
| Threat model is current, with no open high-impact threats | | docs/security/threat-model.md |

## 2. Reliability

| Check | Yes/No | Evidence |
|---|---|---|
| SLOs exist and burn-rate alerts are deployed | | |
| Every alert links to a runbook | | docs/runbooks/ |
| Dashboards for the service, the database, and the model gateway | | |
| Error tracking is live | | |
| On-call rota exists | | |
| Escalation contacts are known | | |
| Load test met the budgets | | |

## 3. Data and recovery

| Check | Yes/No | Evidence |
|---|---|---|
| Point-in-time recovery is on; retention matches the constitution | | |
| A restore test has succeeded at least once | | |
| Measured restore time fits the RTO | | |
| Data stays in the regions the constitution names | | |
| Deletion jobs exist, including embeddings and model traces | | |

## 4. Security

| Check | Yes/No | Evidence |
|---|---|---|
| The chosen ASVS level was checked | | |
| Penetration test done when the constitution requires it; high findings fixed | | |
| Dynamic scan: no high findings | | |
| No unwaived critical or high vulnerabilities | | |
| Secrets are in a vault; CI uses short-lived identity | | |
| Standing production access is removed; access is time-boxed | | |
| A vulnerability contact is published | | |

## 5. Release and rollback

| Check | Yes/No | Evidence |
|---|---|---|
| Artifact signed; SBOM attached | | |
| Deploy-beside-traffic and shift-back have been rehearsed | | |
| Migration rehearsed on a masked snapshot | | |
| Risky features are behind flags that default off | | |
| Mobile store listing and staged rollout, if you ship mobile | | |

## 6. Model features

| Check | Yes/No | Evidence |
|---|---|---|
| Intake is complete for each feature | | spec |
| Evals meet thresholds; abuse tests have zero critical findings | | |
| Input and output checks are on; the kill switch has been tested | | |
| Budgets and rate limits are configured | | |
| Users can tell that a model produced the content | | |

## 7. Handover

| Check | Yes/No | Evidence |
|---|---|---|
| Handover pack delivered, if another team will operate production | | |
| The post-launch support window is scheduled | | |

## 8. Waivers and sign-off

| Waiver | Expires | Approved by |
|---|---|---|
| | | |

| Role | Name | Decision | Date |
|---|---|---|---|
| Tech lead | | | |
| Release manager | | | |
| QA | | | |
| Security reviewer | | | |
