"""Paired wrist excursions and time-matched passive controls before peg recovery."""

import json
import math
from typing import NamedTuple

import mujoco
import numpy as np

import relative_motion as camera
import simulate as sim
import wrist_observation as wrist


START_TICK, TURN_TICK, RETURN_TICK, DECIDE_TICK = 16, 20, 24, 32
AMPLITUDE_M = 0.003
FRAME_TICKS = tuple(range(0, DECIDE_TICK + 1, 4))
FRAME_PAIRS = ((0, 8), (16, 20), (24, 28))
LOADS = (-0.32, -0.16, 0.0, 0.16, 0.32)
REPEATS = camera.WRIST_ENCODER.repeats
CHANNELS = ("both", "wrist", "camera")


class Preparation(NamedTuple):
    direction: int
    decision_tick: int = DECIDE_TICK
    start_tick: int = START_TICK

    def command(self, tick):
        x = 0.0
        if START_TICK < tick < RETURN_TICK:
            phase = math.pi * (tick - START_TICK) / (TURN_TICK - START_TICK)
            x = self.direction * AMPLITUDE_M * 0.5 * (1.0 - math.cos(phase))
        return (x, 0.003, 0.0, 0.0)


PREPARATIONS = {"immediate": None, "hold": Preparation(0), "positive": Preparation(1),
                "negative": Preparation(-1)}


def calibrate(prep, scene=None):
    if scene is None:
        scene = sim.Scene("clean", 0, 0.001)
    data = scene.restore()
    dt = scene.model.opt.timestep
    per_tick = round(sim.PERIOD / dt)
    peak_x = peak_speed = peak_contact = relative = 0.0
    min_clearance = math.inf
    for step in range(prep.decision_tick * per_tick):
        tick = step // per_tick
        if step % per_tick == 0:
            data.ctrl[:] = prep.command(tick)
        mujoco.mj_step(scene.model, data)
        if tick >= START_TICK:
            x = data.qpos[scene.x]
            peak_x = max(peak_x, prep.direction * x)
            peak_speed = max(peak_speed, abs(data.qvel[scene.model.joint("x").dofadr[0]]))
            min_clearance = min(min_clearance, data.qpos[scene.z])
            peak_contact = max(peak_contact, sum(scene.contacts(data)))
            relative = max(relative, abs(data.qpos[scene.inhand] - scene.initial["inhand_m"]))
    check = {"excursion_mm": float(1000 * peak_x), "return_error_mm": float(1000 * abs(data.qpos[scene.x])),
             "max_speed_mm_s": float(1000 * peak_speed), "min_clearance_mm": float(1000 * min_clearance),
             "peak_contact_n": peak_contact, "max_relative_mm": float(1000 * relative)}
    if not (check["excursion_mm"] >= 2 and check["return_error_mm"] <= 0.35 and
            check["min_clearance_mm"] >= 1 and peak_contact <= 0.05 and check["max_relative_mm"] <= 0.20):
        raise RuntimeError(f"Normal pin failed wrist-excursion calibration: {check}")
    return check


