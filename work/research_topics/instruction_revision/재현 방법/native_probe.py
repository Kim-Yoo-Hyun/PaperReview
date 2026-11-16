"""One ReSteer R8 IO/switch qualification; never a performance experiment."""
import hashlib
import json
from pathlib import Path
import sys


def main(run):
    if not Path("/.dockerenv").exists():
        raise RuntimeError("Docker-only native probe")
    import numpy as np
    from resteer import tasks
    from resteer.client import PolicyClient
    from resteer.eval.rollout import run_switch_rollout
    from resteer.sim import libero as sim

    plan = json.loads(Path("/recipe/RESUME_PLAN.json").read_text())["qualification"]
    calls, steps, observed = [], [], []
    real_client = PolicyClient("127.0.0.1", 8000)
    env = None
    result = {"status": "FAILED", "qualification_only": True}

    class AuditedClient:
        def infer(self, query):
            if len(calls) >= plan["max_inference_calls"]:
                raise RuntimeError("Inference budget exceeded")
            for key in plan["observation"]["images"]:
                image = np.asarray(query[key])
                if image.shape != (224, 224, 3) or image.dtype != np.uint8 or np.ptp(image) == 0:
                    raise ValueError(f"Invalid or empty policy image: {key}")
            state = np.asarray(query["observation/state"])
            if state.shape != (8,) or not np.isfinite(state).all():
                raise ValueError("Invalid proprioceptive input")
            expected = plan["source_prompt"] if not calls else plan["target_prompt"]
            if query["prompt"] != expected:
                raise ValueError("Unexpected prompt/order")
            response = real_client.infer(query)
            actions = np.asarray(response["actions"])
            if actions.shape != (10, 7) or not np.isfinite(actions).all():
                raise ValueError("Invalid policy action reply")
            calls.append({"prompt": query["prompt"], "actions": actions.tolist(),
                          "state": state.tolist(), "image_sha256": {
                              key: hashlib.sha256(np.asarray(query[key]).tobytes()).hexdigest()
                              for key in plan["observation"]["images"]}})
            observed.append({k: np.asarray(query[k]).copy() for k in plan["observation"]["images"]})
            return response

    def on_step(step, observation, query, action, prompt):
        call_id = 0 if step < plan["switch_step"] else 1
        action_index = step if call_id == 0 else step - plan["switch_step"]
        if len(calls) != call_id + 1 or not np.allclose(action, calls[call_id]["actions"][action_index], rtol=0, atol=0):
            raise RuntimeError("Executed queue does not match source/target reply")
        expected = plan["source_prompt"] if call_id == 0 else plan["target_prompt"]
        if prompt != expected:
            raise RuntimeError("Prompt did not switch at the frozen action boundary")
        steps.append({"step": step, "call": call_id, "action_index": action_index,
                      "prompt": prompt, "action": np.asarray(action).tolist()})

    try:
        env = sim.make_env(seed=plan["environment_seed"])
        sim.reset(env, num_warmup_steps=plan["warmup_steps"])
        result["initial_sim_state"] = env.get_sim_state().tolist()
        result["control_hz"] = getattr(env.env, "control_freq", None)
        outcome = run_switch_rollout(
            env, AuditedClient(), tasks.get_task(plan["source_task_id"]),
            tasks.get_task(plan["target_task_id"]), plan["switch_step"],
            max_steps=plan["max_policy_steps"], replan_steps=plan["replan_steps"], on_step=on_step
        )
        if outcome.error is not None:
            raise RuntimeError(outcome.error)
        if len(calls) != 2 or not any(s["step"] == plan["switch_step"] and s["call"] == 1 for s in steps):
            raise RuntimeError("Both prompt phases were not executed")
        result.update(status="PASS_IO_ONLY", final_sim_state=env.get_sim_state().tolist(),
                      upstream_goal_first_hit=bool(outcome.success),
                      upstream_first_success_step=outcome.first_success_step,
                      goal_effect_claim=False, env_exception=None)
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
    finally:
        result.update(calls=calls, steps=steps, inference_count=len(calls), action_count=len(steps))
        if observed:
            np.savez_compressed(run / "policy_observations.npz", **{
                f"query{i}_{key.rsplit('/', 1)[-1]}": value
                for i, item in enumerate(observed) for key, value in item.items()
            })
        (run / "native_result.json").write_text(json.dumps(result, indent=2) + "\n")
        if env is not None:
            env.close()
        real_client.close()
    return 0 if result["status"] == "PASS_IO_ONLY" else 1


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1])))
