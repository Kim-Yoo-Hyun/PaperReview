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
import registry_profiles as profiles
from reconcile_registry import build_facets
from render_source_audit import OPEN, PASS, bibliography_digest, check_applied, cited_statement, current_checks, summary_headings
from registry_schema import enrich_record, validate_record_shape


class DocumentMaintenanceTest(unittest.TestCase):
    def test_taxonomy_locations_distinguish_web_sections_from_pdf_pages(self):
        self.assertTrue(audit.valid_source_locations([1, 3], None))
        self.assertTrue(audit.valid_source_locations(None, ["Model and Data Improvements"]))
        for pages, sections in [([], None), ([0], None), ([True], None), (None, [" "]),
                                ([1], ["Experiments"]), (None, "Experiments"), (None, None)]:
            with self.subTest(pages=pages, sections=sections):
                self.assertFalse(audit.valid_source_locations(pages, sections))

    def test_publication_header_requires_one_complete_canonical_value(self):
        matches = audit.overview_publication_matches
        self.assertTrue(matches("- Year/Venue: 2025 / T-RO (journal article)", 2025, "T-RO"))
        self.assertFalse(matches("- Year/Venue\n\n## Claims\n- Year/Venue: 2025 / T-RO", 2025, "T-RO"))
        self.assertFalse(matches("- Year/Venue: 2024 / T-RO", 2025, "T-RO"))
        self.assertFalse(matches("- Year/Venue\n- Year/Venue: 2025 / T-RO", 2025, "T-RO"))

    def test_web_report_uses_its_section_and_preserves_the_overview_layout(self):
        overview = "## Problem and Importance\n\n## Core Idea and Contribution\n\n## Why This Paper Is Here — Researcher Interpretation\n"
        self.assertEqual(summary_headings(overview), ("Problem and Importance", "Core Idea and Contribution"))
        with self.assertRaises(ValueError):
            summary_headings(overview + "## Why This Paper Is Here\n## Main Claims and Actual Contribution\n")
        source = "https://example.org/report"
        self.assertEqual(cited_statement({"text": "Claim.", "section": "Model and Data"},
                                         {"source": source, "source_format": "html"}),
                         "Claim. [Model and Data](https://example.org/report#:~:text=Model%20and%20Data)")
        self.assertEqual(cited_statement({"text": "Claim.", "pages": [2]}, {"source": source}),
                         "Claim. [PDF 2쪽](https://example.org/report#page=2)")

    def test_manual_interface_heading_preserves_a_unique_contribution_section(self):
        overview = "## Why This Paper Is Here\n\n## Contribution and Interface\n\n## Scope and Source Correction\n"
        self.assertEqual(summary_headings(overview), ("Why This Paper Is Here", "Contribution and Interface"))
        with self.assertRaises(ValueError):
            summary_headings(overview + "## Main Claims and Actual Contribution\n")

    def test_reinforcement_is_not_a_contact_or_force_sensor_cue(self):
        paper = {"title": "Reinforcement learning", "tags": []}
        facets = build_facets(paper)
        self.assertIn("reinforcement_learning", facets["learning"])
        self.assertNotIn("contact_rich", facets["interaction"])
        self.assertNotIn("force_torque", facets["modality"])
        paper["tags"] = ["force-feedback"]
        facets = build_facets(paper)
        self.assertIn("force_torque", facets["modality"])
        self.assertIn("contact_rich", facets["interaction"])

    def test_final_byline_correction_preserves_the_earlier_bibliographic_digest(self):
        old, new = ["Ada Doe"], ["Ada M. Doe"]
        source = "https://example.org/final.pdf#page=1"
        day = "2026-11-23"
        fields = {"authors": "https://example.org/abstract"}
        row = {"id": "pr-0001", "checks": {"authors": {"kind": "보완", "corrected": old}},
               "postcheck": {"bibliography": fields, "bibliography_sha256": bibliography_digest({"authors": old}, fields)},
               "byline_correction": {"before": old, "corrected": new, "source": source, "verified_on": day}}
        paper = {"paper_id": row["id"], "folder": ".", "authors": new,
                 "provenance": {"authors_verification": {"source": source, "verified_on": day}},
                 "reproducibility": {key: {"status": "unknown"} for key in ("code", "data", "checkpoint")}}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            overview = root / "01_overview.md"
            overview.write_text("- Authors: Ada M. Doe\n")
            check_applied([row], [paper], root)
            overview.write_text("- Authors: Ada Doe\n")
            with self.assertRaisesRegex(ValueError, "corrected byline missing"):
                check_applied([row], [paper], root)
            paper["authors"] = old
            with self.assertRaisesRegex(ValueError, "final byline differs"):
                check_applied([row], [paper], root)

    def test_source_recheck_updates_each_endpoint_and_release_independently(self):
        row = {"checks": {"link": {"status": OPEN, "endpoints": {
            "primary": {"state": "opened"}, "pdf": {"state": "access-unconfirmed"}}},
            "code": {"status": OPEN}, "weights": {"status": OPEN}, "authors": {"status": PASS}},
            "followup": {"pdf": {"status": PASS}, "project": {"status": OPEN}},
            "postcheck": {"bibliography": {"primary": "https://example.org/paper"},
                          "resources": {"code": {"status": PASS}},
                          "qualification": {"field": "authors", "status": OPEN}}}
        self.assertEqual(current_checks(row), {"link": OPEN, "code": PASS, "weights": OPEN, "authors": OPEN})
        row["taxonomy_review"] = {"project": {"url": "https://example.org/current-project"}}
        self.assertEqual(current_checks(row)["link"], PASS)
        self.assertEqual(current_checks(row, include_reviews=False)["link"], OPEN)
        row["followup"]["pdf"]["status"] = OPEN
        self.assertEqual(current_checks(row)["link"], OPEN)
        row["taxonomy_review"]["pdf"] = {"url": "https://example.org/paper.pdf"}
        self.assertEqual(current_checks(row)["link"], PASS)
        del row["taxonomy_review"]
        row["followup"]["pdf"]["status"] = PASS
        row["postcheck"]["resources"]["project"] = {"status": PASS}
        self.assertEqual(current_checks(row)["link"], PASS)

    def test_audited_code_address_and_release_status_are_independent(self):
        repo = "https://example.org/code"
        implementation = repo + "/policy.py"
        rows = [{"id": "pr-0001", "checks": {"link": {"kind": "오류", "corrected": {"code": repo}}},
                 "followup": {"code": {"corrected": "released", "source": implementation}}}]
        paper = {"paper_id": "pr-0001", "sources": {"code": {"url": repo}},
                 "artifacts": {"code_status": "released"},
                 "reproducibility": {"code": {"status": "released", "source": implementation}}}
        self.assertEqual(check_applied(rows, [paper], Path(".")), (1, 1))
        paper["sources"]["code"]["url"] = "https://example.org/old-repository"
        with self.assertRaisesRegex(ValueError, r"pr-0001 sources\.code"):
            check_applied(rows, [paper], Path("."))

    def test_later_review_keeps_original_sample_and_unchecked_fields_intact(self):
        row = {"checks": {"link": {"status": PASS, "endpoints": {"primary": {"state": "opened"}}},
                          "summary": {"status": OPEN}, "weights": {"status": OPEN}, "data": {"status": OPEN}},
               "summary_review": {"status": PASS},
               "artifact_review": {"fields": {"weights": {"status": PASS}, "data": {"status": OPEN}}}}
        self.assertEqual(current_checks(row, include_reviews=False),
                         {"link": PASS, "summary": OPEN, "weights": OPEN, "data": OPEN})
        self.assertEqual(current_checks(row), {"link": PASS, "summary": PASS, "weights": PASS, "data": OPEN})
        row["artifact_recheck"] = {"fields": {"data": {"status": PASS, "finding": "not_applicable"}}}
        self.assertEqual(current_checks(row), {"link": PASS, "summary": PASS, "weights": PASS, "data": PASS})
        self.assertEqual(current_checks(row, include_reviews=False)["data"], OPEN)
        row["taxonomy_review"] = {"fields": {"data": {"status": OPEN}}}
        self.assertEqual(current_checks(row), {"link": PASS, "summary": PASS, "weights": PASS, "data": OPEN})
        self.assertEqual(current_checks(row, include_reviews=False)["weights"], OPEN)

    def test_legacy_code_scope_normalizes_and_unrecognized_scopes_fail(self):
        code = {"kind": "official_code", "url": "https://example.org/repository",
                "scope": "code_repository", "verified_on": "2026-11-18"}
        record = enrich_record({"title": "Paper", "year": 2025, "venue": "RSS",
                                "category": "Robotics", "tags": [], "folder": "2025/RSS/Paper",
                                "page": "https://example.org/paper", "sources": {"code": code}},
                               paper_id="pr-0001")
        self.assertEqual(record["sources"]["code"], {**code, "scope": "project_landing"})
        self.assertEqual(validate_record_shape(record), [])
        record["sources"]["code"]["scope"] = "undefined_scope"
        self.assertIn("invalid sources.code.scope", validate_record_shape(record))

    def test_evaluation_refresh_keeps_page_citations_and_mixed_settings(self):
        paper = {"paper_id": "paper", "folder": "paper", "title": "Paper"}
        page = "[PDF 5쪽](https://example.org/paper.pdf#page=5)"
        note = (
            "- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.\n"
            f"## Metrics and Success Definition\n\n과제별 성공률. {page}\n"
            "## Baselines and Fairness\n\n[PDF 7쪽](https://example.org/paper.pdf#page=5)\n"
            "## Statistics, Efficiency, and Reproducibility\n\n"
            f"시뮬레이션 과제별 시드 16개. {page}\n"
            f"실물 과제별 시행 25회. {page}\n"
            "추가 실험 계획에는 시행 99회가 필요하다.\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "paper").mkdir()
            (root / "paper/04_evaluation.md").write_text(note, encoding="utf-8")
            profiles.enrich_profiles([paper], root)
        result = paper["evaluation_profile"]
        self.assertEqual(set(result["settings"]), {"simulation", "real_robot"})
        self.assertEqual(result["protocol"]["metrics"], "reported")
        self.assertEqual(result["protocol"]["baselines"], "not_recorded")
        self.assertEqual([(r["count"], r["unit"]) for r in result["trial_evidence"]],
                         [(16, "seed"), (25, "trial")])

    def test_admitting_a_citing_paper_updates_only_relevant_lineage(self):
        baseline = {"paper_id": "baseline", "folder": "baseline", "title": "Baseline"}
        unrelated = {"paper_id": "other", "folder": "other", "title": "Other"}
        new = {"paper_id": "new", "folder": "new", "title": "New",
               "relations": [{"paper_id": "baseline"}]}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles.enrich_profiles([baseline, unrelated], root, reviewed_on="2026-11-19")
            profiles.enrich_profiles([new], root, registry=[baseline, unrelated, new],
                                    reviewed_on="2026-11-20")
        self.assertEqual(new["lineage_profile"]["outgoing_paper_ids"], ["baseline"])
        self.assertEqual(baseline["lineage_profile"]["incoming_paper_ids"], ["new"])
        self.assertEqual(baseline["evaluation_profile"]["reviewed_on"], "2026-11-19")
        self.assertEqual(baseline["reproducibility"]["reviewed_on"], "2026-11-19")
        self.assertEqual(unrelated["lineage_profile"]["audited_on"], "2026-11-19")

    def test_reviewed_release_sources_survive_profile_refresh_until_status_changes(self):
        code = {"status": "released", "source": "https://example.org/tree/release",
                "evidence": "author release tree checked"}
        data = {"status": "released", "source": "https://example.org/data",
                "evidence": "download manifest", "verified_on": "2026-11-19"}
        checkpoint = {"status": "released", "source": "https://example.org/weights",
                      "evidence": "author checkpoint"}
        paper = {"paper_id": "paper", "folder": "paper", "title": "Paper",
                 "artifacts": {"code_status": "released", "data_status": "released"},
                 "sources": {"project": {"url": "https://example.org"}},
                 "reproducibility": {"code": code, "data": data, "checkpoint": checkpoint}}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles.enrich_profiles([paper], root)
            self.assertEqual(paper["reproducibility"]["code"], code)
            self.assertEqual(paper["reproducibility"]["data"], data)
            self.assertEqual(paper["reproducibility"]["checkpoint"], checkpoint)
            paper["artifacts"]["data_status"] = "not_released"
            profiles.enrich_profiles([paper], root)
        self.assertEqual(paper["reproducibility"]["data"]["status"], "not_released")
        self.assertIsNone(paper["reproducibility"]["data"]["source"])

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

    def test_private_font_glyphs_are_flagged_without_guessing_their_meaning(self):
        issue = "private_use_glyph_source_review_required"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            note = root / "03_method.md"
            # The second line also matches a removable footer. The symbol needs a source.
            body = "classi\ue000cation\nCopyright 2020 symbol \U000f0011\nCopyright 2020 encoder \ufffd\n"
            note.write_text(body)
            with patch.object(artifacts, "ROOT", root):
                found = artifacts.scan([note])
                cleaned = artifacts.apply_cleanup([note])
            self.assertEqual(found["findings"][0]["line_numbers"][issue], [1, 2])
            self.assertEqual(found["findings"][0]["line_numbers"]["replacement_character_source_review_required"], [3])
            self.assertEqual(cleaned["modified_file_count"], 0)
            self.assertEqual(note.read_text(), body)
            self.assertNotIn(issue, artifacts.issue_kinds("classification, floor, ∇ and π"))

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
