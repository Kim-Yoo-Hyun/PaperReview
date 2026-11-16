"""One public dev episode. Invoke only inside the prepared local Docker image."""
import collections
import hashlib
import json
import os
from pathlib import Path
import random
import time
import traceback

if not Path('/.dockerenv').exists():
    raise SystemExit('Docker only; do not install or run the simulator on the host.')

import numpy as np
import imageio.v3 as iio
from openpi_client import websocket_client_policy
import VLABench
from VLABench.robots import *  # noqa: F403 - upstream registry registration
from VLABench.tasks import *  # noqa: F403
from VLABench.envs import load_env
from VLABench.utils.utils import euler_to_quaternion, quaternion_to_euler


def main():
    plan = json.loads(Path('/recipe/RESUME_PLAN.json').read_text())
    artifacts = json.loads(Path('/recipe/ARTIFACTS.json').read_text())
    cfg = plan['probe']
    output = Path(os.environ['SET_RUN_DIR'])
    report = {'status': 'STARTED', 'rollouts': 1, 'policy_steps': 0,
              'inference_calls': 0, 'native_condition_met': False,
              'research_effect_verified': False, 'trace': []}
    env = None
    started = time.monotonic()
    try:
        random.seed(cfg['seed'])
        np.random.seed(cfg['seed'])
        env = load_env(cfg['task'], episode_config=artifacts['scene']['episode'],
                       random_init=False, eval=False, run_mode='eval',
                       reset_wait_step=cfg['reset_wait_step'])
        # load_env already resets; do not reset a second time.
        physics_dt = float(env.physics.model.opt.timestep)
        control_dt = float(env.control_timestep())
        report.update(physics_dt=physics_dt, control_dt=control_dt,
                      initialization_sim_time=float(env.physics.data.time))
        if not np.isclose(control_dt / physics_dt, 100):
            raise RuntimeError('Unexpected physics/control substep ratio')
        if env.task.conditions.is_met(env.physics):
            raise RuntimeError('Initial condition already satisfied; invalid competence probe')
        client = websocket_client_policy.WebsocketClientPolicy('127.0.0.1', 8000)
        queue = collections.deque()
        offset = np.array([0., -0.4, 0.78])
        prompt = cfg['prompt']
        if artifacts['scene']['episode']['task']['instructions'] != [prompt]:
            raise RuntimeError('Frozen instruction mismatch')
        for step in range(cfg['max_policy_steps']):
            if not queue:
                if report['inference_calls'] >= cfg['max_inference_calls']:
                    raise RuntimeError('Inference budget exhausted')
                obs = env.get_observation(require_pcd=False)
                rgb = np.asarray(obs['rgb'])
                if rgb.shape != (4, 480, 480, 3) or rgb.dtype != np.uint8:
                    raise RuntimeError(f'Unexpected RGB IO: {rgb.shape}, {rgb.dtype}')
                raw = np.asarray(obs['ee_state']).copy()
                if raw.shape != (8,) or not np.isfinite(raw).all():
                    raise RuntimeError('Unexpected EE state')
                state = np.concatenate([raw[:3] - offset,
                                        quaternion_to_euler(raw[3:7]), raw[-1:]])
                if step == 0:
                    grid = np.vstack([np.hstack(rgb[:2]), np.hstack(rgb[2:])])
                    iio.imwrite(output / 'initial_views.png', grid)
                    report['initial_rgb_sha256'] = hashlib.sha256(rgb.tobytes()).hexdigest()
                    report['initial_state'] = state.tolist()
                    report['initial_raw_ee_state'] = raw.tolist()
                    report['gripper_state_convention'] = 'Upstream raw flag retained: true when both finger qpos < 0.035; not a verified open indicator'
                    np.savez_compressed(output / 'initial_physics.npz',
                                        state=env.physics.get_state())
                response = client.infer({'observation/image': rgb[2],
                                         'observation/second_image': rgb[0],
                                         'observation/wrist_image': rgb[3],
                                         'observation/state': state, 'prompt': prompt})
                actions = np.asarray(response['actions'])
                report['inference_calls'] += 1
                if actions.shape != (50, 7) or not np.isfinite(actions).all():
                    raise RuntimeError(f'Unexpected action chunk {actions.shape}')
                queue.extend(actions[:cfg['replan_steps']].copy())
            action = queue.popleft()
            pos = action[:3] + offset
            quat = euler_to_quaternion(*action[3:6])
            ok, joints = env.robot.get_qpos_from_ee_pos(env.physics, pos=pos, quat=quat)
            if not ok:
                report['status'] = 'IK_FAILURE'
                raise RuntimeError('IK did not converge; no action was applied for this target')
            fingers = np.full(2, 0.04 if action[-1] >= 0.1 else 0.0)
            controls = np.concatenate([joints, fingers])
            if controls.shape != (9,) or not np.isfinite(controls).all():
                raise RuntimeError('Invalid controller input')
            ts = env.step(controls)
            condition = bool(env.task.conditions.is_met(env.physics))
            report['policy_steps'] += 1
            report['trace'].append({'step': step, 'action7': action.tolist(),
                                    'joint_finger_controls': controls.tolist(),
                                    'sim_time': float(env.physics.data.time),
                                    'native_condition': condition, 'last': bool(ts.last())})
            if not np.isfinite(env.physics.get_state()).all():
                raise RuntimeError('Non-finite simulator state')
            if condition or ts.last():
                report['native_condition_met'] = condition
                report['status'] = 'NATIVE_CONTAINMENT' if condition else 'TERMINAL_WITHOUT_CONDITION'
                break
        else:
            report['status'] = 'STEP_BUDGET_EXHAUSTED'
        final = env.get_observation(require_pcd=False)
        iio.imwrite(output / 'final_front.png', final['rgb'][2])
        report['grasped_entity_names_at_end'] = env.get_grasped_entity()[0]
        # Native containment is first-hit geometry, not released/stable final-set success.
        report['stable_release_verified'] = False
    except Exception:
        if report['status'] != 'IK_FAILURE':
            report['status'] = 'RUNTIME_ERROR'
        report['error'] = traceback.format_exc()
        raise
    finally:
        report['wall_seconds'] = time.monotonic() - started
        (output / 'probe.json').write_text(json.dumps(report, indent=2) + '\n')
        if env is not None:
            env.close()


if __name__ == '__main__':
    main()
