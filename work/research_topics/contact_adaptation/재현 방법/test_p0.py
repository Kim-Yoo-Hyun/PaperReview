"""Run in Docker only. These tests are not a physics or policy reproduction."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import probe
import run


class GuardTests(unittest.TestCase):
    def caps(self, **kw):
        return dict(resets=2, control_frames=120, physics_steps=6000, process_seconds=1800, **kw)

    def test_reject_remote_endpoints(self):
        for url in ['ssh://gpu', 'tcp://127.0.0.1:2375', '', 'unix://']:
            self.assertFalse(run.local_endpoint(url))
        self.assertTrue(run.local_endpoint('unix:///var/run/docker.sock'))

    def test_no_mac_or_emulated_native_execution(self):
        native = dict(OSType='linux', Architecture='x86_64')
        self.assertTrue(run.compatible(native, 'Linux', 'x86_64'))
        self.assertFalse(run.compatible(native, 'Darwin', 'arm64'))
        self.assertFalse(run.compatible(dict(OSType='linux', Architecture='aarch64'), 'Linux', 'x86_64'))

    def test_reset_budget_includes_constructor(self):
        b = probe.Budget(self.caps())
        b.reset(); b.reset()
        with self.assertRaises(RuntimeError): b.reset()
        self.assertEqual(b.resets, 2)

    def test_larger_or_invalid_budget_is_rejected(self):
        for key, value in [('control_frames', 121), ('physics_steps', 6001),
                           ('resets', 0), ('process_seconds', float('inf'))]:
            caps = self.caps(); caps[key] = value
            with self.assertRaises(ValueError): probe.Budget(caps)

    def test_existing_results_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileExistsError): run.Launcher(Path(d))

    def test_preroll_consumes_control_budget(self):
        b = probe.Budget(self.caps())
        for _ in range(120 * 24): b.step(1 / 1440)
        with self.assertRaises(RuntimeError): b.step(1 / 1440)
        self.assertEqual(b.physics, 2880)

    def test_physics_budget_independent_of_frames(self):
        caps = self.caps(); caps['physics_steps'] = 2
        b = probe.Budget(caps)
        b.step(1 / 1440); b.step(1 / 1440)
        with self.assertRaises(RuntimeError): b.step(1 / 1440)

    def test_deadline_and_invalid_dt(self):
        clock = [0.0]
        b = probe.Budget(self.caps(), now=lambda: clock[0])
        for dt in [0, -1, float('nan'), float('inf')]:
            with self.assertRaises(RuntimeError): b.step(dt)
        clock[0] = 1800
        with self.assertRaises(RuntimeError): b.step(1 / 1440)

    def test_observation_rejects_privileged_tail(self):
        with self.assertRaises(ValueError):
            probe.actor_state([0]*16, [0]*9, [0]*6, None, 1)

    def test_history_flag_and_causal_previous(self):
        a = probe.actor_state([1]*9, [2]*9, [3]*6, None, 1)
        b = probe.actor_state([1]*9, [2]*9, [4]*6, [3]*6, 0.5)
        self.assertEqual(len(a), 32)
        self.assertEqual(a[18:30], [3.0]*12)
        self.assertEqual(a[-1], 0)
        self.assertEqual(b[18:24], [4.0]*6)
        self.assertEqual(b[24:30], [3.0]*6)
        self.assertEqual(b[-1], 1)

    def test_observation_rejects_bad_values(self):
        with self.assertRaises(ValueError): probe.actor_state([float('nan')]*9, [0]*9, [0]*6, None, 1)
        with self.assertRaises(ValueError): probe.actor_state([0]*9, [0]*9, [0]*6, None, 2)

    def test_gain_clipping_rate_and_nan(self):
        self.assertAlmostEqual(probe.limited_gain(1, -20), 0.9)
        self.assertAlmostEqual(probe.limited_gain(0.25, -20), 0.25)
        self.assertAlmostEqual(probe.limited_gain(0.95, 20), 1)
        with self.assertRaises(ValueError): probe.limited_gain(1, float('nan'))

    def test_payload_mutation_and_missing_files_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); f = root/'asset'; f.write_text('old')
            expected = probe.tree_hashes(root); probe.verify_tree(root, expected)
            f.write_text('changed')
            with self.assertRaises(RuntimeError): probe.verify_tree(root, expected)
            f.unlink()
            with self.assertRaises(RuntimeError): probe.verify_tree(root, expected)

    def test_source_change_invalidates_image_fingerprint(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for n in run.PACKET_FILES: (root/n).write_text(n)
            old, _ = run.fingerprint(root)
            (root/'probe.py').write_text('changed')
            self.assertNotEqual(old, run.fingerprint(root)[0])

    def test_packet_has_no_policy_or_large_budget(self):
        p = json.loads((Path(__file__).parent/'P0_PLAN.json').read_text())
        self.assertEqual(p['caps']['vla_queries'], 0)
        self.assertEqual(p['caps']['optimizer_updates'], 0)
        self.assertEqual(p['caps']['weight_downloads'], 0)
        self.assertLessEqual(p['caps']['control_frames'], 120)
        self.assertIn('@sha256:', p['base_image'])

    def test_host_native_execution_denied(self):
        with patch.dict('os.environ', {'CONTACT_P0_DOCKER': '0'}):
            with self.assertRaises(RuntimeError): probe.require_container()


if __name__ == '__main__':
    if not Path('/.dockerenv').exists():
        raise SystemExit('Run tests inside Docker')
    unittest.main()
