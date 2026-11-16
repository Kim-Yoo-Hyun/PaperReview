#!/usr/bin/env python3
"""Regression checks for reading-input preservation across tier changes."""

import csv
import tempfile
import unittest
from collections import OrderedDict
from pathlib import Path
from unittest.mock import patch

import build_reading_tiers as builder


AUTOMATIC = {
    "tier", "track", "primary_track", "paper_id", "sequence", "year",
    "venue", "title", "overview_path",
}


class ReadingHistoryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.active = self.root / "status.csv"
        self.history = self.root / "history.csv"
        self.rows = []
        for title in ("A", "B"):
            folder = self.root / title
            folder.mkdir()
            (folder / "01_overview.md").write_text("Evidence maturity: `FULL_TEXT_CHECKED`\n")
            self.rows.append({"title": title, "path": f"./{title}/01_overview.md", "year": "2025", "venue": "RSS"})
        self.paths = [row["path"] for row in self.rows]
        self.ids = dict(zip(self.paths, ("paper-a", "paper-b")))

    def read(self, path):
        with path.open(newline="") as handle:
            return list(csv.DictReader(handle))

    def write(self, path, rows):
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def generate(self, first_tier="CORE"):
        tiers = {self.paths[0]: first_tier, self.paths[1]: "CORE"}
        core = ["=B"] if first_tier != "CORE" else ["=A", "=B"]
        next_queries = ["=A"] if first_tier == "NEXT" else []
        with patch.multiple(
            builder, ROOT=self.root, STATUS=self.active, STATUS_HISTORY=self.history,
            CORE_GROUPS=OrderedDict([("core", core)]),
            NEXT_GROUPS=OrderedDict([("next", next_queries)]),
        ):
            builder.write_status(
                self.rows, tiers, {path: "next" if tiers[path] == "NEXT" else "core" for path in self.paths},
                dict.fromkeys(self.paths, "Planning and control"), self.ids,
            )

    def test_demotion_and_repromotion_preserve_every_user_field(self):
        self.generate()
        rows = self.read(self.active)
        first = rows[0]
        for key in first:
            if key not in AUTOMATIC:
                first[key] = f"사용자 입력 {key}\ncomma, quote: \"preserve\""
        first.update(status="READ", evidence_level="FULL_TEXT_CHECKED", started_on="2026-09-01", completed_on="")
        expected = {key: value for key, value in first.items() if key not in AUTOMATIC}
        self.write(self.active, rows)
        self.generate("REFERENCE")
        inactive = self.read(self.history)
        self.assertEqual(len(inactive), 1)
        self.assertEqual(inactive[0]["sequence"], "")
        self.assertEqual({key: inactive[0][key] for key in expected}, expected)
        self.assertEqual([row["paper_id"] for row in self.read(self.active)], ["paper-b"])
        self.generate("NEXT")
        restored = next(row for row in self.read(self.active) if row["paper_id"] == "paper-a")
        self.assertEqual({key: restored[key] for key in expected}, expected)
        self.assertEqual(restored["sequence"], "1")
        self.assertEqual(self.read(self.history), [])

    def test_repeated_generation_is_idempotent(self):
        self.generate()
        self.generate("REFERENCE")
        before = (self.active.read_bytes(), self.history.read_bytes())
        self.generate("REFERENCE")
        self.assertEqual(before, (self.active.read_bytes(), self.history.read_bytes()))

    def test_case_only_path_repair_preserves_active_and_history(self):
        for tier, source_name in (("CORE", "active"), ("REFERENCE", "history")):
            with self.subTest(tier=tier):
                self.generate(tier)
                source = getattr(self, source_name)
                rows = self.read(source)
                row = next(row for row in rows if row["paper_id"] == "paper-a")
                row.update(overview_path="./a/01_overview.md", status="READ", personal_notes="기존 분석, 유지")
                expected = {key: value for key, value in row.items() if key not in AUTOMATIC}
                self.write(source, rows)
                self.generate(tier)
                restored = next(row for row in self.read(source) if row["paper_id"] == "paper-a")
                self.assertEqual(restored["overview_path"], self.paths[0])
                self.assertEqual({key: restored[key] for key in expected}, expected)

    def test_case_only_path_with_wrong_identity_is_not_migrated(self):
        self.generate()
        rows = self.read(self.active)
        rows[0].update(overview_path="./a/01_overview.md", paper_id="other-paper")
        self.write(self.active, rows)
        before = self.active.read_bytes()
        with self.assertRaisesRegex(RuntimeError, "missing from registry"):
            self.generate()
        self.assertEqual(before, self.active.read_bytes())

    def test_reference_tier_survives_path_repair_by_identity(self):
        index = self.root / "tiers.csv"
        self.write(index, [{"overview_path": "./a/01_overview.md", "paper_id": "paper-a", "tier": "REFERENCE"}])
        rows = [dict(row, tags="") for row in self.rows]
        with patch.multiple(
            builder, INDEX=index, CORE_GROUPS=OrderedDict(), NEXT_GROUPS=OrderedDict(),
            FOCUS_PRIORITY_RATIONALES={}, FOCUS_REFERENCE_RATIONALES={}, FOCUS_SOURCE_CHECKS={},
            ARCHIVE_3D_RECONSTRUCTION_IDS=frozenset(), REFERENCE_RECLASSIFIED_IDS=frozenset(),
            REFERENCE_3D_STATE_FOUNDATION_IDS=frozenset(),
        ), patch.object(builder, "manifest_paper_ids", return_value=self.ids), patch.object(builder, "manifest_primary_tracks", return_value={}):
            tiers, _, _ = builder.classify(rows)
        self.assertEqual(tiers[self.paths[0]], "REFERENCE")

    def test_unknown_history_path_fails_without_overwriting_tracker(self):
        self.generate()
        unknown = self.read(self.active)[0]
        unknown["overview_path"] = "./missing/01_overview.md"
        self.write(self.history, [unknown])
        before = self.active.read_bytes()
        with self.assertRaisesRegex(RuntimeError, "missing from registry"):
            self.generate()
        self.assertEqual(before, self.active.read_bytes())


if __name__ == "__main__":
    unittest.main()
