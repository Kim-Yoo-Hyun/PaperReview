"""Matched physical failures and recovery policies in a Cartesian insertion task."""

import hashlib
import json
import math
import platform
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import NamedTuple

import mujoco
import numpy as np
import wrist_observation as wrist
import relative_motion as motion


ROOT = Path(__file__).resolve().parent
OFFSETS_MM = (-9, -7, -5, -3, 3, 5, 7, 9)
FAULTS = ("slip", "fixture", "arrested_slip")
ACTIONS = ("retry", "regrasp", "search", "regrasp_search")
PERIOD = 0.01
SCAN_AMPLITUDE_M = 0.012
SCAN_SPEED_M_S = 0.025
HORIZON = 3.0
CONTACT_S = 2.0
IMPULSE_NS = 5.0
PEAK_N = 12.0
STATE = mujoco.mjtState.mjSTATE_INTEGRATION
CLOSE_TICK = 15
PAD_THRESHOLD_N = 0.05
GAP_MM = (7.5, 8.5)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class JawReading(NamedTuple):
    left_mm: float
    right_mm: float
    gap_mm: float
    left_n: float
    right_n: float

    def ready(self):
        return (min(self.left_n, self.right_n) >= PAD_THRESHOLD_N
                and GAP_MM[0] <= self.gap_mm <= GAP_MM[1])


class GripTransition:
    """A timer uses only the control clock. With no timer, use the first qualified sample."""

    def __init__(self, timer_ticks=None):
        self.timer_ticks = timer_ticks
        self.ready_tick = None
        self.feed_tick = None
        self.feed_at = None
        self.at_feed = None
        self.single_pad_ticks = 0

    def observe(self, tick, t, reading):
        if tick <= CLOSE_TICK:
            return
        if self.ready_tick is None:
            self.single_pad_ticks += (reading.left_n >= PAD_THRESHOLD_N) != (reading.right_n >= PAD_THRESHOLD_N)
            if reading.ready():
                self.ready_tick = tick
        if self.feed_tick is not None:
            return
        due = reading.ready() if self.timer_ticks is None else tick >= CLOSE_TICK + self.timer_ticks
        if due:
            self.feed_tick, self.feed_at, self.at_feed = tick, t, reading

    def record(self, scan_start):
        return {"ready_tick": self.ready_tick, "feed_tick": self.feed_tick,
                "scan_phase_s": None if scan_start is None else round(scan_start, 7),
                "single_pad_ticks_before_ready": self.single_pad_ticks,
                "sample_at_feed": None if self.at_feed is None else self.at_feed._asdict()}


class Scene:
    def __init__(self, fault, offset_mm, dt, lateral_force=0.32, *, force_x_n=None, wrist_x_kv=None):
        self.model = m = mujoco.MjModel.from_xml_path(str(ROOT / "insertion.xml"))
        m.opt.timestep = dt
        if wrist_x_kv is not None:
            # MuJoCo position servo bias is (0, -kp, -kv). Apply before the blocked start settles.
            if not math.isfinite(wrist_x_kv) or wrist_x_kv < 0:
                raise ValueError("The wrist velocity feedback gain must be finite and nonnegative")
            m.actuator_biasprm[m.actuator("wrist_x").id, 2] = -wrist_x_kv
        offset = offset_mm / 1000
        self.socket = m.body("socket").id
        self.part = m.body("part").id
        self.pin = m.geom("pin").id
        self.left_pad, self.right_pad = m.geom("left_pad").id, m.geom("right_pad").id
        self.pads = {self.left_pad, self.right_pad}
        self.left_q, self.right_q = [int(m.joint(j).qposadr[0]) for j in ("left_closure", "right_closure")]
        self.open_gap = (m.body("right_finger").pos[0] - m.body("left_finger").pos[0]
                         - m.geom_size[self.left_pad, 0] - m.geom_size[self.right_pad, 0])
        self.x, self.z, self.inhand = [int(m.joint(j).qposadr[0]) for j in ("x", "z", "inhand")]
        self.tip = m.site("tip").id
        self.force = np.zeros(6)
        m.body_pos[self.socket, 0] = -offset if fault == "fixture" else 0
        data = mujoco.MjData(m)
        data.qpos[self.z] = 0.004
        data.qpos[self.inhand] = offset if fault in ("slip", "arrested_slip") else 0
        data.ctrl[1] = 0.004 if fault == "clean" else -0.002
        mujoco.mj_forward(m, data)
        # Strong retention and zero lateral disturbance while making the blocked start.
        for _ in range(round(0.40 / dt)):
            mujoco.mj_step(m, data)
        mujoco.mj_forward(m, data)
        rim, jaw = self.contacts(data)
        tip = data.site_xpos[self.tip]
        self.initial = {
            "wrist_x_m": float(data.qpos[self.x]), "wrist_z_m": float(data.qpos[self.z]),
            "wrist_vx_m_s": float(data.qvel[m.joint("x").dofadr[0]]),
            "inhand_m": float(data.qpos[self.inhand]), "socket_x_m": float(data.xpos[self.socket, 0]),
            "relative_error_m": float(tip[0] - data.xpos[self.socket, 0]), "depth_m": float(-tip[2]),
            "rim_normal_n": rim, "jaw_normal_n": jaw,
        }
        if fault == "slip":
            m.dof_frictionloss[m.joint("inhand").dofadr[0]] = 0.07
        if fault != "clean":
            # Legacy trials tie direction to the offset. The crossed-load trials specify world x directly.
            data.xfrc_applied[self.part, 0] = math.copysign(lateral_force, offset) if force_x_n is None else force_x_n
        self.saved = np.empty(mujoco.mj_stateSize(m, STATE))
        mujoco.mj_getState(m, data, self.saved, STATE)
        self.initial["state_sha256"] = sha(self.saved.astype("<f8").tobytes())

    def restore(self):
        data = mujoco.MjData(self.model)
        mujoco.mj_setState(self.model, data, self.saved, STATE)
        mujoco.mj_forward(self.model, data)
        return data

    def wrist_mm(self, data):
        return (float(data.qpos[self.x]) * 1000, float(data.qpos[self.z]) * 1000)

    def contacts(self, data):
        rim = jaw = 0.0
        for i in range(data.ncon):
            contact = data.contact[i]
            a, b = contact.geom1, contact.geom2
            if self.pin not in (a, b):
                continue
            mujoco.mj_contactForce(self.model, data, i, self.force)
            normal = max(0.0, float(self.force[0]))
            if (b if a == self.pin else a) in self.pads:
                jaw += normal
            else:
                rim += normal
        return rim, jaw

    def jaw_reading(self, data):
        # A pad senses any contacting geometry. The detector has no access to pin or socket identity.
        left = right = 0.0
        for i in range(data.ncon):
            contact = data.contact[i]
            ids = (contact.geom1, contact.geom2)
            if self.left_pad not in ids and self.right_pad not in ids:
                continue
            mujoco.mj_contactForce(self.model, data, i, self.force)
            normal = max(0.0, float(self.force[0]))
            if self.left_pad in ids:
                left += normal
            if self.right_pad in ids:
                right += normal
        lpos, rpos = float(data.qpos[self.left_q]), float(data.qpos[self.right_q])
        return JawReading(1000 * lpos, 1000 * rpos, 1000 * (self.open_gap - lpos - rpos), left, right)


