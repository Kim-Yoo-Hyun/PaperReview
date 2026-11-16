"""Docker stdlib control tests. No torch, model, simulator, or scientific proxy result."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import probe
import resume


class PacketTests(unittest.TestCase):
    def test_no_control_step_even_on_first_attempt(self):
        b = probe.Budget({'control_steps': 0, 'queries': 2})
        with self.assertRaises(RuntimeError):
            b.charge('control_steps')
        b.charge('queries'); b.charge('queries')
        with self.assertRaises(RuntimeError):
            b.charge('queries')
        self.assertEqual(b.used, {'control_steps': 0, 'queries': 2})

    def test_unknown_cost_rejected(self):
        with self.assertRaises(RuntimeError):
            probe.Budget({'backwards': 8}).charge('backward')

    def test_evaluation_cached_and_defensive_copy(self):
        c = probe.EvaluationCache()
        calls = []
        def event():
            calls.append(1)
            return {'counter': [len(calls)]}
        first = c.get(0, event)
        first['counter'][0] = 100
        self.assertEqual(c.get(0, event), {'counter': [1]})
        self.assertEqual(c.get(1, event), {'counter': [2]})
        self.assertEqual(len(calls), 2)

    def test_observer_keeps_ambiguous_and_none(self):
        self.assertEqual([probe.grasp_label(a, b) for a, b in [(True, False), (False, True), (True, True), (False, False)]],
                         ['correct', 'wrong', 'ambiguous', 'none'])

    def test_value_hook_is_local_and_removed_on_error(self):
        class Tensor:
            def detach(self):
                return 'detached'
        class Handle:
            removed = False
            def remove(self):
                self.removed = True
        class Head:
            def register_forward_pre_hook(self, fn):
                self.fn, self.handle = fn, Handle()
                return self.handle
        head = Head()
        with self.assertRaisesRegex(ValueError, 'fixture'):
            with probe.ValueRouting(head, True):
                self.assertEqual(head.fn(head, (Tensor(),)), ('detached',))
                raise ValueError('fixture')
        self.assertTrue(head.handle.removed)
        # This tests hook lifetime only, not autograd correctness.

    def test_joint_branch_has_no_hook(self):
        class Head:
            def register_forward_pre_hook(self, fn):
                raise AssertionError('Unexpected hook')
        with probe.ValueRouting(Head(), False):
            pass

    def test_bad_value_signature_rejected(self):
        with self.assertRaises(RuntimeError):
            probe.ValueRouting.cut(None, ())

    def test_archive_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / 'x.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('../escape', 'unsafe')
            with self.assertRaises(RuntimeError):
                probe.safe_extract(archive, Path(tmp) / 'out')
            self.assertFalse((Path(tmp) / 'escape').exists())

    def test_cache_tampering_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / 'payload'
            f.write_bytes(b'bad')
            with patch('probe.urllib.request.urlopen') as request:
                with self.assertRaises(RuntimeError):
                    probe.fetch_file('https://unused', f, {'size': 3, 'hash_algorithm': 'sha256', 'hash': 'wrong'})
                request.assert_not_called()
            self.assertEqual(f.read_bytes(), b'bad')

    def test_git_blob_hash_includes_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / 'x'; f.write_bytes(b'abc')
            self.assertEqual(probe.digest(f, 'sha1'), hashlib.sha1(b'blob 3\0abc').hexdigest())

    def test_remote_and_arm_rejected(self):
        self.assertTrue(resume.resource_reasons('Linux', 'x86_64', 'ssh://gpu', {'OSType': 'linux', 'Architecture': 'x86_64'}, []))
        self.assertTrue(resume.resource_reasons('Darwin', 'arm64', 'unix:///docker.sock', {'OSType': 'linux', 'Architecture': 'aarch64'}, []))

    def test_remote_context_not_contacted(self):
        replies = [{'exit_code': 0, 'stdout': 'remote', 'stderr': ''},
                   {'exit_code': 0, 'stdout': 'ssh://gpu', 'stderr': ''}]
        with patch.dict('os.environ', {}, clear=True), patch('resume.shutil.which', return_value='/bin/docker'), \
                patch('resume.capture', side_effect=replies) as capture:
            self.assertEqual(resume.check(0)['decision'], 'RESOURCE_UNMET')
            self.assertEqual(capture.call_count, 2)

    def test_stale_image_rejected(self):
        with patch('resume.capture', return_value={'exit_code': 0, 'stdout': 'old'}):
            with self.assertRaises(RuntimeError):
                resume.validate_image(['docker'], 'test:image', 'new')

    def test_plan_has_bounded_non_scientific_scope(self):
        p = resume.compile_plan()
        self.assertEqual(p['contract']['caps'], {'resets': 2, 'queries': 2, 'control_steps': 0,
            'physics_steps': 8000, 'teacher_forwards': 12, 'backwards': 8, 'optimizer_steps': 3})
        self.assertFalse(p['contract']['full_task_rollout'])
        self.assertEqual(p['design']['arms']['B']['value_detach'], True)
        self.assertEqual(p['design']['task']['episode_id'], 0)
        self.assertEqual(len(p['sources']['checkpoint']['revision']), 40)
        shards = [x for x in p['sources']['checkpoint']['files'] if x['path'].endswith('.safetensors')]
        self.assertEqual(len(shards), 4)
        self.assertTrue(all(len(x['hash']) == 64 and x['hash_algorithm'] == 'sha256' for x in shards))
        self.assertEqual(len(resume.fingerprint()), 64)

    def test_native_functions_do_not_run_on_import(self):
        self.assertNotIn('torch', __import__('sys').modules)
        for f in ['probe.py', 'resume.py', 'test_packet.py']:
            compile((Path(__file__).parent / f).read_text(), f, 'exec')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PacketTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    output = Path('/results/control_tests.json')
    if output.parent.exists():
        output.write_text(json.dumps({'scope': 'stdlib Docker control tests only; no torch/native autograd qualification',
                                     'tests': result.testsRun, 'failures': len(result.failures),
                                     'errors': len(result.errors), 'packet_sha': resume.fingerprint()}, indent=2))
    raise SystemExit(not result.wasSuccessful())
