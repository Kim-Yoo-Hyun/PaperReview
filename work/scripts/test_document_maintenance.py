#!/usr/bin/env python3
"""Regression checks for Markdown coverage and canonical registry views."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import audit_repository as audit
import build_registry_views as views


class DocumentMaintenanceTest(unittest.TestCase):
    def test_notes_instructions_and_history_are_checked_but_code_is_not(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "AGENTS.md").write_text("# Guide\n[removed](missing.md)\n")
            note = root / "2026" / "RSS" / "paper" / "01_overview.md"
            note.parent.mkdir(parents=True)
            note.write_text("# Paper\n[broken](absent.md)\n")
            history = root / "work" / "update" / "old.md"
            history.parent.mkdir(parents=True)
            history.write_text(
                "# History\n`Pick[a](x)`\n```python\n[example](not-a-file)\n```\n"
                "[encoded](../../plus%2B.md)\n"
            )
            (root / "plus+.md").write_text("# Encoded target\n")
            errors = []
            with patch.object(audit, "ROOT", root):
                result = audit.audit_markdown_documents(errors)
            self.assertEqual(result, {"files": 4, "links": 3})
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("AGENTS.md" in value for value in errors))
            self.assertTrue(any("01_overview.md" in value for value in errors))

    def test_malformed_table_and_unclosed_fence_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "note.md").write_text(
                "# Note\n| A | B |\n|---|---|\n| escaped \\| pipe | valid |\n"
                "| truncated |\n\n```text\nunfinished example\n"
            )
            errors = []
            with patch.object(audit, "ROOT", root):
                audit.audit_markdown_documents(errors)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("table column mismatch" in value for value in errors))
            self.assertTrue(any("code fence unclosed" in value for value in errors))

    def test_new_records_use_nested_source_and_actual_identifiers(self):
        paper = {
            "paper_id": "new", "title": "New paper", "year": 2026,
            "folder": "2026/RSS/New", "identifiers": {"arxiv": "2601.00001"},
            "sources": {"primary": {"url": "https://example.org/paper", "scope": "paper_specific"}},
            "provenance": {"content_evidence": "ABSTRACT_CHECKED"},
        }
        with patch.object(views, "read_tiers", return_value={}), patch.object(views, "read_status", return_value={}):
            _, rows = views.build_index([paper], {"entries": []})
        self.assertEqual(rows[0]["identifier_status"], "identified")
        self.assertEqual(rows[0]["primary_source_scope"], "paper_specific")
        self.assertEqual(rows[0]["evidence_level"], "ABSTRACT_CHECKED")
        self.assertEqual(rows[0]["reading_status"], "N/A")

    def test_stale_derived_identifier_flag_does_not_override_manifest(self):
        paper = {
            "paper_id": "old", "title": "Old paper", "year": 2025,
            "folder": "2025/ICML/Old", "identifiers": {},
            "provenance": {"identifier_status": "identified", "primary_source_scope": "venue_index"},
        }
        with patch.object(views, "read_tiers", return_value={}), patch.object(views, "read_status", return_value={}):
            _, rows = views.build_index([paper], {"entries": []})
        self.assertEqual(rows[0]["identifier_status"], "source_only")
        self.assertEqual(rows[0]["primary_source_scope"], "venue_index")


if __name__ == "__main__":
    unittest.main()
