"""Docker CPU control tests only: these do not qualify any native model or simulator."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import probe
import resume


class PacketTests(unittest.TestCase):
    def test_budget_bounds_attempts(self):
        budget = probe.Budget({'query': 1})
        budget.charge('query')
        with self.assertRaises(RuntimeError):
            budget.charge('query')
        self.assertEqual(budget.used['query'], 1)

    def test_unknown_cost_rejected(self):
        with self.assertRaises(RuntimeError):
            probe.Budget({'query': 1}).charge('step')

    def test_reentrant_evaluation_does_not_repeat_event(self):
        cache = probe.EvaluationCache()
        calls = []
        def event():
            calls.append(1)
            return {'values': [len(calls)]}
        first = cache.get(5, event)
        first['values'][0] = 99
        self.assertEqual(cache.get(5, event)['values'], [1])
        self.assertEqual(len(calls), 1)
        cache.get(6, event)
        self.assertEqual(len(calls), 2)

    def test_archive_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / 'x.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('../escape', 'unsafe')
            with self.assertRaises(RuntimeError):
                probe.safe_extract(archive, Path(tmp) / 'out')
            self.assertFalse((Path(tmp) / 'escape').exists())

    def test_existing_payload_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / 'payload'
            f.write_bytes(b'changed')
            with patch('probe.urllib.request.urlopen') as request:
                with self.assertRaises(RuntimeError):
                    probe.fetch_file('https://unused', f, {'size': 7, 'hash_algorithm': 'sha256', 'hash': 'wrong'})
                request.assert_not_called()
            self.assertEqual(f.read_bytes(), b'changed')

    def test_remote_and_arm_hosts_rejected(self):
        self.assertTrue(resume.resource_reasons('Linux', 'x86_64', 'ssh://gpu', {'OSType': 'linux', 'Architecture': 'x86_64'}, []))
        self.assertTrue(resume.resource_reasons('Darwin', 'arm64', 'unix:///docker.sock', {'OSType': 'linux', 'Architecture': 'aarch64'}, []))

    def test_stale_image_rejected(self):
        with patch('resume.capture', return_value={'exit_code': 0, 'stdout': 'old'}):
            with self.assertRaises(RuntimeError):
                resume.validate_image(['docker'], 'test:image', 'new')

    def test_remote_context_never_contacts_daemon(self):
        replies = [{'exit_code': 0, 'stdout': 'remote', 'stderr': ''},
                   {'exit_code': 0, 'stdout': 'ssh://gpu', 'stderr': ''}]
        with patch.dict('os.environ', {}, clear=True), patch('resume.shutil.which', return_value='/usr/bin/docker'), \
                patch('resume.capture', side_effect=replies) as capture:
            self.assertEqual(resume.check(0)['decision'], 'RESOURCE_UNMET')
            self.assertEqual(capture.call_count, 2)

    def test_contract_is_io_only(self):
        plan = json.loads((Path(__file__).parent / 'RESUME_PLAN.json').read_text())
        self.assertEqual(plan['contract']['caps'], {'resets': 2, 'queries': 3, 'control_steps': 6, 'events': 1, 'physics_steps': 2000})
        self.assertFalse(plan['contract']['training'])
        self.assertFalse(plan['validation']['native_verified'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
