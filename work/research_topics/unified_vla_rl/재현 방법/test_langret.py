"""Docker-only stdlib tests. No policy, torch, simulator or payload execution."""
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, Mock

import langret_probe as probe
import langret_resume as resume


class Controls(unittest.TestCase):
    def test_compiled_identity_and_caps(self):
        plan = resume.compile_plan()
        probe.validate_plan(plan)
        self.assertEqual(plan['checkpoint']['revision'], '0a051b39aaebd3fc509fe2aba8bc7e60100e09f5')
        self.assertEqual(sum(r['path'].endswith('.safetensors') for r in plan['checkpoint']['files']), 4)

    def test_overbudget_plan_refused(self):
        plan = resume.compile_plan()
        plan['limits']['policy_queries'] = 3
        with self.assertRaises(RuntimeError):
            probe.validate_plan(plan)

    def test_missing_budget_refused(self):
        plan = resume.compile_plan()
        del plan['limits']['resets']
        with self.assertRaises(RuntimeError):
            probe.validate_plan(plan)

    def test_pair_mismatch_refused(self):
        plan = resume.compile_plan()
        plan['pair']['targets'].append('extra')
        with self.assertRaises(RuntimeError):
            probe.validate_plan(plan)

    def test_fingerprint_changes_with_plan(self):
        plan = resume.compile_plan()
        first = resume.fingerprint(plan)
        plan['seed'] += 1
        self.assertNotEqual(first, resume.fingerprint(plan))

    def test_mac_and_small_daemon_refused(self):
        reasons = resume.resource_reasons('Darwin', 'arm64', 'unix:///local.sock',
            dict(OSType='linux', Architecture='aarch64', MemTotal=8*1024**3), [])
        self.assertEqual(len(reasons), 3)

    def test_eligible_host_is_not_native_success(self):
        reasons = resume.resource_reasons('Linux', 'x86_64', 'unix:///local.sock',
            dict(OSType='linux', Architecture='x86_64', MemTotal=64*1024**3), [])
        self.assertEqual(reasons, [])

    def test_remote_endpoint_stops_before_daemon(self):
        responses = [dict(exit_code=0, stdout='remote', stderr=''), dict(exit_code=0, stdout='ssh://remote', stderr='')]
        with patch.dict(os.environ, {}, clear=True), patch.object(resume.shutil, 'which', return_value='/docker'), patch.object(resume, 'capture', side_effect=responses) as capture:
            self.assertEqual(resume.check(0)['decision'], 'RESOURCE_UNMET')
            self.assertEqual(capture.call_count, 2)

    def test_docker_override_stops_all_calls(self):
        with patch.dict(os.environ, {'DOCKER_HOST': 'tcp://remote'}, clear=True), patch.object(resume, 'capture') as capture:
            self.assertEqual(resume.check(0)['decision'], 'RESOURCE_UNMET')
            capture.assert_not_called()

    def test_unknown_memory_refused(self):
        self.assertTrue(resume.resource_reasons('Linux', 'x86_64', 'unix:///local.sock',
            dict(OSType='linux', Architecture='x86_64', MemTotal=None), []))

    def test_stale_image_refused(self):
        with patch.object(resume, 'capture', return_value=dict(exit_code=0, stdout='old')):
            with self.assertRaises(RuntimeError):
                resume.require_image(['docker'], 'image', 'new')

    def test_unowned_volume_preserved(self):
        with patch.object(resume, 'capture', return_value=dict(exit_code=0, stdout='other')), patch.object(resume.subprocess, 'run') as mutate:
            with self.assertRaises(RuntimeError):
                resume.ensure_volume(['docker'], 'cache')
            mutate.assert_not_called()

    def test_stale_cache_refused(self):
        with self.assertRaises(RuntimeError):
            probe.require_prepared(dict(packet_sha256='new'), dict(packet_sha256='old'))

    def test_reset_including_constructor_refused_before_third_call(self):
        b = probe.Budget(dict(resets=2)); operation = Mock()
        reset = probe.bounded_call(b, 'resets', operation)
        reset('constructor-A'); reset('constructor-B')
        with self.assertRaises(RuntimeError):
            reset('extra-reset')
        self.assertEqual(operation.call_count, 2)

    def test_physics_batch_and_halfsteps_share_cap(self):
        b = probe.Budget(dict(physics_steps=5)); operation = Mock()
        probe.physics_call(b, 'mj_step', operation)(None, None, 3)
        probe.physics_call(b, 'mj_step1', operation)(None, None)
        probe.physics_call(b, 'mj_step2', operation)(None, None)
        with self.assertRaises(RuntimeError):
            probe.physics_call(b, 'mj_step', operation)(None, None, nstep=2)
        self.assertEqual(operation.call_count, 3)
        self.assertEqual(b.counts['physics_steps'], 5)

    def test_invalid_counter_increment_refused(self):
        b = probe.Budget(dict(policy_queries=2))
        for key, value in [('other', 1), ('policy_queries', -1), ('policy_queries', 1.2), ('policy_queries', True)]:
            with self.subTest(key=key, value=value), self.assertRaises(RuntimeError):
                b.take(key, value)
        self.assertEqual(b.counts['policy_queries'], 0)

    def test_sha256_and_git_blob_hash_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'fixture'; path.write_bytes(b'fixture')
            for algo, blob, expected in [('sha256', False, hashlib.sha256(b'fixture').hexdigest()),
                                         ('sha1', True, hashlib.sha1(b'blob 7\0fixture').hexdigest())]:
                probe.verify_file(path, dict(size=7, algorithm=algo, git_blob=blob, hash=expected))
            path.write_bytes(b'changed')
            with self.assertRaises(RuntimeError):
                probe.verify_file(path, dict(size=7, algorithm='sha256', hash=hashlib.sha256(b'fixture').hexdigest()))

    def test_path_escape_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            for relative in ['../outside', '/outside', '.']:
                with self.subTest(relative=relative), self.assertRaises(RuntimeError):
                    probe.safe_path(Path(tmp), relative)

    def test_wrong_goal_or_success_is_rejected(self):
        with self.assertRaises(RuntimeError):
            probe.goal_consistency('A', {'A': False, 'B': True}, 1, True)
        probe.goal_consistency('A', {'A': False, 'B': True}, 0, False)

    def test_target_true_reward_done_must_agree(self):
        probe.goal_consistency('A', {'A': True, 'B': True}, 1, True)
        with self.assertRaises(RuntimeError):
            probe.goal_consistency('A', {'A': True, 'B': False}, 0, True)
        with self.assertRaises(RuntimeError):
            probe.goal_consistency('A', {'A': True, 'B': False}, 1, False)

    def test_preprocess_extraction_does_not_execute_other_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'functions.py'
            path.write_text('raise RuntimeError("do not import")\ndef selected(x):\n    return x + 1\n')
            selected = probe.extract_functions(path, ['selected'], {})
            self.assertEqual(selected['selected'](2), 3)
            with self.assertRaises(RuntimeError):
                probe.extract_functions(path, ['missing'], {})

    def test_plan_has_no_machine_specific_paths(self):
        value = json.dumps(resume.compile_plan())
        self.assertNotIn('/Users/', value)
        self.assertNotIn('/home/', value)


if __name__ == '__main__':
    probe.require_container()
    unittest.main(verbosity=2)
