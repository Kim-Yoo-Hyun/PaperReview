"""Fixed-view marker observations and selective recovery for the planar insertion rig."""

import math
from typing import NamedTuple

import mujoco
import numpy as np

import wrist_observation as wrist


FRAME_TICKS = (0, 4, 8, 12)
DECISION_TICK = 15
FOCAL_PX = 800.0
CAMERA_M = np.array([0.0, -0.250, 0.020])
SIZE_PX = np.array([640, 480])
# The two marker planes stay at fixed depth throughout this prismatic task.
SCALE_MM = np.array([244.0, 246.0]) / FOCAL_PX
PIXEL_SIGMA, FLOW_QUANTUM = 0.5, 0.25
FLOW_VARIANCE = float(np.sum(SCALE_MM**2) * (2 * PIXEL_SIGMA**2 + FLOW_QUANTUM**2 / 12))
WRIST_ENCODER = wrist.ENCODERS["nominal"]
WRIST_VARIANCE = WRIST_ENCODER.sigma_mm**2 + WRIST_ENCODER.quantum_mm**2 / 12
LOG_ODDS_THRESHOLD = math.log(9)


class Condition(NamedTuple):
    channel: str
    delay_ticks: int = 4
    drop: float = 0.0
    use_wrist: bool = True


CONDITIONS = {
    "wrist": Condition("none"),
    "ideal_relative": Condition("ideal", 0),
    "clear_delayed": Condition("clear"),
    "no_drop": Condition("camera"),
    "no_delay": Condition("camera", 0, 0.1),
    "camera": Condition("camera", 4, 0.1),
    "covered": Condition("camera", 4, 1.0),
    "camera_only": Condition("camera", 4, 0.1, False),
}


class MarkerCamera:
    """Recompute marker geometry on separate kinematic data without affecting the live controller."""

    def __init__(self, scene, frame_ticks=FRAME_TICKS):
        self.scene = scene
        self.frame_ticks = frame_ticks
        self.model = scene.model
        self.pose = mujoco.MjData(self.model)
        self.hand = self.model.body("wrist").id
        self.reference_uv = self.reference_relative = None

    def project(self, point):
        x, depth, z = point - CAMERA_M
        return np.array([SIZE_PX[0] / 2 + FOCAL_PX * x / depth,
                         SIZE_PX[1] / 2 - FOCAL_PX * z / depth])

    def visible(self, point, owner):
        ray = point - CAMERA_M
        if ray[1] <= 0:
            return False
        uv = self.project(point)
        if not np.all((0 <= uv) & (uv < SIZE_PX)):
            return False
        distance = np.linalg.norm(ray)
        hit = mujoco.mj_ray(self.model, self.pose, CAMERA_M, ray / distance, None, 1, owner,
                            np.empty(1, dtype=np.int32))
        return bool(hit < 0 or hit >= distance - 1e-7)

    def sample(self, data, tick):
        self.pose.qpos[:] = data.qpos
        mujoco.mj_kinematics(self.model, self.pose)
        hand = self.pose.xpos[self.hand] + [0, -0.006, 0.030]
        pin = self.pose.geom_xpos[self.scene.pin] + [0, -0.004, 0]
        relative = 1000 * (pin[0] - hand[0])
        uv = np.array([self.project(hand)[0], self.project(pin)[0]])
        if tick == 0:
            self.reference_relative, self.reference_uv = relative, uv
        # Pixels denote horizontal flow from frame zero. Absolute image positions stay in the sensor.
        if tick in self.frame_ticks:
            flow = uv - self.reference_uv
            visible = (self.visible(hand, self.hand), self.visible(pin, self.scene.part))
        else:
            flow, visible = (0.0, 0.0), (False, False)
        return (*self.scene.wrist_mm(data), relative - self.reference_relative, *flow, *visible)


def image_motion(trace, stream, index, repetition, noisy):
    """Localize both markers at each exposure, subtract the first frame, then quantize flow."""
    flow = trace[list(FRAME_TICKS), 3:5].copy()
    if noisy:
        rng = np.random.default_rng([wrist.SEED, 21, stream, index, repetition])
        error = rng.normal(0.0, PIXEL_SIGMA, flow.shape)
        flow = FLOW_QUANTUM * np.rint((flow + error - error[0]) / FLOW_QUANTUM)
    return flow[:, 1] * SCALE_MM[1] - flow[:, 0] * SCALE_MM[0]


