"""Docker-only mathematical/IO/control checks; no weights, scenes or policy rollout.

These checks have not run on the preparation host. Native P0 is a separate gate.
"""
import ast
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

if not Path('/.dockerenv').exists() or os.environ.get('RELATION_IN_DOCKER') != '1':
    raise SystemExit('Run these checks inside local Docker via resume.py control/run')

import numpy as np
import torch
from actor import ARM, FLIP, covariance
from probe import Budget, BudgetExceeded, PLAN, instrument_sources, safe_extract
from openpi import transforms as tr
from openpi.policies.aloha_policy import AlohaInputs, AlohaOutputs
from openpi.shared.normalize import NormStats


class BudgetChecks(unittest.TestCase):
    def test_phase_limit_stops_before_extra_step(self):
        with patch.dict(PLAN['budget'], max_physics_per_setup_attempt=2):
            b = Budget(); b.begin('setup')
            b.before_step(); b.before_step()
            with self.assertRaises(BudgetExceeded):
                b.before_step()
            self.assertEqual((b.total, b.setup, b.completed), (2, 2, 0))

    def test_retry_does_not_reset_global_budget(self):
        with patch.dict(PLAN['budget'], max_total_physics_steps=3):
            b = Budget(); b.begin('setup'); b.before_step(); b.before_step()
            b.begin('setup'); b.before_step(); b.begin('control')
            with self.assertRaises(BudgetExceeded):
                b.before_step()
            self.assertEqual(b.total, 3)

    def test_upstream_exception_handler_cannot_swallow_budget(self):
        self.assertFalse(issubclass(BudgetExceeded, Exception))


class DistributionChecks(unittest.TestCase):
    def setUp(self):
        self.cfg = PLAN['actor']
        self.j = torch.cat((torch.eye(6), -torch.eye(6)), dim=1)

    def arm(self, covariance_matrix):
        return covariance_matrix[ARM][:, ARM]

    def test_zero_coupling_is_isotropic_and_grippers_independent(self):
        s = covariance(self.j, torch.tensor(0.), self.cfg)
        expected = torch.eye(14)*self.cfg['sigma_gripper']**2
        expected[ARM, ARM] = self.cfg['sigma_arm']**2
        torch.testing.assert_close(s, expected)

    def test_fixed_trace_positive_and_relative_motion_suppressed(self):
        s0 = covariance(self.j, torch.tensor(0.), self.cfg)
        s1 = covariance(self.j, torch.tensor(5.), self.cfg)
        self.assertGreater(float(torch.linalg.eigvalsh(s1).min()), 0)
        torch.testing.assert_close(torch.trace(self.arm(s0)), torch.trace(self.arm(s1)))
        # For J=[I,-I], a common arm displacement is null; opposite motion is constrained.
        common = torch.ones(12)
        relative = torch.cat((torch.ones(6), -torch.ones(6)))
        self.assertLess(float(relative @ self.arm(s1) @ relative), float(common @ self.arm(s1) @ common))
        self.assertLess(float(torch.trace(self.j @ self.arm(s1) @ self.j.T)),
                        float(torch.trace(self.j @ self.arm(s0) @ self.j.T)))

    def test_raw_likelihood_gradient_and_replay(self):
        logit = torch.tensor(0., requires_grad=True)
        lam = 10*torch.sigmoid(logit)
        mean = torch.zeros(14, requires_grad=True)
        dist = torch.distributions.MultivariateNormal(mean, covariance_matrix=covariance(self.j, lam, self.cfg))
        raw = torch.linspace(-.2, .2, 14).detach()
        score = dist.log_prob(raw)
        replay = torch.distributions.MultivariateNormal(mean, covariance_matrix=covariance(self.j, lam, self.cfg)).log_prob(raw)
        torch.testing.assert_close(score, replay, atol=1e-6, rtol=0)
        (-score).backward()
        self.assertTrue(torch.isfinite(logit.grad) and logit.grad.abs() > 0)
        self.assertTrue(torch.isfinite(mean.grad).all() and mean.grad.norm() > 0)
        self.assertIsNone(raw.grad)
        self.assertGreater(float((score - dist.log_prob(raw.clamp(-.05, .05))).abs()), .001)


