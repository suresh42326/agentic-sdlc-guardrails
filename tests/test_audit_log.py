"""Redaction tests for the audit hook.

Secret-shaped strings are built at runtime so this file does not contain a
complete credential literal.
"""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


def load_audit():
    path = Path(__file__).resolve().parents[1] / ".agents" / "hooks" / "audit_log.py"
    spec = importlib.util.spec_from_file_location("audit_log", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


audit = load_audit()


def _joined(*parts: str) -> str:
    return "".join(parts)


class RedactTests(unittest.TestCase):
    def test_sensitive_key_is_removed_even_when_the_value_looks_harmless(self):
        out = audit.redact({"api_key": "not-a-real-value", "note": "keep me"})
        self.assertEqual(out["api_key"], "[REDACTED]")
        self.assertEqual(out["note"], "keep me")

    def test_tokenizer_key_is_not_treated_as_a_token(self):
        out = audit.redact({"tokenizer": "wordpiece"})
        self.assertEqual(out["tokenizer"], "wordpiece")

    def test_connection_string_under_a_benign_key(self):
        password = _joined("s3", "cret-value")
        url = _joined("postgres://app:", password, "@db.internal:5432/tickets")
        out = audit.redact({"command": f"migrate {url}"})
        self.assertNotIn(password, out["command"])
        self.assertIn("[REDACTED]", out["command"])
        self.assertIn("migrate", out["command"])

    def test_api_key_and_bearer_shapes(self):
        openai = _joined("sk-proj-", "a" * 24)
        github = _joined("ghp_", "b" * 36)
        bearer = _joined("Bearer ", "c" * 24)
        text = f"export OPENAI={openai} GH={github} AUTH='{bearer}'"
        out = audit.redact_text(text)
        self.assertNotIn(openai, out)
        self.assertNotIn(github, out)
        self.assertNotIn("c" * 24, out)
        self.assertIn("[REDACTED]", out)

    def test_aws_slack_and_jwt_shapes(self):
        aws = _joined("AKIA", "Z" * 16)
        slack = _joined("xoxb-", "1" * 12, "-", "abcd")
        jwt = _joined("eyJ", "a" * 12, ".", "b" * 12, ".", "c" * 12)
        out = audit.redact_text(f"{aws} {slack} {jwt}")
        self.assertNotIn(aws, out)
        self.assertNotIn(slack, out)
        self.assertNotIn(jwt, out)

    def test_assignment_form_inside_a_string(self):
        secret = _joined("super", "secret", "99")
        out = audit.redact_text(f"psql 'password={secret}'")
        self.assertNotIn(secret, out)
        self.assertIn("password=[REDACTED]", out)

    def test_short_ordinary_assignment_is_kept(self):
        out = audit.redact_text("token: none")
        self.assertEqual(out, "token: none")

    def test_nested_lists_and_truncation(self):
        long = "ok " * 400
        out = audit.redact({"items": [{"note": long}]})
        self.assertTrue(out["items"][0]["note"].endswith("…[truncated]"))
        self.assertLessEqual(len(out["items"][0]["note"]), audit.MAX_FIELD + len("…[truncated]"))

    def test_main_redacts_before_writing(self):
        import io
        import os
        import tempfile
        from contextlib import redirect_stdout

        password = _joined("s3", "cret-value")
        event = {
            "session_id": "s1",
            "tool_name": "Bash",
            "tool_input": {"cmd": _joined("postgres://u:", password, "@localhost/db")},
        }
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "audit.jsonl"
            os.environ["AGENT_AUDIT_LOG"] = str(log)
            try:
                stdin = io.StringIO(json.dumps(event))
                old = __import__("sys").stdin
                __import__("sys").stdin = stdin
                try:
                    with redirect_stdout(io.StringIO()):
                        self.assertEqual(audit.main(), 0)
                finally:
                    __import__("sys").stdin = old
            finally:
                os.environ.pop("AGENT_AUDIT_LOG", None)
            line = log.read_text(encoding="utf-8")
        self.assertNotIn(password, line)
        self.assertIn("[REDACTED]", line)


if __name__ == "__main__":
    unittest.main()
