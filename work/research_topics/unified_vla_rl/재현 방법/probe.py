#!/usr/bin/env python3
"""Bounded Docker-only IO and autograd wiring probe; no scientific effect estimate."""
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
SOURCE = Path('/opt/unified/RL4VLA')


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
    verify_sources(plan)
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
        robot.symlink_to('/opt/unified/widowx', target_is_directory=True)
    require((asset_dir / 'stages/bridge_table_1_v1.glb').is_file(), 'Bridge scene missing')
    require((robot / 'wx250s.urdf').is_file(), 'WidowX URDF missing')
    # Git checkout contains task-specific carrot/plate/table assets, distinct from Bridge assets.
    carrot = SOURCE / 'ManiSkill/mani_skill/assets/carrot'
    for name in ['more_carrot', 'more_plate', 'more_table']:
        require((carrot / name / 'model_db.json').is_file(), f'Missing task assets: {name}')
    record = {'packet_sha': os.environ['UNIFIED_PACKET_SHA'], 'checkpoint_revision': cp['revision'],
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


# This packet deliberately avoids importing the upstream RLDS/trainer stack.
def verify_sources(plan):
    rev = subprocess.check_output(['git', '-C', str(SOURCE), 'rev-parse', 'HEAD'], text=True).strip()
    require(rev == plan['sources']['rl4vla_revision'], 'Source revision drift')
    for path, expected in plan['sources']['code_files'].items():
        require(digest(SOURCE / path) == expected, f'Source bytes drift: {path}')


def verify_ready(plan):
    ready = json.loads((CACHE / 'ready.json').read_text())
    require(ready['packet_sha'] == os.environ['UNIFIED_PACKET_SHA'], 'Stale prepared cache')
    model_dir = CACHE / 'model' / plan['sources']['checkpoint']['revision']
    for f in plan['sources']['checkpoint']['files']:
        verify_file(model_dir / f['path'], f)
    for key, path in [('bridge_files', CACHE / 'assets/data/tasks/bridge_v2_real2sim_dataset'),
                      ('robot_files', Path('/opt/unified/widowx')),
                      ('task_files', SOURCE / 'ManiSkill/mani_skill/assets/carrot')]:
        require(ready[key] == tree_hashes(path), f'Asset drift: {key}')
    verify_sources(plan)
    return model_dir


class ValueRouting:
    """One pre-hook on the value head, never on the actor/backbone."""
    def __init__(self, head, detached):
        self.head, self.detached, self.handle = head, detached, None

    def __enter__(self):
        if self.detached:
            self.handle = self.head.register_forward_pre_hook(self.cut)
        return self

    @staticmethod
    def cut(module, args):
        require(len(args) == 1, 'Value head signature changed')
        return (args[0].detach(),)

    def __exit__(self, *args):
        if self.handle:
            self.handle.remove()


def grasp_label(target, other):
    return 'ambiguous' if target and other else 'correct' if target else 'wrong' if other else 'none'


def physical_snapshot(env):
    # Do not call evaluate/get_info: those mutate the task counters.
    import pickle
    rng = {k: getattr(env, k) for k in ['_main_rng', '_episode_rng', '_batched_main_rng', '_batched_episode_rng']}
    return serial({'physics': env.get_state_dict(), 'controller': env.agent.controller.get_state(),
                   'elapsed_steps': env.elapsed_steps,
                   'overlay': {'ids': env.select_overlay_ids, 'images_sha256': hashlib.sha256(env.overlay_images.cpu().numpy().tobytes()).hexdigest(),
                               'textures_sha256': hashlib.sha256(env.overlay_textures.cpu().numpy().tobytes()).hexdigest(), 'mix': env.overlay_mix},
                   'environment_rng_sha256': hashlib.sha256(pickle.dumps(rng)).hexdigest()})


class GoalBinding:
    """Reset-only goal binding for two visible actors. Not a full-state rollout fork."""
    def __init__(self, env, task):
        import torch
        self.env, self.task = env, task
        self.ids = [env.carrot_names.index(task[k]) for k in ['source_object', 'alternate_object']]
        require(int(env.select_carrot_ids[0]) == self.ids[0] and int(env.select_extra_ids[0]) == self.ids[1],
                'Native episode did not instantiate the declared pair')
        require(env.plate_names[int(env.select_plate_ids[0])] == task['receptacle'], 'Receptacle mismatch')
        self.reward_old = torch.zeros((1, 1), device=env.device, dtype=torch.float32)

    def bind(self, goal):
        import torch
        from mani_skill.utils.geometry import rotation_conversions
        require(goal in (0, 1), 'Unknown goal')
        env = self.env
        require(int(env.elapsed_steps[0]) == 0, 'P0 binding only supports the reset state')
        before = physical_snapshot(env)
        selected, other = self.ids[goal], self.ids[1 - goal]
        name = env.carrot_names[selected]
        env.select_carrot_ids = torch.tensor([selected], device=env.device)
        env.select_extra_ids = torch.tensor([other], device=env.device)
        env.source_obj_name = name
        env.target_obj_name = self.task['receptacle']
        env.objs = {name: env.objs_carrot[name], env.target_obj_name: env.objs_plate[env.target_obj_name]}
        q = env.objs_carrot[name].pose.q.clone()
        env.carrot_q_after_settle = q
        signs = torch.tensor([[x, y, z] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]],
                             device=env.device, dtype=q.dtype)
        half = env.model_bbox_sizes[name].reshape(1, 1, 3) / 2
        corners = (half * signs[None]) @ rotation_conversions.quaternion_to_matrix(q).transpose(1, 2)
        env.carrot_bbox_world = corners.max(dim=1).values - corners.min(dim=1).values
        env.consecutive_grasp.zero_()
        for value in env.episode_stats.values():
            value.zero_()
        env.extra_stats.clear()
        env.evaluation_cache = EvaluationCache()
        self.reward_old.zero_()  # P0 has no reward/rollout; any future wrapper must bind this state explicitly.
        require(physical_snapshot(env) == before, 'Goal binding changed physical/controller/overlay/RNG state')
        instruction = env.get_language_instruction()[0]
        require(instruction == self.task['instructions'][goal], 'Language/target binding mismatch')
        return instruction

    def observe(self, goal):
        env = self.env
        # No evaluate(), score accumulation or hidden stepping.
        a = bool(env.agent.is_grasping(env.objs_carrot[env.carrot_names[self.ids[goal]]])[0])
        b = bool(env.agent.is_grasping(env.objs_carrot[env.carrot_names[self.ids[1 - goal]]])[0])
        return {'goal': goal, 'target_grasped': a, 'other_grasped': b, 'label': grasp_label(a, b)}


