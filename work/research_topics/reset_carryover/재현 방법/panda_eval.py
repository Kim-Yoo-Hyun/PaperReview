"""Blocked replay of the 2020 robosuite Panda Door evaluation policies (CPU)."""

import argparse
import hashlib
import json
import multiprocessing
import os
import platform
import random
from collections import Counter
from pathlib import Path
from statistics import mean

import mujoco_py
import numpy as np
import pkg_resources
import robosuite as suite
import torch
from robosuite.controllers import load_controller_config
from robosuite.wrappers import GymWrapper


SCENES = (1101, 1102, 1103, 1104)
POLICIES = (17, 59)
WAITS = (0.6, 3.0)
RESETS = ("panel", "angle", "angle_speed", "fresh")
ROOT = Path("/panda")
HORIZON = 500


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vectors_hash(*arrays):
    h = hashlib.sha256()
    for arr in arrays:
        h.update(np.asarray(arr, dtype="<f8").tobytes())
    return h.hexdigest()


def load_policies():
    torch.set_num_threads(1)
    return {n: torch.load(str(ROOT / str(n) / "params.pkl"), map_location="cpu")["evaluation/policy"]
            for n in POLICIES}


def make_env():
    configs = [json.loads((ROOT / str(p) / "variant.json").read_text())["eval_environment_kwargs"] for p in POLICIES]
    if configs[0] != configs[1] or configs[0]["horizon"] != HORIZON:
        raise ValueError("Incompatible evaluation configurations")
    config = configs[0]
    controller = load_controller_config(default_controller=config.pop("controller"))
    config.update(hard_reset=True, has_renderer=False, has_offscreen_renderer=False,
                  use_object_obs=True, use_camera_obs=False, reward_shaping=True)
    return GymWrapper(suite.make(controller_configs=controller, **config))


def start_scene(wrapped, scene):
    np.random.seed(scene)
    random.seed(scene)
    flat = wrapped.reset()
    env = wrapped.env
    raw = env._get_observation()
    keys = [k for k in raw if k in wrapped.keys]
    reconstructed = np.concatenate([raw[k] for k in keys])
    if keys != ["robot0_robot-state", "object-state"] or not np.array_equal(reconstructed, flat):
        raise ValueError("Legacy observation keys or values do not match")
    body = env.sim.model.body_name2id("Door")
    layout = np.r_[env.sim.model.body_pos[body], env.sim.model.body_quat[body]]
    signature = vectors_hash(layout, env.sim.data.qpos, env.sim.data.qvel, flat)
    return flat, keys, layout.tolist(), signature


def first_action_check(policy, observation):
    net = policy.stochastic_policy
    x = observation.astype("float32")
    for layer in net.fcs:
        x = np.maximum(0, layer.weight.detach().numpy().dot(x) + layer.bias.detach().numpy())
    layer = net.last_fc
    manual = np.tanh(layer.weight.detach().numpy().dot(x) + layer.bias.detach().numpy())
    actual = policy.get_action(observation)[0]
    if actual.shape != (7,) or not np.allclose(actual, manual, atol=2e-5, rtol=1e-5):
        raise ValueError("Saved deterministic policy disagrees with its independent forward calculation")
    return {"action": actual.tolist(), "network_input_dim": int(net.fcs[0].in_features),
            "max_forward_error": float(np.max(np.abs(manual - actual)))}


def latch_state(env):
    d = env.sim.data
    return [float(d.qpos[env.handle_qpos_addr]), float(d.get_joint_qvel("latch_joint"))]


def rollout(wrapped, policy, obs, full_horizon):
    env = wrapped.env
    first = None
    max_angle = float(env.sim.data.qpos[env.hinge_qpos_addr])
    for step in range(1, HORIZON + 1):
        action = policy.get_action(obs)[0]
        if not np.isfinite(action).all():
            raise ValueError("Non-finite policy output")
        obs, _, _, _ = wrapped.step(action)
        hinge = float(env.sim.data.qpos[env.hinge_qpos_addr])
        if not np.isfinite(obs).all() or not np.isfinite(hinge):
            raise ValueError("Non-finite simulator state")
        success = bool(env._check_success())
        if success != (hinge > 0.3):
            raise ValueError("Success rule differs from the public task")
        max_angle = max(max_angle, hinge)
        if success and first is None:
            first = step
            if not full_horizon:
                break
    return {"success": first is not None, "first_hit_step": first, "steps": step,
            "last_hinge_rad": hinge, "max_hinge_rad": max_angle, "end_latch": latch_state(env)}


def references(scene):
    policies, wrapped = load_policies(), make_env()
    records = {}
    try:
        for p in POLICIES:
            obs, keys, layout, signature = start_scene(wrapped, scene)
            if records and signature != meta["fresh_signature"]:
                raise ValueError("The two policies did not receive the same start")
            model = wrapped.env.sim.model
            raw = wrapped.env._get_observation()
            meta = {"scene": scene, "fresh_signature": signature, "door_pos_quat": layout,
                    "joint_names": list(model.joint_names), "physics_step_s": model.opt.timestep,
                    "observation_keys": keys, "observation_widths": [len(raw[k]) for k in keys],
                    "first_observation": obs.tolist()}
            check = first_action_check(policies[p], obs)
            records[str(p)] = dict(check, **rollout(wrapped, policies[p], obs, True))
    finally:
        wrapped.close()
    print("reference", scene, {p: r["first_hit_step"] for p, r in records.items()}, flush=True)
    return dict(meta, policies=records)


