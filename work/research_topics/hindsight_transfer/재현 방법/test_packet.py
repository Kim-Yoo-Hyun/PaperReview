"""Stdlib control tests only. Execute in Docker; these never import a policy or simulator."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import probe
import resume


class PacketTests(unittest.TestCase):
    def test_remote_daemon_rejected(self):
        self.assertTrue(resume.resource_reasons('Linux', 'x86_64', 'ssh://gpu',
                        {'OSType': 'linux', 'Architecture': 'amd64'}, []))

    def test_current_mac_rejected(self):
        self.assertTrue(resume.resource_reasons('Darwin', 'arm64', 'unix:///sock',
                        {'OSType': 'linux', 'Architecture': 'aarch64'}, []))

    def test_linux_endpoint_allowed_for_further_checks(self):
        self.assertEqual(resume.resource_reasons('Linux', 'x86_64', 'unix:///sock',
                         {'OSType': 'linux', 'Architecture': 'amd64'}, []), [])

    def test_override_blocks_before_daemon_contact(self):
        with patch.dict(os.environ, {'DOCKER_HOST': 'ssh://remote'}), patch.object(resume, 'capture') as cap:
            self.assertEqual(resume.check(0)['decision'], 'RESOURCE_UNMET')
            cap.assert_not_called()

    def test_budget_refuses_before_excess_action(self):
        b = probe.Budget({'query': 2}, 10, clock=lambda: 0)
        b.take('query', 2)
        with self.assertRaises(RuntimeError):
            b.take('query')
        self.assertEqual(b.counts['query'], 2)

    def test_optimizer_always_forbidden(self):
        b = probe.Budget(resume.compile_plan()['contract']['limits'], 10)
        with self.assertRaises(RuntimeError):
            b.take('optimizer')

    def test_wall_clock_limit(self):
        clock = iter([0, 10])
        b = probe.Budget({'reset': 2}, 10, clock=lambda: next(clock))
        with self.assertRaises(RuntimeError):
            b.take('reset')
        self.assertEqual(b.counts['reset'], 0)

    def test_git_blob_and_raw_hash_are_distinct(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'data'
            p.write_bytes(b'abc')
            raw = hashlib.sha1(b'abc').hexdigest()
            git = hashlib.sha1(b'blob 3\0abc').hexdigest()
            probe.verify_file(p, 3, git, 'sha1', git_blob=True)
            self.assertNotEqual(raw, git)
            with self.assertRaises(RuntimeError):
                probe.verify_file(p, 3, raw, 'sha1', git_blob=True)

    def test_changed_or_truncated_payload_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'data'
            p.write_bytes(b'xyz')
            with self.assertRaises(RuntimeError):
                probe.verify_file(p, 3, hashlib.sha256(b'abc').hexdigest())
            with self.assertRaises(RuntimeError):
                probe.verify_file(p, 4, hashlib.sha256(b'xyz').hexdigest())

    def test_stale_image_refused(self):
        with patch.object(resume, 'capture', return_value={'exit_code': 0, 'stdout': 'old'}):
            with self.assertRaises(RuntimeError):
                resume.validate_image(['docker'], 'image', 'new')

    def test_foreign_volume_preserved(self):
        with patch.object(resume, 'capture', return_value={'exit_code': 0, 'stdout': 'someone-else'}), \
             patch.object(resume.subprocess, 'run') as run:
            with self.assertRaises(RuntimeError):
                resume.volume(['docker'], 'foreign')
            run.assert_not_called()

    def test_fingerprint_covers_source_contract(self):
        first = resume.fingerprint()
        plan = resume.compile_plan()
        plan['contract']['same_goal_logprob_atol'] *= 2
        with patch.object(resume, 'compile_plan', return_value=plan):
            self.assertNotEqual(first, resume.fingerprint())

    def test_no_p1_p2_entrypoint(self):
        with patch('sys.argv', ['resume.py', 'p2', '--results', '/tmp/unused']), \
             patch('sys.stderr', new_callable=io.StringIO), patch.object(resume, 'check') as check:
            with self.assertRaises(SystemExit):
                resume.main()
            check.assert_not_called()

    def test_seed_streams_are_stable_and_separate(self):
        args = ('P0', 11, 'task-A', 0, 0)
        self.assertEqual(probe.seed_key(*args, 'collection'), probe.seed_key(*args, 'collection'))
        self.assertNotEqual(probe.seed_key(*args, 'collection'), probe.seed_key(*args, 'selector'))

    def test_probe_denies_host_execution(self):
        with patch.object(Path, 'exists', return_value=False):
            with self.assertRaises(RuntimeError):
                probe.container_only()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    probe.container_only()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PacketTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    record = {'kind': 'stdlib Docker control tests; no model/simulator', 'tests_run': result.testsRun,
              'failures': len(result.failures), 'errors': len(result.errors),
              'successful': result.wasSuccessful(), 'packet_sha': resume.fingerprint()}
    if args.report:
        probe.write_json(args.report, record)
    raise SystemExit(0 if result.wasSuccessful() else 1)
