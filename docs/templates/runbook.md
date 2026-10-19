<!--
TEMPLATE: Runbook
Copy to: docs/runbooks/<alert-or-procedure>.md
Every alert links to exactly one runbook.
Write it for someone who has never seen the service: numbered steps,
commands they can paste, and a clear branch when they must choose.
Do not put secret values in a runbook. Name the secret's vault entry.
-->

# Runbook: <Alert or procedure>

| Field | Value |
|---|---|
| Service | <service> |
| Alerts | <alert names> |
| Severity | <Sev2 if …; Sev1 if …> |
| Owner | <team or role> |
| Last rehearsed | <YYYY-MM-DD> |

## 1. What this means

<!-- The indicator, the threshold, and what the user feels. -->

## 2. Where to look

- Dashboard: <name>
- Traces: <saved query>
- Errors: <project>
- Model traces, if this feature calls a model: <project>

## 3. First 10 minutes

1. Acknowledge the alert. Open an incident channel for Sev1 or Sev2.
2. Check whether a deploy happened in the last two hours.
3. Check the database, the model gateway, and any third party you depend on.
4. Was this caused by the latest release?
   - **Yes.** Go to §4.
   - **No, or you are not sure.** Go to §5.

## 4. Mitigation

| Situation | Action | Command |
|---|---|---|
| Bad release | Shift traffic back to the previous revision | `<command>` |
| One feature | Turn its flag off | `<flag>` |
| Model feature misbehaving | Turn its kill switch off and confirm the budget | `<flag>` |
| Bad mobile update | Republish the previous package to the channel | `<command>` |
| Database overload | <scale, or stop the long query> | `<command>` |

Do not roll back a database migration without the tech lead. Prefer a roll-forward when the previous application version still works with the expanded schema.

## 5. Diagnosis

1. <step>
2. <step>

| Symptom | Likely cause | Fix |
|---|---|---|
| | | |

## 6. Verification

- [ ] The indicator is back inside its objective for 15 minutes
- [ ] No new errors of this class
- [ ] Smoke checks are green

## 7. Escalation

| After | Who | How |
|---|---|---|
| 30 minutes unresolved | Tech lead | <channel> |
| Suspected data exposure | Tech lead and the security contact | follow the incident process |

## 8. Afterwards

- Sev1 and Sev2: write a postmortem within five working days (`postmortem.md`).
- Add any step this runbook was missing.
