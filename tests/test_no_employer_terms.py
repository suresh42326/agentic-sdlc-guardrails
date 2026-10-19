"""Fail if internal-standard markers or email addresses reappear.

The check looks for shapes (numbered internal filenames, a standards-owner
role, email addresses) so this file does not have to store a company name.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {".git", "__pycache__", "node_modules"}

NUMBERED_DOC = re.compile(r"\b\d{2}-[A-Z0-9]+(?:-[A-Z0-9]+)+\.md\b")
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
MARKERS = (
    "standard_version",
    "platform/standards owner",
)


def _files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if rel.startswith(".agents/audit/"):
            continue
        if rel == "tests/test_no_employer_terms.py":
            continue
        yield path


class IdentifierTests(unittest.TestCase):
    def test_tree_has_no_internal_markers_or_emails(self):
        hits = []
        for path in _files():
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            rel = path.relative_to(ROOT).as_posix()
            lowered = text.lower()
            for marker in MARKERS:
                if marker in lowered:
                    hits.append(f"{rel}: marker {marker}")
            if NUMBERED_DOC.search(text):
                hits.append(f"{rel}: numbered internal document id")
            if EMAIL.search(text):
                hits.append(f"{rel}: email address")
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
