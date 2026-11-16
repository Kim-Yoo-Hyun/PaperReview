"""Small contract probe. Execute/import only inside the provided local Docker.

New state-based adapter, not GenSafeNav/SocialNav reproduction or a certified policy.
ORCA comes from pinned Python-RVO2; no model weights or datasets are used.
"""
from __future__ import annotations

import copy
import hashlib
import math
import random
from dataclasses import dataclass

import rvo2


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(a, v):
    return (a[0] * v, a[1] * v)


def norm(a):
    return math.hypot(*a)


def distance(a, b):
    return norm(sub(a, b))


def stream(seed, name):
    digest = hashlib.sha256(f"{seed}:{name}".encode()).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


def swept_clearance(a0, a1, b0, b1, radius_sum):
    """Exact minimum for two discs moving linearly during one integration tick."""
    r = sub(a0, b0)
    v = sub(sub(a1, a0), sub(b1, b0))
    vv = v[0] ** 2 + v[1] ** 2
    u = 0.0 if vv == 0 else max(0.0, min(1.0, -(r[0]*v[0]+r[1]*v[1])/vv))
    return norm(add(r, scale(v, u))) - radius_sum


@dataclass(frozen=True)
class Track:
    track_id: str
    generation: int
    position: tuple[float, float]
    observed_tick: int

    @property
    def key(self):
        return (self.track_id, self.generation)


@dataclass(frozen=True)
class Observation:
    episode_id: str
    tick: int
    ego: tuple[float, float]
    velocity: tuple[float, float]
    route_target: tuple[float, float]
    route_id: str
    tracks: tuple[Track, ...]


class Calibrator:
    """Delayed-score adapter; no inherited conformal guarantee is asserted."""
    def __init__(self, method, horizon, rng, config):
        self.method, self.rng, self.config = method, rng, config
        self.initial = config['fixed_fixture_radius_m'][horizon - 1]
        self.experts = [self.initial] * len(config['dtaci_gammas'])
        self.weights = [1.0 / len(self.experts)] * len(self.experts)
        self.chosen = rng.randrange(len(self.experts))
        self.scores = []

    def radius(self):
        if self.method == 'M1':
            return self.experts[self.chosen]
        if self.method == 'M2' and self.scores:
            scores = sorted(self.scores[-self.config['rolling_window']:])
            k = min(len(scores)-1, math.ceil((len(scores)+1)*(1-self.config['alpha']))-1)
            return scores[k]
        return self.initial

    def update(self, score):
        self.scores.append(score)
        if self.method != 'M1':
            return
        alpha, eta = self.config['alpha'], self.config['dtaci_eta']
        residuals = [score - v for v in self.experts]
        losses = [alpha*u - min(u, 0) for u in residuals]
        logw = [math.log(max(w, 1e-300))-eta*l for w, l in zip(self.weights, losses)]
        mx = max(logw)
        ws = [math.exp(w-mx) for w in logw]
        total = sum(ws)
        sigma = self.config['dtaci_sigma']
        self.weights = [(1-sigma)*w/total + sigma/len(ws) for w in ws]
        self.chosen = self.rng.choices(range(len(ws)), weights=self.weights)[0]
        self.experts = [v-g*(alpha-float(v < score))
                        for v, g in zip(self.experts, self.config['dtaci_gammas'])]


