"""Run only inside the topic Docker image; not native physics/model validation."""
import copy
import json
import os
from pathlib import Path
import unittest

if os.environ.get("POSE_ACTIVE_CONTAINER") != "1" or not Path("/.dockerenv").exists():
    raise SystemExit("Use the local Docker launcher; do not run checks on host")

from probe import Budget, Evaluator, PLAN, valid_tokens


class ContractChecks(unittest.TestCase):
    def setUp(self):
        self.good = dict(inside=True, support=True, released=True, eef_distance=.1,
                         linear_speed=0., angular_speed=0., upright=1., angle_deg=0.)

    def evaluate(self, witness, count=4):
        e = Evaluator(PLAN["evaluator_fixture"])
        for _ in range(count):
            decision = e.update(witness, .05)
        return decision

    def test_positive_requires_dwell(self):
        self.assertEqual(self.evaluate(self.good, 3), dict(place=False, align=False))
        self.assertEqual(self.evaluate(self.good), dict(place=True, align=True))

    def test_opposite_heading_separates_instructions(self):
        self.assertEqual(self.evaluate(dict(self.good, angle_deg=180.)), dict(place=True, align=False))

    def test_support_release_and_footprint_are_required(self):
        for flag in ("inside", "support", "released"):
            with self.subTest(flag=flag):
                self.assertEqual(self.evaluate(dict(self.good, **{flag: False})), dict(place=False, align=False))

    def test_held_tilted_and_moving_objects_are_rejected(self):
        for key, value in (("eef_distance", .01), ("upright", 0.), ("linear_speed", 1.), ("angular_speed", 2.)):
            with self.subTest(key=key):
                self.assertFalse(self.evaluate(dict(self.good, **{key: value}))["place"])

    def test_interruption_resets_dwell(self):
        e = Evaluator(PLAN["evaluator_fixture"])
        for _ in range(3):
            e.update(self.good, .05)
        e.update(dict(self.good, support=False), .05)
        self.assertFalse(e.update(self.good, .05)["place"])

    def test_missing_and_nonfinite_witnesses_stop(self):
        missing = copy.deepcopy(self.good)
        missing.pop("support")
        for witness in (missing, dict(self.good, angle_deg=float("nan")), dict(self.good, linear_speed=float("inf"))):
            with self.assertRaises(ValueError):
                self.evaluate(witness)

    def test_invalid_witness_domains_stop(self):
        for witness in (dict(self.good, inside=1), dict(self.good, angle_deg=-1.), dict(self.good, upright=2.)):
            with self.assertRaises(ValueError):
                self.evaluate(witness)

    def test_nonpositive_sample_duration_stops(self):
        for seconds in (0., -1., float("nan")):
            with self.assertRaises(ValueError):
                Evaluator(PLAN["evaluator_fixture"]).update(self.good, seconds)

    def test_invalid_tokens_cannot_reach_clipping_decoder(self):
        ranges = [(10, 12), (20, 22), (30, 31)]
        self.assertTrue(valid_tokens([10, 21, 31] * 4, ranges))
        self.assertFalse(valid_tokens([10, 21, 31] * 3, ranges))
        self.assertFalse(valid_tokens([21, 10, 31] * 4, ranges))
        self.assertFalse(valid_tokens([10, 21, 32] * 4, ranges))

    def test_budget_refuses_before_consumption(self):
        b = Budget(dict(control_calls=1, physics_steps=2, model_steps=3))
        b.take("control_calls")
        with self.assertRaises(RuntimeError):
            b.take("control_calls")
        self.assertEqual(b.used["control_calls"], 1)
        with self.assertRaises(RuntimeError):
            b.take("physics_steps", -1)
        self.assertEqual(b.used["physics_steps"], 0)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    Path("/out/checks.json").write_text(json.dumps({
        "scope": "contract checks only; no native physics, model, policy or research effect",
        "tests": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "passed": result.wasSuccessful()
    }, indent=2) + "\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
