"""Measure how much a recovery choice can gain when horizontal servo damping changes."""

import argparse
import json
from pathlib import Path

import numpy as np

import active_probe as probe
import reference_transfer as ref
import simulate as sim


DT = 0.0005
NOMINAL_KV, CHANGED_KV = 28, 35
MODES = ("immediate", "hold", "positive")
SOURCE_FOLDS = "f2b14a27eb6b2765935f8167ccdf76da7ced7089e80e7e7571138550d5f84d26"
SOURCE_NORMAL = "7868d0b0c86ae6e8429ddf7b259d7a89805ca25266d7da7c9e021d3b2b0fac9d"


def digest(value):
    return sim.sha(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode())


def source_inputs(result):
    def extract(reference):
        folds = {m: reference["folds"]["0.5ms"][m] for m in MODES}
        records = {m: reference["calibration"]["0.5ms"][m] for m in ("hold", "positive")}
        return folds, records

    folds, records = extract(result["normal_reference"])
    if (digest(folds), digest(records)) != (SOURCE_FOLDS, SOURCE_NORMAL):
        # Keep the original policy and source measurements on other architectures.
        with Path("/pilot-reference.json").open() as f:
            folds, records = extract(json.load(f)["normal_reference"])
        if (digest(folds), digest(records)) != (SOURCE_FOLDS, SOURCE_NORMAL):
            raise ValueError("The frozen 0.5 ms training values or source calibration changed")
    folds = {m: {int(k): v for k, v in values.items()} for m, values in folds.items()}
    return folds, {m: ref.reference_signals(records, m) for m in MODES}


def physical_trials(kv, timer):
    scenes, references, starts = [], [], []
    for load in ref.LOADS:
        group, cases = sim.wrist_scenes(DT, marker_camera=True, force_x_n=load, wrist_x_kv=kv)
        for scene, case in zip(group, cases, strict=True):
            sim.run_load_actions(scene, case, load, timer)
            starts.append(dict(scene.initial, kinematic_sha256=case["kinematic_start_sha256"]))
            references.append((load, case))
        scenes.extend(group)
    domain = {}
    for mode in MODES:
        cases = probe.collect_cases(scenes, references, probe.PREPARATIONS[mode], timer)
        for case in cases:
            del case["live_checks"]  # Replays of the frozen selector are recorded separately.
        domain[mode] = cases
    return domain, starts


def check_nominal(domain, archived):
    for mode, cases in domain.items():
        for c, old in zip(cases, archived[mode]["cases"], strict=True):
            if digest(c) != digest({k: old[k] for k in c}):
                raise RuntimeError(f"Nominal replay disagrees with the prior {mode} case {c['case_id']}")


def time_frontier(cases, budget):
    """Exact minimum total scored ticks for each attainable number of successes."""
    frontier = {0: 0}
    oracle = []
    for c in cases:
        rows = [c["rollouts"][a][budget] for a in ref.OPTIONS]
        best = max(range(len(rows)), key=lambda i: (rows[i]["success"], -rows[i]["scored_s"]))
        oracle.append(ref.CODES[best])
        next_frontier = {}
        for row in rows:
            ticks = round(row["scored_s"] / DT)
            for count, total in frontier.items():
                n = count + int(row["success"])
                value = total + ticks
                if n not in next_frontier or value < next_frontier[n]:
                    next_frontier[n] = value
        frontier = next_frontier
    means = {n: round(ticks * DT / len(cases), 9) for n, ticks in sorted(frontier.items())}
    return {"max_success": max(means), "fastest_action_by_case": "".join(oracle), "min_mean_s_by_success": means}


def headroom(domain, raw, budget):
    table = ref.outcome_table(domain, raw, budget)
    frontiers = {mode: time_frontier(cases, budget) for mode, cases in domain.items()}
    active = frontiers["positive"]
    n = len(domain["positive"])
    capture = ref.SETTLING_S + probe.DECIDE_TICK * sim.PERIOD
    per_case = {"free": 0.0, "single": capture / n, "mean8": ref.DRAWS * capture / n}
    repetitions = []
    for rep in range(probe.REPEATS):
        def rank(key):
            return int(table[key].ok[0, rep].sum()), -table[key].charged_time(0, rep)

        best = max(table, key=rank)
        successes, negative_time = rank(best)
        gain = active["max_success"] - successes
        tie = active["min_mean_s_by_success"].get(successes)
        possible = {k: gain >= 2 or (tie is not None and -negative_time - (tie + cost) >= 0.20 - 1e-9)
                    for k, cost in per_case.items()}
        repetitions.append({"best_control": best, "control_success": successes,
                            "control_mean_s": round(-negative_time, 9), "extra_successes": gain,
                            "min_mean_at_tie_s": tie, "could_pass": possible})
    return {"frontiers": frontiers, "best_by_repeat": repetitions,
            "possible_repeats": {k: sum(r["could_pass"][k] for r in repetitions) for k in per_case},
            "setup_s_per_case": per_case, "methods": {k: ref.method_summary(v) for k, v in table.items()}}