class Forecasts:
    def __init__(self, config, episode_id, seed, method='M1'):
        self.config, self.episode_id, self.seed, self.method = config, episode_id, seed, method
        self.history, self.calibrators, self.pending = {}, {}, []
        self.last_tick = -1
        self.last_issue_tick = -1

    def calibrator(self, key, h):
        full_key = (*key, h)
        if full_key not in self.calibrators:
            self.calibrators[full_key] = Calibrator(
                self.method, h, stream(self.seed, f'calibrator:{full_key}'), self.config['controller'])
        return self.calibrators[full_key]

    def observe(self, obs):
        if obs.episode_id != self.episode_id or obs.tick <= self.last_tick:
            raise ValueError('Wrong episode or non-increasing physical tick')
        if any(t.observed_tick != obs.tick for t in obs.tracks):
            raise ValueError('This zero-observation-delay probe requires current-time tracks')
        by_key = {t.key: t for t in obs.tracks}
        if len(by_key) != len(obs.tracks):
            raise ValueError('Duplicate track identity')
        matured, remaining = [], []
        for old in self.pending:
            if old['target_tick'] > obs.tick:
                remaining.append(old)
                continue
            row = copy.deepcopy(old)
            track = by_key.get((row['track_id'], row['track_generation']))
            valid = track is not None and row['target_tick'] == obs.tick
            row.update(score_used=valid, score_available_time_s=obs.tick*self.config['dt_s'],
                       observed_target_position_xy_m=None, nonconformity_score_m=None,
                       covered=None, missing_reason=None)
            if valid:
                score = distance(track.position, row['predicted_position_xy_m'])
                row.update(observed_target_position_xy_m=track.position,
                           nonconformity_score_m=score, covered=score <= row['radius_used_m'])
                self.calibrator(track.key, row['horizon_index']).update(score)
            else:
                row['missing_reason'] = 'target_not_observed_at_target_tick_or_generation_replaced'
            matured.append(row)
        self.pending = remaining
        for t in obs.tracks:
            self.history.setdefault(t.key, []).append((obs.tick, t.position))
            self.history[t.key] = self.history[t.key][-2:]
        self.last_tick = obs.tick
        return matured

    def issue(self, obs):
        if self.last_tick != obs.tick or obs.episode_id != self.episode_id or self.last_issue_tick == obs.tick:
            raise ValueError('Observe and mature scores before issuing')
        self.last_issue_tick = obs.tick
        rows = []
        # Sorting is a view, never an identity join. Store its inverse witness.
        ordered = sorted(obs.tracks, key=lambda t: (distance(obs.ego, t.position), t.key))
        permutation = [t.key for t in ordered]
        for t in ordered:
            history = self.history[t.key]
            valid = len(history) == 2
            velocity = None
            if valid:
                (old_tick, old_pos), (now_tick, now_pos) = history
                velocity = scale(sub(now_pos, old_pos), 1/((now_tick-old_tick)*self.config['dt_s']))
            for h in range(1, self.config['prediction_horizon_steps'] + 1):
                raw = self.calibrator(t.key, h).radius()
                low, high = self.config['controller']['radius_clip_m']
                row = dict(episode_id=obs.episode_id, track_id=t.track_id,
                           track_generation=t.generation, issue_tick=obs.tick,
                           target_tick=obs.tick+h, issue_time_s=obs.tick*self.config['dt_s'],
                           target_time_s=(obs.tick+h)*self.config['dt_s'], horizon_index=h,
                           prediction_id=f'{obs.episode_id}:{t.track_id}:{t.generation}:{obs.tick}:{h}',
                           observation_time_s=t.observed_tick*self.config['dt_s'],
                           observation_available_time_s=obs.tick*self.config['dt_s'],
                           prediction_valid=valid, predicted_position_xy_m=None,
                           radius_raw_m=raw, radius_used_m=max(low, min(high, raw)),
                           missing_reason=None if valid else 'insufficient_observed_history')
                if valid:
                    row['predicted_position_xy_m'] = add(t.position, scale(velocity, h*self.config['dt_s']))
                    self.pending.append(copy.deepcopy(row))
                rows.append(row)
        return rows, permutation


