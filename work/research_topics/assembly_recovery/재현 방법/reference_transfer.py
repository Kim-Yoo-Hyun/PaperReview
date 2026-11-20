"""Transfer a peg-recovery selector using wrist measurements of a normally retained pin."""

import json
from typing import NamedTuple

import numpy as np

import active_probe as probe
import relative_motion as camera
import simulate as sim
import wrist_observation as wrist


STEPS = {"1ms": 0.001, "0.5ms": 0.0005}
LOADS = (-0.16, 0.0, 0.16)
BANKS = DRAWS = 8
SETTLING_S = 0.40
OPTIONS = sim.LOAD_OPTIONS
CODES = ("R", "S", "F")
VARIANTS = ("raw", "single", "mean8", "ideal")


def normal_measurements(domain_index, dt, *, wrist_x_kv=None, modes=("hold", "positive", "negative")):
    records = {}
    encoder = camera.WRIST_ENCODER
    for name in modes:
        mode_index = ("hold", "positive", "negative").index(name)
        prep = probe.PREPARATIONS[name]
        recordings = []
        for bank in range(BANKS):
            counts = []
            for draw in range(DRAWS):
                scene = sim.Scene("clean", 0, dt, force_x_n=0.0, wrist_x_kv=wrist_x_kv)
                start = scene.restore()
                if start.xfrc_applied.any() or abs(start.qpos[scene.inhand]) > 1e-8:
                    raise RuntimeError("The reference pin must be centered and unloaded")
                positions = np.asarray(sim.common_wrist_trace(scene, preparation=prep))
                if bank == 0 and draw == 0:
                    reference = positions.copy()
                    if name != "hold" and (np.max(prep.direction * reference[:, 0]) < 2.0
                                           or abs(reference[-1, 0]) > 0.35):
                        raise RuntimeError("Normal reference did not complete the prescribed excursion")
                elif not np.array_equal(reference, positions):
                    raise RuntimeError("A repeated calibration changed the normal pin trajectory")
                measured = encoder.measure(positions, 70 + domain_index, mode_index, bank * DRAWS + draw)
                counts.append(np.rint(measured[:, 0] / encoder.quantum_mm).astype(int).tolist())
            recordings.append(counts)
        records[name] = {"initial_sha256": scene.initial["state_sha256"], "wrist_xz_mm": reference.tolist(),
                         "x_encoder_counts": recordings}
    return records


def reference_signals(records, mode):
    rec = records["hold"] if mode == "immediate" else records[mode]
    ticks = 1 + (sim.CLOSE_TICK if mode == "immediate" else probe.DECIDE_TICK)
    counts = np.asarray(rec["x_encoder_counts"])[:, :, :ticks]
    measured = counts * camera.WRIST_ENCODER.quantum_mm
    measured -= measured.mean(axis=2, keepdims=True)
    ideal = camera.centered(np.asarray(rec["wrist_xz_mm"])[:ticks, 0])
    return {"raw": np.zeros((1, ticks)), "ideal": ideal[None, :], "single": measured[:, 0, :],
            "mean8": measured.mean(axis=1)}


def matched_cases(previous):
    experiment = previous["active_probe"]
    fine = experiment["finer_step"]
    archived = [c for g in previous["lateral_load"]["conditions"] for c in g["cases"]]
    domains = {name: {} for name in STEPS}
    ids = fine["source_case_ids"]
    for name in probe.PREPARATIONS:
        coarse = experiment["modes"][name]["cases"]
        fine_cases = fine["modes"][name]["cases"]
        pairs = []
        for i, (original_id, target) in enumerate(zip(ids, fine_cases, strict=True)):
            case = dict(coarse[original_id], case_id=i)
            if name == "immediate":
                case.update(trace=archived[original_id]["trace"], rollouts=archived[original_id]["rollouts"])
            if (target["case_id"] != i or
                    any(case[k] != target[k] for k in ("index", "load_n", "offset_mm", "fault"))):
                raise ValueError("Source and target scenes do not match")
            pairs.append(case)
        if len(pairs) != 48 or {c["load_n"] for c in pairs} != set(LOADS):
            raise ValueError("Expected the full common three-load grid")
        domains["1ms"][name] = pairs
        domains["0.5ms"][name] = fine_cases
    return domains


