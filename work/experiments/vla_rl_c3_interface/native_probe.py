"""Run ONLY in Docker. Native-function audit, not checkpoint/policy evaluation."""
import ast
import hashlib
import json
import platform
import time
import types
import urllib.request
from pathlib import Path
from enum import Enum

import numpy as np
import torch

START = time.monotonic()
ROOT = Path('/tmp/c3_sources')
OUT = Path('/tmp/c3_evidence')
ROOT.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)
SHA = '7c51662df27b586f9e8a1ab35fcf849f2b8852f9'
BASE = f'https://raw.githubusercontent.com/PRIME-RL/SimpleVLA-RL/{SHA}/'
HF = 'Haozhan72/Openvla-oft-SFT-libero10-trajall'
HF_SHA = '97d6e58bc5fbc402e85bab382e4206bb8e5f0db0'
receipts = []


def fetch(url, name):
    raw = urllib.request.urlopen(url, timeout=60).read()
    (ROOT / name).write_bytes(raw)
    receipts.append({'url': url, 'file': name, 'bytes': len(raw),
                     'sha256': hashlib.sha256(raw).hexdigest()})
    return raw.decode()


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, allow_nan=False) + '\n')


paths = {
    'loss': 'verl/trainer/ppo/core_algos.py',
    'functional': 'verl/utils/torch_functional.py',
    'gripper': 'verl/utils/libero_utils.py',
    'model': 'verl/utils/vla_utils/openvla_oft/modeling_prismatic.py',
    'actor': 'verl/workers/actor/dp_rob.py',
    'rollout': 'verl/workers/rollout/rob_rollout.py',
    'recipe': 'examples/run_openvla_oft_rl_libero.sh',
    'constants': 'verl/utils/vla_utils/openvla_oft/constants.py',
}
src = {key: fetch(BASE + path, key + '.txt') for key, path in paths.items()}
cfg = json.loads(fetch(f'https://huggingface.co/{HF}/resolve/{HF_SHA}/config.json', 'config.json'))
stats = json.loads(fetch(f'https://huggingface.co/{HF}/resolve/{HF_SHA}/dataset_statistics.json', 'stats.json'))


def load_function(key, name, namespace):
    nodes = [n for n in ast.walk(ast.parse(src[key]))
             if isinstance(n, ast.FunctionDef) and n.name == name]
    assert len(nodes) == 1, (key, name, len(nodes))
    node = nodes[0]
    assert not node.decorator_list, name
    exec(compile(ast.Module(body=[node], type_ignores=[]), paths[key], 'exec'), namespace)
    return namespace[name]


ns = {'np': np, 'torch': torch}
masked_mean = load_function('functional', 'masked_mean', ns)
ns['verl_F'] = types.SimpleNamespace(masked_mean=masked_mean)
native_loss = load_function('loss', 'compute_policy_loss', ns)
normalize = load_function('gripper', 'normalize_gripper_action', ns)
invert = load_function('gripper', 'invert_gripper_action', ns)


class NormalizationType(str, Enum):
    BOUNDS = 'bounds'
    BOUNDS_Q99 = 'bounds_q99'


ns.update(NormalizationType=NormalizationType,
          ACTION_PROPRIO_NORMALIZATION_TYPE=NormalizationType.BOUNDS_Q99)
unnormalize = load_function('model', '_unnormalize_actions', ns)
keys = [k for k in stats if 'libero_10' in k]
assert len(keys) == 1, list(stats)
key = keys[0]
action_stats = stats[key]['action']
bins = np.linspace(-1, 1, cfg['n_action_bins'])
centers = (bins[:-1] + bins[1:]) / 2
vocab_size = cfg['text_config']['vocab_size'] - cfg['pad_to_multiple_of']
ids = np.arange(vocab_size - 256, vocab_size)

# Execute original decoder assignment nodes, not a reimplemented mapping.
model_tree = ast.parse(src['model'])
method = next(n for n in ast.walk(model_tree) if isinstance(n, ast.FunctionDef)
              and n.name == '_verl_discrete_prediction')
tail = [n for n in method.body if isinstance(n, ast.Assign)
        and 1742 <= n.lineno <= 1744]
assert len(tail) == 3
decoder_ns = {'np': np, 'self': types.SimpleNamespace(vocab_size=vocab_size, bin_centers=centers),
              'predicted_action_token_ids': ids}
