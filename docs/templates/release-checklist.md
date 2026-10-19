<!--
TEMPLATE: Release go / no-go
Attach to the release pull request or copy to docs/release/<version>.md
Automated checks produce most of the evidence. Humans confirm and sign.
Any unchecked blocking item is a no-go, unless a waiver in waiver.md covers it and has not expired.
-->

# Release <vX.Y.Z> — Go / No-go

| Field | Value |
|---|---|
| Project | <name> |
| Release tag | <vX.Y.Z> |
| Artifact digest | <image@sha256:…> |
| Previous production digest (rollback target) | <image@sha256:…> |
| Mobile | <store build / not applicable> |
| Date | <YYYY-MM-DD> |

## 1. Automated checks (blocking)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | End-to-end and API suites pass (quarantined tests listed) | ☐ | |
| 2 | Every acceptance criterion in this release has a passing test | ☐ | |
| 3 | Dynamic scan: no high findings | ☐ | |
| 4 | Load test meets the constitution budgets | ☐ | |
| 5 | Accessibility: no serious violations on key flows | ☐ | |
| 6 | Model evals meet thresholds, with zero critical abuse findings | ☐ / n/a | |
| 7 | SBOM generated; artifact signed | ☐ | |
| 8 | No unwaived critical or high vulnerabilities | ☐ | |
| 9 | Migration rehearsed on a masked snapshot; duration <mm:ss> | ☐ / n/a | |
| 10 | Rollback target recorded | ☐ | |

## 2. What is in the release

- Changelog: <link>
- Breaking API changes: <none / list>
- Flags and their rollout state: <...>
- Migrations: <expand / migrate / contract>

## 3. Operations

- [ ] The on-call person knows the window
- [ ] Dashboards and alerts cover new behaviour
- [ ] Runbooks updated for new alerts
- [ ] First production launch? The production-readiness review is done
- [ ] Any extra approval your release process requires is recorded

## 4. Deploy

1. Deploy the signed digest beside production traffic.
2. Run smoke tests against that revision.
3. Shift traffic.
4. Watch the SLO dashboards for 30 minutes.
5. Mobile, if any: staged store rollout starting at a small percent.

Rollback trigger: <for example, error rate above twice the baseline for five minutes> → shift back and turn the flag off.

## 5. Sign-off

| Role | Name | Go / No-go | Date |
|---|---|---|---|
| QA | | | |
| Release manager | | | |