def compile_folds(folds):
    """Keep original class/load order, variances and probability cutoff from probe.select."""
    result = {}
    for held, fold in folds.items():
        groups = [fold["templates"][fault] for fault in ("slip", "fixture")]
        result[held] = (np.asarray([[g["wrist_mm"] for g in group] for group in groups]),
                        np.asarray([[g["relative_mm"] for g in group] for group in groups]))
    return result


def classify(enc, flow, templates):
    """Score the camera once and the wrist for every independent reference setup."""
    wx, pixel = templates
    wrist_loss = np.sum((enc[:, None, None, :] - wx)**2, axis=-1) / camera.WRIST_VARIANCE
    visible = np.isfinite(flow)
    image_loss = np.sum((flow[visible] - pixel[:, :, visible])**2, axis=-1) / camera.FLOW_VARIANCE
    outcomes = {}
    for name, loss in (("both", wrist_loss + image_loss), ("wrist", wrist_loss), ("camera", image_loss[None, :])):
        scores = np.logaddexp.reduce(-0.5 * loss, axis=-1)
        odds = scores[:, 0] - scores[:, 1]
        selected = np.full(len(odds), OPTIONS.index("regrasp_search"), np.uint8)
        selected[odds >= camera.LOG_ODDS_THRESHOLD] = OPTIONS.index("regrasp")
        selected[odds <= -camera.LOG_ODDS_THRESHOLD] = OPTIONS.index("search")
        outcomes[name] = selected
    return outcomes


def choose(cases, folds, source_refs, target_refs, within, *, variants=VARIANTS):
    fitted = compile_folds(folds)
    choices = {}
    if within and any(np.any(source_refs[v] - target_refs[v]) for v in VARIANTS):
        raise ValueError("A within-domain reference must cancel point by point")
    if within:
        variants = ("raw",)
    shifts = {v: source_refs[v] - target_refs[v] for v in variants}
    for v, delta in shifts.items():
        for ch in (probe.CHANNELS if v == "raw" else ("both", "wrist")):
            choices[v + "/" + ch] = np.empty((len(delta), probe.REPEATS, len(cases)), np.uint8)
    for c in cases:
        held = abs(c["offset_mm"])
        for rep in range(probe.REPEATS):
            enc, flow = probe.observation(c["trace"], c["index"], rep, 1)
            for v, delta in shifts.items():
                # (target reading - target normal) - (training mean - source normal).
                selected = classify(enc + delta, flow, fitted[held])
                for ch, actions in selected.items():
                    if ch != "camera" or v == "raw":
                        choices[v + "/" + ch][:, rep, c["case_id"]] = actions
    return choices


def encode(choices):
    return {key: [["".join(CODES[a] for a in row) for row in bank] for bank in actions]
            for key, actions in choices.items()}


