"""Compare fixed and observation-based recovery under matched lateral search paths."""

import argparse
import json
from pathlib import Path

import numpy as np

import active_probe as probe
import reference_transfer as ref
import relative_motion as camera
import servo_response as servo
import simulate as sim


PATHS = ((12, 1), (9, 1), (12, -1), (9, -1))
SEARCH_ACTIONS = ("search", "regrasp_search")


def scan_motion(samples, direction):
    """Summarize commands and wrist measurements during the lateral search, before entry."""
    if not samples:
        return None
    recorded = np.asarray(samples)
    ticks = recorded[:, 0].astype(int)
    result = {"scan_start_tick": int(ticks[0]), "last_sample_tick": int(ticks[-1])}
    for name, x in zip(("command", "wrist"), recorded[:, 1:].T * 1000, strict=True):
        crossings = ticks[direction * x <= -6.0 + 1e-9]
        result[name + "_range_mm"] = [round(float(x.min()), 6), round(float(x.max()), 6)]
        result[name + "_opposite_6mm_tick"] = int(crossings[0]) if len(crossings) else None
    return result


def frozen_condition(previous, gain, folds, source_refs):
    prior = previous["servo_response"]
    gains = {int(k): v for k, v in prior["conditions"].items()}
    calibrated = gain == servo.CHANGED_KV
    if calibrated:
        baseline = gains[gain]["cases"]
        evaluation = prior["calibrated_evaluation"]
        if not evaluation["executed"]:
            raise ValueError("This comparison requires the tested healthy-pin selector at the changed gain")
        target_refs = {m: ref.reference_signals(evaluation["normal_measurements"], m) for m in servo.MODES}
    else:
        archived = previous["active_probe"]["finer_step"]["modes"]
        baseline = {m: archived[m]["cases"] for m in servo.MODES}
        target_refs = source_refs

    choices = {}
    for m, cases in baseline.items():
        packed = dict(gains[gain]["raw_actions"][m])
        if calibrated:
            packed.update(evaluation["actions"][m])
        choices[m] = ref.choose(cases, folds[m], source_refs[m], target_refs[m], within=not calibrated)
        if ref.encode(choices[m]) != packed:
            raise ValueError("The pre-search choices or sensor repeats changed")
    return baseline, choices, target_refs


def matched_scenes(baseline, gain):
    scenes = []
    for i, case in enumerate(baseline["immediate"]):
        scene = sim.Scene(case["fault"], case["offset_mm"], servo.DT, force_x_n=case["load_n"], wrist_x_kv=gain)
        for mode in servo.MODES:
            expected = baseline[mode][i]
            if expected["case_id"] != i or scene.initial["state_sha256"] != expected["initial_sha256"]:
                raise ValueError("The search intervention must start from the matched physical state")
            sampler = camera.MarkerCamera(scene, probe.FRAME_TICKS)
            trace = sim.common_wrist_trace(scene, sampler.sample, probe.PREPARATIONS[mode])
            if sim.sha(np.asarray(trace, dtype="<f8").tobytes()) != expected["prefix_sha256"]:
                raise ValueError("Pre-search wrist or camera input changed")
        scenes.append(scene)
    return scenes


def path_trials(baseline, scenes, radius, direction, timer):
    archived = (radius, direction) == PATHS[0]
    domain, new_rollouts, fixed_motion = {}, {}, []
    for mode, cases in baseline.items():
        domain[mode] = []
        if not archived:
            new_rollouts[mode] = []
        for scene, case in zip(scenes, cases, strict=True):
            outcomes = dict(case["rollouts"])
            updates, motion = {}, {}
            for action in SEARCH_ACTIONS:
                observe = mode == "immediate" and action == "regrasp_search"
                if archived and not observe:
                    continue
                pair = {}
                for budget in sim.LOAD_BUDGETS:
                    samples = []
                    transition = sim.GripTransition(timer) if action == "regrasp_search" else None
                    row = sim.trial(scene, action, first_direction=direction, budget=budget, transition=transition,
                                    preparation=probe.PREPARATIONS[mode], scan_amplitude_m=radius / 1000,
                                    scan_sample=samples.append if observe else None)
                    if mode != "immediate" and row.pop("preparation_cost") != case["preparation_cost"]:
                        raise RuntimeError("Search geometry changed the cost before the decision")
                    pair[budget] = row
                    if observe:
                        motion[budget] = scan_motion(samples, direction)
                if archived and pair != case["rollouts"][action]:
                    raise RuntimeError("The published 12 mm positive-first fixed recovery did not replay")
                outcomes[action] = pair
                updates[action] = pair
            if mode == "immediate":
                fixed_motion.append(motion)
            if not archived:
                new_rollouts[mode].append(updates)
            domain[mode].append(dict(case, rollouts=outcomes))
    return domain, new_rollouts, fixed_motion


def score(domain, choices, calibrated):
    raw = {m: {k: a for k, a in values.items() if k.startswith("raw/")} for m, values in choices.items()}
    results = {}
    for budget in sim.LOAD_BUDGETS:
        ceiling = servo.headroom(domain, raw, budget)
        table = ref.outcome_table(domain, choices, budget)
        contrasts = ("single", "mean8") if calibrated else ("raw",)
        results[budget] = {
            "methods": {key: ref.method_summary(v) for key, v in table.items()},
            "positive_oracle": ceiling["frontiers"]["positive"],
            "possible_repeats": ceiling["possible_repeats"], "best_raw_by_repeat": ceiling["best_by_repeat"],
            "comparisons": {v: ref.comparison(table, "positive", v) for v in contrasts}}
    return results


def run(previous):
    timer = previous["grip_timing"]["calibrated_wait_ticks"]
    folds, source = servo.source_inputs(previous)
    result = {"timestep_s": servo.DT, "scan_speed_mm_s": 1000 * sim.SCAN_SPEED_M_S,
              "recovery_actions": list(ref.OPTIONS), "gains": {}}
    for gain in (servo.NOMINAL_KV, servo.CHANGED_KV):
        baseline, choices, target = frozen_condition(previous, gain, folds, source)
        scenes = matched_scenes(baseline, gain)
        paths = []
        for radius, direction in PATHS:
            domain, updates, motion = path_trials(baseline, scenes, radius, direction, timer)
            record = {"radius_mm": radius, "first_direction": direction,
                      "fixed_scan_motion": motion, "budgets": score(domain, choices, gain == servo.CHANGED_KV)}
            if updates:
                record["search_rollouts"] = updates
                record["live_positive"] = ref.check_live(
                    domain["positive"], choices["positive"], folds["positive"], source["positive"],
                    target["positive"], "positive", servo.DT, timer, wrist_x_kv=gain,
                    first_direction=direction, scan_amplitude_m=radius / 1000)
            paths.append(record)
        result["gains"][gain] = paths
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    stages = parser.add_mutually_exclusive_group()
    stages.add_argument("--servo-only", action="store_true", help="Replay the preceding servo experiment")
    stages.add_argument("--scan-only", action="store_true", help="Replay only the matched search-range experiment")
    args = parser.parse_args()
    if args.servo_only or args.scan_only:
        with Path("/pilot-reference.json").open() as f:
            archived = json.load(f)
        output = servo.run(archived) if args.servo_only else run(archived)
    else:
        output = servo.servo_suite()
        output["source_sha256"]["scan_range.py"] = sim.sha((sim.ROOT / "scan_range.py").read_bytes())
        output["scan_range"] = run(output)
    print(json.dumps(output, indent=2, allow_nan=False))
