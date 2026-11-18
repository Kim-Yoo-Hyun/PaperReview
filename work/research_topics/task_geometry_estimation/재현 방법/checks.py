"""Docker-only geometry and intervention checks; never model-performance tests."""
import os
from pathlib import Path
import json
import unittest

if os.environ.get('TASK_GEOMETRY_CONTAINER') != '1' or not Path('/.dockerenv').exists():
    raise SystemExit('Use the local Docker launcher; do not run checks on host')

import torch
from config import manifest
from geometry import Budget, DepthOverride, checked_depth, perturb, pooled, xyz_grid, rms_xyz, unpack_xyz


class Contracts(unittest.TestCase):
    def setUp(self):
        self.depth = torch.linspace(1., 2., 224 * 224).reshape(1, 1, 224, 224)
        self.roi = torch.zeros_like(self.depth, dtype=torch.bool)
        self.roi[:, :, 70:84, 70:84] = True
        self.K = torch.tensor([[224., 0., 112.], [0., 224., 112.], [0., 0., 1.]])

    def test_nonfinite_nonpositive_and_wrong_shape_rejected(self):
        for value in (0., -1., float('nan'), float('inf')):
            with self.assertRaises(ValueError): checked_depth(torch.full_like(self.depth, value))
        with self.assertRaises(ValueError): checked_depth(self.depth[:, :, :32, :32])

    def test_identity_preserves_depth_without_alias(self):
        result = perturb(self.depth, self.roi, 'identity', .02)
        self.assertTrue(torch.equal(result, self.depth))
        self.assertNotEqual(result.data_ptr(), self.depth.data_ptr())

    def test_roi_changes_only_target_support(self):
        result = perturb(self.depth, self.roi, 'roi_bias', .02)
        self.assertTrue(torch.equal(result[~self.roi], self.depth[~self.roi]))
        self.assertTrue(torch.allclose(result[self.roi]-self.depth[self.roi], torch.tensor(.02)))
        self.assertGreater(rms_xyz(xyz_grid(self.K, result), xyz_grid(self.K, self.depth)), 0)

    def test_subpatch_permutation_preserves_cell_mean(self):
        result = perturb(self.depth, self.roi, 'subpatch_permutation', .02)
        self.assertFalse(torch.equal(result, self.depth))
        self.assertTrue(torch.allclose(pooled(result), pooled(self.depth), atol=5e-7, rtol=0))
        self.assertTrue((result > 0).all())

    def test_camera_units_and_optical_axis(self):
        points = xyz_grid(self.K, torch.full_like(self.depth, 2.))
        self.assertTrue(torch.allclose(points[..., 2], torch.tensor(2.)))
        self.assertAlmostEqual(float(points[0, 0, 0, 0]), (3.5-112.) / 224. * 2., places=6)
        self.assertAlmostEqual(float(points[0, 0, 0, 1]), (3.5-112.) / 224. * 2., places=6)

    def test_patch_layout_is_not_plain_point_reshape(self):
        grid = xyz_grid(self.K, self.depth)
        packed = grid.reshape(1, 16, 2, 16, 2, 3).permute(0, 1, 3, 2, 4, 5).reshape(1, 256, 12)
        self.assertTrue(torch.equal(unpack_xyz(packed), grid))

    def test_loaded_bf16_rays_are_preserved_and_reportable(self):
        y, x = torch.meshgrid(torch.arange(32)*7+3.5, torch.arange(32)*7+3.5, indexing='ij')
        uv = torch.stack((x, y, torch.ones_like(x))).reshape(3, -1).to(torch.bfloat16)
        loaded = xyz_grid(self.K, self.depth, uv)
        nominal = xyz_grid(self.K, self.depth)
        self.assertGreater(float((loaded-nominal).abs().max()), 0)
        uv[0, 0] = -1
        with self.assertRaises(ValueError): xyz_grid(self.K, self.depth, uv)

    def test_injection_energy_is_not_ground_truth_error(self):
        ref = torch.zeros(1, 1, 1, 3)
        truth = torch.tensor([[[[1., 0., 0.]]]])
        a, b = truth, -truth
        self.assertEqual(rms_xyz(a, ref), rms_xyz(b, ref))
        self.assertNotEqual(rms_xyz(a, truth), rms_xyz(b, truth))

    def test_invalid_mask_and_unknown_condition_rejected(self):
        with self.assertRaises(ValueError): perturb(self.depth, self.roi.float(), 'identity', .02)
        with self.assertRaises(ValueError): perturb(self.depth, self.roi, 'unreviewed', .02)
        with self.assertRaises(ValueError): rms_xyz(torch.ones(1, 3), torch.zeros(1, 3), torch.zeros(1, dtype=torch.bool))

    def test_budget_blocks_before_execution(self):
        b = Budget(manifest())
        b.take('queries', 8)
        with self.assertRaises(RuntimeError): b.take('queries')
        with self.assertRaises(RuntimeError): b.take('vla_commands')
        with self.assertRaises(RuntimeError): b.take('optimizer_steps')
        with self.assertRaises(ValueError): b.take('queries', -1)
        self.assertEqual(b.used['queries'], 8)
        self.assertEqual(b.used['vla_commands'], 0)

    def test_hook_restores_method_on_exception_and_requires_consumption(self):
        class Fake(torch.nn.Module):
            def __init__(self):
                super().__init__(); self.multi_modal_projector = torch.nn.Identity()
            def backproject_patch(self, K, depth, patch_size=14, reso=2):
                grid = xyz_grid(K, depth)
                return grid.reshape(1, 16, 2, 16, 2, 3).permute(0, 1, 3, 2, 4, 5).reshape(1, 256, 12)
        m = Fake()
        with self.assertRaisesRegex(RuntimeError, 'deliberate'):
            with DepthOverride(m, 'original', self.roi, .02): raise RuntimeError('deliberate')
        self.assertNotIn('backproject_patch', m.__dict__)
        with self.assertRaisesRegex(RuntimeError, 'not consumed'):
            with DepthOverride(m, 'original', self.roi, .02): pass
        with DepthOverride(m, 'identity', self.roi, .02, self.depth.clone()) as hook:
            xyz = m.backproject_patch(self.K, self.depth)
            m.multi_modal_projector(xyz)
        self.assertEqual(hook.calls, 1)
        self.assertNotIn('backproject_patch', m.__dict__)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Contracts))
    Path('/out/checks.json').write_text(json.dumps(dict(tests=result.testsRun,
        failures=len(result.failures), errors=len(result.errors), passed=result.wasSuccessful(),
        scope='Geometry contracts and wrapper lifecycle only; no native checkpoint or robotics performance'), indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