exec(compile(ast.Module(body=tail, type_ignores=[]), paths['model'], 'exec'), decoder_ns)
decoded = decoder_ns['normalized_actions']
actions = np.zeros((256, 7))
actions[:, -1] = decoded
stub = types.SimpleNamespace(get_action_stats=lambda _: action_stats)
unnorm = unnormalize(stub, actions, key)
executed = invert(normalize(unnorm, binarize=True))
classes, label = np.unique(executed[:, -1], return_inverse=True)
assert len(classes) == 2, classes
assert np.array_equal(executed[:, :6], unnorm[:, :6])
counts = np.bincount(label)
save('source_audit.json', {'date': '2026-10-21', 'receipts': receipts,
     'commit': SHA, 'checkpoint_metadata_revision': HF_SHA, 'checkpoint_weights_loaded': False,
     'native_functions_executed': ['masked_mean', 'compute_policy_loss',
        'normalize_gripper_action', 'invert_gripper_action', '_unnormalize_actions'],
     'native_decoder_AST_lines': [1742, 1743, 1744], 'normalization_key': key,
     'config': {'n_action_bins': cfg['n_action_bins'], 'vocab_size': vocab_size},
     'action_stats': action_stats, 'gripper_classes': classes.tolist(),
     'token_count_by_class': counts.tolist(), 'token_to_class': label.tolist(),
     'original_loss_eos_mask': 'all ones in uniform-distribution enumeration',
     'nonuniform_expectation': 'analytic finite sums, separate from native loss replay'})

torch.set_num_threads(2)
DT = torch.float64
lab = torch.tensor(label)
old = torch.full((256,), 1 / 256, dtype=DT)
class_mass = torch.stack([old[lab == c].sum() for c in range(2)])
reward = (lab == 0).to(DT)
adv = reward - torch.sum(old * reward)


def class_probs(p):
    return torch.stack([p[lab == c].sum() for c in range(2)])


def native_compare(new, name):
    assert torch.all(new > 0) and abs(new.sum().item() - 1) < 1e-12
    cp = class_probs(new)
    old_log = old.log()[None]
    new_log = new.log()[None]
    mask = torch.ones_like(old_log)
    raw = native_loss(old_log, new_log, adv[None], mask, 0.28, 0.2)
    grouped = native_loss(class_mass[lab].log()[None], cp[lab].log()[None],
                          adv[None], mask, 0.28, 0.2)
    raw_unclip = -(old * adv * new / old).sum()
    class_unclip = -(old * adv * cp[lab] / class_mass[lab]).sum()
    return {'name': name, 'class_mass_old': class_mass.tolist(), 'class_mass_new': cp.tolist(),
            'max_class_mass_difference': (cp - class_mass).abs().max().item(),
            'token_KL_old_new': (old * (old.log() - new.log())).sum().item(),
            'executed_KL_old_new': (class_mass * (class_mass.log() - cp.log())).sum().item(),
            'token_loss': raw[0].item(), 'class_loss': grouped[0].item(),
            'token_clip_fraction': raw[1].item(), 'class_clip_fraction': grouped[1].item(),
            'unclipped_loss_difference': abs(raw_unclip.item() - class_unclip.item())}


cases = [native_compare(old.clone(), 'identity')]
for scale in [0.1, 0.3, 0.6, 0.9]:
    q = old.clone()
    for c in range(2):
        indices = torch.nonzero(lab == c).flatten()
        weights = torch.ones(len(indices), dtype=DT)
        half = len(indices) // 2
        weights[:half] -= scale
        weights[half:2 * half] += scale
        q[indices] *= weights
    row = native_compare(q, f'class_preserving_redistribution_{scale}')
    assert row['max_class_mass_difference'] < 1e-12
    assert abs(row['class_loss']) < 1e-12
    assert row['unclipped_loss_difference'] < 1e-12
    cases.append(row)
q = old.clone()
new_mass = class_mass + torch.tensor([0.05, -0.05], dtype=DT)
for c in range(2):
    q[lab == c] *= new_mass[c] / class_mass[c]
cases.append(native_compare(q, 'physical_class_mass_change_0.05'))

# Injective transform control: each token is its own executed action.
raw = native_loss(old.log()[None], q.log()[None], adv[None], torch.ones((1,256),dtype=DT), .28, .2)
singleton_lab = torch.arange(256)
singleton_old = torch.stack([old[singleton_lab == c].sum() for c in range(256)])
singleton_new = torch.stack([q[singleton_lab == c].sum() for c in range(256)])
singleton = native_loss(singleton_old[singleton_lab].log()[None],
                        singleton_new[singleton_lab].log()[None], adv[None],
                        torch.ones((1,256),dtype=DT), .28, .2)