class Recovery:
    """Wrist encoders and time control the path. Only the optional grip transition adds pad sensing."""

    def __init__(self, action, first_direction=1, transition=None, *, scan_amplitude_m=SCAN_AMPLITUDE_M):
        self.grip = action in ("regrasp", "regrasp_search")
        self.scan = action in ("search", "regrasp_search")
        if not math.isfinite(scan_amplitude_m) or scan_amplitude_m <= 0:
            raise ValueError("Scan amplitude must be positive and finite")
        self.scan_amplitude_m = scan_amplitude_m
        self.first_direction = first_direction
        self.transition = transition
        self.scan_start = None
        self.entry = None

    def command(self, t, wrist_x, wrist_z):
        jaw = 0.0195 if self.grip and t >= 0.15 else 0.0
        feed_at = 0.50 if self.grip else 0.15
        if self.transition is not None:
            feed_at = self.transition.feed_at
        if feed_at is None or t < feed_at:
            return (0.0, 0.003, jaw, jaw)
        if self.entry is None and wrist_z < -0.0015:
            self.entry = (t, wrist_x, wrist_z)
        if self.entry is not None:
            entry_t, entry_x, entry_z = self.entry
            return (entry_x, max(-0.013, entry_z - 0.025 * (t - entry_t)), jaw, jaw)
        z = max(-0.0022, 0.003 - 0.010 * (t - feed_at))
        if self.scan_start is None and self.scan and wrist_z <= 0.0002:
            self.scan_start = t
        if self.scan_start is None:
            return (0.0, z, jaw, jaw)
        # In the one-dimensional error subspace the scan covers both directions.
        amplitude = self.scan_amplitude_m
        phase = (t - self.scan_start) * SCAN_SPEED_M_S * math.pi / (2 * amplitude)
        x = self.first_direction * amplitude * (2 / math.pi) * math.asin(math.sin(phase))
        return (x, z, jaw, jaw)


