#!/usr/bin/env python3
"""Append-only audit log for coding-agent tool calls.

Wire it as a Claude Code PreToolUse and PostToolUse hook in
`.claude/settings.json`, and as a Copilot preToolUse/postToolUse hook in
`.github/hooks/audit.json`.

    audit_log.py <pre|post> [harness]

Both harnesses write one JSON object to stdin. Field names differ
(snake_case vs camelCase); this script accepts either. It never blocks a
tool call. Permission lists do that.

The log path is `$AGENT_AUDIT_LOG`, or `.agents/audit/audit.jsonl`. That
directory is gitignored. Do not commit it.

Redaction is applied to every string, not only to sensitive key names:
known token shapes, credential-bearing URLs, and assignment forms such as
`password=...`. Matching key names are removed entirely.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MAX_FIELD = 500

# Match sensitive key names without swallowing unrelated words
# ("tokenizer", "secretary").
SENSITIVE_KEY = re.compile(
    r"(?i)(?:^|[^a-z])(?:"
    r"secret|password|passwd|api[_-]?key|authorization|cookie|"
    r"credential|connection[_-]?string|token"
    r")(?:$|[^a-z])"
)

# Value shapes. Order matters only where a broader pattern would otherwise
# leave a fragment a narrower one still needs to see; replacements do not
# overlap in a way that un-redacts.
_PRIVATE_KEY = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
    re.DOTALL,
)
_JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")
_GITHUB = re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")
_GITHUB_PAT = re.compile(r"\bgithub_pat_[A-Za-z0-9_]{16,}\b")
_AWS_ACCESS = re.compile(r"\b(?:AKIA|ASIA|AROA)[0-9A-Z]{16}\b")
_SLACK = re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")
_GITLAB = re.compile(r"\bglpat-[A-Za-z0-9\-_]{16,}\b")
_NPM = re.compile(r"\bnpm_[A-Za-z0-9]{20,}\b")
_SK = re.compile(r"\bsk-(?:proj-|ant-|live-|test-)?[A-Za-z0-9_\-]{16,}\b")
_STRIPE = re.compile(r"\b(?:sk|rk|pk)_(?:live|test)_[A-Za-z0-9]{10,}\b")
_GOOGLE = re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b")
_BEARER = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9\-._~+/]{8,}={0,2}")
_URL_USERINFO = re.compile(
    r"(?i)\b[a-z][a-z0-9+.-]*://[^\s/:\"']+:[^\s@\"']+@[^\s\"']+"
)
_AZURE_KEY = re.compile(
    r"(?i)\b(?:AccountKey|SharedAccessKey|SharedAccessSignature)=[^;\s\"']+"
)
_ASSIGNMENT = re.compile(
    r"(?i)\b(password|passwd|pwd|secret|api[_-]?key|access[_-]?token|"
    r"token|authorization|connection[_-]?string)\b\s*[:=]\s*([^\s,;\"']+)"
)

VALUE_PATTERNS = (
    _PRIVATE_KEY,
    _JWT,
    _GITHUB,
    _GITHUB_PAT,
    _AWS_ACCESS,
    _SLACK,
    _GITLAB,
    _NPM,
    _SK,
    _STRIPE,
    _GOOGLE,
    _BEARER,
    _URL_USERINFO,
    _AZURE_KEY,
)


def _redact_assignment(match: re.Match) -> str:
    value = match.group(2)
    # Leave short ordinary words alone ("token: none").
    if len(value) < 8 and value.isalnum() and not any(c.isdigit() for c in value):
        return match.group(0)
    return f"{match.group(1)}=[REDACTED]"


def redact_text(text: str) -> str:
    text = _ASSIGNMENT.sub(_redact_assignment, text)
    for pattern in VALUE_PATTERNS:
        text = pattern.sub("[REDACTED]", text)
    if len(text) > MAX_FIELD:
        return text[:MAX_FIELD] + "…[truncated]"
    return text


def redact(value, key: str | None = None):
    if key is not None and SENSITIVE_KEY.search(key):
        return "[REDACTED]"
    if isinstance(value, dict):
        return {k: redact(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, str):
        return redact_text(value)
    return value


def git_branch() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        ).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception:
        event = {}
    if not isinstance(event, dict):
        event = {}

    def pick(*keys):
        for k in keys:
            if event.get(k) is not None:
                return event[k]
        return None

    phase = sys.argv[1] if len(sys.argv) > 1 else None
    harness = sys.argv[2] if len(sys.argv) > 2 else "claude"
    is_post = phase == "post" or pick("hook_event_name", "hookEventName") == "PostToolUse"

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "harness": harness,
        "session": pick("session_id", "sessionId"),
        "event": "post" if is_post else "pre",
        "tool": pick("tool_name", "toolName"),
        "input": redact(pick("tool_input", "toolArgs", "toolInput")),
        "outcome": redact(pick("tool_response", "toolResult")) if is_post else None,
        "branch": git_branch(),
        "operator": os.environ.get("AGENT_OPERATOR")
        or os.environ.get("USER")
        or os.environ.get("USERNAME"),
        "mode": os.environ.get("AGENT_MODE", "M1"),
        "cwd": pick("cwd"),
    }

    path = Path(os.environ.get("AGENT_AUDIT_LOG", ".agents/audit/audit.jsonl"))
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception as exc:  # logging must not break the agent
        print(f"audit_log: could not write audit record: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
