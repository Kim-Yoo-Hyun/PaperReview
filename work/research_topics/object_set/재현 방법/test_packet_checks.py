"""Run in Docker; validates packaging/result handling, never a native policy."""
import json
from pathlib import Path
import tempfile
import unittest

from packet_checks import RECIPE_FILES, classify_probe, recipe_hashes, verify_recipe


class PacketChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.built = Path(self.tmp.name) / 'built'
        self.current = Path(self.tmp.name) / 'current'
        for root in (self.built, self.current):
            root.mkdir()
            for name in RECIPE_FILES:
                (root / name).write_text('fixture:' + name)
        (self.built / 'recipe_sha256.json').write_text(json.dumps(recipe_hashes(self.built)))

    def test_matching_packet(self):
        self.assertEqual(verify_recipe(self.built, self.current), recipe_hashes(self.built))

    def test_changed_local_plan_rejects_stale_image(self):
        (self.current / 'RESUME_PLAN.json').write_text('changed budget')
        with self.assertRaisesRegex(RuntimeError, 'Stale image.*RESUME_PLAN.json'):
            verify_recipe(self.built, self.current)

    def test_changed_built_adapter_rejects_receipt(self):
        (self.built / 'native_probe.py').write_text('changed adapter')
        with self.assertRaisesRegex(RuntimeError, 'build receipt'):
            verify_recipe(self.built, self.current)

    def test_incomplete_clone_rejects(self):
        (self.current / 'ARTIFACTS.json').unlink()
        with self.assertRaises(FileNotFoundError):
            verify_recipe(self.built, self.current)

    def test_native_containment_is_not_research_effect(self):
        result = classify_probe({'status': 'NATIVE_CONTAINMENT', 'native_condition_met': True}, 0)
        self.assertEqual(result['native_rollouts_completed'], 1)
        self.assertTrue(result['native_containment_observed'])
        self.assertFalse(result['research_effect_verified'])

    def test_task_nonsuccess_is_still_completed_rollout(self):
        for status in ('STEP_BUDGET_EXHAUSTED', 'TERMINAL_WITHOUT_CONDITION'):
            with self.subTest(status=status):
                result = classify_probe({'status': status, 'native_condition_met': False}, 0)
                self.assertEqual(result['native_rollouts_completed'], 1)
                self.assertFalse(result['native_containment_observed'])

    def test_ik_cannot_pass_even_if_process_exits_zero(self):
        result = classify_probe({'status': 'IK_FAILURE', 'native_condition_met': False}, 0)
        self.assertEqual(result['stage'], 'CLIENT_FAILED')
        self.assertEqual(result['native_rollouts_completed'], 0)

    def test_nonzero_exit_with_stale_success_does_not_pass(self):
        result = classify_probe({'status': 'NATIVE_CONTAINMENT', 'native_condition_met': True}, 1)
        self.assertEqual(result['native_rollouts_completed'], 0)

    def test_missing_unknown_or_contradictory_result_cannot_pass(self):
        for probe in (None, {}, {'status': 'STARTED'},
                      {'status': 'NATIVE_CONTAINMENT', 'native_condition_met': False}):
            with self.subTest(probe=probe):
                self.assertEqual(classify_probe(probe, 0)['stage'], 'CLIENT_FAILED')

    def test_packet_keeps_single_rollout_budget(self):
        plan = json.loads(Path(__file__).with_name('RESUME_PLAN.json').read_text())
        probe = plan['probe']
        self.assertEqual((probe['rollouts'], probe['max_rollouts_authorized']), (1, 1))
        self.assertEqual((probe['max_policy_steps'], probe['max_inference_calls']), (200, 40))
        self.assertFalse(probe['automatic_retry'])


if __name__ == '__main__':
    if not Path('/.dockerenv').exists():
        raise SystemExit('Run this check inside Docker only')
    unittest.main(verbosity=2)