assert max(abs(a.item() - b.item()) for a,b in zip(raw,singleton)) == 0
save('ppo_cases.json', {'input_kind': 'synthetic categorical logits; exact enumeration',
     'clip_low': 0.2, 'clip_high': 0.28, 'cases': cases,
     'injective_control_max_difference': 0.0})


def variance_row(p, name):
    p = p / p.sum()
    pc = np.bincount(label, weights=p)
    r = (label == 0).astype(float)
    a = r - p @ r
    raw_score = np.eye(256) - p[None, :]
    class_score = np.stack([p * (label == label[i]) / pc[label[i]] - p for i in range(256)])
    raw_g = a[:, None] * raw_score
    class_g = a[:, None] * class_score
    gm = p @ raw_g
    cm = p @ class_g
    raw_var = float(p @ ((raw_g - gm) ** 2).sum(axis=1))
    marginal_var = float(p @ ((class_g - cm) ** 2).sum(axis=1))
    err = float(np.max(np.abs(gm - cm)))
    assert err < 1e-12
    assert marginal_var <= raw_var + 1e-12
    # Autograd checks mean gradient against actual expected executed reward.
    logits = torch.tensor(np.log(p), dtype=DT, requires_grad=True)
    objective = (logits.softmax(-1) * reward).sum()
    exact_g = torch.autograd.grad(objective, logits)[0].detach().numpy()
    autograd_error = float(np.max(np.abs(gm - exact_g)))
    assert autograd_error < 1e-12
    return {'name': name, 'raw_variance_trace': raw_var,
            'marginal_variance_trace': marginal_var,
            'variance_reduction_percent': 100 * (1 - marginal_var / raw_var),
            'mean_gradient_max_error': err, 'autograd_gradient_max_error': autograd_error,
            'class_probability': pc.tolist()}


rows = [variance_row(np.ones(256) / 256, 'uniform')]
for seed in range(20):
    rng = np.random.default_rng(seed)
    logits = rng.normal(0, 1.5, size=256)
    p = np.exp(logits - logits.max())
    rows.append(variance_row(p, f'nonuniform_seed_{seed}'))
concentrated = []
for retained in [0.5, 0.9, 0.99, 0.9999, 0.999999]:
    p = np.zeros(256)
    for c in range(2):
        ix = np.where(label == c)[0]
        # Each physical class retains its original mass; one token takes most of it.
        p[ix] = float(class_mass[c]) * (1-retained)/(len(ix)-1)
        p[ix[0]] = float(class_mass[c])*retained
    concentrated.append(variance_row(p, f'one_token_per_class_mass_{retained}'))
save('gradient_variance.json', {'metric': 'variance trace of gradient w.r.t. independent token logits',
     'not_measured': 'gradient variance through native VLA parameters or real rollout advantages',
     'rows': rows, 'concentration_negative_controls': concentrated})

# Coupled-history negative example: gripper aliases may cause different later arm tokens.
# Do not infer whole-trajectory equivalence from one coordinate's binarization.
history_old = {'alias_a': .5, 'alias_b': .5}
history_new = {'alias_a': .9, 'alias_b': .1}
save('scope_controls.json', {'autoregressive_counterexample': {
    'same_gripper_probability': 1.0,
    'next_arm_left_probability_given_alias_a': 1.0,
    'next_arm_left_probability_given_alias_b': 0.0,
    'old_next_arm_left_probability': history_old['alias_a'],
    'new_next_arm_left_probability': history_new['alias_a'],
    'conclusion': 'same gripper marginal does not imply same subsequent action distribution'},
    'all_assertions_passed': True})
save('runtime.json', {'python': platform.python_version(), 'machine': platform.machine(),
     'numpy': np.__version__, 'torch': torch.__version__, 'cuda_available': torch.cuda.is_available(),
     'wall_seconds': time.monotonic() - START, 'checkpoint_forward_calls': 0,
     'robot_rollouts': 0, 'training_updates': 0, 'all_assertions_passed': True})
print(json.dumps({'class_counts': counts.tolist(), 'class_values': classes.tolist(),
                  'ppo_cases': cases, 'uniform_gradient': rows[0],
                  'concentrated_last': concentrated[-1], 'wall_seconds': time.monotonic()-START}))