class Controller:
    def __init__(self, config, method='M1'):
        self.config, self.method = config, method
        self.waiting, self.clear_ticks = False, 0
        self.episode_id, self.last_tick = None, -1
        c = config['controller']
        self.candidates = [(0., 0.)] + [
            (v*math.cos(2*math.pi*i/c['heading_count']), v*math.sin(2*math.pi*i/c['heading_count']))
            for v in c['speeds_mps'] for i in range(c['heading_count'])]

    def choose(self, obs, forecasts, queue, delay_ticks):
        c, dt = self.config['controller'], self.config['dt_s']
        if any(row['issue_tick'] != obs.tick or row['episode_id'] != obs.episode_id for row in forecasts):
            raise ValueError('Forecast issue time/episode must match the observation')
        expected = {(t.track_id, t.generation, h) for t in obs.tracks
                    for h in range(1, self.config['prediction_horizon_steps']+1)}
        actual = {(r['track_id'], r['track_generation'], r['horizon_index']) for r in forecasts}
        if actual != expected or len(forecasts) != len(expected):
            raise ValueError('Forecast identities/horizons must match observed tracks exactly')
        if (self.episode_id is not None and self.episode_id != obs.episode_id) or obs.tick <= self.last_tick:
            raise ValueError('Use one controller decision per increasing physical tick and a fresh controller per episode')
        self.episode_id, self.last_tick = obs.episode_id, obs.tick
        if any(not row['prediction_valid'] for row in forecasts):
            return (0., 0.), 'insufficient_history'
        # Empty/all-missing perception is unknown, never a free-space certificate.
        if len(obs.tracks) != 4:
            return (0., 0.), 'missing_track'
        min_clearance = min(distance(obs.ego, t.position)-2*self.config['radius_m'] for t in obs.tracks)
        if self.method == 'M3':
            if min_clearance < c['wait_enter_clearance_m']:
                self.waiting, self.clear_ticks = True, 0
            if self.waiting:
                self.clear_ticks = self.clear_ticks+1 if min_clearance > c['wait_exit_clearance_m'] else 0
                if self.clear_ticks < c['wait_release_ticks']:
                    return (0., 0.), 'hysteresis_wait'
                self.waiting, self.clear_ticks = False, 0
        best = None
        for index, action in enumerate(self.candidates):
            pos, active = obs.ego, obs.velocity
            feasible = True
            for h in range(1, self.config['prediction_horizon_steps']+1):
                dispatch_tick = obs.tick+h-1
                due = [item for item in queue if item['execution_tick'] == dispatch_tick]
                if due:
                    active = tuple(due[-1]['action'])
                if dispatch_tick >= obs.tick+delay_ticks:
                    active = action
                pos = add(pos, scale(active, dt))
                for row in forecasts:
                    if row['horizon_index'] == h:
                        if distance(pos, row['predicted_position_xy_m']) < 2*self.config['radius_m']+row['radius_used_m']:
                            feasible = False
            if feasible:
                objective = (c['route_distance_weight']*distance(pos, obs.route_target)
                             + c['velocity_change_weight']*norm(sub(action, obs.velocity))**2
                             + c['speed_squared_weight']*norm(action)**2)
                candidate = (objective, index, action)
                if best is None or candidate[:2] < best[:2]:
                    best = candidate
        return ((0., 0.), 'no_feasible_candidate') if best is None else (best[2], None)