def trial(scene, action, first_direction=1, budget="all_contacts", transition=None, wrist_selector=None,
          sample=None, fallback_ticks=None, preparation=None, *, scan_amplitude_m=SCAN_AMPLITUDE_M,
          scan_sample=None):
    model, data = scene.model, scene.restore()
    dt = model.opt.timestep
    steps_control = round(PERIOD / dt)
    decision_tick = CLOSE_TICK if preparation is None else preparation.decision_tick
    delay_ticks = decision_tick - CLOSE_TICK
    if (action == "wrist_choice") != (wrist_selector is not None):
        raise ValueError("A wrist-choice trial needs a selector")
    policy = Recovery("search" if wrist_selector is not None else action, first_direction, transition,
                      scan_amplitude_m=scan_amplitude_m)
    prefix = []
    chosen = None
    if transition is not None and not policy.grip:
        raise ValueError("A grip transition requires a jaw-closing action")
    rim_impulse = jaw_impulse = peak_n = drift = max_depth = 0.0
    touched = rim_steps = jaw_steps = seated = touches = 0
    was_on_rim = False
    preparation_cost = None
    moving_clearance = math.inf
    moving_peak_n = 0.0
    stop = "timeout"
    for i in range(round(HORIZON / dt)):
        if i % steps_control == 0:
            tick = i // steps_control
            if wrist_selector is not None and tick <= decision_tick:
                prefix.append(scene.wrist_mm(data) if sample is None else sample(data, tick))
                if tick == decision_tick:
                    chosen = wrist_selector(np.asarray(prefix))
                    if chosen == "regrasp_search" and fallback_ticks is not None:
                        transition = GripTransition(fallback_ticks)
                    elif chosen in ("regrasp", "search"):
                        transition = GripTransition() if chosen == "regrasp" else None
                    else:
                        raise ValueError(f"Invalid wrist-selected action: {chosen}")
                    policy = Recovery(chosen, first_direction, transition, scan_amplitude_m=scan_amplitude_m)
            if preparation is not None and tick < decision_tick:
                data.ctrl[:] = preparation.command(tick)
            else:
                # Shift only the recovery controller's clock. Contact and timeout start at the first lift.
                recovery_time = (i - delay_ticks * steps_control) * dt
                if transition is not None and (transition.feed_tick is None or transition.ready_tick is None):
                    transition.observe(tick - delay_ticks, recovery_time, scene.jaw_reading(data))
                data.ctrl[:] = policy.command(recovery_time, data.qpos[scene.x], data.qpos[scene.z])
                if scan_sample is not None and policy.scan_start is not None and policy.entry is None:
                    scan_sample((tick, float(data.ctrl[0]), float(data.qpos[scene.x])))
        mujoco.mj_step(model, data)
        # MuJoCo contact forces refer to the substep that produced the new qpos.
        rim, jaw = scene.contacts(data)
        total = rim + jaw
        rim_impulse += rim * dt
        jaw_impulse += jaw * dt
        peak_n = max(peak_n, total)
        touched += total > 0.05
        on_rim = rim > 0.05
        rim_steps += on_rim
        jaw_steps += jaw > 0.05
        touches += on_rim and not was_on_rim
        was_on_rim = on_rim
        # Pin and wrist have only prismatic DOFs; these coordinates are post-step.
        pin_error = data.qpos[scene.x] + data.qpos[scene.inhand] - model.body_pos[scene.socket, 0]
        depth = -data.qpos[scene.z]
        if preparation is not None and preparation.start_tick * steps_control <= i < decision_tick * steps_control:
            moving_clearance = min(moving_clearance, -depth)
            moving_peak_n = max(moving_peak_n, total)
            if i + 1 == decision_tick * steps_control:
                preparation_cost = {"elapsed_s": round((i + 1) * dt, 7),
                                    "contact_s": round(touched * dt, 7), "socket_contact_s": round(rim_steps * dt, 7),
                                    "rim_impulse_ns": round(rim_impulse, 7), "jaw_impulse_ns": round(jaw_impulse, 7),
                                    "min_clearance_from_move_mm": round(1000 * moving_clearance, 7),
                                    "peak_contact_from_move_n": round(moving_peak_n, 7)}
        max_depth = max(max_depth, depth)
        drift = max(drift, abs(data.qpos[scene.inhand] - scene.initial["inhand_m"]))
        seated = seated + 1 if depth >= 0.009 and abs(pin_error) <= 0.0011 else 0
        charged_steps = rim_steps if budget == "socket_only" else touched
        charged_impulse = rim_impulse if budget == "socket_only" else rim_impulse + jaw_impulse
        if peak_n > PEAK_N:
            stop = "force_limit"
        elif charged_impulse > IMPULSE_NS:
            stop = "impulse_limit"
        elif charged_steps > round(CONTACT_S / dt):
            stop = "contact_time_limit"
        elif seated >= round(0.10 / dt):
            stop = "inserted"
        if stop != "timeout":
            break
    if any(data.warning.number) or not np.isfinite(data.qpos).all():
        raise RuntimeError("Invalid simulation state")
    elapsed = (i + 1) * dt
    result = {
        "stop": stop, "success": stop == "inserted", "elapsed_s": round(elapsed, 7),
        "scored_s": round(elapsed, 7) if stop == "inserted" else HORIZON,
        "rim_impulse_ns": round(rim_impulse, 7), "jaw_impulse_ns": round(jaw_impulse, 7),
        "peak_normal_n": round(peak_n, 6), "contact_s": round(touched * dt, 7),
        "socket_contact_s": round(rim_steps * dt, 7), "jaw_contact_s": round(jaw_steps * dt, 7),
        "rim_contact_onsets": touches, "max_inhand_change_mm": round(drift * 1000, 5),
        "final_inhand_mm": round(data.qpos[scene.inhand] * 1000, 5),
        "max_depth_mm": round(max_depth * 1000, 5), "final_error_mm": round(pin_error * 1000, 5),
    }
    if preparation is not None:
        if preparation_cost is None:
            raise RuntimeError(f"Recovery stopped in the preparation at {elapsed:.3f}s: {stop}")
        result["preparation_cost"] = preparation_cost
    if transition is not None:
        timings = transition.record(policy.scan_start)
        if delay_ticks:
            for key in ("feed_tick", "ready_tick"):
                if timings[key] is not None:
                    timings[key] += delay_ticks
            if timings["scan_phase_s"] is not None:
                timings["scan_phase_s"] = round(timings["scan_phase_s"] + delay_ticks * PERIOD, 7)
        result["transition"] = timings
    if wrist_selector is not None:
        if chosen is None:
            raise RuntimeError("The common unloading prefix ended before action selection")
        result["wrist_decision"] = {"action": chosen, "prefix_sha256": sha(np.asarray(prefix, dtype="<f8").tobytes())}
    return result