def choice_replays(domain, choices, folds, source, target, timer):
    return {m: ref.check_live(domain[m], choices[m], folds[m], source[m], target[m], m, DT, timer,
                              wrist_x_kv=CHANGED_KV) for m in MODES}


def run(previous):
    timer = previous["grip_timing"]["calibrated_wait_ticks"]
    if timer != 5:
        raise ValueError("Expected the frozen 0.05 s combined recovery")
    folds, source = source_inputs(previous)
    calibration = {}
    for kv in (NOMINAL_KV, CHANGED_KV):
        clean = sim.Scene("clean", 0, DT, force_x_n=0.0, wrist_x_kv=kv)
        calibration[kv] = probe.calibrate(probe.PREPARATIONS["positive"], clean)
    result = {"timestep_s": DT, "nominal_kv": NOMINAL_KV, "changed_kv": CHANGED_KV,
              "frozen_folds_sha256": SOURCE_FOLDS, "source_measurements_sha256": SOURCE_NORMAL,
              "clean_excursion": calibration, "conditions": {}}
    for kv in (NOMINAL_KV, CHANGED_KV):
        domain, starts = physical_trials(kv, timer)
        raw = {m: ref.choose(domain[m], folds[m], source[m], source[m], False, variants=("raw",)) for m in MODES}
        record = {"starting_states": starts, "raw_actions": {m: ref.encode(v) for m, v in raw.items()},
                  "budgets": {b: headroom(domain, raw, b) for b in sim.LOAD_BUDGETS}}
        result["conditions"][kv] = record
        if kv == NOMINAL_KV:
            check_nominal(domain, previous["active_probe"]["finer_step"]["modes"])
            nominal_starts = starts
        else:
            record["cases"] = domain
    for field, tol in (("relative_error_m", 0.0001), ("depth_m", 0.0001), ("rim_normal_n", 0.15)):
        if any(abs(a[field] - b[field]) > tol for a, b in zip(nominal_starts, starts, strict=True)):
            raise ValueError(f"The matched gain conditions started with different {field}")

    upper = record["budgets"]["all_contacts"]["possible_repeats"]
    open_gate = max(upper["single"], upper["mean8"]) > probe.REPEATS // 2
    result["calibrated_evaluation"] = {"executed": open_gate}
    if not open_gate:
        result["live_checks"] = choice_replays(domain, raw, folds, source, source, timer)
        return result

    records = ref.normal_measurements(2, DT, wrist_x_kv=CHANGED_KV, modes=("hold", "positive"))
    target = {m: ref.reference_signals(records, m) for m in MODES}
    choices = {m: ref.choose(domain[m], folds[m], source[m], target[m], False) for m in MODES}
    for mode in MODES:
        if not all(np.array_equal(arr, choices[mode][k]) for k, arr in raw[mode].items()):
            raise RuntimeError("A raw baseline changed after the sequential gate")
    result["live_checks"] = choice_replays(domain, choices, folds, source, target, timer)
    evaluation = result["calibrated_evaluation"]
    evaluation["normal_measurements"] = records
    evaluation["actions"] = {m: ref.encode({k: a for k, a in v.items() if not k.startswith("raw/")})
                             for m, v in choices.items()}
    evaluation["budgets"] = {}
    for budget in sim.LOAD_BUDGETS:
        table = ref.outcome_table(domain, choices, budget)
        evaluation["budgets"][budget] = {
            "methods": {k: ref.method_summary(v) for k, v in table.items() if k.split("/")[1] not in ("fixed", "raw")},
            "comparisons": {v: ref.comparison(table, "positive", v) for v in ("single", "mean8", "ideal")}}
    return result


def servo_suite():
    output = ref.reference_suite()
    output["source_sha256"]["servo_response.py"] = sim.sha((sim.ROOT / "servo_response.py").read_bytes())
    output["servo_response"] = run(output)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--servo-only", action="store_true", help="Replay this stage against the mounted registry result")
    args = parser.parse_args()
    if args.servo_only:
        with Path("/pilot-reference.json").open() as f:
            output = run(json.load(f))
    else:
        output = servo_suite()
    print(json.dumps(output, indent=2, allow_nan=False))
