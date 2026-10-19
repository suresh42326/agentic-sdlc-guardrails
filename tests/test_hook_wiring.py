"""The audit hook is actually referenced by both harness configs."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HookWiringTests(unittest.TestCase):
    def test_claude_settings_call_the_audit_script(self):
        settings = json.loads((ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
        hooks = settings["hooks"]
        for event in ("PreToolUse", "PostToolUse"):
            commands = [
                hook["command"]
                for group in hooks[event]
                for hook in group["hooks"]
            ]
            self.assertTrue(commands, event)
            joined = "\n".join(commands)
            self.assertIn(".agents/hooks/audit_log.py", joined)
            self.assertIn("claude", joined)

    def test_copilot_hook_file_calls_the_audit_script(self):
        raw = json.loads((ROOT / ".github" / "hooks" / "audit.json").read_text(encoding="utf-8"))
        for phase in ("preToolUse", "postToolUse"):
            commands = [entry["bash"] for entry in raw["hooks"][phase]]
            self.assertTrue(any("audit_log.py" in cmd and "copilot" in cmd for cmd in commands))

    def test_skill_mirrors_match(self):
        canonical = ROOT / ".agents" / "skills"
        mirror = ROOT / ".claude" / "skills"
        canon_files = sorted(p.relative_to(canonical).as_posix() for p in canonical.rglob("*") if p.is_file())
        mirror_files = sorted(p.relative_to(mirror).as_posix() for p in mirror.rglob("*") if p.is_file())
        self.assertEqual(canon_files, mirror_files)
        for rel in canon_files:
            self.assertEqual(
                (canonical / rel).read_bytes(),
                (mirror / rel).read_bytes(),
                rel,
            )


if __name__ == "__main__":
    unittest.main()
