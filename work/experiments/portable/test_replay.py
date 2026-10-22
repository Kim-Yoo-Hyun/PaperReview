"""Run inside the same Docker image; no host NumPy required."""
import tempfile
import unittest
from pathlib import Path
import numpy as np
from replay_c3 import checked_hash, probabilities, scores, verify


class ReplayTests(unittest.TestCase):
    def test_hash_corruption_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "evidence"
            p.write_bytes(b"modified")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                checked_hash(p, "0" * 64)

    def test_alias_removal_preserves_command_distribution(self):
        p = np.array([.1, .3, .6])
        raw, marginal, alias = scores(p, np.array([0, 0, 1]))
        self.assertAlmostEqual(raw, .54)
        self.assertAlmostEqual(marginal, .39)
        self.assertAlmostEqual(alias, .1)

    def test_singleton_classes_have_identical_trace(self):
        p = probabilities(np.array([10000., 10001.]), 1.)
        self.assertAlmostEqual(float(p.sum()), 1.)
        raw, marginal, alias = scores(p, np.array([0, 1]))
        self.assertAlmostEqual(raw, marginal)
        self.assertEqual(alias, 0.)

    def test_reference_mismatch_fails(self):
        with self.assertRaisesRegex(ValueError, "Oracle mismatch"):
            verify({"1.0": {"aggregate_score_trace_reduction_percent": 4.}},
                   {"temperatures": {"1.0": {"aggregate_score_trace_reduction_percent": 2.}}}, {})


if __name__ == "__main__":
    unittest.main()