def verify_start(scenes, offset):
    initial = [s.initial for s in scenes.values()]
    for s in initial:
        if (abs(s["relative_error_m"] - offset / 1000) > 0.0001 or
                abs(s["depth_m"]) > 0.0001 or s["rim_normal_n"] < 0.2 or s["jaw_normal_n"] > 0.05):
            raise ValueError(f"An invalid stalled start at {offset} mm: {s}")
    for key, tol in (("relative_error_m", 0.0001), ("depth_m", 0.0001), ("rim_normal_n", 0.15)):
        values = [s[key] for s in initial]
        if max(values) - min(values) > tol:
            raise ValueError(f"Unmatched {key} at {offset} mm")


def stats(rows):
    return {"n": len(rows), "success": sum(r["success"] for r in rows),
            "mean_scored_s": round(mean(r["scored_s"] for r in rows), 6),
            "stops": dict(Counter(r["stop"] for r in rows))}


def paired_win(a, b):
    return a["success"] and (not b["success"] or b["scored_s"] - a["scored_s"] >= 0.20 - 1e-9)


def summarize(blocks):
    by_fault = {}
    for fault in blocks[0]["faults"]:
        by_fault[fault] = {action: stats([b["faults"][fault]["trials"][action] for b in blocks])
                           for action in ACTIONS}
    fixed = {act: stats([b["faults"][f]["trials"][act] for b in blocks for f in ("slip", "fixture")])
             for act in ACTIONS}
    oracle_rows = []
    wins = {}
    for fault, expected, other in (("slip", "regrasp", "search"), ("fixture", "search", "regrasp")):
        pairs = [b["faults"][fault]["trials"] for b in blocks]
        wins[fault] = sum(paired_win(p[expected], p[other]) for p in pairs)
        oracle_rows.extend(p[expected] for p in pairs)
    oracle = stats(oracle_rows)
    best = max(fixed, key=lambda a: (fixed[a]["success"], -fixed[a]["mean_scored_s"]))
    gain = oracle["success"] - fixed[best]["success"]
    saved = fixed[best]["mean_scored_s"] - oracle["mean_scored_s"]
    return {"by_fault": by_fault, "fixed": fixed, "oracle": oracle, "best_fixed": best,
            "predicted_wins": wins, "oracle_extra_successes": gain, "oracle_time_saved_s": round(saved, 6),
            "passes": min(wins.values()) >= 6 and (gain >= 2 or (gain == 0 and saved >= 0.20 - 1e-9))}


def qualifications(dt):
    centered = trial(Scene("clean", 0, dt), "retry")
    searches = {str(mm): trial(Scene("fixture", mm, dt, lateral_force=0), "search") for mm in (-5, 5)}
    slips = {}
    for retention in (0.90, 0.07):
        scene = Scene("clean", 0, dt)
        model, data = scene.model, scene.restore()
        model.dof_frictionloss[model.joint("inhand").dofadr[0]] = retention
        data.xfrc_applied[scene.part, 0] = 0.32
        for _ in range(round(1 / dt)):
            mujoco.mj_step(model, data)
        slips[str(retention)] = float(1000 * abs(data.qpos[scene.inhand]))
    if not centered["success"] or not all(r["success"] for r in searches.values()):
        raise ValueError(f"Nominal centered insertion or bilateral search failed: {centered}, {searches}")
    if slips["0.9"] > 0.20 or slips["0.07"] < 1:
        raise ValueError(f"Retention calibration failed: {slips}")
    return {"centered_retry": centered, "unloaded_search": searches, "free_slide_at_one_second_mm": slips}


def matrix(dt, faults, first_direction=1, budget="all_contacts"):
    blocks = []
    for offset in OFFSETS_MM:
        scenes = {f: Scene(f, offset, dt) for f in faults}
        verify_start(scenes, offset)
        conditions = {f: {"initial": s.initial,
                          "trials": {a: trial(s, a, first_direction, budget) for a in ACTIONS}}
                      for f, s in scenes.items()}
        blocks.append({"offset_mm": offset, "faults": conditions})
    return {"timestep_s": dt, "first_direction": first_direction, "budget": budget,
            "blocks": blocks, "summary": summarize(blocks)}


def run(dt):
    controls = qualifications(dt)
    return dict(controls=controls, **matrix(dt, FAULTS))


def qualify_grip_signal():
    results = {}
    for name, absent in (("centered", ()), ("left_only", ("right_pad",)),
                         ("no_pad_contact", ("left_pad", "right_pad"))):
        scene = Scene("clean", 0, 0.001)
        for pad in absent:
            index = scene.model.geom(pad).id
            scene.model.geom_contype[index] = scene.model.geom_conaffinity[index] = 0
        gate = GripTransition()
        result = trial(scene, "regrasp_search", transition=gate)
        if name == "centered" and (gate.feed_tick is None or not result["success"]):
            raise RuntimeError(f"Centered grasp did not qualify: {result}")
        if absent and (gate.feed_tick is not None or result["success"]):
            raise RuntimeError(f"False grasp completion in the {name} control: {result}")
        if name == "left_only" and not gate.single_pad_ticks:
            raise RuntimeError("The unilateral control never touched its enabled pad")
        results[name] = result
    return results


