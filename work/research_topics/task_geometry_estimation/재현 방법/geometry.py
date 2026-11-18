"""Container-only post-crop depth intervention; no training or control interface."""
import os
from pathlib import Path
import types

if os.environ.get('TASK_GEOMETRY_CONTAINER') != '1' or not Path('/.dockerenv').exists():
    raise SystemExit('Use resume.py in local Docker; geometry probes are not host experiments')

import torch
import torch.nn.functional as F


class Budget:
    def __init__(self, plan):
        self.limits = plan['budgets']
        self.used = {k: 0 for k in self.limits if k != 'tokens_per_query'}

    def take(self, name, count=1):
        if type(count) is not int or count < 0 or name not in self.used:
            raise ValueError('Invalid budget consumption')
        if self.used[name] + count > self.limits[name]:
            raise RuntimeError('Global budget exceeded: ' + name)
        self.used[name] += count


def checked_depth(value):
    if value.shape != (1, 1, 224, 224) or not value.is_floating_point():
        raise ValueError('Expected floating depth [1,1,224,224]')
    if not torch.isfinite(value).all() or not (value > 0).all():
        raise ValueError('Invalid/nonpositive depth; no clipping or imputation')
    return value


def pooled(depth):
    return F.interpolate(depth, size=(32, 32), mode='area')


def xyz_grid(K, depth, uv_h=None):
    """Independent math with nominal or actual (possibly BF16-rounded) rays."""
    K = K.reshape(3, 3).float()
    if not torch.isfinite(K).all() or K[0, 0] <= 0 or K[1, 1] <= 0:
        raise ValueError('Invalid camera intrinsic')
    y, x = torch.meshgrid(torch.arange(32, device=depth.device) * 7 + 3.5,
                          torch.arange(32, device=depth.device) * 7 + 3.5, indexing='ij')
    uv = torch.stack((x, y, torch.ones_like(x))).reshape(3, -1).float()
    if uv_h is not None:
        expected = uv.to(uv_h.dtype)
        if uv_h.shape != (3, 1024) or not torch.equal(uv_h, expected):
            raise ValueError('Loaded ray layout differs from pinned cell-center convention')
        uv = uv_h.float()
    rays = torch.linalg.solve(K, uv).T.reshape(1, 32, 32, 3)
    return rays * pooled(depth).permute(0, 2, 3, 1).float()


def unpack_xyz(patches):
    if patches.shape != (1, 256, 12):
        raise ValueError('Expected 16x16 patches with four XYZ points')
    return patches.reshape(1, 16, 16, 2, 2, 3).permute(0, 1, 3, 2, 4, 5).reshape(1, 32, 32, 3)


def perturb(depth, roi, mode, bias):
    checked_depth(depth)
    if roi.shape != depth.shape or roi.dtype != torch.bool:
        raise ValueError('ROI must be a same-shape bool mask')
    if mode == 'identity':
        result = depth.clone()
    elif mode == 'roi_bias':
        result = depth + roi.to(depth.dtype) * bias
    elif mode == 'subpatch_permutation':
        # Permute values inside each 7x7 cell: preserve positivity and its multiset.
        blocks = depth.reshape(1, 1, 32, 7, 32, 7).permute(0, 1, 2, 4, 3, 5).reshape(1, 1, 32, 32, 49)
        result = blocks.roll(1, -1).reshape(1, 1, 32, 32, 7, 7).permute(0, 1, 2, 4, 3, 5).reshape_as(depth)
    else:
        raise ValueError('Unknown geometry condition: ' + str(mode))
    return checked_depth(result)


def rms_xyz(a, b, support=None):
    squared = (a.float() - b.float()).square().sum(-1)
    if support is not None:
        squared = squared[support]
    if squared.numel() == 0 or not torch.isfinite(squared).all():
        raise ValueError('Empty or invalid common support')
    return float(squared.mean().sqrt())


class DepthOverride:
    """Instance-local wrapper around the loaded module's ORIGINAL backprojection.

    Captures post-crop, pre-area depth; preserves both upstream no-grad boundaries.
    The baseline calls the original function with its unchanged arguments.
    """
    def __init__(self, model, mode, roi, bias, reference=None):
        self.model, self.mode, self.roi, self.bias = model, mode, roi, bias
        self.reference = reference
        self.calls, self.feature_calls = 0, 0
        self.captured = {}

    def __enter__(self):
        if 'backproject_patch' in self.model.__dict__:
            raise RuntimeError('Refuse to overwrite another instance patch')
        self.original = self.model.backproject_patch

        def wrapped(_model, K, depth, patch_size=14, reso=2):
            self.calls += 1
            if self.calls != 1 or patch_size != 14 or reso != 2:
                raise RuntimeError('Unexpected geometry hook count/configuration')
            checked_depth(depth)
            self.captured['upstream_depth'] = depth.detach().clone()
            used = depth
            if self.mode != 'original':
                ref = self.reference
                if ref is None or ref.dtype != depth.dtype or ref.device != depth.device:
                    raise ValueError('Reference depth dtype/device not matched')
                if not torch.equal(ref, depth):
                    raise RuntimeError('Upstream depth changed across controlled conditions')
                used = perturb(ref, self.roi, self.mode, self.bias)
            xyz = self.original(K, used, patch_size=patch_size, reso=reso)
            self.captured.update(depth=used.detach().clone(), xyz=unpack_xyz(xyz.detach()), K=K.detach().clone())
            return xyz

        def capture(_module, _args, output):
            self.feature_calls += 1
            if self.feature_calls != 1:
                raise RuntimeError('Unexpected projector replay within one query')
            self.captured['projected_features'] = output.detach().float().cpu()

        self.model.backproject_patch = types.MethodType(wrapped, self.model)
        try:
            self.handle = self.model.multi_modal_projector.register_forward_hook(capture)
        except Exception:
            delattr(self.model, 'backproject_patch')
            raise
        return self

    def __exit__(self, _type, _value, _traceback):
        self.handle.remove()
        delattr(self.model, 'backproject_patch')
        if _type is None and (self.calls != 1 or self.feature_calls != 1):
            raise RuntimeError('Depth override was not consumed exactly once at prefill')