class TransformChecks(unittest.TestCase):
    def test_state_token_precedes_padding_and_arm_action_roundtrip(self):
        state = np.linspace(-.2, .3, 14).astype(np.float32)
        state[[6, 13]] = [.2, .8]
        images = {k:np.full((3,8,8), 128, np.uint8) for k in ('cam_high','cam_left_wrist','cam_right_wrist')}
        d = AlohaInputs(adapt_to_pi=True)({'images':images, 'state':state.copy(), 'prompt':'lift pot'})
        stats = {k:NormStats(mean=np.zeros(14), std=np.ones(14), q01=-np.ones(14), q99=np.ones(14)) for k in ('state','actions')}
        d = tr.Normalize(stats, use_quantiles=True)(d)
        observed = []
        class Tokenizer:
            def tokenize(self, prompt, actual_state):
                observed.append(actual_state.copy())
                return np.array([1, 2]), np.array([True, True])
        d = tr.TokenizePrompt(Tokenizer(), discrete_state_input=True)(d)
        d = tr.PadStatesAndActions(32)(d)
        self.assertEqual(observed[0].shape, (14,))
        self.assertEqual(d['state'].shape, (32,))
        raw = np.linspace(-.01, .01, 14)[None]
        restored = tr.Unnormalize(stats, use_quantiles=True)({'state':d['state'], 'actions':raw.copy()})
        restored = tr.AbsoluteActions(tr.make_bool_mask(6,-1,6,-1))(restored)
        command = AlohaOutputs(adapt_to_pi=True)(restored)['actions'][0]
        # Independent physical-unit oracle for selected symmetric quantiles.
        delta = (raw[0]+1)/2*(2+1e-6)-1
        np.testing.assert_allclose(command[ARM], state[ARM]+FLIP[ARM]*delta[ARM], atol=1e-6)
        np.testing.assert_allclose(command[[6,13]], (delta[[6,13]]+.5476+.6213)/(1.4910+.6213), atol=1e-6)


class FileChecks(unittest.TestCase):
    def test_archive_traversal_and_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for filename, mode in [('../escape', 0), ('link', stat.S_IFLNK | 0o777)]:
                zpath = root/'asset.zip'
                with zipfile.ZipFile(zpath,'w') as z:
                    info = zipfile.ZipInfo(filename); info.external_attr = mode << 16
                    z.writestr(info, 'target')
                with self.assertRaises(ValueError):
                    safe_extract(zpath, root/'out')
            self.assertFalse((root/'escape').exists())

    def test_pinned_source_instrumentation_covers_explicit_scene_steps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree('/opt/relation-src/robotwin/envs', root/'envs')
            changes = instrument_sources(root)
            self.assertTrue(changes)
            for file in (root/'envs').rglob('*.py'):
                tree = ast.parse(file.read_text())
                for n in ast.walk(tree):
                    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'step':
                        receiver = n.func.value
                        is_scene = (isinstance(receiver,ast.Name) and receiver.id=='scene') or (isinstance(receiver,ast.Attribute) and receiver.attr=='scene')
                        self.assertFalse(is_scene, str(file))


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    report = {'tests':result.testsRun, 'passed':result.wasSuccessful(),
        'failures':[(str(t), text) for t,text in result.failures], 'errors':[(str(t),text) for t,text in result.errors],
        'packet':os.environ['RELATION_PACKET_SHA'], 'native_model_loads':0, 'physics_steps':0,
        'scope':'CPU contract checks inside Docker; not native P0'}
    Path('/results/control.json').write_text(json.dumps(report, indent=2)+'\n')
    marker = Path('/cache') / ('control-'+os.environ['RELATION_PACKET_SHA']+'.json')
    if result.wasSuccessful():
        marker.write_text(json.dumps(report, indent=2)+'\n')
    else:
        marker.unlink(missing_ok=True)
    sys.exit(0 if result.wasSuccessful() else 1)
