"""Dependency-free contract helpers. No simulator or policy is implemented here."""
import hashlib
import json
import math


def require(condition, message):
    if not condition:
        raise ValueError(message)


def is_digest(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def resolve_fixture(config, seed, difficulty):
    """Called by the patched native environment before scene construction."""
    if config is None:
        return None
    required = {'schema_version', 'group_id', 'split', 'scene_seed', 'target_color', 'color_permutation'}
    require(isinstance(config, dict) and set(config) == required, 'fixture keys')
    require(config['schema_version'] == 1 and difficulty == 'easy', 'only easy v1 fixture supported')
    require(type(config['scene_seed']) is int and config['scene_seed'] == seed, 'scene seed mismatch')
    require(isinstance(config['group_id'], str) and bool(config['group_id']), 'group identity')
    require(config['split'] in {'qualification_dev', 'train', 'selector_validation', 'test'}, 'split')
    perm = config['color_permutation']
    require(isinstance(perm, list) and len(perm) == 3 and all(type(x) is int for x in perm) and sorted(perm) == [0, 1, 2], 'permutation')
    colors = ['red', 'green', 'blue']
    require(config['target_color'] in colors, 'target color')
    result = dict(config)
    result['color_permutation'] = list(perm)
    result['target_bin_index'] = perm.index(colors.index(config['target_color']))
    return result


def build_identity_index(episodes):
    """Build a sidecar plan; does not read HDF5 or replace the upstream builder."""
    seen, group_split, rows = set(), {}, []
    for item in episodes:
        require(is_digest(item['raw_file_sha256']), 'raw digest')
        require(isinstance(item['raw_episode_key'], str) and item['raw_episode_key'], 'raw episode key')
        key = (item['raw_file_sha256'], item['raw_episode_key'])
        require(key not in seen, 'duplicate raw identity')
        seen.add(key)
        group, split = item['group_id'], item['split']
        require(isinstance(group, str) and bool(group), 'group identity')
        require(split in {'qualification_dev', 'train', 'selector_validation', 'test'}, 'split')
        require(group_split.setdefault(group, split) == split, 'group crosses splits')
        stable_id = hashlib.sha256(json.dumps(key, separators=(',', ':')).encode()).hexdigest()
        rows.append({**item, 'stable_episode_id': stable_id})
    rows.sort(key=lambda row: row['stable_episode_id'])
    return [{**row, 'global_episode_idx': idx} for idx, row in enumerate(rows)]


def align_post_step_rows(rows):
    """For verified consecutive post-step records only; never shift unknown data."""
    require(len(rows) >= 2, 'need consecutive rows')
    for row in rows:
        require(row['observation_phase'] == 'post_action', 'unverified observation phase')
        require(type(row['physics_step']) is int, 'physics step')
        require(row['episode_id'] == rows[0]['episode_id'], 'cross-episode alignment')
    output = []
    for current, following in zip(rows, rows[1:]):
        require(following['physics_step'] == current['physics_step'] + 1, 'gap or duplicate step')
        output.append({'episode_id': current['episode_id'], 'observation_step': current['physics_step'],
                       'observation': current['post_observation'],
                       'action_step': following['physics_step'], 'target_action': following['executed_action']})
    return output  # Last observation has no observed next-action target.


def make_history_views(sampled_indices, cutoff, cue_indices, control_indices):
    """Plan masks with fixed raw-time slots; does not encode or evaluate images."""
    require(type(cutoff) is int and cutoff >= 0, 'cutoff')
    require(0 < len(sampled_indices) <= 32, 'frame budget')
    require(all(type(i) is int and 0 <= i <= cutoff for i in sampled_indices), 'future or invalid frame')
    require(list(sampled_indices) == sorted(set(sampled_indices)), 'reordered/duplicate frame')
    cue, control = set(cue_indices), set(control_indices)
    require(bool(cue) and len(cue) == len(control) and not cue & control, 'matched nonempty control')
    require(cue | control <= set(sampled_indices), 'mask references absent cue/control')
    require(cutoff not in cue | control, 'current frame must remain unchanged')
    slots = list(sampled_indices) + [None] * (32 - len(sampled_indices))
    masks = {}
    for name, removed in [('cue_access', set()), ('cue_withheld', cue), ('irrelevant_removed', control)]:
        mask = [index is not None and index not in removed for index in slots for _ in range(16)]
        require(any(mask), 'all-masked memory')
        masks[name] = mask
    return {'raw_time_slots': slots, 'masks': masks}


def check_policy_input(keys, resolved):
    """Check a captured-input description, not actual tensor contents or provenance."""
    expected = {'front_rgb', 'wrist_rgb', 'proprioception', 'goal_prompt',
                'history_rgb_features', 'history_position', 'history_valid_mask'}
    require(set(keys) == expected, 'missing or answer-bearing policy input')
    require(resolved['variant'] == 'perceptual-framesamp-modul', 'resolved history variant')
    require(resolved['predictor'] == 'none', 'oracle/symbolic predictor')
    for key in ['checkpoint_sha256', 'normalizer_sha256', 'offline_encoder_sha256', 'online_encoder_sha256']:
        require(is_digest(resolved[key]), 'missing artifact digest')
    require(resolved['offline_encoder_sha256'] == resolved['online_encoder_sha256'], 'encoder identity not established')
    require(resolved['valid_history_tokens'] > 0, 'all-masked history')
    return True


class ApproachObserver:
    """Frozen auxiliary proxy, not a ground-truth choice or grasp-success label."""
    def __init__(self):
        self.last_tick = None
        self.pending = None
        self.count = 0
        self.event = None

    def observe(self, tick, tcp, centers, any_bin_lifted=False):
        require(type(tick) is int and tick >= 0, 'tick')
        require(self.last_tick is None or tick == self.last_tick + 1, 'non-consecutive or duplicate tick')
        require(len(tcp) == 3 and all(math.isfinite(x) for x in tcp), 'tcp')
        require(len(centers) == 3 and all(len(c) == 3 and all(math.isfinite(x) for x in c) for c in centers), 'centers')
        self.last_tick = tick
        if self.event is not None:
            return self.event
        if any_bin_lifted:
            self.event = {'status': 'unobserved_before_lift', 'tick': tick, 'bin_index': None}
            return self.event
        matches = [i for i, c in enumerate(centers)
                   if math.hypot(tcp[0] - c[0], tcp[1] - c[1]) <= 0.04 and 0.02 <= tcp[2] - c[2] <= 0.12]
        if len(matches) > 1:
            self.event = {'status': 'ambiguous', 'tick': tick, 'bin_index': None}
        elif matches:
            candidate = matches[0]
            self.count = self.count + 1 if self.pending == candidate else 1
            self.pending = candidate
            if self.count == 2:
                self.event = {'status': 'committed_region', 'tick': tick, 'bin_index': candidate}
        else:
            self.pending, self.count = None, 0
        return self.event

    def finish(self):
        return self.event or {'status': 'no_commitment', 'tick': self.last_tick, 'bin_index': None}
