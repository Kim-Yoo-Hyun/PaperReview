#!/usr/bin/env python3
"""Regression checks for Markdown coverage and canonical registry views."""

import tempfile
import argparse
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import audit_repository as audit
import build_registry_views as views
import audit_note_artifacts as artifacts
import build_lit_survey as survey


class DocumentMaintenanceTest(unittest.TestCase):
    def test_registry_cli_uses_manifest_not_incomplete_discovery(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "papers.json"
            papers = [{"paper_id": "pr-0001", "title": "Existing", "folder": "2025/RSS/existing"},
                      {"paper_id": "pr-0002", "title": "Later admission", "folder": "2026/RSS/later"}]
            manifest.write_text(json.dumps(papers))
            args = argparse.Namespace(refresh_metadata=False, download_pdfs=False,
                                      create_missing_notes=False, overwrite_notes=False,
                                      write_registry=True, write_manifest=False)
            with patch.object(survey, "MANIFEST", manifest), patch.object(survey, "parse_args", return_value=args), \
                    patch.object(survey, "build_papers") as legacy, patch.object(survey, "write_registry") as write, \
                    patch.object(survey, "write_manifest") as write_manifest, patch.object(survey, "write_notes") as notes:
                survey.main()
            legacy.assert_not_called()
            write.assert_called_once_with(papers)
            write_manifest.assert_not_called()
            notes.assert_not_called()

    def test_incomplete_registry_rebuild_is_rejected_before_write(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "papers.json"
            manifest.write_text(json.dumps([{"paper_id": "pr-0001"}, {"paper_id": "pr-0002"}]))
            destination = Path(directory) / "PAPER.md"
            destination.write_text("preserve me\n")
            with patch.object(survey, "MANIFEST", manifest), patch.object(survey, "ROOT", Path(directory)):
                with self.assertRaisesRegex(ValueError, "omit 1 canonical"):
                    survey.write_registry([{"paper_id": "pr-0001"}])
            self.assertEqual(destination.read_text(), "preserve me\n")

    def test_exact_case_path_check_is_portable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "2022" / "arXiv" / "paper").mkdir(parents=True)
            with patch.object(audit, "ROOT", root):
                self.assertTrue(audit.path_has_exact_case("2022/arXiv/paper"))
                self.assertFalse(audit.path_has_exact_case("2022/arxiv/paper"))
                self.assertFalse(audit.path_has_exact_case("2022/arXiv/Paper"))
                self.assertFalse(audit.path_has_exact_case("../outside"))

    def test_pdf_control_glyphs_are_reported_and_never_auto_cleaned(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            note = root / "03_method.md"
            # NUL, a splitlines separator and C1 NEL can all be PDF glyphs.
            original = "# Method\nformula \x00 \x1c \x85\nCopyright 2020\n"
            note.write_text(original)
            with patch.object(artifacts, "ROOT", root):
                result = artifacts.scan([note])
                cleaned = artifacts.apply_cleanup([note])
            issue = "control_character_source_review_required"
            self.assertEqual(result["findings"][0]["line_numbers"][issue], [2])
            self.assertEqual(cleaned["modified_file_count"], 0)
            self.assertEqual(note.read_text(), original)
            self.assertNotIn(issue, artifacts.issue_kinds("valid\ttext\r\n"))

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