def load_policy(plan, model_dir, report):
    import torch
    from peft import LoraConfig, get_peft_model
    from transformers import AutoTokenizer
    from unified_hf.configuration_prismatic import OpenVLAConfig
    from unified_hf.modeling_prismatic import OpenVLAForActionPredictionWithValueHead
    from unified_hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
    config = OpenVLAConfig.from_pretrained(model_dir, local_files_only=True)
    model, loading = OpenVLAForActionPredictionWithValueHead.from_pretrained(
        model_dir, config=config, vh_mode='a0', attn_implementation='flash_attention_2',
        torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, local_files_only=True,
        output_loading_info=True)
    require(all(k.startswith('value_head.') for k in loading['missing_keys']), 'Missing actor weights')
    require(not loading['unexpected_keys'] and not loading.get('mismatched_keys'), 'Actor load mismatch')
    model = model.to('cuda:0')
    cfg = plan['design']['lora']
    model = get_peft_model(model, LoraConfig(r=cfg['r'], lora_alpha=cfg['alpha'],
                        lora_dropout=cfg['dropout'], target_modules=cfg['targets'], init_lora_weights=cfg['init']))
    base = model.get_base_model()
    base.value_head.requires_grad_(True)
    named = {n: p for n, p in model.named_parameters() if p.requires_grad}
    require(named and all('lora_' in n or 'value_head' in n for n in named), 'Unexpected trainable parameter')
    require(any('value_head' in n for n in named) and any('lora_' in n for n in named), 'Missing trainable group')
    report['loader'] = loading
    report['trainable_parameters'] = [{'name': n, 'shape': list(p.shape), 'dtype': str(p.dtype), 'count': p.numel()}
                                      for n, p in named.items()]
    report['lora_modules'] = [n for n, m in model.named_modules() if hasattr(m, 'lora_A')]
    model.eval()  # Gradients remain enabled; deterministic wiring fixture, not a training recipe claim.
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True, trust_remote_code=False, padding_side='left')
    processor = PrismaticProcessor(PrismaticImageProcessor.from_pretrained(model_dir, local_files_only=True), tokenizer)
    stats = config.norm_stats
    ds = json.loads((model_dir / 'dataset_statistics.json').read_text())
    require(stats['bridge_orig']['action'] == stats['warmup']['action'] == ds['warmup']['action'], 'Normalizer disagreement')
    return model, base, processor, tokenizer, named


