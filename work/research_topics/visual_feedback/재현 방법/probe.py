#!/usr/bin/env python3
"""Bounded Docker-only IO diagnostic; no training or full-task evaluation."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import time
import urllib.request
import zipfile

HERE = Path(__file__).resolve().parent
CACHE = Path('/cache')
SOURCE = Path('/opt/feedback/RL4VLA')


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with Path(path).open('rb') as f:
        if algorithm == 'sha1':
            h.update(f'blob {Path(path).stat().st_size}\0'.encode())
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


class Budget:
    """Charge attempted operations before invoking native code, including failures."""
    def __init__(self, caps):
        self.caps = dict(caps)
        self.used = dict.fromkeys(caps, 0)

    def charge(self, key):
        require(key in self.caps, f'Unknown cost unit: {key}')
        require(self.used[key] < self.caps[key], f'Budget exhausted: {key}')
        self.used[key] += 1


class EvaluationCache:
    """One evaluation per control step; protects teleport AND grasp counters."""
    def __init__(self):
        self.step = None
        self.value = None

    def get(self, step, evaluate):
        if step != self.step:
            value = evaluate()  # Failed evaluations are not cached or retried by this probe.
            self.value = copy.deepcopy(value)
            self.step = step
        return copy.deepcopy(self.value)


def verify_file(path, spec):
    require(Path(path).is_file(), f'Missing file: {path}')
    require(Path(path).stat().st_size == spec['size'], f'Size mismatch: {path}')
    require(digest(path, spec['hash_algorithm']) == spec['hash'], f'Checksum mismatch: {path}')


def fetch_file(url, destination, spec):
    destination = Path(destination)
    if destination.exists():
        verify_file(destination, spec)
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_name(destination.name + '.partial')
    require(not partial.exists(), f'Partial download exists; inspect before a manual retry: {partial}')
    # No automatic retry and no unbounded response accepted.
    with urllib.request.urlopen(url, timeout=60) as response, partial.open('xb') as output:
        count = 0
        while chunk := response.read(8 * 1024 * 1024):
            count += len(chunk)
            require(count <= spec['size'], 'Remote file exceeded pinned size')
            output.write(chunk)
    verify_file(partial, spec)
    partial.rename(destination)


def safe_extract(archive, target):
    target = Path(target)
    require(not target.exists(), f'Asset destination already exists without ready manifest: {target}')
    with zipfile.ZipFile(archive) as z:
        members = [x for x in z.infolist() if not x.is_dir()]
        names = [Path(x.filename) for x in members]
        require(all(not p.is_absolute() and '..' not in p.parts for p in names), 'Unsafe zip member')
        require(all((x.external_attr >> 16) & 0o170000 != 0o120000 for x in members), 'Zip symlink unsupported')
        roots = {p.parts[0] for p in names}
        strip = len(roots) == 1 and all(len(p.parts) > 1 for p in names)
        for member, name in zip(members, names):
            dest = target.joinpath(*(name.parts[1:] if strip else name.parts))
            dest.parent.mkdir(parents=True, exist_ok=True)
            with z.open(member) as src, dest.open('xb') as dst:
                while block := src.read(1024 * 1024):
                    dst.write(block)


def tree_hashes(path):
    return {str(p.relative_to(path)): digest(p) for p in sorted(Path(path).rglob('*'))
            if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}


def runtime():
    require(Path('/.dockerenv').is_file(), 'All dependency/model/simulator work must run in Docker')
    import torch
    require(torch.cuda.is_available(), 'Container CUDA allocation unavailable')
    require(torch.version.cuda == '12.1', 'Expected torch CUDA 12.1')
    require(torch.cuda.is_bf16_supported(), 'Native BF16 GPU required')
    v = subprocess.run(['vulkaninfo', '--summary'], capture_output=True, text=True, timeout=30)
    require(v.returncode == 0 and 'NVIDIA' in v.stdout, 'NVIDIA Vulkan enumeration failed')
    return {'torch': torch.__version__, 'cuda': torch.version.cuda,
            'gpu': torch.cuda.get_device_name(0), 'gpu_total_bytes': torch.cuda.get_device_properties(0).total_memory,
            'vulkan_enumerated': True, 'rendering_verified': False, 'vulkan_summary': v.stdout}


def prepare(plan, out):
    env = runtime()
    cp = plan['sources']['checkpoint']
    model_dir = CACHE / 'model' / cp['revision']
    for item in cp['files']:
        fetch_file(f"https://huggingface.co/{cp['repo']}/resolve/{cp['revision']}/{item['path']}",
                   model_dir / item['path'], item)
    asset = plan['sources']['bridge_asset']
    archive = CACHE / 'downloads' / 'bridge.zip'
    fetch_file(asset['url'], archive, asset)
    asset_dir = CACHE / 'assets/data/tasks/bridge_v2_real2sim_dataset'
    ready_path = CACHE / 'ready.json'
    if not ready_path.exists():
        safe_extract(archive, asset_dir)
    robot = CACHE / 'assets/data/robots/widowx'
    robot.parent.mkdir(parents=True, exist_ok=True)
    if not robot.exists():
        robot.symlink_to('/opt/feedback/widowx', target_is_directory=True)
    require((asset_dir / 'stages/bridge_table_1_v1.glb').is_file(), 'Bridge scene missing')
    require((robot / 'wx250s.urdf').is_file(), 'WidowX URDF missing')
    # Git checkout contains task-specific carrot/plate/table assets, distinct from Bridge assets.
    carrot = SOURCE / 'ManiSkill/mani_skill/assets/carrot'
    for name in ['more_carrot', 'more_plate', 'more_table']:
        require((carrot / name / 'model_db.json').is_file(), f'Missing task assets: {name}')
    record = {'packet_sha': os.environ['FEEDBACK_PACKET_SHA'], 'checkpoint_revision': cp['revision'],
              'model_files': {i['path']: digest(model_dir / i['path']) for i in cp['files']},
              'bridge_files': tree_hashes(asset_dir), 'robot_files': tree_hashes(robot),
              'task_files': tree_hashes(carrot), 'runtime': env,
              'scope': 'Payload checksums and CUDA/Vulkan enumeration; native scene/policy unverified'}
    if ready_path.exists():
        prior = json.loads(ready_path.read_text())
        for key in ['packet_sha', 'checkpoint_revision', 'model_files', 'bridge_files', 'robot_files', 'task_files']:
            require(prior[key] == record[key], f'Prepared cache drift: {key}')
    else:
        ready_path.write_text(json.dumps(record, indent=2))
    (out / 'prepare.json').write_text(json.dumps(record, indent=2))


def serial(value):
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    if hasattr(value, 'detach'):
        return value.detach().cpu().tolist()
    if hasattr(value, 'tolist'):
        return value.tolist()
    return value


def snapshot(env):
    # Deliberately no get_info/evaluate: observation must not advance task state.
    return serial({'physics': env.get_state_dict(), 'elapsed_steps': env.elapsed_steps,
                   'controller': env.agent.controller.get_state(),
                   'selection': {k: getattr(env, k) for k in ['select_carrot_ids', 'select_plate_ids',
                                 'select_overlay_ids', 'select_pos_ids', 'select_quat_ids']},
                   'event_applied': env.event_applied, 'episode_stats': env.episode_stats,
                   'consecutive_grasp': env.consecutive_grasp})


def p0(plan, out, report):
    import torch
    import numpy as np
    from PIL import Image
    from unittest.mock import patch
    from transformers import AutoTokenizer
    from feedback_hf.configuration_prismatic import OpenVLAConfig
    from feedback_hf.modeling_prismatic import OpenVLAForActionPredictionWithValueHead
    from feedback_hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
    from mani_skill.envs.scene import ManiSkillScene
    from mani_skill.envs.tasks.digital_twins.bridge_dataset_eval.put_on_in_scene_multi import PutOnPlateInScene25PositionChange
    from simpler_env.env.simpler_wrapper import SimlerWrapper

    report['runtime'] = runtime()
    ready = json.loads((CACHE / 'ready.json').read_text())
    require(ready['packet_sha'] == os.environ['FEEDBACK_PACKET_SHA'], 'Stale prepared cache')
    cp = plan['sources']['checkpoint']
    model_dir = CACHE / 'model' / cp['revision']
    for item in cp['files']:
        verify_file(model_dir / item['path'], item)
    for key, path in [('bridge_files', CACHE / 'assets/data/tasks/bridge_v2_real2sim_dataset'),
                      ('robot_files', Path('/opt/feedback/widowx')),
                      ('task_files', SOURCE / 'ManiSkill/mani_skill/assets/carrot')]:
        require(ready[key] == tree_hashes(path), f'Asset drift: {key}')
    contract = plan['contract']
    budget = Budget(contract['caps'])
    report['budget_used'] = budget.used
    torch.manual_seed(contract['seed'])
    np.random.seed(contract['seed'])
    random.seed(contract['seed'])
    torch.backends.cuda.matmul.allow_tf32 = False

    class ProbeEnv(PutOnPlateInScene25PositionChange):
        def reset(self, seed=None, options=None):
            budget.charge('resets')
            self.event_applied = False
            self.evaluation_cache = EvaluationCache()
            opts = dict(options or {})
            opts.update(obj_set='test', episode_id=torch.tensor([contract['episode_id']], device=self.device))
            return super().reset(seed=[contract['seed']], options=opts)

        def evaluate(self, success_require_src_completely_on_target=True):
            step = int(self.elapsed_steps[0].item())

            def once():
                if self.can_change_position and step == 5:
                    require(not self.event_applied, 'Duplicate physical intervention')
                    budget.charge('events')
                    self.event_applied = True
                return super(ProbeEnv, self).evaluate(success_require_src_completely_on_target)

            return self.evaluation_cache.get(step, once)

        def step(self, action):
            budget.charge('control_steps')
            return super().step(action)

    original_step = ManiSkillScene.step

    def counted_physics(scene, *args, **kwargs):
        budget.charge('physics_steps')
        return original_step(scene, *args, **kwargs)

    env = None
    try:
        with patch.object(ManiSkillScene, 'step', counted_physics):
            # Direct environment construction avoids an extra reset in SimlerWrapper.
            env = ProbeEnv(num_envs=1, obs_mode='rgb+segmentation', sim_backend='gpu',
                           control_mode=contract['control_mode'], sim_config={'sim_freq': 500, 'control_freq': 5},
                           sensor_configs={'shader_pack': 'default'})
            obs, _ = env.reset()
            instruction = env.get_language_instruction()
            require(len(instruction) == 1 and isinstance(instruction[0], str), 'Instruction batch mismatch')
            neutral = torch.tensor([contract['neutral_command']], device=env.device, dtype=torch.float32)
            pre = None
            for step in range(1, 6):
                obs, _, terminated, truncated, _ = env.step(neutral)
                require(not bool(terminated.any() or truncated.any()), 'Fixture unexpectedly terminal')
                require(int(env.elapsed_steps[0]) == step, 'Control timestamp mismatch')
                if step == 4:
                    pre = obs['sensor_data']['3rd_view_camera']['rgb'].clone().to(torch.uint8)
                    report['pre_event_state'] = snapshot(env)
                    selected_name = env.carrot_names[int(env.select_carrot_ids[0])]
                    pre_object_position = env.objs_carrot[selected_name].pose.p.clone()
            fresh = obs['sensor_data']['3rd_view_camera']['rgb'].clone().to(torch.uint8)
            require(pre.shape == fresh.shape == (1, 480, 640, 3), 'Unexpected native RGB shape')
            require(budget.used['events'] == 1, 'Missing physical intervention')
            post_object_position = env.objs_carrot[selected_name].pose.p.clone()
            displacement = float(torch.linalg.vector_norm(post_object_position - pre_object_position))
            require(displacement > 0.1, 'Selected object did not move as required by the fixture')
            report['event'] = {'selected_object': selected_name, 'displacement_metres': displacement,
                               'pre_position': serial(pre_object_position), 'post_position': serial(post_object_position)}
            state = snapshot(env)
            cost_before = dict(budget.used)
            env.evaluate()  # Verify observer re-entry does not repeat the teleport or grasp counters.
            require(state == snapshot(env) and cost_before == budget.used, 'Evaluation re-entry mutated state')
            report['post_event_state'] = state
            report['selection'] = state['selection']
            report['instruction'] = instruction
            for name, rgb in [('pre_step4', pre), ('post_step5', fresh)]:
                pixels = rgb[0].cpu().numpy()
                Image.fromarray(pixels).save(out / (name + '.png'))
                report.setdefault('rgb', {})[name] = {'sha256': hashlib.sha256(pixels.tobytes()).hexdigest(),
                                                      'shape': list(pixels.shape)}
            require(report['rgb']['pre_step4']['sha256'] != report['rgb']['post_step5']['sha256'],
                    'No RGB difference observed; fixture qualification incomplete')
            report['runtime']['rendering_verified'] = True
            config = OpenVLAConfig.from_pretrained(model_dir, local_files_only=True)
            model, loading = OpenVLAForActionPredictionWithValueHead.from_pretrained(
                model_dir, config=config, vh_mode='a0', attn_implementation='eager',
                torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, local_files_only=True,
                output_loading_info=True)
            # Published action checkpoint has no critic weights; this unused head may be initialized.
            require(all(k.startswith('value_head.') for k in loading['missing_keys']), 'Missing actor weights')
            require(not loading['unexpected_keys'] and not loading.get('mismatched_keys'), 'Actor load mismatch')
            model = model.to('cuda:0').eval()
            model.requires_grad_(False)
            report['loading'] = loading
            tok = AutoTokenizer.from_pretrained(model_dir, local_files_only=True, trust_remote_code=False,
                                                padding_side='left')
            processor = PrismaticProcessor(PrismaticImageProcessor.from_pretrained(model_dir, local_files_only=True), tok)
            normalizer = model.get_action_stats(cp['normalizer_key'])
            require(all(normalizer[k] == v for k, v in cp['normalizer_stats'].items()), 'Pinned normalizer drift')
            converter = object.__new__(SimlerWrapper)
            converter.unnorm_state = normalizer
            bins = np.linspace(-1, 1, 256)
            converter.bin_centers = (bins[:-1] + bins[1:]) / 2
            results = []
            for name, rgb in [('stale_step4', pre), ('fresh_step5', fresh), ('repeat_fresh_step5', fresh)]:
                budget.charge('queries')
                prompt = [f'In: What action should the robot take to {instruction[0].lower()}?\nOut: ']
                inputs = processor(prompt, rgb.permute(0, 3, 1, 2).to('cuda:0', dtype=torch.bfloat16), padding=True)
                inputs = inputs.to('cuda:0', dtype=torch.bfloat16)
                started = time.monotonic()
                with torch.inference_mode():
                    _, tokens, _ = model.predict_action_batch(**inputs, unnorm_key=cp['normalizer_key'],
                                                               do_sample=False)
                torch.cuda.synchronize()
                require(tuple(tokens.shape) == (1, 7), 'Unexpected action-token shape')
                command = converter._process_action(tokens)
                require(bool(torch.isfinite(command).all()), 'Non-finite controller command')
                results.append({'input': name, 'tokens': serial(tokens), 'command': serial(command),
                                'elapsed_seconds': time.monotonic() - started})
                require(snapshot(env) == state, 'Inference unexpectedly advanced simulator state')
            report['queries'] = results
            require(results[1]['tokens'] == results[2]['tokens'], 'Greedy repeated query was not reproducible')
            report['repeat_fresh_tokens_equal'] = True
            report['fresh_minus_stale_command'] = (np.array(results[1]['command']) - np.array(results[0]['command'])).tolist()
            # Only fresh action is executed; this is not a stale/fresh success-rate comparison.
            env.step(torch.tensor(results[1]['command'], device=env.device, dtype=torch.float32))
            require(int(env.elapsed_steps[0]) == 6, 'Final action did not produce one control step')
            report['final_state'] = snapshot(env)
            report['status'] = 'IO_QUALIFIED_NOT_RESEARCH_EFFECT'
            report['full_state_restore_verified'] = False
    finally:
        if env is not None:
            env.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['prepare', 'p0'])
    parser.add_argument('--output', type=Path, default=Path('/results'))
    args = parser.parse_args()
    require(Path('/.dockerenv').exists(), 'Docker required')
    require(os.environ.get('FEEDBACK_PACKET_SHA'), 'Packet identity required')
    plan = json.loads((HERE / 'RESUME_PLAN.json').read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'phase': args.phase, 'status': 'STARTED', 'research_effect_measured': False,
              'packet_sha': os.environ['FEEDBACK_PACKET_SHA']}
    destination = args.output / (args.phase + '_result.json')
    require(not destination.exists(), 'Results are append-only; choose a new output directory')
    try:
        for name in ['resolved-packages.txt', 'resolved-system-packages.txt']:
            shutil.copyfile(Path('/opt/feedback') / name, args.output / name)
        if args.phase == 'prepare':
            prepare(plan, args.output)
            report['status'] = 'PAYLOAD_PREPARED_NATIVE_UNVERIFIED'
        else:
            p0(plan, args.output, report)
    except Exception as exc:
        report.update(status='FAILED_NO_RESEARCH_CONCLUSION', error=f'{type(exc).__name__}: {exc}')
        raise
    finally:
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
