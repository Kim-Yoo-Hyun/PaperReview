"""Control-plane guards only; this is NOT CUDA/EGL/model or action-adapter validation."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import native_p0
import resume


class PacketTests(unittest.TestCase):
    def test_mac_stops_before_gpu_or_payload(self):
        replies = [
            {'argv': [], 'exit_code': 0, 'stdout': 'desktop-linux', 'stderr': ''},
            {'argv': [], 'exit_code': 0, 'stdout': 'unix:///tmp/docker.sock', 'stderr': ''},
            {'argv': [], 'exit_code': 0, 'stdout': json.dumps({'OSType': 'linux', 'Architecture': 'aarch64'}), 'stderr': ''},
        ]
        with patch.object(resume.platform, 'system', return_value='Darwin'), \
             patch.object(resume.platform, 'machine', return_value='arm64'), \
             patch.dict(resume.os.environ, {}, clear=True), \
             patch.object(resume.shutil, 'which', return_value='/docker'), \
             patch.object(resume, 'capture', side_effect=replies) as calls:
            self.assertEqual(resume.check()['decision'], 'RESOURCE_UNMET')
            self.assertEqual(calls.call_count, 3)

    def test_override_does_not_contact_daemon(self):
        for variable in ('DOCKER_HOST', 'DOCKER_CONTEXT', 'BUILDX_BUILDER', 'BUILDKIT_HOST'):
            with self.subTest(variable=variable), patch.dict(resume.os.environ, {variable: 'remote'}, clear=True), \
                 patch.object(resume.shutil, 'which', return_value='/docker'), patch.object(resume, 'capture') as call:
                self.assertEqual(resume.check()['decision'], 'RESOURCE_UNMET')
                call.assert_not_called()

    def test_remote_context_does_not_contact_daemon(self):
        replies = [{'argv': [], 'exit_code': 0, 'stdout': s, 'stderr': ''} for s in ('remote', 'ssh://remote')]
        with patch.dict(resume.os.environ, {}, clear=True), patch.object(resume.shutil, 'which', return_value='/docker'), \
             patch.object(resume, 'capture', side_effect=replies) as call:
            self.assertEqual(resume.check()['decision'], 'RESOURCE_UNMET')
            self.assertEqual(call.call_count, 2)

    def test_linux_host_eligibility_is_not_native_pass(self):
        self.assertEqual(resume.resource_reasons('Linux', 'x86_64', 'unix:///var/run/docker.sock',
                                                {'OSType': 'linux', 'Architecture': 'x86_64'}, []), [])

    def test_stale_image_rejected(self):
        with patch.object(resume, 'capture', return_value={'exit_code': 0, 'stdout': 'old'}):
            with self.assertRaisesRegex(RuntimeError, 'stale'):
                resume.require_fresh_image('image', 'new')

    def test_each_budget_cap_is_enforced_before_extra_call(self):
        b = native_p0.Budget()
        for key, cap in b.CAPS.items():
            for _ in range(cap):
                b.charge(key)
            with self.assertRaisesRegex(RuntimeError, 'cap reached'):
                b.charge(key)
            self.assertEqual(b.used[key], cap)
        self.assertEqual(b.used['warmup_steps'] + b.used['policy_steps'], 36)

    def test_unknown_counter_rejected(self):
        with self.assertRaisesRegex(RuntimeError, 'Unknown'):
            native_p0.Budget().charge('training')

    def test_current_contract_matches_and_changed_cap_is_rejected(self):
        current = json.loads(resume.LEDGER.read_text())
        native_p0.validate_contract(current)
        changed = copy.deepcopy(current)
        changed['r2_review']['comparison_contract']['budget']['P0']['vla_queries'] = 3
        with self.assertRaisesRegex(RuntimeError, 'contract changed'):
            native_p0.validate_contract(changed)

    def test_source_syntax(self):
        for name in ['resume.py', 'native_p0.py']:
            p = Path(__file__).parent / name
            compile(p.read_text(), str(p), 'exec')


if __name__ == '__main__':
    unittest.main(verbosity=2)