def policy_input(processor, rgb, instruction, cap, action_text=None):
    import torch
    suffix = '' if action_text is None else action_text + '</s>'
    prompt = [f'In: What action should the robot take to {instruction.lower()}?\nOut: {suffix}']
    inputs = processor(prompt, rgb.permute(0, 3, 1, 2).to('cuda:0', dtype=torch.bfloat16), padding=True)
    inputs = inputs.to('cuda:0', dtype=torch.bfloat16)
    require(inputs['input_ids'].shape[1] <= cap, 'Prompt exceeded fixed input cap')
    if action_text is not None:
        inputs['labels'] = inputs['input_ids'].clone()
    return inputs


def gradient_summary(named):
    import torch
    result = {}
    for group in ['shared', 'head']:
        values = [p.grad for n, p in named.items() if ('value_head' in n) == (group == 'head') and p.grad is not None]
        require(all(bool(torch.isfinite(g).all()) for g in values), 'Nonfinite gradient')
        result[group] = sum(float(g.float().square().sum()) for g in values) ** 0.5
    return result


def clipped_value_loss(value, old, target):
    import torch
    def huber(error):
        return torch.where(error.abs() <= 10, error.square() / 2, 10 * (error.abs() - 5))
    clipped = old + (value - old).clamp(-0.2, 0.2)
    return torch.maximum(huber(target - value), huber(target - clipped)).mean()


