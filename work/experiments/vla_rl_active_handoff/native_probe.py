"""Bounded native-checkpoint prerequisite probe. Execute only in Docker."""
import hashlib
import importlib.util
import json
import os
import resource
import subprocess
import time
import traceback
from pathlib import Path

assert Path("/.dockerenv").exists(), "Run this probe inside Docker only."
OUT = Path("/artifacts/native_probe.json")
REPORT = {"stage": "starting", "episodes": [], "research_effect_tested": False}


def save():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(REPORT, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in REPORT.items() if k != "packages"},
                     ensure_ascii=False), flush=True)


def main():
    import numpy as np
    import torch
    import yaml
    from huggingface_hub import snapshot_download
    # Pin the simulator assets and configure the official package before its
    # interactive first-import prompt. Everything remains inside Docker.
    REPORT["stage"] = "downloading_simulator_assets"
    save()
    assets_dir = snapshot_download(
        "lerobot/libero-assets", repo_type="dataset",
        revision="0b3ea86be5fe169d0fd036ae63d1070ec09e90f6",
        local_dir="/artifacts/libero-assets",
    )
    asset_cache = Path.home() / ".cache/libero/assets"
    asset_cache.parent.mkdir(parents=True, exist_ok=True)
    if not asset_cache.exists():
        asset_cache.symlink_to(assets_dir, target_is_directory=True)
    libero_root = Path(next(iter(
        importlib.util.find_spec("libero").submodule_search_locations
    ))) / "libero"
    config_dir = Path("/artifacts/libero_config")
    config_dir.mkdir(parents=True, exist_ok=True)
    os.environ["LIBERO_CONFIG_PATH"] = str(config_dir)
    (config_dir / "config.yaml").write_text(yaml.safe_dump({
        "benchmark_root": str(libero_root),
        "bddl_files": str(libero_root / "bddl_files"),
        "init_states": str(libero_root / "init_files"),
        "datasets": "/artifacts/unused-datasets",
        "assets": assets_dir,
    }))
    from libero.libero import benchmark
    from lerobot.envs.libero import LiberoEnv
    from lerobot.envs.utils import preprocess_observation
    from lerobot.policies.factory import make_pre_post_processors
    from lerobot.policies.smolvla.configuration_smolvla import SmolVLAConfig
    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
    from lerobot.processor.env_processor import LiberoProcessorStep
    from safetensors.torch import load_file

    torch.set_num_threads(6)
    torch.set_num_interop_threads(1)
    REPORT["packages"] = subprocess.check_output(
        ["python", "-m", "pip", "freeze"], text=True
    ).splitlines()
    REPORT["torch_cuda_available"] = torch.cuda.is_available()
    REPORT["stage"] = "downloading_checkpoint"
    save()
    model_dir = snapshot_download(
        "HuggingFaceVLA/smolvla_libero",
        revision="6721902bc4d61e50a3bfdb11dfb4cb626f05d102",
        allow_patterns=["*.json", "*.safetensors"],
    )
    config = SmolVLAConfig.from_pretrained(model_dir)
    vlm_dir = snapshot_download(
        "HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
        revision="7b375e1b73b11138ff12fe22c8f2822d8fe03467",
        allow_patterns=["*.json", "*.txt"],
        ignore_patterns=["onnx/*"],
    )
    config.vlm_model_name = vlm_dir
    config.device = "cpu"
    config.load_vlm_weights = False
    assert config.n_obs_steps == 1 and config.n_action_steps == 1
    assert config.chunk_size == 50 and config.num_steps == 10
    model_start = time.monotonic()
    policy = SmolVLAPolicy(config)
    state = load_file(str(Path(model_dir) / "model.safetensors"))
    policy.load_state_dict(state, strict=True)
    del state
    policy.to("cpu").float().eval()
    preprocess, postprocess = make_pre_post_processors(
        config,
        model_dir,
        preprocessor_overrides={
            "device_processor": {"device": "cpu"},
            "tokenizer_processor": {"tokenizer_name": vlm_dir},
        },
    )
    env_processor = LiberoProcessorStep()
    REPORT.update(stage="native_rollouts", strict_checkpoint_load=True,
                  model_load_seconds=time.monotonic() - model_start)
    save()
    rollout_start = time.monotonic()
    def add_batch(value):
        if isinstance(value, dict):
            return {key: add_batch(item) for key, item in value.items()}
        return np.expand_dims(value, 0) if isinstance(value, np.ndarray) else value

    for suite_name, seed, horizon in [
        ("libero_spatial", 71000, 280),
        ("libero_goal", 72000, 300),
    ]:
        torch.manual_seed(seed)
        np.random.seed(seed)
        suite = benchmark.get_benchmark_dict()[suite_name](task_order_index=0)
        env = LiberoEnv(
            task_suite=suite, task_id=0, task_suite_name=suite_name,
            obs_type="pixels_agent_pos", observation_width=256, observation_height=256,
            episode_index=0, n_envs=1, num_steps_wait=10, control_freq=20,
            control_mode="relative", init_states=True, hard_reset=True,
        )
        entry = dict(suite=suite_name, task_id=0, task=suite.get_task(0).name,
                     seed=seed, init_state_index=0, horizon=horizon,
                     status="running", action_steps=0, success=None)
        REPORT["episodes"].append(entry)
        started = time.monotonic()
        infer_times = []
        try:
            obs, _ = env.reset(seed=seed)
            entry["available_init_states"] = len(env._init_states)
            policy.reset()
            for step in range(horizon):
                if time.monotonic() - rollout_start > 900:
                    entry["status"] = "budget_exhausted"
                    break
                # Match the batch dimension supplied by the official vector runner.
                batch = preprocess_observation(add_batch(obs))
                batch = env_processor.observation(batch)
                batch["task"] = [suite.get_task(0).language]
                batch = preprocess(batch)
                if step == 0:
                    entry["input_shapes"] = {
                        k: list(v.shape) for k, v in batch.items() if hasattr(v, "shape")
                    }
                    entry["first_state_sha256"] = hashlib.sha256(
                        batch["observation.state"].numpy().tobytes()
                    ).hexdigest()
                ti = time.monotonic()
                with torch.inference_mode():
                    action = postprocess(policy.select_action(batch))
                infer_times.append(time.monotonic() - ti)
                action = action.squeeze(0).cpu().numpy()
                assert action.shape == (7,) and np.isfinite(action).all()
                obs, _, terminated, truncated, info = env.step(action)
                entry["action_steps"] = step + 1
                if (step + 1) % 20 == 0:
                    entry["elapsed_seconds"] = time.monotonic() - started
                    entry["mean_inference_seconds"] = float(np.mean(infer_times))
                    save()
                if terminated or truncated:
                    entry.update(status="completed", success=bool(info["is_success"]))
                    break
            else:
                entry.update(status="completed", success=False)
        finally:
            env.close()
        entry["elapsed_seconds"] = time.monotonic() - started
        entry["mean_inference_seconds"] = float(np.mean(infer_times)) if infer_times else None
        entry["max_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save()
        if entry["status"] == "budget_exhausted":
            break
    REPORT["stage"] = "finished"
    REPORT["native_competence_qualified"] = False
    save()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        REPORT.update(stage="error", error_type=type(exc).__name__,
                      error=str(exc), traceback=traceback.format_exc())
        save()
        raise