GRIP_COMBINED = ("fixed_350ms", "calibrated_timer", "bilateral")


def timing_cases(dt, direction, budget, timer_ticks):
    cases = []
    for offset in OFFSETS_MM:
        scenes = {f: Scene(f, offset, dt) for f in ("slip", "fixture")}
        verify_start(scenes, offset)
        for fault, scene in scenes.items():
            trials = {}
            for name, delay in zip(GRIP_COMBINED, (35, timer_ticks, None), strict=True):
                trials[name] = trial(scene, "regrasp_search", direction, budget, GripTransition(delay))
            if fault == "slip":
                trials["regrasp_fixed"] = trial(scene, "regrasp", direction, budget)
                trials["regrasp_bilateral"] = trial(scene, "regrasp", direction, budget, GripTransition())
            else:
                trials["search"] = trial(scene, "search", direction, budget)
            cases.append({"offset_mm": offset, "fault": fault, "initial_sha256": scene.initial["state_sha256"],
                          "trials": trials})
    return cases


def timing_comparison(dt, direction, budget, timer_ticks):
    cases = timing_cases(dt, direction, budget, timer_ticks)
    methods = {name: stats([c["trials"][name] for c in cases]) for name in GRIP_COMBINED}
    for name, regrasp in (("known_original", "regrasp_fixed"), ("known_matched", "regrasp_bilateral")):
        methods[name] = stats([c["trials"][regrasp if c["fault"] == "slip" else "search"] for c in cases])
    best = max(GRIP_COMBINED, key=lambda a: (methods[a]["success"], -methods[a]["mean_scored_s"]))
    advantage = methods["known_matched"]["success"] - methods[best]["success"]
    seconds = round(methods[best]["mean_scored_s"] - methods["known_matched"]["mean_scored_s"], 6)
    return {"timestep_s": dt, "direction": direction, "budget": budget, "cases": cases,
            "summary": {"methods": methods, "best_combined": best, "extra_successes_with_cause": advantage,
                        "scored_seconds_saved_with_cause": seconds,
                        "meets_diagnostic_threshold": advantage >= 2 or (advantage == 0 and seconds >= 0.20)}}


def grip_timing():
    controls = qualify_grip_signal()
    nominal_ticks = controls["centered"]["transition"]["ready_tick"] - CLOSE_TICK
    conditions = {}
    for name, dt, direction in (("primary", 0.001, 1), ("half_step", 0.0005, 1), ("reverse_scan", 0.001, -1)):
        conditions[name] = {budget: timing_comparison(dt, direction, budget, nominal_ticks)
                            for budget in ("all_contacts", "socket_only")}
    return {"close_tick": CLOSE_TICK, "period_s": PERIOD, "pad_threshold_n": PAD_THRESHOLD_N,
            "aperture_range_mm": GAP_MM, "fixed_wait_ticks": 35, "calibrated_wait_ticks": nominal_ticks,
            "signal_controls": controls, "conditions": conditions}


def common_wrist_trace(scene, sample=None, preparation=None):
    data = scene.restore()
    prelude = Recovery("search")
    trace = []
    decision_tick = CLOSE_TICK if preparation is None else preparation.decision_tick
    for tick in range(decision_tick + 1):
        trace.append(scene.wrist_mm(data) if sample is None else sample(data, tick))
        if tick < decision_tick:
            if preparation is None:
                data.ctrl[:] = prelude.command(tick * PERIOD, data.qpos[scene.x], data.qpos[scene.z])
            else:
                data.ctrl[:] = preparation.command(tick)
            mujoco.mj_step(scene.model, data, nstep=round(PERIOD / scene.model.opt.timestep))
    return trace


def execute_wrist_choice(scene, case, encoder, means, repetition, budgets):
    def selector(raw_prefix):
        measured = encoder.measure(raw_prefix, 1, case["index"], repetition)
        return wrist.choose_action(measured, means)

    return execute_choice(scene, case, selector, budgets)


def execute_choice(scene, case, selector, budgets, sample=None, fallback_ticks=None):
    decisions = []
    for budget in budgets:
        result = trial(scene, "wrist_choice", budget=budget, wrist_selector=selector,
                       sample=sample, fallback_ticks=fallback_ticks)
        decision = result.pop("wrist_decision")
        if decision["prefix_sha256"] != case["prefix_sha256"]:
            raise RuntimeError("Live pre-decision encoders diverged from the common unloading trace")
        action = decision["action"]
        # Repeated noise changes the decision only. Keep each distinct physical result once.
        outcomes = case["rollouts"].setdefault(action, {})
        if outcomes.setdefault(budget, result) != result:
            raise RuntimeError("Repeated action diverged in the same physical scene and budget")
        decisions.append(action)
    if len(set(decisions)) != 1:
        raise RuntimeError("The contact budget changed a pre-action observation or choice")
    return decisions[0]