def passive_latch(wrapped, scene, reference, latch, wait):
    """Hold the robot and closed panel kinematically; evolve the original passive latch."""
    _, _, _, signature = start_scene(wrapped, scene)
    if signature != reference["fresh_signature"]:
        raise ValueError("Reset scene differs from its predecessor")
    env = wrapped.env
    sim = env.sim
    q, v = sim.data.qpos.copy(), sim.data.qvel.copy()
    pos = env.handle_qpos_addr
    vel = sim.model.get_joint_qvel_addr("latch_joint")
    if sim.model.na:
        raise ValueError("Unaccounted actuator activation in the door model")
    if latch is None:
        latch = [float(q[pos]), float(v[vel])]
    sim.data.ctrl[:] = 0
    for _ in range(round(wait / sim.model.opt.timestep)):
        sim.data.qpos[:] = q
        sim.data.qvel[:] = v
        sim.data.qpos[pos], sim.data.qvel[vel] = latch
        sim.forward()
        sim.step()
        latch = latch_state(env)
    return latch


def continuations(reference):
    scene = reference["scene"]
    policies, wrapped = load_policies(), make_env()
    trials, paths, cache = [], {}, {}
    try:
        for wait in WAITS:
            fresh = passive_latch(wrapped, scene, reference, None, wait)
            for previous in POLICIES:
                terminal = reference["policies"][str(previous)]["end_latch"]
                held = passive_latch(wrapped, scene, reference, terminal, wait)
                starts = {"panel": held, "angle": [fresh[0], held[1]],
                          "angle_speed": list(fresh), "fresh": list(fresh)}
                for reset, latch in starts.items():
                    for current in POLICIES:
                        # No actuator activation in this model. Initialize all other state,
                        # placement, solver and controller from the identical fresh block.
                        # Exact duplicates share a rollout; rows remain identifiable.
                        key = (current, *latch)
                        if key not in cache:
                            _, _, _, signature = start_scene(wrapped, scene)
                            if signature != reference["fresh_signature"]:
                                raise ValueError("Current policy received a different scene")
                            env = wrapped.env
                            data = env.sim.data
                            data.qpos[env.handle_qpos_addr], data.qvel[env.sim.model.get_joint_qvel_addr("latch_joint")] = latch
                            env.sim.forward()
                            obs = wrapped._flatten_obs(env._get_observation())
                            label = "path-{:02d}".format(len(paths) + 1)
                            paths[label] = dict(start_signature=vectors_hash(data.qpos, data.qvel, obs),
                                                current=current, **rollout(wrapped, policies[current], obs, False))
                            cache[key] = label
                        trials.append({"previous": previous, "current": current, "wait_s": wait,
                                       "reset": reset, "start_latch": list(latch), "path": cache[key]})
    finally:
        wrapped.close()
    print("continuation", scene, len(trials), "assignments", len(paths), "executed", flush=True)
    return {"scene": scene, "trials": trials, "paths": paths}


def contrasts(blocks):
    output = []
    for wait in WAITS:
        for reset in RESETS:
            by_current = {p: [] for p in POLICIES}
            by_previous = {p: {prev: [] for prev in POLICIES} for p in POLICIES}
            for block in blocks:
                rows = [r for r in block["trials"] if r["wait_s"] == wait and r["reset"] == reset]
                if Counter((r["previous"], r["current"]) for r in rows) != Counter((a, b) for a in POLICIES for b in POLICIES):
                    raise ValueError("Missing or repeated predecessor/current allocation")
                for r in rows:
                    success = block["paths"][r["path"]]["success"]
                    by_current[r["current"]].append(success)
                    by_previous[r["current"]][r["previous"]].append(success)
            output.append({"reset": reset, "wait_s": wait, "assignments_per_policy": len(by_current[17]),
                           "successes": {p: sum(v) for p, v in by_current.items()},
                           "success_by_previous": {p: {prev: sum(v) for prev, v in cells.items()} for p, cells in by_previous.items()},
                           "success_rate_59_minus_17": mean(by_current[59]) - mean(by_current[17])})
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--workers", type=int, choices=(1, 2, 3, 4), default=2)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Choose a new output file")
    with multiprocessing.get_context("spawn").Pool(args.workers) as pool:
        ref = pool.map(references, SCENES)
        if len({r["fresh_signature"] for r in ref}) != len(SCENES):
            raise ValueError("Independent scene blocks are duplicated")
        viable = all(any(b["policies"][str(p)]["success"] for b in ref) for p in POLICIES)
        blocks = pool.map(continuations, ref) if viable else []
    sources = {str(p): {f: digest(ROOT / str(p) / f) for f in ("params.pkl", "variant.json")} for p in POLICIES}
    report = {"evidence": "simulated_native_policies", "physics_version": mujoco_py.functions.mj_version(),
              "control_hz": 20, "scene_seeds": list(SCENES),
              "waits_s": list(WAITS), "success": "first observed door hinge angle > 0.3 rad",
              "environment": {k: pkg_resources.get_distribution(k).version for k in ("robosuite", "mujoco-py", "torch", "numpy", "numba")},
              "python": platform.python_version(), "arch": platform.machine(), "gpu": torch.cuda.is_available(),
              "script_sha256": digest(Path(__file__)), "rlkit_commit": os.environ["PANDA_RLKIT_COMMIT"],
              "checkpoints": sources, "horizon": HORIZON,
              "reference": ref, "both_viable": viable, "blocks": blocks, "summary": contrasts(blocks) if viable else []}
    with args.output.open("x") as f:
        json.dump(report, f, indent=2, allow_nan=False)
        f.write("\n")


if __name__ == "__main__":
    main()