def observation(trace, index, repeat, stream):
    """Return centered wrist x and disjoint camera differences available at the decision."""
    trace = np.asarray(trace)
    positions = camera.WRIST_ENCODER.measure(trace[:, :2], stream, index, repeat)
    encoder = camera.centered(positions[:, 0])
    # Paired noise across modes and loads. Separate draws for training, test, and frame drops.
    rng = np.random.default_rng([wrist.SEED, 31, stream, index, repeat])
    error = rng.normal(0, camera.PIXEL_SIGMA, (len(FRAME_TICKS), 2))
    rng = np.random.default_rng([wrist.SEED, 32, stream, index // 2, repeat])
    keep = rng.random(len(FRAME_TICKS)) >= 0.10
    flow = []
    for left, right in FRAME_PAIRS:
        if right + 4 > len(trace) - 1:
            continue
        li, ri = FRAME_TICKS.index(left), FRAME_TICKS.index(right)
        if not (keep[li] and keep[ri] and trace[[left, right], 5:7].all()):
            flow.append(np.nan)
            continue
        pixels = trace[right, 3:5] - trace[left, 3:5] + error[ri] - error[li]
        pixels = camera.FLOW_QUANTUM * np.rint(pixels / camera.FLOW_QUANTUM)
        flow.append(pixels[1] * camera.SCALE_MM[1] - pixels[0] * camera.SCALE_MM[0])
    return encoder, np.asarray(flow)


def fit(cases, held, loads=LOADS):
    train = [c for c in cases if abs(c["offset_mm"]) != held]
    templates = {}
    for fault in wrist.ACTION_FOR_FAULT:
        groups = []
        for load in loads:
            match = [c for c in train if c["load_n"] == load and c["fault"] == fault]
            if len(match) != 6:
                raise ValueError("An offset fold must have six signed scenes per load and fault")
            readings = [observation(c["trace"], c["index"], r, 0) for c in match for r in range(REPEATS)]
            enc, flow = map(np.asarray, zip(*readings))
            if not np.isfinite(flow).any(axis=0).all():
                raise ValueError("Calibration lacks a visible example of a required frame pair")
            groups.append({"load_n": load, "wrist_mm": enc.mean(axis=0).tolist(),
                           "relative_mm": np.nanmean(flow, axis=0).tolist()})
        templates[fault] = groups
    return {"training_case_ids": [c["case_id"] for c in train], "templates": templates}


def select(reading, templates, channel):
    enc, flow = reading
    visible = np.isfinite(flow)
    scores = {}
    for fault, groups in templates.items():
        log_terms = []
        for group in groups:
            loss = 0.0
            if channel in ("both", "wrist"):
                loss += np.sum((enc - group["wrist_mm"])**2) / camera.WRIST_VARIANCE
            if channel in ("both", "camera"):
                diff = flow[visible] - np.asarray(group["relative_mm"])[visible]
                loss += np.sum(diff**2) / camera.FLOW_VARIANCE
            log_terms.append(-0.5 * loss)
        scores[fault] = np.logaddexp.reduce(log_terms)
    odds = scores["slip"] - scores["fixture"]
    if odds >= camera.LOG_ODDS_THRESHOLD:
        return "regrasp"
    if odds <= -camera.LOG_ODDS_THRESHOLD:
        return "search"
    return "regrasp_search"


def collect_cases(scenes, references, prep, timer_ticks):
    cases = []
    for case_id, (scene, (load, ref)) in enumerate(zip(scenes, references, strict=True)):
        case = {k: ref[k] for k in ("index", "offset_mm", "fault", "initial_sha256")}
        case.update(case_id=case_id, load_n=load, live_checks={})
        if case["initial_sha256"] != scene.initial["state_sha256"]:
            raise ValueError("Unmatched starting state for probe and immediate recovery")
        if prep is None:
            case.update(trace=ref["trace"], prefix_sha256=ref["prefix_sha256"], rollouts=ref["rollouts"])
        else:
            sampler = camera.MarkerCamera(scene, FRAME_TICKS)
            trace = sim.common_wrist_trace(scene, sampler.sample, prep)
            if not np.array_equal(trace[:sim.CLOSE_TICK + 1], ref["trace"]):
                raise ValueError("The new preparation changed the common lift before the wrist moved")
            case.update(trace=trace, prefix_sha256=sim.sha(np.asarray(trace, dtype="<f8").tobytes()), rollouts={})
            for action in sim.LOAD_OPTIONS:
                outcomes = {}
                for budget in sim.LOAD_BUDGETS:
                    gate = None
                    if action != "search":
                        gate = sim.GripTransition(timer_ticks if action == "regrasp_search" else None)
                    row = sim.trial(scene, action, budget=budget, transition=gate, preparation=prep)
                    cost = row.pop("preparation_cost")
                    if cost != case.setdefault("preparation_cost", cost):
                        raise RuntimeError("Preparation outcomes depend on a future recovery action")
                    outcomes[budget] = row
                case["rollouts"][action] = outcomes
        cases.append(case)
    return cases


def check_live(scene, case, prep, templates, channel, repetition, action, timer_ticks):
    def selector(trace):
        return select(observation(trace, case["index"], repetition, 1), templates, channel)

    for budget in sim.LOAD_BUDGETS:
        sampler = camera.MarkerCamera(scene, FRAME_TICKS)
        outcome = sim.trial(scene, "wrist_choice", budget=budget, wrist_selector=selector,
                            sample=sampler.sample, fallback_ticks=timer_ticks, preparation=prep)
        decision = outcome.pop("wrist_decision")
        if decision != {"action": action, "prefix_sha256": case["prefix_sha256"]}:
            raise RuntimeError("Live choice differs from the common pre-decision record")
        if prep is not None and outcome.pop("preparation_cost") != case["preparation_cost"]:
            raise RuntimeError("Live and fixed actions charged different costs before their decision")
        if outcome != case["rollouts"][action][budget]:
            raise RuntimeError("The selected action did not reproduce its matched physical rollout")


def evaluate_mode(cases, scenes, prep, timer_ticks, fitted=None):
    folds = fitted if fitted is not None else {n: fit(cases, n) for n in sorted({abs(c["offset_mm"]) for c in cases})}
    profiles = {ch: [[] for _ in range(REPEATS)] for ch in CHANNELS}
    for scene, case in zip(scenes, cases, strict=True):
        templates = folds[abs(case["offset_mm"])]["templates"]
        for r in range(REPEATS):
            reading = observation(case["trace"], case["index"], r, 1)
            for channel in CHANNELS:
                action = select(reading, templates, channel)
                profiles[channel][r].append(action)
                if action not in case["live_checks"]:
                    check_live(scene, case, prep, templates, channel, r, action, timer_ticks)
                    case["live_checks"][action] = {"channel": channel, "repeat": r}
    mode = {"cases": cases, "actions": profiles}
    if fitted is None:
        mode["folds_by_held_mm"] = folds
    return mode


def paired_difference(rows, reference, ids):
    gained, lost = [], []
    for i, a, b in zip(ids, rows, reference, strict=True):
        if a["success"] != b["success"]:
            (gained if a["success"] else lost).append(i)
    saved = sum(b["scored_s"] - a["scored_s"] for a, b in zip(rows, reference, strict=True)) / len(ids)
    return {"gained": gained, "lost": lost, "seconds_saved": round(saved, 6)}


def scoreboard(modes, ids, budget):
    summary, contrasts = {}, {"positive": [], "negative": []}
    for r in range(REPEATS):
        rows = {}
        for name, mode in modes.items():
            cases = [mode["cases"][i] for i in ids]
            for action in sim.LOAD_OPTIONS:
                rows[name + "/" + action] = [c["rollouts"][action][budget] for c in cases]
            for ch, repetitions in mode["actions"].items():
                rows[name + "/" + ch] = [c["rollouts"][repetitions[r][i]][budget]
                                          for i, c in zip(ids, cases, strict=True)]
            rows[name + "/best_in_scene"] = [
                max((bs[budget] for bs in c["rollouts"].values()), key=lambda x: (x["success"], -x["scored_s"]))
                for c in cases]
        records = {key: sim.stats(results) for key, results in rows.items()}
        for key, stats in records.items():
            entry = summary.setdefault(key, {"successes": [], "mean_scored_s": []})
            entry["successes"].append(stats["success"])
            entry["mean_scored_s"].append(stats["mean_scored_s"])
        for name in contrasts:
            controls = [k for k in rows if k.split("/")[0] in ("immediate", "hold") and
                        not k.endswith("/best_in_scene")]
            controls.extend(name + "/" + a for a in sim.LOAD_OPTIONS)
            best = max(controls, key=lambda k: (records[k]["success"], -records[k]["mean_scored_s"]))
            chosen = rows[name + "/both"]
            differences = {"best_control": best}
            for label, control in (("vs_best", best), ("vs_same_motion_fixed", name + "/regrasp_search"),
                                   ("vs_hold_choice", "hold/both"), ("vs_immediate_fixed", "immediate/regrasp_search")):
                differences[label] = paired_difference(chosen, rows[control], ids)
            contrasts[name].append(differences)
    return {"case_ids": ids, "methods": summary, "comparisons": contrasts}


def primary_gate(scores):
    gates = {}
    for budget, score in scores.items():
        gates[budget] = {}
        for direction, reps in score["comparisons"].items():
            passes = []
            for rep in reps:
                diff = rep["vs_best"]
                gain = len(diff["gained"]) - len(diff["lost"])
                passes.append(gain >= 2 or (gain == 0 and diff["seconds_saved"] >= 0.20))
            gates[budget][direction] = {"passes": passes, "majority": sum(passes) > len(passes) / 2}
    return gates


def run_modes(scenes, references, timer_ticks, trained=None):
    modes = {}
    for name, prep in PREPARATIONS.items():
        fitted = None if trained is None else {int(k): v for k, v in trained[name]["folds_by_held_mm"].items()}
        cases = collect_cases(scenes, references, prep, timer_ticks)
        modes[name] = evaluate_mode(cases, scenes, prep, timer_ticks, fitted)
    return modes


def finer_step(trained, timer_ticks):
    scenes, references, source_ids = [], [], []
    for load in LOADS:
        if abs(load) > 0.16:
            continue
        batch, cases = sim.wrist_scenes(0.0005, marker_camera=True, force_x_n=load)
        for scene, case in zip(batch, cases, strict=True):
            sim.run_load_actions(scene, case, load, timer_ticks)
            references.append((load, case))
            source_ids.append(LOADS.index(load) * len(cases) + case["index"])
        scenes.extend(batch)
    modes = run_modes(scenes, references, timer_ticks, trained)
    scores = {b: scoreboard(modes, list(range(len(scenes))), b) for b in sim.LOAD_BUDGETS}
    return {"timestep_s": 0.0005, "source_case_ids": source_ids, "fold_source": "active_probe.modes",
            "modes": modes, "scores": scores, "primary_gate": primary_gate(scores)}


def run_probe(baseline, timer_ticks):
    controls = {k: calibrate(PREPARATIONS[k]) for k in ("positive", "negative")}
    groups = baseline["conditions"]
    if tuple(g["force_x_n"] for g in groups) != LOADS:
        raise ValueError("The reference load grid has changed")
    references = [(g["force_x_n"], c) for g in groups for c in g["cases"]]
    scenes = [sim.Scene(c["fault"], c["offset_mm"], 0.001, force_x_n=n) for n, c in references]
    modes = run_modes(scenes, references, timer_ticks)
    subsets = {"primary": [i for i, (n, _) in enumerate(references) if abs(n) <= 0.16],
               "strong": [i for i, (n, _) in enumerate(references) if abs(n) == 0.32]}
    for n in LOADS:
        subsets[str(n)] = [i for i, (force, _) in enumerate(references) if force == n]
    scores = {group: {b: scoreboard(modes, ids, b) for b in sim.LOAD_BUDGETS} for group, ids in subsets.items()}
    # The immediate traces and action outcomes already have a canonical copy in the same result file.
    for c in modes["immediate"]["cases"]:
        del c["trace"], c["rollouts"]
    return {"calibration": controls, "control_period_s": sim.PERIOD, "target_amplitude_mm": AMPLITUDE_M * 1000,
            "move_turn_return_decision_ticks": [START_TICK, TURN_TICK, RETURN_TICK, DECIDE_TICK],
            "camera_frame_pairs": FRAME_PAIRS, "camera_delay_ticks": 4, "seed": wrist.SEED, "repeats": REPEATS,
            "immediate_reference": "lateral_load.conditions[].cases", "modes": modes,
            "scores": scores, "primary_gate": primary_gate(scores["primary"]),
            "finer_step": finer_step(modes, timer_ticks)}


def probe_suite():
    result = sim.baseline_suite()
    result["source_sha256"]["active_probe.py"] = sim.sha((sim.ROOT / "active_probe.py").read_bytes())
    result["active_probe"] = run_probe(result["lateral_load"], result["grip_timing"]["calibrated_wait_ticks"])
    return result


if __name__ == "__main__":
    print(json.dumps(probe_suite(), indent=2, allow_nan=False))