def score_against_timer(outcomes, timer_rows, case_indices):
    regained, lost = [], []
    for i, result, timer in zip(case_indices, outcomes, timer_rows, strict=True):
        if result["success"] != timer["success"]:
            (regained if result["success"] else lost).append(i)
    score, timer = stats(outcomes), stats(timer_rows)
    gain = score["success"] - timer["success"]
    return {**score, "gained_vs_timer": regained, "lost_vs_timer": lost,
            "meets_gain_rule": gain >= 2 or (gain == 0 and timer["mean_scored_s"] - score["mean_scored_s"] >= 0.20 - 1e-9)}


def wrist_scores(cases, decisions, baselines):
    budgets = {}
    indices = [c["index"] for c in cases]
    for budget, reference in baselines.items():
        outcomes, timer_rows = [], []
        for case, action, control in zip(cases, decisions, reference["cases"], strict=True):
            if (case["offset_mm"], case["fault"], case["initial_sha256"]) != (
                control["offset_mm"], control["fault"], control["initial_sha256"]
            ):
                raise RuntimeError("Baseline and wrist trial use different starting scenes")
            result = case["rollouts"][action][budget]
            trials = control["trials"]
            if action == "regrasp_search" and result != trials["calibrated_timer"]:
                raise RuntimeError("Fallback did not reproduce the calibrated timer from the same start")
            if action == wrist.ACTION_FOR_FAULT[case["fault"]]:
                oracle_action = "regrasp_bilateral" if action == "regrasp" else "search"
                if result != trials[oracle_action]:
                    raise RuntimeError("Matched action did not reproduce the known-cause rollout")
            outcomes.append(result)
            timer_rows.append(trials["calibrated_timer"])
        score = score_against_timer(outcomes, timer_rows, indices)
        oracle = reference["summary"]["methods"]["known_matched"]
        score["matches_oracle"] = score["success"] == oracle["success"] and score["mean_scored_s"] == oracle["mean_scored_s"]
        budgets[budget] = score
    return budgets


def wrist_scenes(timestep, *, marker_camera=False, force_x_n=None, wrist_x_kv=None):
    scenes, cases = [], []
    for offset in OFFSETS_MM:
        pair = {fault: Scene(fault, offset, timestep, force_x_n=force_x_n, wrist_x_kv=wrist_x_kv)
                for fault in wrist.ACTION_FOR_FAULT}
        verify_start(pair, offset)
        for fault, scene in pair.items():
            sample = motion.MarkerCamera(scene).sample if marker_camera else None
            trace = common_wrist_trace(scene, sample)
            cases.append({
                "index": len(cases), "fault": fault, "offset_mm": offset,
                ("trace" if marker_camera else "wrist_mm"): trace,
                "initial_sha256": scene.initial["state_sha256"],
                "prefix_sha256": sha(np.asarray(trace, dtype="<f8").tobytes()), "rollouts": {},
            })
            scenes.append(scene)
    return scenes, cases


def wrist_comparison(baselines):
    scenes, cases = wrist_scenes(0.001)
    profiles = {}
    for name, encoder in wrist.ENCODERS.items():
        folds = wrist.fit_folds(cases, encoder)
        repetitions = []
        for repetition in range(encoder.repeats):
            decisions = [
                execute_wrist_choice(scene, case, encoder, folds[abs(case["offset_mm"])]["means_mm"], repetition, baselines)
                for scene, case in zip(scenes, cases, strict=True)
            ]
            correct = sum(a == wrist.ACTION_FOR_FAULT[c["fault"]] for c, a in zip(cases, decisions, strict=True))
            repetitions.append({"repetition": repetition, "actions": decisions, "correct": correct,
                                "budgets": wrist_scores(cases, decisions, baselines)})
        profiles[name] = {**encoder._asdict(), "folds_by_held_mm": folds, "repetitions": repetitions}
    _, fine_cases = wrist_scenes(0.0005)
    return {"decision_tick": CLOSE_TICK, "period_s": PERIOD, "seed": wrist.SEED,
            "rng_key": ["seed", "stream (0 calibration, 1 evaluation)", "case index", "repetition"],
            "cases": cases, "signal_separation": wrist.signal_separation(cases), "profiles": profiles,
            "half_step_prefix_check": {"timestep_s": 0.0005, "signal_separation": wrist.signal_separation(fine_cases),
                                       "prefix_sha256": [c["prefix_sha256"] for c in fine_cases]},
            "baseline_source": "grip_timing.conditions.primary"}


def marker_controls(scene):
    camera = motion.MarkerCamera(scene)
    camera.sample(scene.restore(), 0)
    clear_point = np.array([0.0, -0.030, 0.030])
    behind_wall = np.array([0.0, 0.0, -0.008])
    hand = np.array([0.0, -0.006, 0.030])
    pin = np.array([0.004, -0.004, 0.012])
    shift = np.array([0.001, 0.0, 0.0])
    flows = [camera.project(p + shift)[0] - camera.project(p)[0] for p in (hand, pin)]
    hand_mm, pin_mm = flows * motion.SCALE_MM
    controls = {"in_view": camera.visible(clear_point, -1),
                "behind_socket_wall": camera.visible(behind_wall, -1),
                "outside_frame": camera.visible(clear_point + [1, 0, 0], -1),
                "common_translation_mm": float(pin_mm - hand_mm), "pin_translation_mm": float(pin_mm)}
    if not controls["in_view"] or controls["behind_socket_wall"] or controls["outside_frame"]:
        raise RuntimeError("Camera geometry failed the visibility controls")
    if abs(pin_mm - 1) > 1e-9 or abs(pin_mm - hand_mm) > 1e-9:
        raise RuntimeError("Image motion failed the metric translation controls")
    return controls


