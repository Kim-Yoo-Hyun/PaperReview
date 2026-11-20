"""Headless paired trials of a two-link arm opening a drawer with a frictional shoe."""

import argparse
import hashlib
import itertools
import json
import math
import platform
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from statistics import mean

import mujoco
import numpy as np


ROOT = Path(__file__).resolve().parent
VARIANTS = ("coupled", "uncoupled")
RESETS = ("ordinary", "reference")
OPEN_TARGET_M = 0.060
SUCCESS_M = 0.045
OPEN_TIME_S = 0.8
CLOSE_TIME_S = 1.0
RESET_TIME_S = 0.6
EARLY_TIME_S = 0.2
START_TOL_MM = 0.5
START_SPEED_TOL_MM_S = 1.0


@dataclass(frozen=True)
class Policy:
    force_limit_n: float
    return_target_m: float


POLICIES = {"A": Policy(5.5, 0.0), "B": Policy(9.0, -0.026)}


class Drawer:
    def __init__(self, variant, rail_friction, shoe_friction, timestep_ms):
        model = mujoco.MjModel.from_xml_path(str(ROOT / "drawer.xml"))
        self.model = model
        model.opt.timestep = timestep_ms / 1000
        self.drawer = model.joint("drawer").qposadr.item()
        self.shoe = model.joint("shoe").qposadr.item()
        self.drawer_dof = model.joint("drawer").dofadr.item()
        model.dof_frictionloss[self.drawer_dof] = rail_friction
        model.dof_frictionloss[model.joint("shoe").dofadr.item()] = shoe_friction
        self.coupling = model.tendon("coupling").id
        if variant == "uncoupled":
            model.tendon_stiffness[self.coupling] = 0
        self.hand = model.site("hand").id
        self.arm_dofs = [model.joint(name).dofadr.item() for name in ("shoulder", "elbow")]
        self.jac = np.zeros((3, model.nv))
        self.drawer_hold = model.equality("center_drawer").id
        self.shoe_hold = model.equality("center_shoe").id

    def steps(self, duration_s):
        return round(duration_s / self.model.opt.timestep)

    def move(self, data, target_m, force_limit, duration_s):
        # The policy only sees hand pose and velocity, via the two arm encoders.
        # The shoe, spring force, reset label and previous policy are never inputs.
        ref_x = self.model.body("drawer_body").pos[0]
        early_step = self.steps(EARLY_TIME_S)
        early_x_mm = None
        max_x = data.qpos[self.drawer]
        for step in range(1, self.steps(duration_s) + 1):
            mujoco.mj_step1(self.model, data)
            mujoco.mj_jacSite(self.model, data, self.jac, None, self.hand)
            hand_x = data.site_xpos[self.hand, 0] - ref_x
            jac_x = self.jac[0, self.arm_dofs]
            hand_velocity = jac_x @ data.qvel[self.arm_dofs]
            force = 260 * (target_m - hand_x) - 10 * hand_velocity
            data.ctrl[:] = jac_x * min(force_limit, max(-force_limit, force))
            mujoco.mj_step2(self.model, data)
            x = data.qpos[self.drawer]
            max_x = max(max_x, x)
            if step == early_step:
                early_x_mm = float(1000 * x)
        return bool(max_x >= SUCCESS_M), early_x_mm

    def trial_pair(self, previous, current, reset, matched_close):
        model = self.model
        data = mujoco.MjData(model)  # Every pair starts independently at the reference state.
        previous_opened, _ = self.move(data, OPEN_TARGET_M, previous.force_limit_n, OPEN_TIME_S)
        closer = POLICIES["A"] if matched_close else previous
        self.move(data, closer.return_target_m, closer.force_limit_n, CLOSE_TIME_S)
        data.ctrl[:] = 0
        data.eq_active[self.drawer_hold] = 1
        data.eq_active[self.shoe_hold] = int(reset == "reference")
        mujoco.mj_step(model, data, nstep=self.steps(RESET_TIME_S))
        data.eq_active[self.drawer_hold] = 0
        data.eq_active[self.shoe_hold] = 0
        mujoco.mj_forward(model, data)
        start_mm = 1000 * data.qpos[self.drawer]
        speed_mm_s = 1000 * data.qvel[self.drawer_dof]
        resistance = model.tendon_stiffness[self.coupling] * (data.qpos[self.drawer] - data.qpos[self.shoe])
        success, early_mm = self.move(data, OPEN_TARGET_M, current.force_limit_n, OPEN_TIME_S)
        if np.any(data.warning.number) or not np.all(np.isfinite(data.qpos)):
            raise RuntimeError("MuJoCo warning or non-finite position")
        return {
            "previous_opened": previous_opened,
            "start_mm": round(float(start_mm), 6),
            "start_speed_mm_s": round(float(speed_mm_s), 6),
            "start_in_tolerance": bool(abs(start_mm) <= START_TOL_MM and abs(speed_mm_s) <= START_SPEED_TOL_MM_S),
            "spring_resistance_n": round(float(resistance), 6),
            "travel_at_200ms_mm": round(early_mm, 6),
            "current_success": success,
        }


