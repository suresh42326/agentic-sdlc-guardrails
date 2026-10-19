<!--
TEMPLATE: Time-boxed waiver
Copy to: docs/waivers/WVR-<nnn>-<slug>.md
A waiver is a dated exception to a required check, threshold, or rule.
Permanent exceptions are not waivers; they are a change to the rule (see rfc.md).
Record the same expiry in whatever machine-readable config your checks read.
Loosening a model-eval threshold is not a waiver. It needs an ADR.

Suggested approvers:
- A gate or threshold: tech lead and repository owner.
- A high or critical vulnerability past its fix-by date: tech lead and repository owner, 30 days, renewable once.
-->

# WVR-<nnn>: <Short title>

| Field | Value |
|---|---|
| Project | <name> |
| Waived item | <check, threshold, or rule> |
| Type | Gate / Threshold / Vulnerability / Other |
| Requested by | <name> |
| Date | <YYYY-MM-DD> |
| Expires | <YYYY-MM-DD> |
| Status | Requested / Approved / Rejected / Expired / Closed early |

## 1. What is waived

<!-- The exact check, and the scope: whole repo, one path, one advisory, one release. -->

## 2. Why it cannot be met now

<!-- Evidence. "Not enough time" on its own is not a reason. -->

## 3. Risk while the waiver is open

| Risk | Likelihood | Impact | Compensating control |
|---|---|---|---|
| | | | |

## 4. How it will be closed

| Step | Owner | Due | Issue |
|---|---|---|---|
| | | | |

## 5. Machine-readable entry

```yaml
waivers:
  - gate: <gate-id>
    reason: "<one line>"
    expires: "<YYYY-MM-DD>"
    ref: "docs/waivers/WVR-<nnn>-<slug>.md"
```

## 6. Approval

| Role | Name | Date |
|---|---|---|
| Tech lead | | |
| Repository owner | | |