def marker_decision(scene, case, condition, templates, repetition, budgets, timer_ticks):
    readings = []

    def selector(trace):
        obs = motion.observation(trace, case["index"], repetition, condition)
        reading = motion.select(*obs, templates, condition.channel)
        readings.append(reading)
        return reading["action"]

    execute_choice(scene, case, selector, budgets, motion.MarkerCamera(scene).sample, timer_ticks)
    if readings[0] != readings[1]:
        raise RuntimeError("Camera inputs or scores changed across budgets")
    return readings[0]


def compare_selective_controls(scores, wrist_scores_for_rep, timer_scores):
    for budget, score in scores.items():
        timer = timer_scores[budget]
        wrist_score = wrist_scores_for_rep[budget]
        best = max((timer, wrist_score), key=lambda s: (s["success"], -s["mean_scored_s"]))
        delta = score["success"] - best["success"]
        saved = best["mean_scored_s"] - score["mean_scored_s"]
        score["best_control"] = "calibrated_timer" if best is timer else "selective_wrist"
        score["success_gain_over_best"] = delta
        score["seconds_saved_over_best"] = round(saved, 6)
        score["passes_best_control"] = delta >= 2 or (delta == 0 and saved >= 0.20 - 1e-9)


def relative_comparison(timing):
    baselines = timing["conditions"]["primary"]
    timer_scores = {b: ref["summary"]["methods"]["calibrated_timer"] for b, ref in baselines.items()}
    timer_ticks = timing["calibrated_wait_ticks"]
    scenes, cases = wrist_scenes(0.001, marker_camera=True)
    folds = motion.fit_folds(cases)
    profiles = {}
    for name, condition in motion.CONDITIONS.items():
        repeats = []
        for repetition in range(motion.WRIST_ENCODER.repeats):
            readings = [marker_decision(scene, case, condition, folds[abs(case["offset_mm"])]["templates"],
                                        repetition, baselines, timer_ticks)
                        for scene, case in zip(scenes, cases, strict=True)]
            actions = [reading["action"] for reading in readings]
            scores = wrist_scores(cases, actions, baselines)
            wrist_ref = scores if name == "wrist" else profiles["wrist"]["repetitions"][repetition]["budgets"]
            compare_selective_controls(scores, wrist_ref, timer_scores)
            repeats.append({"readings": readings, "action_counts": dict(Counter(actions)), "budgets": scores})
        profiles[name] = {"condition": condition._asdict(), "repetitions": repeats}
    return {"decision_tick": CLOSE_TICK, "period_s": PERIOD, "frame_ticks": motion.FRAME_TICKS,
            "seed": wrist.SEED, "confidence_threshold": 0.90, "controls": marker_controls(scenes[0]),
            "trace_columns": ["wrist_x_mm", "wrist_z_mm", "ideal_relative_change_mm", "hand_flow_px",
                              "pin_flow_px", "hand_visible", "pin_visible"],
            "cases": cases, "folds_by_held_mm": folds, "profiles": profiles,
            "baseline_source": "grip_timing.conditions.primary"}


LOAD_OPTIONS = ("regrasp", "search", "regrasp_search")
LOAD_BUDGETS = ("all_contacts", "socket_only")
FROZEN_FOLDS_SHA256 = "f8f62d704b842dc05542cb032a23b3f9ce4d29e97180787c9123860f67b91a26"


def frozen_load_folds(previous):
    def digest(folds):
        return sha(json.dumps(folds, sort_keys=True, separators=(",", ":"), allow_nan=False).encode())

    folds = previous["folds_by_held_mm"]
    if digest(folds) != FROZEN_FOLDS_SHA256:
        # Different architectures can round the original training trajectories differently.
        with Path("/pilot-reference.json").open() as reference:
            folds = json.load(reference)["relative_motion"]["folds_by_held_mm"]
        if digest(folds) != FROZEN_FOLDS_SHA256:
            raise ValueError("The archived source-condition folds differ from the frozen policy")
    return {int(k): v for k, v in folds.items()}


def run_load_actions(scene, case, force_x_n, timer_ticks):
    start = scene.restore()
    forces = start.xfrc_applied
    if forces[scene.part, 0] != force_x_n or np.count_nonzero(forces) != int(force_x_n != 0):
        raise RuntimeError("The restored pin load differs from the assigned world-x force")
    case["applied_x_n"] = float(forces[scene.part, 0])
    positions_and_velocities = np.concatenate((start.qpos, start.qvel)).astype("<f8")
    case["kinematic_start_sha256"] = sha(positions_and_velocities.tobytes())
    for action in LOAD_OPTIONS:
        outcomes = {}
        for budget in LOAD_BUDGETS:
            gate = None
            if action == "regrasp":
                gate = GripTransition()
            elif action == "regrasp_search":
                gate = GripTransition(timer_ticks)
            outcomes[budget] = trial(scene, action, budget=budget, transition=gate)
        case["rollouts"][action] = outcomes