def latest_frame(trace, index, repetition, condition):
    geometric = trace[list(FRAME_TICKS), 5:7].astype(bool).all(axis=1)
    # Matched fault pairs see identical missing-frame draws; camera noise is independent per scene.
    rng = np.random.default_rng([wrist.SEED, 22, index // 2, repetition])
    visible = geometric & (rng.random(len(FRAME_TICKS)) >= condition.drop)
    eligible = [k for k, t in enumerate(FRAME_TICKS) if visible[k] and 0 < t <= DECISION_TICK - condition.delay_ticks]
    return eligible[-1] if visible[0] and eligible else None


def centered(positions):
    return positions - np.mean(positions, axis=0)


def fit_group(cases):
    encoders, ideal = [], []
    clear, noisy = [[] for _ in FRAME_TICKS], [[] for _ in FRAME_TICKS]
    for case in cases:
        trace = np.asarray(case["trace"])
        ideal.append(float(trace[DECISION_TICK, 2]))
        clear_motion = image_motion(trace, 0, case["index"], 0, False)
        geometric = trace[list(FRAME_TICKS), 5:7].astype(bool).all(axis=1)
        paired = np.flatnonzero(geometric & geometric[0])
        for frame in paired:
            clear[frame].append(clear_motion[frame])
        for rep in range(WRIST_ENCODER.repeats):
            encoders.append(centered(WRIST_ENCODER.measure(trace[:, :2], 0, case["index"], rep)))
            observed = image_motion(trace, 0, case["index"], rep, True)
            for frame in paired:
                noisy[frame].append(observed[frame])
    return {"wrist": np.mean(encoders, axis=0).tolist(), "ideal": float(np.mean(ideal)),
            "clear": [float(np.mean(x)) if x else None for x in clear],
            "camera": [float(np.mean(x)) if x else None for x in noisy]}


def fit_folds(cases):
    folds = {}
    for held in sorted({abs(c["offset_mm"]) for c in cases}):
        training = [c for c in cases if abs(c["offset_mm"]) != held]
        templates = {}
        for fault in wrist.ACTION_FOR_FAULT:
            templates[fault] = [
                fit_group([c for c in training if c["fault"] == fault and np.sign(c["offset_mm"]) == sign])
                for sign in (-1, 1)
            ]
        folds[held] = {"training_indices": [c["index"] for c in training], "templates": templates}
    return folds


def observation(trace, index, repetition, condition):
    positions = WRIST_ENCODER.measure(trace[:, :2], 1, index, repetition)
    encoder = centered(positions) if condition.use_wrist else None
    if condition.channel == "ideal":
        return encoder, float(trace[DECISION_TICK, 2]), DECISION_TICK
    if condition.channel == "none":
        return encoder, None, None
    frame = latest_frame(trace, index, repetition, condition)
    if frame is None:
        return encoder, None, None
    values = image_motion(trace, 1, index, repetition, condition.channel == "camera")
    return encoder, float(values[frame]), FRAME_TICKS[frame]


def select(encoder, displacement, tick, templates, channel):
    frame = FRAME_TICKS.index(tick) if displacement is not None and channel != "ideal" else None
    if frame is not None and any(g[channel][frame] is None for pair in templates.values() for g in pair):
        displacement, tick = None, None
    scores = {}
    for fault, groups in templates.items():
        by_sign = []
        for group in groups:
            loss = 0.0
            if encoder is not None:
                loss = np.sum((encoder - group["wrist"])**2) / WRIST_VARIANCE
            if displacement is not None:
                target = group["ideal"] if channel == "ideal" else group[channel][frame]
                variance = FLOW_VARIANCE if channel == "camera" else 0.001**2
                loss += (displacement - target)**2 / variance
            by_sign.append(-0.5 * loss)
        scores[fault] = np.logaddexp(*by_sign)
    odds = float(scores["slip"] - scores["fixture"])
    action = "regrasp_search"
    if odds >= LOG_ODDS_THRESHOLD:
        action = "regrasp"
    elif odds <= -LOG_ODDS_THRESHOLD:
        action = "search"
    return {"action": action, "log_odds_slip": odds, "capture_tick": tick, "displacement_mm": displacement}
