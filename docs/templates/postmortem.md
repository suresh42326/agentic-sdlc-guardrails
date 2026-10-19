<!--
TEMPLATE: Blameless postmortem
Copy to: docs/postmortems/<YYYY-MM-DD>-<slug>.md
Write one for every Sev1 and Sev2, within five working days of resolution.
Describe systems and decisions. Name roles in the analysis, not individuals as the cause.
Every action becomes an issue with an owner and a due date.
-->

# Postmortem: <Incident title>

| Field | Value |
|---|---|
| Incident | INC-<nnn> |
| Severity | Sev1 / Sev2 |
| Status | Draft / Reviewed / Closed |
| Date | <YYYY-MM-DD> |
| Detected to resolved | <hh:mm> |
| Incident commander | <role> |
| Author | <name> |
| Reviewed | <YYYY-MM-DD> |
| People outside the team told? | <yes, when / not required> |

## 1. Summary

<!-- What happened, who was affected, how it ended. -->

## 2. Impact

| Dimension | Impact |
|---|---|
| Users affected | <n or %> |
| Functionality | <features> |
| Data loss or exposure | <none / what> |
| Error budget consumed | <% of the 28-day budget> |

## 3. Timeline (UTC)

| Time | Event |
|---|---|
| <hh:mm> | Trigger |
| <hh:mm> | First alert |
| <hh:mm> | Acknowledged |
| <hh:mm> | Mitigation |
| <hh:mm> | Resolved |

## 4. Detection

- How it was noticed: <alert / user report>
- Time to detect: <minutes>. What would have made that shorter?

## 5. Cause and contributing factors

- Cause: <...>
- Contributing factors: <...>
- Did generated code or a model feature play a part? <no / yes: which agent mode and which review>

## 6. What went well

- <...>

## 7. What went poorly

- <...>

## 8. Actions

| # | Action | Type (prevent / detect / mitigate / process) | Owner | Issue | Due |
|---|---|---|---|---|---|
| 1 | | | | | |

## 9. Should a guardrail change?

<!-- If a rule, template, or check should change, open an RFC. -->

- <...>