def summarize(rows):
    results = {}
    for variant in VARIANTS:
        selected = [r for r in rows if r["variant"] == variant]
        cells = {}
        contrasts = {}
        policy_gaps = {}
        for reset in RESETS:
            for current in POLICIES:
                means = {}
                for previous in POLICIES:
                    cell = [r for r in selected if (r["previous"], r["current"], r["reset"]) == (previous, current, reset)]
                    means[previous] = {k: mean(r[k] for r in cell) for k in ("spring_resistance_n", "travel_at_200ms_mm", "current_success")}
                    cells[f"{previous}{current}/{reset}"] = {"successes": sum(r["current_success"] for r in cell), "pairs": len(cell)}
                contrasts[f"{current}/{reset}"] = {k: round(means["B"][k] - means["A"][k], 6) for k in means["A"]}
            # Every cell has the same block count; average over a 50:50 predecessor mix.
            rates = [mean(r["current_success"] for r in selected if r["reset"] == reset and r["current"] == p) for p in POLICIES]
            policy_gaps[reset] = round(rates[1] - rates[0], 6)
        results[variant] = {
            "pairs": len(selected),
            "outside_start_tolerance": sum(not r["start_in_tolerance"] for r in selected),
            "max_abs_start_mm": max(abs(r["start_mm"]) for r in selected),
            "max_abs_start_speed_mm_s": max(abs(r["start_speed_mm_s"]) for r in selected),
            "cells": cells,
            "previous_B_minus_A_by_current_and_reset": contrasts,
            "current_B_minus_A_success_rate": policy_gaps,
        }
    return results


def run(args):
    parameters = random.Random(args.seed)
    order = random.Random(args.seed + 1)
    rows = []
    blocks = []
    for block in range(1, args.blocks + 1):
        rail = round(parameters.uniform(0.7, 1.1), 6)
        shoe = round(parameters.uniform(1.7, 2.3), 6)
        blocks.append({"block": block, "rail_friction_n": rail, "shoe_friction_n": shoe})
        schedule = list(itertools.product(POLICIES, POLICIES, RESETS))
        order.shuffle(schedule)
        for variant in VARIANTS:
            drawer = Drawer(variant, rail, shoe, args.timestep_ms)
            for slot, (previous, current, reset) in enumerate(schedule, 1):
                obs = drawer.trial_pair(POLICIES[previous], POLICIES[current], reset, args.matched_close)
                rows.append(dict(variant=variant, block=block, slot=slot, previous=previous, current=current, reset=reset, **obs))
    return {
        "evidence": "simulation_only",
        "environment": {"python": platform.python_version(), "mujoco": mujoco.__version__, "numpy": np.__version__, "architecture": platform.machine()},
        "sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in ("simulate.py", "drawer.xml", "Dockerfile")},
        "seed": args.seed, "timestep_ms": args.timestep_ms, "matched_close": args.matched_close, "blocks": blocks,
        "summary": summarize(rows), "pairs": rows,
    }


def check(report):
    if report["evidence"] != "simulation_only" or not report["blocks"]:
        raise ValueError("Expected a nonempty simulation run")
    block_ids = [b["block"] for b in report["blocks"]]
    expected = set(itertools.product(VARIANTS, block_ids, POLICIES, POLICIES, RESETS))
    rows = report["pairs"]
    keys = [(r["variant"], r["block"], r["previous"], r["current"], r["reset"]) for r in rows]
    if len(set(block_ids)) != len(block_ids) or set(keys) != expected or len(keys) != len(expected):
        raise ValueError("Missing or repeated block or trial assignment")
    for r in rows:
        for name in ("start_mm", "start_speed_mm_s", "spring_resistance_n", "travel_at_200ms_mm"):
            if not math.isfinite(r[name]):
                raise ValueError(f"Invalid {name}")
        if any(type(r[k]) is not bool for k in ("previous_opened", "current_success", "start_in_tolerance")):
            raise ValueError("Invalid gate or success flag")
    if report["summary"] != summarize(rows):
        raise ValueError("Recorded summaries disagree with trial pairs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    simulate = sub.add_parser("run")
    simulate.add_argument("--blocks", type=int, default=6)
    simulate.add_argument("--seed", type=int, default=20261119)
    simulate.add_argument("--timestep-ms", type=int, choices=(1, 2), default=2)
    simulate.add_argument("--matched-close", action="store_true")
    sub.add_parser("check", help="Read a simulation report on stdin and validate cells and summaries")
    args = parser.parse_args()
    if args.command == "check":
        checked = json.load(sys.stdin)
        if "primary" in checked:
            import door_probe

            for name, step, matched in (("primary", 2, False), ("half_step", 1, False), ("matched_close", 2, True)):
                result = checked[name]
                check(result)
                if (result["timestep_ms"], result["matched_close"]) != (step, matched):
                    raise ValueError(f"Unexpected settings in {name}")
                if (result["seed"], result["blocks"]) != (checked["primary"]["seed"], checked["primary"]["blocks"]):
                    raise ValueError("Control runs must reuse the primary parameter blocks")
            fixture = checked["public_door"]
            if (fixture["asset_sha256"], fixture["revision"]) != (door_probe.ASSET_HASH, door_probe.REVISION):
                raise ValueError("Unexpected public fixture revision")
            conditions = [(r["handle_target_rad"], r["reset"], r["dwell_s"]) for r in fixture["states"]]
            if sorted(conditions) != sorted(itertools.product((-0.6, 0.6), RESETS, (0.6, 3.0))):
                raise ValueError("Incomplete public fixture measurements")
            print(f"Verified {len(checked['primary']['pairs'])} primary pairs, two matched control runs and eight public fixture states")
        else:
            check(checked)
            print(f"Verified {len(checked['pairs'])} simulated pairs")
    else:
        if args.blocks < 1:
            parser.error("--blocks must be positive")
        report = run(args)
        check(report)
        json.dump(report, sys.stdout, allow_nan=False, ensure_ascii=False, indent=2)
        print()
