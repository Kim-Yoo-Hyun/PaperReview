"""Docker-only scene capture and bounded SpatialVLA geometry-input qualification."""
import argparse
import hashlib
import inspect
import json
import os
from pathlib import Path
import random
import sys
import time
import xml.etree.ElementTree as ET

if os.environ.get('TASK_GEOMETRY_CONTAINER') != '1' or not Path('/.dockerenv').exists():
    raise SystemExit('Use resume.py in local Docker; host experiments are forbidden')

from config import manifest
from geometry import Budget, DepthOverride, pooled, rms_xyz, xyz_grid
import shared_probe

PLAN = manifest()
shared_probe.PLAN = PLAN


def write(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scene(output, budget):
    import numpy as np
    import mujoco
    import robosuite
    from PIL import Image
    from robosuite.environments.manipulation.nut_assembly import NutAssemblySquare
    from robosuite.utils.binding_utils import MjSim
    from robosuite.utils.camera_utils import get_camera_intrinsic_matrix, get_camera_extrinsic_matrix, get_real_depth_map

    class PlacementView(NutAssemblySquare):
        def _load_model(self):
            super()._load_model()
            world = self.model.worldbody
            for name in ('peg1', 'peg2'):
                body = world.find(".//body[@name='" + name + "']")
                if body is None: raise RuntimeError('Pinned arena changed')
                for geom in body.iter('geom'):
                    geom.set('contype', '0'); geom.set('conaffinity', '0'); geom.set('rgba', '0 0 0 0')
            ET.SubElement(world, 'geom', name='geometry_target', type='box', pos='0 0 0.8005',
                          size='0.12 0.10 0.0004', rgba='0.1 0.7 0.1 0.5', contype='0', conaffinity='0', group='1')
            for name, ends in (('shaft', '0 -0.16 0.802 0.07 -0.16 0.802'),
                               ('tip1', '0.07 -0.16 0.802 0.05 -0.145 0.802'),
                               ('tip2', '0.07 -0.16 0.802 0.05 -0.175 0.802')):
                ET.SubElement(world, 'geom', name='geometry_arrow_' + name, type='capsule', fromto=ends,
                              size='0.003', rgba='1 0 0 1', contype='0', conaffinity='0', group='1')

        def reward(self, action=None): return 0.
        def _check_success(self): return False

    originals = {key: getattr(MjSim, key) for key in ('step', 'step2')}
    for key, original in originals.items():
        def step(sim, *args, _original=original, **kwargs):
            budget.take('physics_steps')
            return _original(sim, *args, **kwargs)
        setattr(MjSim, key, step)
    env = None
    try:
        cfg = json.loads((Path(robosuite.__file__).parent / 'controllers/config/robots/default_panda.json').read_text())
        env = PlacementView(robots='Panda', controller_configs=cfg, has_renderer=False,
                            has_offscreen_renderer=True, use_camera_obs=False, use_object_obs=False,
                            hard_reset=False, seed=PLAN['seed'], control_freq=20, horizon=20)
        env.reset()
        nut = env.nuts[0]
        body = env.obj_body_id[nut.name]
        env.sim.data.set_joint_qpos(nut.joints[0], np.array(PLAN['scene']['object_position'] + [1., 0., 0., 0.]))
        env.sim.data.set_joint_qvel(nut.joints[0], np.zeros(6))
        env.sim.forward()
        camera = PLAN['scene']['camera']
        rgb, raw_depth = env.sim.render(width=224, height=224, camera_name=camera, depth=True)
        seg = env.sim.render(width=224, height=224, camera_name=camera, segmentation=True)
        rgb = rgb[::-1].copy()
        depth = get_real_depth_map(env.sim, raw_depth[::-1].copy())
        seg = seg[::-1].copy()
        # Include visual and collision geoms in the nut's body subtree.
        descendants = {body}
        for _ in range(env.sim.model.nbody):
            descendants |= {i for i, parent in enumerate(env.sim.model.body_parentid) if parent in descendants}
        geom_ids = [i for i, b in enumerate(env.sim.model.geom_bodyid) if b in descendants]
        roi = (seg[..., 0] == int(mujoco.mjtObj.mjOBJ_GEOM)) & np.isin(seg[..., 1], geom_ids)
        if roi.sum() < PLAN['geometry']['minimum_roi_pixels']:
            raise RuntimeError('Nut not sufficiently visible; no ROI fallback or view search')
        if depth.shape != (224, 224) or not np.isfinite(depth).all() or depth.min() <= 0:
            raise RuntimeError('Invalid metric depth')
        K = get_camera_intrinsic_matrix(env.sim, camera, 224, 224)
        T = get_camera_extrinsic_matrix(env.sim, camera)
        world = env.sim.data.body_xpos[body]
        cam = np.linalg.solve(T, np.r_[world, 1.])
        if cam[2] <= 0: raise RuntimeError('Object behind optical camera')
        pixel_h = K @ cam[:3]
        uv = pixel_h[:2] / pixel_h[2]
        recovered = T @ np.r_[np.linalg.solve(K, np.r_[uv, 1.]) * cam[2], 1.]
        err = float(np.linalg.norm(recovered[:3] - world))
        if err > 1e-8: raise RuntimeError('Camera projection roundtrip failed')
        Image.fromarray(rgb).save(output / 'rgb.png')
        np.savez(output / 'scene_arrays.npz', depth_m=depth, roi=roi, K=K, T_world_camera_cv=T,
                 qpos=env.sim.data.qpos.copy(), qvel=env.sim.data.qvel.copy())
        write(output / 'scene.json', dict(status='RENDER_ONLY', camera=camera, roi_pixels=int(roi.sum()),
              roi_source='Evaluator-only MuJoCo geom IDs; mask is not a VLA input',
              projection_roundtrip_error=err, object_center_pixel=uv.tolist(), budgets_used=budget.used,
              image_sha256=sha(output / 'rgb.png'), arrays_sha256=sha(output / 'scene_arrays.npz'),
              scope='One script-positioned fixture. No settling, success evaluator, robot commands or task competence.'))
    finally:
        if env is not None: env.close()
        for key, original in originals.items(): setattr(MjSim, key, original)


def load_model(path, report):
    import torch
    from transformers import AutoConfig, AutoProcessor, PreTrainedModel
    from transformers.dynamic_module_utils import get_class_from_dynamic_module
    shared_probe.verify_model(path)
    config = AutoConfig.from_pretrained(path, trust_remote_code=True, local_files_only=True)
    cls = get_class_from_dynamic_module(config.auto_map['AutoModel'], str(path), local_files_only=True)
    loaded_file = Path(inspect.getfile(cls))
    if sha(loaded_file) != PLAN['loaded_model_sha256']:
        raise RuntimeError('Actual remote modeling module differs from inspected source')
    # Pinned custom from_pretrained assumes a model return, so output_loading_info
    # would break it. Invoke HF base loader, inspect all loading errors, then apply
    # the same spatial-token weight copy from that pinned override explicitly.
    model, info = PreTrainedModel.from_pretrained.__func__(
        cls, path, config=config, local_files_only=True, torch_dtype=torch.bfloat16,
        attn_implementation='eager', output_loading_info=True)
    report['loading_info'] = info
    if any(info.get(k) for k in ('missing_keys', 'unexpected_keys', 'mismatched_keys', 'error_msgs')):
        raise RuntimeError('Strict load mismatch; do not relax or replace checkpoint')
    with torch.no_grad():
        if config.use_spatial_token:
            model.language_model.model.embed_tokens.weight[-config.spatial_token_num:].copy_(model.spatial_embed_tokens.weight)
    processor = AutoProcessor.from_pretrained(path, trust_remote_code=True, local_files_only=True)
    if not config.use_vision_zoe or config.vision_config.patch_size != 14 or config.ego3d_patch_reso != 2:
        raise RuntimeError('Geometry contract changed')
    if processor.action_chunk_size != 4 or processor.num_obs_steps != 1:
        raise RuntimeError('Action/observation contract changed')
    model = model.eval().cuda()
    model.config.text_config._attn_implementation = 'eager'
    model.language_model.config._attn_implementation = 'eager'
    report.update(loaded_module_sha256=sha(loaded_file), model_revision=PLAN['model']['revision'],
                  gradient_boundary='Both upstream no-grad boundaries retained; no backward or training')
    return model, processor


def vla(output, budget, report):
    import numpy as np
    import torch
    from PIL import Image
    from transformers import GenerationConfig, LogitsProcessor
    torch.use_deterministic_algorithms(True)
    torch.backends.cudnn.benchmark = False
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    observed = json.loads((output / 'scene.json').read_text())
    if sha(output / 'rgb.png') != observed['image_sha256'] or sha(output / 'scene_arrays.npz') != observed['arrays_sha256']:
        raise RuntimeError('Scene changed between stages')
    budget.used['physics_steps'] = observed['budgets_used']['physics_steps']
    if budget.used['physics_steps'] > PLAN['budgets']['physics_steps']:
        raise RuntimeError('Scene exhausted global physics budget')
    arrays = np.load(output / 'scene_arrays.npz', allow_pickle=False)
    image = Image.open(output / 'rgb.png').convert('RGB')
    K = torch.tensor(arrays['K'], dtype=torch.float32, device='cuda')
    gt = torch.tensor(arrays['depth_m'], dtype=torch.float32, device='cuda')[None, None]
    roi = torch.tensor(arrays['roi'], dtype=torch.bool, device='cuda')[None, None]
    roi_grid = pooled(roi.float())[:, 0] > 0
    path = Path(Path('/cache/model_path.txt').read_text().strip())
    model, processor = load_model(path, report)
    gt_xyz = xyz_grid(K, gt, model.uv_h)
    report['camera_ray_numeric_contract'] = dict(
        uv_dtype=str(model.uv_h.dtype), K_dtype=str(K.dtype),
        gt_xyz_nominal_vs_loaded_max_m=float((gt_xyz-xyz_grid(K, gt)).abs().max()),
        scope='Preserve loaded ray buffer; report quantization separately, never silently fix upstream')
    tok = processor.action_tokenizer
    ranges = [(x.token_start_idx, x.token_end_idx) for x in
              (tok.translation_tokenizer, tok.rotation_tokenizer, tok.gripper_tokenizer)]
    records = []
    report['conditions'] = records

    class Counter(LogitsProcessor):
        def __init__(self, length): self.length = length
        def __call__(self, input_ids, scores):
            if not 0 <= input_ids.shape[1] - self.length < 12:
                raise RuntimeError('Unexpected autoregressive step')
            budget.take('model_steps')
            return scores  # No family forcing: do not turn invalid output into evidence.

    for index, instruction in enumerate(PLAN['instructions']):
        inputs = processor(images=[image], text=instruction, return_tensors='pt', do_normalize=False)
        inputs = {k: v.to(device='cuda', dtype=torch.bfloat16 if v.is_floating_point() else v.dtype) for k, v in inputs.items()}
        inputs['intrinsic'] = K  # Native float32 camera K, no dataset fallback.
        if inputs['pixel_values'].shape != (1, 3, 224, 224): raise RuntimeError('RGB shape changed')
        length = inputs['input_ids'].shape[1]
        ref, baseline_ids, baseline_logits, baseline_feature, baseline_xyz = None, None, None, None, None
        for mode in PLAN['conditions']:
            budget.take('queries')
            torch.manual_seed(PLAN['seed'] + index)
            cfg = GenerationConfig.from_dict(model.generation_config.to_dict())
            cfg.update(max_new_tokens=12, min_new_tokens=12, do_sample=False, eos_token_id=[],
                       forced_eos_token_id=None, use_cache=True, return_dict_in_generate=True,
                       output_logits=True, output_scores=False, output_hidden_states=False)
            start = time.monotonic()
            cache = getattr(model, '_cache', None)
            if cache is not None:
                if not hasattr(cache, 'reset'): raise RuntimeError('Cannot reset existing generation cache')
                cache.reset()
            with torch.inference_mode(), DepthOverride(model, mode, roi, PLAN['geometry']['roi_bias_m'], ref) as hook:
                # A fresh cache is allocated per call; never pass past_key_values.
                result = model.generate(**inputs, generation_config=cfg, logits_processor=[Counter(length)])
            capture = hook.captured
            ids = result.sequences[0, length:].cpu().tolist()
            if len(result.logits) != 12 or len(ids) != 12:
                raise RuntimeError('Unexpected token count')
            first_logits = result.logits[0][0].detach().float().cpu()
            if not torch.isfinite(first_logits).all(): raise RuntimeError('Nonfinite logits')
            feature = capture['projected_features']
            depth, xyz = capture['depth'], capture['xyz']
            if not torch.isfinite(feature).all(): raise RuntimeError('Nonfinite projected feature')
            check_xyz = xyz_grid(K, depth, model.uv_h)
            xyz_error = float((xyz - check_xyz).abs().max())
            if xyz_error > PLAN['geometry']['backproject_atol_m']:
                raise RuntimeError('Loaded backprojection differs from independent camera contract')
            if mode == 'original':
                ref, baseline_ids, baseline_logits = depth.clone(), ids, first_logits
                baseline_feature, baseline_xyz = feature.clone(), xyz.clone()
            valid = shared_probe.valid_tokens(ids, ranges)
            entry = dict(instruction=index, condition=mode, token_ids=ids, valid_action_tokens=valid,
                         e_inj_xyz_m=rms_xyz(xyz, baseline_xyz), e_gt_xyz_m=rms_xyz(xyz, gt_xyz),
                         e_gt_roi_xyz_m=rms_xyz(xyz, gt_xyz, roi_grid),
                         depth_change_rms_m=float((depth.float()-ref.float()).square().mean().sqrt()),
                         gt_depth_rmse_m=float((depth.float()-gt).square().mean().sqrt()),
                         pooled_depth_change_max_m=float((pooled(depth).float()-pooled(ref).float()).abs().max()),
                         feature_change_max=float((feature-baseline_feature).abs().max()),
                         first_logit_change_max=float((first_logits-baseline_logits).abs().max()),
                         same_generated_tokens=ids == baseline_ids, coordinate_check_max_m=xyz_error,
                         depth_dtype=str(depth.dtype), depth_hook_calls=hook.calls, projector_calls=hook.feature_calls,
                         elapsed_seconds=time.monotonic()-start,
                         decode_status='NORMALIZED_ONLY' if valid else 'INVALID_NO_DECODE', physical_commands=0)
            if valid:
                decoded = tok.decode_token_ids_to_actions(np.asarray(ids).reshape(4, 3))
                if decoded.shape != (4, 7) or not np.isfinite(decoded).all(): raise RuntimeError('Invalid normalized decode')
                entry['normalized_actions'] = decoded.tolist()
            records.append(entry)
            np.savez_compressed(output / (str(index)+'_'+mode+'.npz'), depth=depth.float().cpu().numpy(),
                                xyz=xyz.float().cpu().numpy(), features=feature.numpy(), first_logits=first_logits.numpy())
            report['budgets_used'] = budget.used
            write(output / 'vla.json', report)
            if mode == 'identity' and (entry['depth_change_rms_m'] > PLAN['geometry']['identity_depth_atol_m']
                    or entry['e_inj_xyz_m'] > PLAN['geometry']['identity_xyz_atol_m']
                    or entry['feature_change_max'] > PLAN['geometry']['identity_feature_atol'] or not entry['same_generated_tokens']
                    or entry['first_logit_change_max'] > PLAN['geometry']['identity_logit_atol']):
                raise RuntimeError('Identity mismatch; stop before interpreting perturbations')
            if mode == 'roi_bias' and entry['e_inj_xyz_m'] <= 0:
                raise RuntimeError('ROI perturbation vanished before policy geometry')
            if mode == 'subpatch_permutation' and entry['e_inj_xyz_m'] > PLAN['geometry']['null_xyz_atol_m']:
                raise RuntimeError('Supposed nullspace change survived pooling; inspect dtype/aggregation')
            del result, hook, capture
    report.update(status='P0_INPUT_PATH_QUALIFIED', action_io_status='VALID' if all(x['valid_action_tokens'] for x in records) else 'INVALID_TOKEN_OUTPUTS_PRESENT',
                  peak_cuda_bytes=torch.cuda.max_memory_allocated(),
                  nullspace_note='Feature/logit sensitivity includes measured floating-point residual; not exact-zero proof',
                  research_effect='NOT_MEASURED', task_success='NOT_MEASURED', normalizer='UNAVAILABLE', training=False)
    write(output / 'vla.json', report)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('environment', 'fetch', 'scene', 'vla'))
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if args.mode == 'environment': shared_probe.environment(args.output); return
    if args.mode == 'fetch': shared_probe.fetch(args.output); return
    import numpy as np
    random.seed(PLAN['seed']); np.random.seed(PLAN['seed'])
    budget = Budget(PLAN)
    report = dict(status='STARTED', stage=args.mode, claim_boundary=PLAN['claim_boundary'])
    try:
        if args.mode == 'scene': scene(args.output, budget)
        else: vla(args.output, budget, report)
        report['status'] = 'P0_STAGE_PASSED'
    except Exception as exc:
        report.update(status='FAILED', error=type(exc).__name__ + ': ' + str(exc))
        raise
    finally:
        report.update(budgets_used=budget.used, unimplemented=PLAN['unimplemented'])
        write(args.output / (args.mode + '_result.json'), report)


if __name__ == '__main__':
    main()
