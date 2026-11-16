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
import allocation
from dataclasses import replace


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


    def test_packet_python_compiles_without_importing_dependencies(self):
        for name in ('allocation.py', 'probe.py', 'resume.py', 'test_packet.py'):
            path = resume.HERE / name
            compile(path.read_text(), str(path), 'exec')

    def test_allocator_uniform_without_history(self):
        q = allocation.probabilities([0] * 10, [0] * 10)
        self.assertAlmostEqual(sum(q), 1.)
        self.assertTrue(all(abs(v - .1) < 1e-12 for v in q))

    def test_allocator_frontier_and_floor(self):
        q = allocation.probabilities([0, 16, 32] + [0] * 7, [32] * 10)
        self.assertGreater(q[1], q[0])
        self.assertAlmostEqual(q[0], q[2])
        self.assertAlmostEqual(sum(q), 1.)
        self.assertTrue(all(v >= .02 and .1 / v <= 5 for v in q))
        with self.assertRaises(RuntimeError):
            allocation.probabilities([33] * 10, [32] * 10)

    def test_sampler_keeps_train_split_group_and_seed(self):
        q = resume.compile_plan()['contract']['fixture_q']
        rows = allocation.sample_groups(q, 20, 11)
        allocation.validate_groups(rows)
        self.assertEqual(rows, allocation.sample_groups(q, 20, 11))
        self.assertNotEqual(rows, allocation.sample_groups(q, 20, 12))
        self.assertTrue(all(r.row < 30 and r.p == .1 and r.q == q[r.task] for r in rows))
        self.assertEqual(len(rows), 160)

    def test_sampler_rejects_invalid_probability_vector(self):
        for q in ([.1] * 9, [.09] * 10, [float('nan')] + [.1] * 9, [.01, .19] + [.1] * 8):
            with self.assertRaises(RuntimeError):
                allocation.sample_groups(q, 1, 11)

    def test_identity_and_group_corruption_rejected(self):
        rows = allocation.sample_groups([.1] * 10, 1, 11)
        corruptions = [rows[:-1], rows + rows, rows[::-1]]
        for key, value in [('task', (rows[0].task + 1) % 10), ('row', 49), ('policy', 1), ('q_version', 1), ('q', .2), ('replicate', 0)]:
            corruptions.append(rows[:1] + [replace(rows[1], **{key:value})] + rows[2:])
        for bad in corruptions:
            with self.assertRaises(RuntimeError):
                allocation.validate_groups(bad)
        for key, value in [('q', .01), ('p', .2), ('q', float('inf')), ('task', 10), ('row', 50), ('replicate', 8), ('epoch', -1)]:
            with self.assertRaises(RuntimeError):
                replace(rows[0], **{key:value})

    def test_fixture_has_distinct_task_weights(self):
        plan = resume.compile_plan()
        q = plan['contract']['fixture_q']
        self.assertAlmostEqual(sum(q), 1.)
        ids = [c['task_id'] for c in plan['cases']]
        self.assertEqual(ids, [0, 3])
        self.assertNotEqual(q[ids[0]], q[ids[1]])
        self.assertTrue(all(c['init_row'] == 30 for c in plan['cases']))

    def test_budget_reservations_do_not_partially_overrun(self):
        limits = resume.compile_plan()['contract']['limits']
        b = probe.Budget(limits, 100, clock=lambda: 0)
        b.take('query_slots', limits['query_slots'])
        with self.assertRaises(RuntimeError):
            b.take('query_slots', 8)
        for key, n in [('control', 0), ('control', -1), ('unknown', 1)]:
            with self.assertRaises(RuntimeError):
                b.take(key, n)
        self.assertEqual(b.counts['query_slots'], limits['query_slots'])
        self.assertEqual(b.counts['control'], 0)

    def test_native_resource_rejection_prevents_build_and_download(self):
        with tempfile.TemporaryDirectory() as d:
            with patch('sys.argv', ['resume.py', 'build', '--results', str(Path(d) / 'run')]), \
                 patch.object(resume, 'check', return_value={'decision': 'RESOURCE_UNMET'}), \
                 patch.object(resume.subprocess, 'run') as run, patch('sys.stdout', new_callable=io.StringIO):
                self.assertEqual(resume.main(), 3)
                run.assert_not_called()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    probe.container_only()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PacketTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    record = {'kind': 'stdlib Docker control tests; no torch tensor/model/simulator', 'native_executed': False, 'tests_run': result.testsRun,
              'failures': len(result.failures), 'errors': len(result.errors),
              'successful': result.wasSuccessful(), 'packet_sha': resume.fingerprint()}
    if args.report:
        probe.write_json(args.report, record)
    raise SystemExit(0 if result.wasSuccessful() else 1)