def gradient_probe(plan, model, base, named, inputs, budget, report):
    import torch
    initial = {n: p.detach().cpu().clone() for n, p in named.items()}
    shared = [p for n, p in named.items() if 'value_head' not in n]
    head = [p for n, p in named.items() if 'value_head' in n]
    baseline = None
    old_logprob = old_value = target = None
    report['gradient_checks'] = []
    report['fixture'] = {'targets': 'Artificial old-value + 1 and advantage +1; NOT collected rewards/returns',
                         'mode': 'eval with autograd enabled', 'same_action_and_instruction': True}

    def restore():
        model.zero_grad(set_to_none=True)
        with torch.no_grad():
            for n, p in named.items():
                p.copy_(initial[n].to(p.device))

    def forward(detached):
        budget.charge('teacher_forwards')
        captured = []
        action_len = 7
        handle = base.language_model.lm_head.register_forward_hook(
            lambda m, a, out: captured.append(out[:, -action_len-2:-2, 32000-256:32000].detach().float().cpu()))
        try:
            with ValueRouting(base.value_head, detached), torch.autocast('cuda', dtype=torch.bfloat16):
                lp, ent, value = base.evaluate_action(**inputs, unnorm_key='bridge_orig')
        finally:
            handle.remove()
        require(len(captured) == 1, 'Action logits capture mismatch')
        return lp.float(), value.float(), captured[0]

    # Four independent graph checks, then three disposable matched optimizer steps.
    for name, detached, loss_kind in [('A_policy', False, 'policy'), ('A_value', False, 'value'),
                                     ('B_value', True, 'value'), ('B_policy', True, 'policy')]:
        restore()
        lp, value, logits = forward(detached)
        if baseline is None:
            baseline = (lp.detach().cpu(), value.detach().cpu(), logits)
            old_logprob, old_value = lp.detach(), value.detach()
            target = old_value + plan['contract']['fixture_return_offset']
            require(bool(torch.isfinite(target).all()), 'Nonfinite fixture target')
        for a, b in zip((lp.detach().cpu(), value.detach().cpu(), logits), baseline):
            require(torch.allclose(a, b, atol=plan['contract']['forward_atol'],
                                   rtol=plan['contract']['forward_rtol']), 'A/B initial forward mismatch')
        loss = -lp.mean() if loss_kind == 'policy' else clipped_value_loss(value, old_value, target)
        budget.charge('backwards')
        loss.backward()
        g = gradient_summary(named)
        if loss_kind == 'policy':
            require(g['shared'] > 0 and g['head'] == 0, 'Policy gradient routing failed')
        else:
            require(g['head'] > 0, 'Value-head gradient missing')
            require(g['shared'] == 0 if detached else g['shared'] > 0, 'Value/shared gradient routing failed')
        report['gradient_checks'].append({'name': name, 'norms': g, 'loss': float(loss.detach())})
        del lp, value, loss

    report['updates'] = []
    for arm, spec in plan['design']['arms'].items():
        restore()
        actor_opt = torch.optim.AdamW(shared, lr=1e-4, betas=(0.9, 0.999), weight_decay=0.01)
        head_opt = torch.optim.AdamW(head, lr=3e-3, betas=(0.9, 0.999), weight_decay=0.01)
        lp, value, logits = forward(spec['value_detach'])
        ratio = torch.exp(lp - old_logprob)
        advantage = plan['contract']['fixture_advantage']
        policy_loss = -torch.minimum(ratio * advantage, ratio.clamp(0.8, 1.2) * advantage).mean()
        value_loss = clipped_value_loss(value, old_value, target)
        loss = policy_loss + spec['value_loss_coefficient'] * value_loss
        budget.charge('backwards')
        loss.backward()
        preclip = gradient_summary(named)
        # Same two disjoint clipping groups in every arm; upstream joint clipping is not used here.
        torch.nn.utils.clip_grad_norm_(shared, plan['contract']['group_clip_norm'], error_if_nonfinite=True)
        torch.nn.utils.clip_grad_norm_(head, plan['contract']['group_clip_norm'], error_if_nonfinite=True)
        postclip = gradient_summary(named)
        budget.charge('optimizer_steps')  # A logical paired-optimizer update, not two independent actor steps.
        actor_opt.step()
        head_opt.step()
        deltas = {}
        for group in ['shared', 'head']:
            total = 0.0
            for n, p in named.items():
                if ('value_head' in n) == (group == 'head'):
                    require(bool(torch.isfinite(p).all()), 'Nonfinite updated parameter')
                    delta = p.detach().float().cpu() - initial[n].float()
                    total += float(delta.square().sum())
            deltas[group] = total ** 0.5
        require(deltas['shared'] > 0 and deltas['head'] > 0, 'Disposable optimizer step had no observable update')
        report['updates'].append({'arm': arm, 'preclip_norms': preclip, 'postclip_norms': postclip,
                                  'parameter_delta_norms': deltas, 'policy_loss': float(policy_loss.detach()),
                                  'value_loss': float(value_loss.detach())})
        del actor_opt, head_opt, lp, value, loss, policy_loss, value_loss
    restore()  # Never save trained weights or carry a fixture update into a rollout.
    report['initial_trainable_weights_restored'] = True