def check_live(cases, choices, folds, src, dst, mode, dt, timer_ticks, *, wrist_x_kv=None,
               first_direction=1, scan_amplitude_m=sim.SCAN_AMPLITUDE_M):
    prep = probe.PREPARATIONS[mode]
    checks = []
    for c in cases:
        i = c["case_id"]
        first = {}
        # Prioritize primary calibrated policies, then cover any additional actions from the controls.
        primary = tuple(k for k in ("single/both", "mean8/both") if k in choices)
        for key in (*primary, *(k for k in choices if k not in primary)):
            cube = choices[key]
            for act in np.unique(cube[:, :, i]):
                if int(act) not in first:
                    bank, rep = np.argwhere(cube[:, :, i] == act)[0]
                    first[int(act)] = (key, int(bank), int(rep))
        witnesses = [(act, *info) for act, info in first.items()]
        for key in primary:
            if not any(w[1] == key for w in witnesses):
                witnesses.append((int(choices[key][0, 0, i]), key, 0, 0))
        scene = sim.Scene(c["fault"], c["offset_mm"], dt, force_x_n=c["load_n"], wrist_x_kv=wrist_x_kv)
        if scene.initial["state_sha256"] != c["initial_sha256"]:
            raise ValueError("Live recovery must start from the archived physical state")
        for act, key, bank, rep in witnesses:
            variant, channel = key.split("/")
            templates = folds[abs(c["offset_mm"])]["templates"]
            # Explicit residuals and the scalar selector also check the batched scoring formula.
            residual = {fault: [dict(g, wrist_mm=np.asarray(g["wrist_mm"]) - src[variant][bank])
                                for g in groups] for fault, groups in templates.items()}

            def selector(trace):
                enc, flow = probe.observation(trace, c["index"], rep, 1)
                return probe.select((enc - dst[variant][bank], flow), residual, channel)

            for budget in sim.LOAD_BUDGETS:
                sampler = camera.MarkerCamera(scene, probe.FRAME_TICKS)
                row = sim.trial(scene, "wrist_choice", first_direction=first_direction, budget=budget,
                                wrist_selector=selector, sample=sampler.sample, fallback_ticks=timer_ticks,
                                preparation=prep, scan_amplitude_m=scan_amplitude_m)
                decision = row.pop("wrist_decision")
                if decision != {"action": OPTIONS[act], "prefix_sha256": c["prefix_sha256"]}:
                    raise RuntimeError("A live residual decision or observation trace changed")
                if prep is not None and row.pop("preparation_cost") != c["preparation_cost"]:
                    raise RuntimeError("Live preparation cost differs from the archived trial")
                if row != c["rollouts"][OPTIONS[act]][budget]:
                    raise RuntimeError("Live recovered trajectory differs from its archived action")
        checks.append([[CODES[act], key, bank, rep] for act, key, bank, rep in witnesses])
    return checks


class Outcomes(NamedTuple):
    ok: np.ndarray
    mean_time: np.ndarray
    setup_s: float

    def charged_time(self, bank, rep):
        return float(self.mean_time[bank, rep]) + self.setup_s / self.ok.shape[-1]


def outcome_table(domain, choices, budget):
    table = {}
    for mode, policies in choices.items():
        cases = domain[mode]
        n = len(cases)
        samples = [[c["rollouts"][a][budget] for a in OPTIONS] for c in cases]
        ok = np.asarray([[r["success"] for r in row] for row in samples])
        seconds = np.asarray([[r["scored_s"] for r in row] for row in samples])
        decision_s = sim.PERIOD * (sim.CLOSE_TICK if mode == "immediate" else probe.DECIDE_TICK)
        for a, action in enumerate(OPTIONS):
            fixed = np.full((1, probe.REPEATS, n), a)
            table[mode + "/fixed/" + action] = Outcomes(ok[np.arange(n), fixed],
                                                        seconds[np.arange(n), fixed].mean(axis=2), 0.)
        for key, selected in policies.items():
            variant = key.split("/")[0]
            count = {"raw": 0, "single": 1, "mean8": DRAWS, "ideal": 1}[variant]
            table[mode + "/" + key] = Outcomes(ok[np.arange(n), selected],
                                               seconds[np.arange(n), selected].mean(axis=2),
                                               count * (SETTLING_S + decision_s))
    return table


def method_summary(out):
    return {"success_by_setup_and_repeat": out.ok.sum(axis=2).tolist(), "success": int(out.ok.sum()),
            "assignments": out.ok.size, "mean_scored_s": round(float(out.mean_time.mean()), 6),
            "setup_s": round(out.setup_s, 5),
            "amortized_s": round(float(out.mean_time.mean() + out.setup_s / out.ok.shape[-1]), 6)}