def load_mechanics(cases, budget):
    options = [{a: c["rollouts"][a][budget] for a in LOAD_OPTIONS} for c in cases]
    by_fault, expected_wins = {}, {}
    for fault, expected in wrist.ACTION_FOR_FAULT.items():
        rows = [r for c, r in zip(cases, options, strict=True) if c["fault"] == fault]
        by_fault[fault] = {a: stats([r[a] for r in rows]) for a in LOAD_OPTIONS}
        other = "search" if expected == "regrasp" else "regrasp"
        expected_wins[fault] = sum(paired_win(r[expected], r[other]) for r in rows)
    prescribed = [r[wrist.ACTION_FOR_FAULT[c["fault"]]] for c, r in zip(cases, options, strict=True)]
    best_in_scene = [max(r.values(), key=lambda o: (o["success"], -o["scored_s"])) for r in options]
    return {"by_fault": by_fault, "expected_wins": expected_wins, "both_reach_six": min(expected_wins.values()) >= 6,
            "fixed": {a: stats([r[a] for r in options]) for a in LOAD_OPTIONS},
            "original_fault_rule": stats(prescribed), "best_of_three_by_scene": stats(best_in_scene)}


def load_policies(scenes, cases, folds, timer_ticks):
    indices = [c["index"] for c in cases]
    timers = {b: [c["rollouts"]["regrasp_search"][b] for c in cases] for b in LOAD_BUDGETS}
    timer_scores = {b: stats(rows) for b, rows in timers.items()}
    profiles = {}
    for name in ("wrist", "camera_only", "camera", "ideal_relative"):
        condition = motion.CONDITIONS[name]
        repeats = []
        for repetition in range(motion.WRIST_ENCODER.repeats):
            actions = []
            for case, scene in zip(cases, scenes, strict=True):
                templates = folds[abs(case["offset_mm"])]["templates"]
                obs = motion.observation(np.asarray(case["trace"]), case["index"], repetition, condition)
                reading = motion.select(*obs, templates, condition.channel)
                action = reading["action"]
                live = case["live_checks"]
                if action not in live:
                    check = marker_decision(scene, case, condition, templates, repetition, LOAD_BUDGETS, timer_ticks)
                    if check != reading:
                        raise RuntimeError("Live decision disagrees with the stored pre-action observation")
                    live[action] = {"profile": name, "repetition": repetition}
                actions.append(action)
            scores = {}
            for b in LOAD_BUDGETS:
                rows = [c["rollouts"][a][b] for c, a in zip(cases, actions, strict=True)]
                scores[b] = score_against_timer(rows, timers[b], indices)
            wrist_ref = scores if name == "wrist" else profiles["wrist"][repetition]["budgets"]
            compare_selective_controls(scores, wrist_ref, timer_scores)
            repeats.append({"actions": actions, "budgets": scores})
        profiles[name] = repeats
    return profiles


def load_comparison(previous, timer_ticks):
    folds = frozen_load_folds(previous)
    starts, conditions = {}, []
    for load in (-0.32, -0.16, 0.0, 0.16, 0.32):
        scenes, cases = wrist_scenes(0.001, marker_camera=True, force_x_n=load)
        for case, scene in zip(cases, scenes, strict=True):
            run_load_actions(scene, case, load, timer_ticks)
            kinematic = case["kinematic_start_sha256"]
            key = (case["fault"], case["offset_mm"])
            if starts.setdefault(key, kinematic) != kinematic:
                raise RuntimeError("The lateral load changed the settled starting pose or velocity")
            case["live_checks"] = {}
        mechanics = {b: load_mechanics(cases, b) for b in LOAD_BUDGETS}
        profiles = load_policies(scenes, cases, folds, timer_ticks)
        conditions.append({"force_x_n": load, "cases": cases, "mechanics": mechanics, "profiles": profiles})
    return {"frozen_folds_sha256": FROZEN_FOLDS_SHA256, "fold_source": "relative_motion.folds_by_held_mm",
            "conditions": conditions}


def baseline_suite():
    source = {f: sha((ROOT / f).read_bytes()) for f in
              ("insertion.xml", "simulate.py", "wrist_observation.py", "relative_motion.py", "Dockerfile")}
    result = {
        "environment": {"mujoco": mujoco.__version__, "numpy": np.__version__,
                        "python": platform.python_version(), "architecture": platform.machine()},
        "source_sha256": source, "control_period_s": PERIOD, "offsets_mm": OFFSETS_MM,
        "limits": {"horizon_s": HORIZON, "contact_s": CONTACT_S, "impulse_ns": IMPULSE_NS, "peak_n": PEAK_N},
        "primary": run(0.001), "half_step": run(0.0005),
        "reverse_scan": matrix(0.001, ("slip", "fixture"), first_direction=-1),
        "socket_budget": matrix(0.001, ("slip", "fixture"), budget="socket_only"),
        "grip_timing": grip_timing(),
    }
    result["wrist_choice"] = wrist_comparison(result["grip_timing"]["conditions"]["primary"])
    result["relative_motion"] = relative_comparison(result["grip_timing"])
    result["lateral_load"] = load_comparison(result["relative_motion"], result["grip_timing"]["calibrated_wait_ticks"])
    return result


if __name__ == "__main__":
    print(json.dumps(baseline_suite(), indent=2, allow_nan=False))
