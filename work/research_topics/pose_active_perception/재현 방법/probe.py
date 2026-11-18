"""Container-only bounded scene/evaluator and SpatialVLA IO qualification.

No VLA commands are connected to the simulator. No optimizer or label rollout.
"""
import argparse
import copy
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import random
import shutil
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
PLAN = json.loads((ROOT / "PLAN.json").read_text())


def write(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")


class Budget:
    def __init__(self, limits=None):
        self.limits = limits or PLAN["budgets"]
        self.used = {k: 0 for k in ("control_calls", "physics_steps", "model_steps")}

    def take(self, key, n=1):
        if n < 0 or self.used[key] + n > self.limits[key]:
            raise RuntimeError("Global budget exceeded: " + key)
        self.used[key] += n


def valid_tokens(ids, ranges):
    return len(ids) == 12 and all(ranges[i % 3][0] <= x <= ranges[i % 3][1] for i, x in enumerate(ids))


class Evaluator:
    """Consumes evaluator-only physical witnesses, never policy observation."""
    def __init__(self, config):
        self.c = config
        self.elapsed = {"place": 0., "align": 0.}

    def update(self, witness, seconds):
        if not 0 < seconds <= 1:
            raise ValueError("invalid sample duration")
        required = ("inside", "support", "released", "eef_distance", "linear_speed", "angular_speed", "upright", "angle_deg")
        if any(k not in witness for k in required):
            raise ValueError("missing physical witness")
        if not all(math.isfinite(float(witness[k])) for k in required):
            raise ValueError("nonfinite physical witness")
        if any(type(witness[k]) is not bool for k in ("inside", "support", "released")):
            raise ValueError("physical flags must be booleans")
        if any(witness[k] < 0 for k in ("eef_distance", "linear_speed", "angular_speed", "angle_deg")):
            raise ValueError("invalid negative physical magnitude")
        if not -1 <= witness["upright"] <= 1 or witness["angle_deg"] > 180:
            raise ValueError("invalid angle witness")
        c = self.c
        base = (witness["inside"] and witness["support"] and witness["released"]
                and witness["eef_distance"] >= c["min_eef_distance_m"]
                and witness["linear_speed"] <= c["max_linear_speed_m_s"]
                and witness["angular_speed"] <= c["max_angular_speed_rad_s"]
                and witness["upright"] >= c["upright_cosine_min"])
        conditions = {"place": bool(base), "align": bool(base and witness["angle_deg"] <= c["align_tolerance_deg"])}
        for k, ok in conditions.items():
            self.elapsed[k] = self.elapsed[k] + seconds if ok else 0.
        return {k: self.elapsed[k] + 1e-12 >= c["dwell_seconds"] for k in conditions}


def verify_model(directory):
    verified = []
    for item in PLAN["model"]["files"]:
        f = directory / item["path"]
        if not f.is_file() or f.stat().st_size != item["bytes"]:
            raise RuntimeError("Missing/size-mismatched payload: " + item["path"])
        h = hashlib.sha256() if item["algorithm"] == "sha256" else hashlib.sha1()
        if item["algorithm"] == "git_blob_sha1":
            h.update(("blob " + str(item["bytes"]) + "\0").encode())
        with f.open("rb") as src:
            for chunk in iter(lambda: src.read(8 * 1024 * 1024), b""):
                h.update(chunk)
        if h.hexdigest() != item["digest"]:
            raise RuntimeError("Payload hash mismatch: " + item["path"])
        verified.append({"path": item["path"], "digest": h.hexdigest()})
    return verified


def fetch(output):
    from huggingface_hub import snapshot_download
    if shutil.disk_usage("/cache").free < PLAN["hardware"]["minimum_free_disk_gib"] * 2**30:
        raise RuntimeError("Insufficient free space in Docker cache volume")
    directory = Path(snapshot_download(PLAN["model"]["repo"], revision=PLAN["model"]["revision"],
                                      allow_patterns=[x["path"] for x in PLAN["model"]["files"]]))
    hashes = verify_model(directory)
    Path("/cache/model_path.txt").write_text(str(directory))
    write(output / "payload.json", {"revision": PLAN["model"]["revision"], "verified": hashes})


def environment(output):
    import torch
    import importlib.metadata as md
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError("CUDA/BF16 unavailable")
    p = torch.cuda.get_device_properties(0)
    if p.major < 8 or p.total_memory < PLAN["hardware"]["minimum_gpu_vram_gib"] * 2**30:
        raise RuntimeError("GPU below provisional P0 threshold")
    data = {"cuda": torch.version.cuda, "gpu": p.name, "memory_bytes": p.total_memory,
            "packages": {n: md.version(n) for n in ("torch", "torchvision", "transformers", "mujoco", "robosuite", "numpy")},
            "egl": "Not proven until scene renders", "research_effect": "UNTESTED"}
    write(output / "environment.json", data)
    for name in ("packages.txt", "system-packages.txt"):
        shutil.copyfile(ROOT / name, output / name)


def scene(output, budget, report):
    import numpy as np
    import mujoco
    import robosuite
    from PIL import Image
    from robosuite.environments.manipulation.nut_assembly import NutAssemblySquare
    from robosuite.utils.binding_utils import MjSim
    from robosuite.utils.camera_utils import get_camera_intrinsic_matrix, get_camera_extrinsic_matrix, get_real_depth_map

    class PlacementFixture(NutAssemblySquare):
        def _load_model(self):
            super()._load_model()
            world = self.model.worldbody
            # Keep peg bodies for parent references, remove their collision/appearance.
            for name in ("peg1", "peg2"):
                body = world.find(".//body[@name='" + name + "']")
                if body is None:
                    raise RuntimeError("Pinned arena peg missing")
                for geom in body.iter("geom"):
                    geom.set("contype", "0")
                    geom.set("conaffinity", "0")
                    geom.set("rgba", "0 0 0 0")
            ET.SubElement(world, "geom", name="pose_target", type="box", pos="0 0 0.8005",
                          size="0.12 0.10 0.0004", rgba="0.1 0.7 0.1 0.5", contype="0", conaffinity="0", group="1")
            for name, ends in (("shaft", "0 -0.16 0.802 0.07 -0.16 0.802"),
                               ("tip1", "0.07 -0.16 0.802 0.05 -0.145 0.802"),
                               ("tip2", "0.07 -0.16 0.802 0.05 -0.175 0.802")):
                ET.SubElement(world, "geom", name="pose_arrow_" + name, type="capsule", fromto=ends,
                              size="0.003", rgba="1 0 0 1", contype="0", conaffinity="0", group="1")
            ET.SubElement(world, "geom", name="pose_occluder", type="box",
                          pos=" ".join(map(str, PLAN["scene"]["occluder_position"])),
                          size=" ".join(map(str, PLAN["scene"]["occluder_halfsize"])), rgba="0.3 0.3 0.3 1")

        def reward(self, action=None):
            return 0.  # Never use original insertion reward as placement evidence.

        def _check_success(self):
            return False  # Custom evaluator below owns fixture predicates.

    originals = {k: getattr(MjSim, k) for k in ("step", "step2")}
    for method, original in originals.items():
        def bounded(sim, *args, _original=original, **kwargs):
            budget.take("physics_steps")
            return _original(sim, *args, **kwargs)
        setattr(MjSim, method, bounded)
    env = None
    try:
        cfg_path = Path(robosuite.__file__).parent / "controllers/config/robots/default_panda.json"
        cfg = json.loads(cfg_path.read_text())
        cfg["body_parts"]["arms"]["right"].update(input_ref_frame="base", input_type="delta", interpolation=None)
        env = PlacementFixture(robots="Panda", controller_configs=cfg, has_renderer=False,
                               has_offscreen_renderer=True, use_camera_obs=False, use_object_obs=False,
                               control_freq=20, horizon=20, ignore_done=True, hard_reset=False, seed=0)
        env.reset()
        robot = env.robots[0]
        arm = robot.arms[0]
        controller = robot.part_controllers[arm]
        controller._goal_update_mode = "achieved"
        if env.action_dim != 7:
            raise RuntimeError("Expected Panda seven-command interface")
        nut = env.nuts[0]
        body = env.obj_body_id[nut.name]
        geoms = set(env.obj_geom_id[nut.name])
        table = env.sim.model.geom_name2id("table_collision")
        fingers = {env.sim.model.geom_name2id(x) for x in robot.gripper[arm].contact_geoms}
        finger_q = robot._ref_gripper_joint_pos_indexes[arm]
        joint = nut.joints[0]
        handle = env.sim.model.site_name2id(nut.important_sites["handle"])
        model = env.sim.model
        data = env.sim.data
        assert all(model.geom_type[g] == 6 for g in geoms), "SquareNut collision geometry must be boxes"

        def put(yaw):
            pos = PLAN["scene"]["object_position"]
            data.set_joint_qpos(joint, np.array(pos + [math.cos(yaw / 2), 0., 0., math.sin(yaw / 2)]))
            data.set_joint_qvel(joint, np.zeros(6))
            env.sim.forward()

        def step():
            budget.take("control_calls")
            env.step(np.array([0., 0., 0., 0., 0., 0., -1.]))  # hold arm / open fingers

        def witness():
            corners = []
            for g in geoms:
                local = np.array(list(itertools.product((-1, 1), repeat=3))) * model.geom_size[g]
                corners.extend(local @ data.geom_xmat[g].reshape(3, 3).T + data.geom_xpos[g])
            corners = np.asarray(corners)
            inside = bool(np.all(np.abs(corners[:, :2] - PLAN["scene"]["target_xy"]) <= PLAN["scene"]["target_halfsize"]))
            pairs = [(c.geom1, c.geom2) for c in data.contact[:data.ncon] if c.dist <= 0.001]
            support = False
            for index, contact in enumerate(data.contact[:data.ncon]):
                a, b = contact.geom1, contact.geom2
                if (a in geoms and b == table) or (b in geoms and a == table):
                    force = np.zeros(6)
                    mujoco.mj_contactForce(model._model, data._data, index, force)
                    support |= bool(force[0] > 1e-6)
            grasp_contact = any((a in geoms and b in fingers) or (b in geoms and a in fingers) for a, b in pairs)
            finger_width = float(abs(data.qpos[finger_q[0]] - data.qpos[finger_q[1]]))
            v = data.get_joint_qvel(joint)
            direction = data.site_xpos[handle][:2] - data.body_xpos[body][:2]
            norm = np.linalg.norm(direction)
            angle = math.degrees(math.acos(float(np.clip(direction[0] / norm, -1, 1)))) if norm > 1e-8 else 180.
            return dict(inside=inside, support=bool(support), released=not grasp_contact and finger_width >= PLAN["evaluator_fixture"]["min_finger_width_m"],
                        eef_distance=float(np.linalg.norm(data.site_xpos[robot.eef_site_id[arm]] - data.body_xpos[body])),
                        linear_speed=float(np.linalg.norm(v[:3])), angular_speed=float(np.linalg.norm(v[3:])),
                        upright=float(np.clip(data.body_xmat[body].reshape(3, 3)[2, 2], -1, 1)), angle_deg=angle)

        def simple(value):
            if value is None or isinstance(value, (str, int, float, bool, np.ndarray, np.number)):
                return True
            if isinstance(value, (list, tuple)):
                return all(simple(v) for v in value)
            if isinstance(value, dict):
                return all(simple(v) for v in value.values())
            return False

        def snapshot():
            return {"arrays": {k: getattr(data, k).copy() for k in ("qpos", "qvel", "act", "ctrl", "qacc_warmstart", "mocap_pos", "mocap_quat", "qfrc_applied", "xfrc_applied")},
                    "time": data.time, "env": {k: copy.deepcopy(getattr(env, k)) for k in ("timestep", "cur_time", "done", "_obs_cache")},
                    "rng": copy.deepcopy(env.rng.bit_generator.state), "numpy_rng": np.random.get_state(), "python_rng": random.getstate(),
                    "controllers": {name: {k: copy.deepcopy(v) for k, v in c.__dict__.items() if simple(v)} for name, c in robot.part_controllers.items()},
                    "gripper": {a: g.current_action.copy() for a, g in robot.gripper.items()}}

        def restore(s):
            for k, v in s["arrays"].items():
                getattr(data, k)[:] = v
            data.time = s["time"]
            env.sim.forward()
            for k, v in s["env"].items():
                setattr(env, k, copy.deepcopy(v))
            env.rng.bit_generator.state = copy.deepcopy(s["rng"])
            np.random.set_state(s["numpy_rng"])
            random.setstate(s["python_rng"])
            for name, saved in s["controllers"].items():
                c = robot.part_controllers[name]
                c.update(force=True)
                for k, v in saved.items():
                    setattr(c, k, copy.deepcopy(v))
            for a, v in s["gripper"].items():
                robot.gripper[a].current_action = v.copy()

        put(0.)
        for _ in range(4):
            step()
        snapshot0 = snapshot()
        traces = []
        for _ in range(2):
            restore(snapshot0)
            trace = []
            for _ in range(3):
                step()
                trace.append(np.concatenate((data.qpos.copy(), data.qvel.copy(), data.ctrl.copy())))
            traces.append(np.asarray(trace))
        replay_error = float(np.max(np.abs(traces[0] - traces[1])))
        report.update(replay_error=replay_error, restore_scope="Fixed scripted hold/open with no VLA history; NOT general counterfactual reset qualification")
        if replay_error > PLAN["replay"]["max_state_absolute_error"]:
            raise RuntimeError("Limited physics/controller replay mismatch")
        restore(snapshot0)
        ImageInputs = []
        frame_records = []
        for camera in PLAN["scene"]["cameras"]:
            rgb, depth = env.sim.render(width=224, height=224, camera_name=camera, depth=True)
            rgb, depth = rgb[::-1].copy(), get_real_depth_map(env.sim, depth[::-1].copy())
            K = get_camera_intrinsic_matrix(env.sim, camera, 224, 224)
            T = get_camera_extrinsic_matrix(env.sim, camera)
            # Algebraic roundtrip for actual camera geometry; visibility is not certified by this check.
            world = data.body_xpos[body]
            cam = np.linalg.inv(T) @ np.r_[world, 1.]
            if cam[2] <= 0 or not np.isfinite(depth).all() or depth.min() <= 0:
                raise RuntimeError("Invalid depth/camera convention")
            pixel = (K @ cam[:3]); pixel = pixel[:2] / pixel[2]
            recon = T @ np.r_[np.linalg.inv(K) @ np.r_[pixel, 1.] * cam[2], 1.]
            if np.linalg.norm(recon[:3] - world) > 1e-8:
                raise RuntimeError("Camera roundtrip failed")
            Image.fromarray(rgb).save(output / (camera + ".png"))
            np.save(output / (camera + "_depth_m.npy"), depth)
            frame_records.append(dict(camera=camera, K=K.tolist(), T_world_camera_cv=T.tolist(), projected_center=pixel.tolist()))
            ImageInputs.append((Image.fromarray(rgb), K))
        result = {}
        for name, yaw in (("aligned_fixture", 0.), ("opposite_fixture", math.pi)):
            restore(snapshot0)
            put(yaw)
            evaluator = Evaluator(PLAN["evaluator_fixture"])
            samples = []
            for _ in range(5):
                step()
                w = witness()
                decision = evaluator.update(w, 1 / 20)
                samples.append(dict(witness=w, decision=decision))
            result[name] = samples
        report.update(frames=frame_records, evaluator_fixture=result, task_performance="NOT_MEASURED; evaluator-only pose placement by script")
        write(output / "scene.json", report)
        if not result["aligned_fixture"][-1]["decision"]["align"]:
            raise RuntimeError("Positive placement fixture not qualified")
        if not result["opposite_fixture"][-1]["decision"]["place"] or result["opposite_fixture"][-1]["decision"]["align"]:
            raise RuntimeError("Opposite-heading negative fixture not qualified")
        return ImageInputs[0]
    finally:
        if env is not None:
            env.close()
        for k, v in originals.items():
            setattr(MjSim, k, v)


def vla(image, K, output, budget, report):
    import numpy as np
    import torch
    from transformers import AutoModel, AutoProcessor, LogitsProcessor
    path = Path(Path("/cache/model_path.txt").read_text().strip())
    verify_model(path)
    processor = AutoProcessor.from_pretrained(path, trust_remote_code=True, local_files_only=True)
    model, loading = AutoModel.from_pretrained(path, trust_remote_code=True, local_files_only=True,
                                             torch_dtype=torch.bfloat16, attn_implementation="eager",
                                             output_loading_info=True)
    if any(loading.get(k) for k in ("missing_keys", "unexpected_keys", "mismatched_keys", "error_msgs")):
        raise RuntimeError("Strict model load mismatch: " + str(loading))
    model = model.eval().cuda()
    model.config.text_config._attn_implementation = "eager"
    model.language_model.config._attn_implementation = "eager"
    tok = processor.action_tokenizer
    ranges = [(x.token_start_idx, x.token_end_idx) for x in (tok.translation_tokenizer, tok.rotation_tokenizer, tok.gripper_tokenizer)]
    if processor.action_chunk_size != 4 or processor.num_obs_steps != 1:
        raise RuntimeError("Pinned processor contract changed")

    class Gate(LogitsProcessor):
        def __init__(self, prefix_length, constrained=False, forced=None):
            self.prefix = prefix_length
            self.constrained = constrained
            self.forced = forced

        def __call__(self, input_ids, scores):
            budget.take("model_steps")
            step = input_ids.shape[1] - self.prefix
            if not 0 <= step < 12:
                raise RuntimeError("Unexpected generation step")
            if self.forced is not None:
                masked = torch.full_like(scores, -float("inf"))
                masked[:, self.forced[step]] = 0.
                return masked  # Never modify raw logits in-place.
            if self.constrained:
                lo, hi = ranges[step % 3]
                masked = torch.full_like(scores, -float("inf"))
                masked[:, lo:hi+1] = scores[:, lo:hi+1]
                return masked
            return scores

    records = []
    for instruction_index, instruction in enumerate(PLAN["instructions"]):
        seen = set()
        inputs = processor(images=[image], text=instruction, return_tensors="pt", do_normalize=False)
        inputs["intrinsic"] = torch.tensor(K, dtype=torch.float32)  # actual resized camera, no dataset fallback
        inputs = {k: v.to(device="cuda", dtype=torch.bfloat16 if v.is_floating_point() else v.dtype) for k, v in inputs.items()}
        length = inputs["input_ids"].shape[1]

        def generate(constrained, forced=None):
            torch.manual_seed(PLAN["seed"] + instruction_index)
            with torch.inference_mode():
                return model.generate(**inputs, max_new_tokens=12, min_new_tokens=12,
                                      eos_token_id=None, do_sample=bool(constrained and forced is None),
                                      top_k=0, top_p=1., temperature=1., use_cache=True,
                                      logits_processor=[Gate(length, constrained, forced)],
                                      return_dict_in_generate=True, output_logits=True, output_hidden_states=True)

        for constrained in (False, True):
            start = time.monotonic()
            generated = generate(constrained)
            ids = generated.sequences[0, length:].cpu().tolist()
            valid = valid_tokens(ids, ranges)
            entry = dict(instruction=instruction, constrained=constrained, ids=ids, valid=valid)
            if not valid:
                entry["status"] = "INVALID_NO_DECODE"
                records.append(entry)
                del generated
                continue
            if tuple(ids) in seen:
                entry["status"] = "DUPLICATE_NO_NEW_CANDIDATE"
                records.append(entry)
                del generated
                continue
            seen.add(tuple(ids))
            # Capture prefix hidden state without candidate or label tokens.
            hidden = generated.hidden_states[0][-1][0, -1].float().cpu().numpy()
            if hidden.ndim != 1 or not np.isfinite(hidden).all():
                raise RuntimeError("Invalid prefix feature")
            np.save(output / ("prefix_" + str(instruction_index) + "_" + str(int(constrained)) + ".npy"), hidden)

            def logps(result):
                if len(result.logits) != 12:
                    raise RuntimeError("Expected twelve raw next-token logits")
                raw, masked = [], []
                for i, (scores, chosen) in enumerate(zip(result.logits, ids)):
                    scores = scores[0].float()
                    lo, hi = ranges[i % 3]
                    raw.append(float(torch.log_softmax(scores, -1)[chosen]))
                    masked.append(float(scores[chosen] - torch.logsumexp(scores[lo:hi+1], -1)))
                if not all(math.isfinite(x) for x in raw + masked):
                    raise RuntimeError("Nonfinite token log probability")
                return raw, masked

            generated_scores = logps(generated)
            del generated
            replay = generate(constrained, ids)
            if replay.sequences[0, length:].cpu().tolist() != ids:
                raise RuntimeError("Forced replay changed tokens")
            replay_scores = logps(replay)
            error = max(abs(a-b) for xs, ys in zip(generated_scores, replay_scores) for a, b in zip(xs, ys))
            decoded = tok.decode_token_ids_to_actions(np.array(ids).reshape(4, 3))
            if decoded.shape != (4, 7) or not np.isfinite(decoded).all():
                raise RuntimeError("Invalid normalized action decode")
            entry.update(normalized_actions=decoded.tolist(), raw_token_logps=generated_scores[0],
                         family_normalized_logps=generated_scores[1], replay_max_error=error,
                         seconds=time.monotonic()-start, physical_decode="BLOCKED_NO_TASK_NORMALIZER",
                         physical_execution=False, feature_shape=list(hidden.shape))
            records.append(entry)
            report["candidates"] = records
            write(output / "vla.json", report)
            if error > PLAN["replay"]["max_logprob_absolute_error"]:
                raise RuntimeError("Generation/forced replay score mismatch")
            del replay
        if not seen:
            raise RuntimeError("No valid candidate for instruction: " + instruction)
    report.update(candidates=records, peak_cuda_bytes=torch.cuda.max_memory_allocated(),
                  effect="NOT_MEASURED", pose_conditioning="NOT_IMPLEMENTED", training=False)
    write(output / "vla.json", report)
    if not any(x["valid"] for x in records):
        raise RuntimeError("No valid candidate")


def main():
    if os.environ.get("POSE_ACTIVE_CONTAINER") != "1" or not Path("/.dockerenv").exists():
        raise SystemExit("Run through resume.py in local Docker; host experiments are forbidden")
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["environment", "fetch", "run"])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if args.mode == "environment":
        environment(args.output)
        return
    if args.mode == "fetch":
        fetch(args.output)
        return
    random.seed(PLAN["seed"])
    import numpy as np
    np.random.seed(PLAN["seed"])
    budget = Budget()
    report = {"status": "STARTED", "scene": {}, "vla": {}, "training": False, "foundationpose_register": 0}
    try:
        image, K = scene(args.output, budget, report["scene"])
        vla(image, K, args.output, budget, report["vla"])
        report["status"] = "P0_QUALIFICATION_ONLY"
    except Exception as exc:
        report.update(status="FAILED", error=type(exc).__name__ + ": " + str(exc))
        raise
    finally:
        report["budgets_used"] = budget.used
        report["unimplemented"] = PLAN["unimplemented"]
        write(args.output / "result.json", report)


if __name__ == "__main__":
    main()