def comparison(table, mode, variant):
    selected_key = mode + "/" + variant + "/both"
    selected = table[selected_key]
    controls = []
    for key in table:
        if key == selected_key:
            continue
        prep, method, _ = key.split("/")
        if (prep in ("immediate", "hold") and method in ("fixed", "raw", variant)
                or prep == mode and method in ("fixed", "raw")):
            controls.append(key)
    fixed = "fixed/regrasp_search"
    pairs = {"same_raw": mode + "/raw/both", "same_fixed": mode + "/" + fixed,
             "immediate_fixed": "immediate/" + fixed, "hold_choice": "hold/" + variant + "/both"}
    totals = {label: {"gained": 0, "lost": 0, "seconds_saved": 0.0} for label in ("best", *pairs)}
    best_controls, passed = [], []
    for bank in range(len(selected.ok)):
        winners, gates = [], []
        for rep in range(probe.REPEATS):
            def rank(key):
                other = table[key]
                b = bank if len(other.ok) > 1 else 0
                return int(other.ok[b, rep].sum()), -other.charged_time(b, rep)

            winner = max(controls, key=rank)
            winners.append(winner)
            for label, key in {"best": winner, **pairs}.items():
                other = table[key]
                b = bank if len(other.ok) > 1 else 0
                success, ref = selected.ok[bank, rep], other.ok[b, rep]
                good, lost = int((success & ~ref).sum()), int((ref & ~success).sum())
                saved = other.charged_time(b, rep) - selected.charged_time(bank, rep)
                totals[label]["gained"] += good
                totals[label]["lost"] += lost
                totals[label]["seconds_saved"] += saved
                if label == "best":
                    gates.append(good - lost >= 2 or (good == lost and saved >= 0.20 - 1e-9))
        best_controls.append(winners)
        passed.append(gates)
    for value in totals.values():
        value["seconds_saved"] = round(value["seconds_saved"] / selected.mean_time.size, 6)
    passing_banks = sum(sum(row) > probe.REPEATS // 2 for row in passed)
    return {"paired": totals, "best_controls": best_controls, "pass_by_setup_and_repeat": passed,
            "passing_setups": passing_banks, "majority": passing_banks > len(passed) // 2}


def transfer(source, target, domains, trained, refs, timer_ticks):
    within = source == target
    decisions, live = {}, {}
    for mode, cases in domains[target].items():
        folds = trained[source][mode]
        src, dst = refs[source][mode], refs[target][mode]
        decisions[mode] = choose(cases, folds, src, dst, within)
        if not within:
            live[mode] = check_live(cases, decisions[mode], folds, src, dst, mode, STEPS[target], timer_ticks)
    scores = {}
    for budget in sim.LOAD_BUDGETS:
        table = outcome_table(domains[target], decisions, budget)
        result = {"methods": {key: method_summary(out) for key, out in table.items()}}
        if not within:
            result["comparisons"] = {mode: {v: comparison(table, mode, v) for v in ("single", "mean8", "ideal")}
                                     for mode in ("positive", "negative")}
        scores[budget] = result
    return {"source": source, "target": target, "scores": scores, "actions": {m: encode(v) for m, v in decisions.items()},
            "live_checks": live}


def run(previous):
    records = {d: normal_measurements(i, dt) for i, (d, dt) in enumerate(STEPS.items())}
    refs = {d: {m: reference_signals(rec, m) for m in probe.PREPARATIONS} for d, rec in records.items()}
    domains = matched_cases(previous)
    trained = {d: {m: {held: probe.fit(cases, held, loads=LOADS) for held in (3, 5, 7, 9)}
                   for m, cases in modes.items()} for d, modes in domains.items()}
    timer = previous["grip_timing"]["calibrated_wait_ticks"]
    experiments = {s + "_to_" + t: transfer(s, t, domains, trained, refs, timer) for s in STEPS for t in STEPS}
    return {"common_loads_n": LOADS, "settling_s_per_capture": SETTLING_S, "calibration_sets": BANKS,
            "captures_per_set": DRAWS, "sensor_repeats": probe.REPEATS, "action_codes": dict(zip(CODES, OPTIONS)),
            "case_ids_in_active_probe": previous["active_probe"]["finer_step"]["source_case_ids"],
            "calibration": records, "folds": trained, "transfers": experiments}


def reference_suite():
    previous = probe.probe_suite()
    previous["source_sha256"]["reference_transfer.py"] = sim.sha((sim.ROOT / "reference_transfer.py").read_bytes())
    previous["normal_reference"] = run(previous)
    return previous


if __name__ == "__main__":
    print(json.dumps(reference_suite(), indent=2, allow_nan=False))