def p0(plan, out, report):
    import torch
    import numpy as np
    from PIL import Image
    from unittest.mock import patch
    from mani_skill.envs.scene import ManiSkillScene
    from mani_skill.envs.tasks.digital_twins.bridge_dataset_eval.put_on_in_scene_multi import PutOnPlateInScene25MultiCarrot
    from simpler_env.env.simpler_wrapper import SimlerWrapper
    report['runtime'] = runtime()
    model_dir = verify_ready(plan)
    contract, task = plan['contract'], plan['design']['task']
    budget = Budget(contract['caps'])
    report['budget_used'] = budget.used
    torch.manual_seed(contract['seed'])
    np.random.seed(contract['seed'])
    random.seed(contract['seed'])
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False

    class ProbeEnv(PutOnPlateInScene25MultiCarrot):
        def reset(self, seed=None, options=None):
            budget.charge('resets')
            self.evaluation_cache = EvaluationCache()
            opts = dict(options or {}, obj_set=task['obj_set'],
                        episode_id=torch.tensor([task['episode_id']], device=self.device))
            return super().reset(seed=[task['seed']], options=opts)

        def evaluate(self, success_require_src_completely_on_target=True):
            step = int(self.elapsed_steps[0])
            return self.evaluation_cache.get(step,
                lambda: super(ProbeEnv, self).evaluate(success_require_src_completely_on_target))

        def step(self, action):
            budget.charge('control_steps')  # cap=0; no transition can execute, even by accidental call.
            return super().step(action)

    original_step = ManiSkillScene.step
    def counted_step(scene, *args, **kwargs):
        budget.charge('physics_steps')
        return original_step(scene, *args, **kwargs)

    env = None
    try:
        with patch.object(ManiSkillScene, 'step', counted_step):
            env = ProbeEnv(num_envs=1, obs_mode='rgb+segmentation', sim_backend='gpu',
                           control_mode=contract['control_mode'], sim_config={'sim_freq': 500, 'control_freq': 5},
                           sensor_configs={'shader_pack': 'default'})
            obs, _ = env.reset()
            binding = GoalBinding(env, task)
            reference = physical_snapshot(env)
            model, base, processor, tokenizer, named = load_policy(plan, model_dir, report)
            normalizer = base.get_action_stats('bridge_orig')
            converter = object.__new__(SimlerWrapper)
            converter.unnorm_state = normalizer
            bins = np.linspace(-1, 1, 256)
            converter.bin_centers = (bins[:-1] + bins[1:]) / 2
            report['queries'] = []
            canonical_rgb = first_tokens = None
            for goal in (0, 1):
                instruction = binding.bind(goal)
                # Explicit info avoids get_info/evaluate counter mutations during rendering.
                rgb = env.get_obs(info={})['sensor_data']['3rd_view_camera']['rgb'].clone().to(torch.uint8)
                require(tuple(rgb.shape) == (1, 480, 640, 3), 'Native RGB shape mismatch')
                if canonical_rgb is None:
                    canonical_rgb = rgb.clone()
                    Image.fromarray(rgb[0].cpu().numpy()).save(out / 'paired_scene.png')
                require(torch.equal(rgb, canonical_rgb), 'Goal binding changed the visual input')
                before_observer = serial({'stats': env.episode_stats, 'counter': env.consecutive_grasp})
                observed = binding.observe(goal)
                require(before_observer == serial({'stats': env.episode_stats, 'counter': env.consecutive_grasp}),
                        'Observer advanced task history')
                require(physical_snapshot(env) == reference, 'Goal binding/observer changed native state')
                features = policy_input(processor, canonical_rgb, instruction, contract['input_sequence_cap'])
                budget.charge('queries')
                with torch.no_grad(), torch.autocast('cuda', dtype=torch.bfloat16):
                    value, tokens, lp = base.predict_action_batch(**features, unnorm_key='bridge_orig', do_sample=False)
                require(tuple(tokens.shape) == (1, 7), 'Wrong action token shape')
                command = converter._process_action(tokens)
                require(bool(torch.isfinite(command).all()), 'Nonfinite decoded action')
                require(physical_snapshot(env) == reference, 'Query unexpectedly changed environment state')
                report['queries'].append({'goal': goal, 'instruction': instruction, 'tokens': serial(tokens),
                                           'controller_command_not_executed': serial(command),
                                           'observation_sha256': hashlib.sha256(rgb.cpu().numpy().tobytes()).hexdigest(),
                                           'observer': observed, 'value': serial(value), 'logprob': serial(lp)})
                if goal == 0:
                    first_tokens = tokens.detach().clone()
            report['same_scene_rgb_equal'] = True
            report['physical_state_unchanged'] = True
            report['runtime']['rendering_verified'] = True
            action_text = tokenizer.batch_decode(first_tokens)[0]
            inputs = policy_input(processor, canonical_rgb, task['instructions'][0],
                                  contract['input_sequence_cap'], action_text)
            require(torch.equal(inputs['input_ids'][:, -8:-1], first_tokens), 'Action text round-trip changed tokens')
            gradient_probe(plan, model, base, named, inputs, budget, report)
            require(physical_snapshot(env) == reference, 'Gradient probe changed environment state')
            require(budget.used['control_steps'] == 0, 'P0 executed an unapproved action')
            report['status'] = 'IO_AND_GRADIENT_WIRING_QUALIFIED_NOT_RESEARCH_EFFECT'
            report['full_state_restore_verified'] = False
            report['goal_feasibility_or_competence_verified'] = False
            report['peak_cuda_allocated_bytes'] = torch.cuda.max_memory_allocated()
    finally:
        if env is not None:
            env.close()