class World:
    def __init__(self, config, scene, episode_id=None, reactive=True, delay_ticks=2, switch=True):
        self.config, self.scene = config, copy.deepcopy(scene)
        self.episode_id = episode_id or scene['id']
        self.seed, self.reactive, self.delay_ticks, self.switch = scene['seed'], reactive, delay_ticks, switch
        self.rng = {s: stream(self.seed, s) for s in ['scene', 'human_exogenous', 'policy']}
        self.ego, self.velocity = tuple(scene['ego']), (0., 0.)
        self.humans = [dict(track_id=h['id'], generation=0, position=tuple(h['start']),
                            velocity=(0., 0.), goal=tuple(h['goal'])) for h in scene['humans']]
        self.tick, self.path_length, self.terminal = 0, 0., None
        self.queue, self.route_reached = [], False

    def clone(self):
        return copy.deepcopy(self)

    def observe(self, missing=(), reverse=False):
        routes = self.config['routes']
        route_id = 'approach' if self.tick < self.config['event_tick'] else ('switch' if self.switch else 'hold')
        target = tuple(routes[route_id])
        if self.tick >= self.config['event_tick'] and (self.route_reached or distance(self.ego, target) < 0.4):
            target, route_id = tuple(routes['final']), 'final'
        tracks = tuple(Track(h['track_id'], h['generation'], h['position'], self.tick)
                       for h in self.humans if h['track_id'] not in missing)
        return Observation(self.episode_id, self.tick, self.ego, self.velocity, target,
                           route_id, tuple(reversed(tracks)) if reverse else tracks)

    def human_actions(self):
        """Focal-agent ORCA, using pre-integration observations (including old ego velocity)."""
        cfg, dt, radius = self.config['orca'], self.config['dt_s'], self.config['radius_m']
        actions, witnesses = [], []
        for human in self.humans:
            others = [h for h in self.humans if h is not human]
            if self.reactive:
                others += [dict(track_id='ego', position=self.ego, velocity=self.velocity)]
            sim = rvo2.PyRVOSimulator(dt, cfg['neighbor_dist_m'], len(others), cfg['time_horizon_s'],
                                      cfg['time_horizon_obstacles_s'], radius, self.config['speed_mps'])
            for agent in [human] + others:
                sim.addAgent(agent['position'], cfg['neighbor_dist_m'], len(others), cfg['time_horizon_s'],
                             cfg['time_horizon_obstacles_s'], radius+0.01+cfg['safety_space_m'],
                             self.config['speed_mps'], agent['velocity'])
            direction = sub(human['goal'], human['position'])
            pref = scale(direction, 1/max(1., norm(direction)))
            sim.setAgentPrefVelocity(0, pref)
            for j in range(1, len(others)+1):
                sim.setAgentPrefVelocity(j, (0., 0.))
            sim.doStep()
            actions.append(tuple(sim.getAgentVelocity(0)))
            witnesses.append(dict(track_id=human['track_id'], observed_agent_ids=[h['track_id'] for h in others],
                                  ego_velocity_seen=self.velocity if self.reactive else None,
                                  input_tick=self.tick))
        return actions, witnesses

    def step(self, command):
        if self.terminal:
            raise ValueError('Terminal world must be explicitly replaced; no automatic reset')
        command = tuple(command)
        if not all(math.isfinite(v) for v in command) or norm(command) > self.config['speed_mps']+1e-8:
            raise ValueError('Invalid command')
        issue_tick = self.tick
        self.queue.append(dict(command_tick=issue_tick, execution_tick=issue_tick+self.delay_ticks, action=command))
        due = [x for x in self.queue if x['execution_tick'] == issue_tick]
        self.queue = [x for x in self.queue if x['execution_tick'] > issue_tick]
        active = tuple(due[-1]['action']) if due else self.velocity
        h_actions, witnesses = self.human_actions()
        old_ego, old_humans = self.ego, [h['position'] for h in self.humans]
        self.ego = add(self.ego, scale(active, self.config['dt_s']))
        self.velocity = active
        for human, action in zip(self.humans, h_actions):
            human['position'] = add(human['position'], scale(action, self.config['dt_s']))
            human['velocity'] = action
        self.tick += 1
        self.path_length += distance(old_ego, self.ego)
        actual_clearance = min(swept_clearance(old_ego, self.ego, old, h['position'], 2*self.config['radius_m'])
                               for old, h in zip(old_humans, self.humans))
        selected = self.config['routes']['switch' if self.switch else 'hold']
        if self.tick >= self.config['event_tick'] and distance(self.ego, selected) < 0.4:
            self.route_reached = True
        if actual_clearance < 0:
            self.terminal = 'collision'
        elif distance(self.ego, self.config['routes']['final']) < self.config['radius_m']:
            self.terminal = 'goal'
        elif self.tick >= self.config['episode_limit_ticks']:
            self.terminal = 'timeout'
        return dict(physical_tick=self.tick, physical_time_s=self.tick*self.config['dt_s'],
                    command=command, command_time_s=issue_tick*self.config['dt_s'],
                    scheduled_execution_time_s=(issue_tick+self.delay_ticks)*self.config['dt_s'],
                    execution_time_s=issue_tick*self.config['dt_s'] if due else None,
                    applied_command_time_s=due[-1]['command_tick']*self.config['dt_s'] if due else None,
                    applied_action=active, applied_command_tick=due[-1]['command_tick'] if due else None,
                    ego_before=old_ego, ego_after=self.ego, path_length_m=self.path_length,
                    actual_clearance_m=actual_clearance, human_input=witnesses,
                    terminal_reason=self.terminal,
                    terminal_observation=self.observe().__dict__ if self.terminal else None)