def build_wheel(plan):
    """Only in Docker build; pinned release identity, observed hash recorded separately."""
    require(Path('/.dockerenv').exists(), 'Docker required')
    item = plan['environment']['flash_wheel']
    wheel = Path('/tmp') / item['name']
    with urllib.request.urlopen(item['browser_download_url'], timeout=60) as src, wheel.open('xb') as dst:
        count = 0
        while block := src.read(1024 * 1024):
            count += len(block)
            require(count <= item['size'], 'Flash wheel exceeds declared release size')
            dst.write(block)
    require(count == item['size'], 'Flash wheel truncated')
    observed = digest(wheel)
    if item.get('digest'):
        require(item['digest'] == 'sha256:' + observed, 'Flash release checksum mismatch')
    (Path('/opt/unified') / 'flash-wheel.json').write_text(json.dumps(
        {'url': item['browser_download_url'], 'sha256': observed, 'size': count,
         'upstream_digest_available': bool(item.get('digest'))}, indent=2))
    subprocess.run(['python3', '-m', 'pip', 'install', '--no-cache-dir', '--no-deps', str(wheel)], check=True)
    wheel.unlink()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['prepare', 'p0', 'verify-source', 'build-wheel'])
    parser.add_argument('--output', type=Path, default=Path('/results'))
    args = parser.parse_args()
    require(Path('/.dockerenv').exists(), 'Docker required')
    plan = json.loads((HERE / 'plan.json').read_text())
    if args.phase == 'verify-source':
        verify_sources(plan)
        return
    if args.phase == 'build-wheel':
        build_wheel(plan)
        return
    require(os.environ.get('UNIFIED_PACKET_SHA'), 'Packet identity required')
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'phase': args.phase, 'status': 'STARTED', 'research_effect_measured': False,
              'packet_sha': os.environ['UNIFIED_PACKET_SHA']}
    destination = args.output / (args.phase + '_result.json')
    require(not destination.exists(), 'Result exists: choose a new output directory')
    try:
        for name in ['resolved-packages.txt', 'resolved-system-packages.txt', 'flash-wheel.json', 'pip-check.txt']:
            shutil.copyfile(Path('/opt/unified') / name, args.output / name)
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
