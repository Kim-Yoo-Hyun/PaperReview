"""Container-only ContactBench P0-A. No VLA, optimizer, task SR or scripted ending."""
import argparse
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for data in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(data)
    return h.hexdigest()


def require_container():
    if not Path('/.dockerenv').exists() or os.environ.get('CONTACT_P0_DOCKER') != '1':
        raise RuntimeError('Run through local Docker; host simulation is disabled')


class Budget:
    def __init__(self, caps, now=time.monotonic):
        ceilings = dict(resets=2, control_frames=120, physics_steps=6000, process_seconds=1800)
        if any(not isinstance(caps.get(k), int) or not 0 < caps[k] <= v for k, v in ceilings.items()):
            raise ValueError('Caps exceed the approved P0-A scope or are invalid')
        self.caps, self.now, self.started = caps, now, now()
        self.resets = self.physics = 0
        self.sim_seconds = 0.0

    def deadline(self):
        if self.now() - self.started >= self.caps['process_seconds']:
            raise RuntimeError('P0 wallclock budget exhausted')

    def reset(self):
        self.deadline()
        if self.resets >= self.caps['resets']:
            raise RuntimeError('P0 reset budget exhausted')
        self.resets += 1

    def step(self, dt):
        self.deadline()
        if not math.isfinite(dt) or dt <= 0:
            raise RuntimeError('Invalid physics dt')
        frames = math.ceil((self.sim_seconds + dt) * 60 - 1e-7)
        if self.physics >= self.caps['physics_steps'] or frames > self.caps['control_frames']:
            raise RuntimeError('P0 physics/control budget exhausted')
        self.physics += 1
        self.sim_seconds += dt


def actor_state(q, qd, force, previous, alpha):
    # Explicit whitelist. Object pose/phase/success never enter this interface.
    if len(q) != 9 or len(qd) != 9 or len(force) != 6 or (previous is not None and len(previous) != 6):
        raise ValueError('Wrong observation shape')
    if not 0.25 <= alpha <= 1:
        raise ValueError('Out-of-range gain')
    history = force if previous is None else previous
    raw = list(q) + list(qd) + list(force) + list(history) + [alpha, float(previous is not None)]
    if not all(math.isfinite(float(v)) for v in raw):
        raise ValueError('Non-finite actor observation')
    # P0 records raw q/qd and alpha: final model normalization is P0-B work.
    return [float(v) for v in raw]


def limited_gain(current, request):
    if not all(math.isfinite(x) for x in (current, request)):
        raise ValueError('Non-finite gain')
    return max(0.25, min(1.0, current + max(-0.1, min(0.1, request - current))))


def tree_hashes(root):
    return {str(p.relative_to(root)): sha(p) for p in sorted(root.rglob('*'))
            if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}


def verify_tree(root, expected):
    actual = tree_hashes(root)
    if actual != expected:
        raise RuntimeError(f'Payload changed or incomplete: {root}')


def versions(plan):
    found = {name: importlib.metadata.version(name) for name in plan['physics_packages']}
    if found != plan['physics_packages']:
        raise RuntimeError('Physics package version mismatch: ' + str(found))
    rev = subprocess.check_output(['git', '-C', '/opt/contactbench', 'rev-parse', 'HEAD'], text=True).strip()
    if rev != plan['contactbench_commit']:
        raise RuntimeError('ContactBench source identity mismatch')
    if subprocess.check_output(['git', '-C', '/opt/contactbench', 'status', '--porcelain', '--untracked-files=no'], text=True):
        raise RuntimeError('ContactBench tracked source changed')
    return found


def prepare(plan, result):
    import newton.utils
    import warp as wp
    result['versions'] = versions(plan)
    wp.init()
    if not wp.is_cuda_available():
        raise RuntimeError('Warp CUDA unavailable')
    manifest = Path('/cache/contact_assets.json')
    identity = os.environ['CONTACT_P0_FINGERPRINT']
    if manifest.exists():
        payload = json.loads(manifest.read_text())
        if payload['packet_fingerprint'] != identity:
            raise RuntimeError('Existing cache belongs to another packet; select a fresh volume or inspect it explicitly')
        verify_tree(Path(payload['fr3_path']), payload['fr3_files'])
        verify_tree(Path('/opt/contactbench/assets'), payload['task_asset_files'])
    else:
        fr3 = newton.utils.download_asset('franka_emika_panda', cache_dir='/cache/newton',
                                         ref=plan['fr3_commit'])
        if not (fr3 / 'urdf/fr3_franka_hand.urdf').is_file():
            raise RuntimeError('Missing FR3 URDF')
        urdf = (fr3 / 'urdf/fr3_franka_hand.urdf').read_bytes()
        blob = hashlib.sha1(f'blob {len(urdf)}\0'.encode() + urdf).hexdigest()
        if blob != plan['fr3_urdf_git_blob']:
            raise RuntimeError('FR3 URDF does not match pinned remote Git blob')
        payload = dict(packet_fingerprint=identity, fr3_commit=plan['fr3_commit'],
                       fr3_path=str(fr3), fr3_files=tree_hashes(fr3),
                       task_asset_files=tree_hashes(Path('/opt/contactbench/assets')))
        manifest.write_text(json.dumps(payload, indent=2) + '\n')
    result.update(status='PREPARED_PAYLOAD_NOT_SIMULATED', payload_manifest_sha256=sha(manifest),
                  payload_manifest=payload, physics_steps=0)
    Path('/results/pip-freeze.txt').write_text(Path('/opt/build/pip-freeze.txt').read_text())
    Path('/results/pip-install.json').write_text(Path('/opt/build/pip-install.json').read_text())


def native(plan, result, budget):
    result['versions'] = versions(plan)
    manifest = Path('/cache/contact_assets.json')
    payload = json.loads(manifest.read_text())
    if payload['packet_fingerprint'] != os.environ['CONTACT_P0_FINGERPRINT']:
        raise RuntimeError('Prepared packet fingerprint mismatch')
    verify_tree(Path(payload['fr3_path']), payload['fr3_files'])
    verify_tree(Path('/opt/contactbench/assets'), payload['task_asset_files'])
    result['payload_manifest_sha256'] = sha(manifest)
    import numpy as np
    import warp as wp
    import newton
    import newton.utils
    wp.init()
    if not wp.is_cuda_available():
        raise RuntimeError('CUDA unavailable; CPU fallback forbidden')
    wp.set_device('cuda:0')
    result['device'] = str(wp.get_device())
    # Offline p0: prevent first-run asset lookup/network even if upstream changes.
    def pinned_asset(name, *args, **kwargs):
        if name != 'franka_emika_panda':
            raise RuntimeError('Unprepared asset requested: ' + name)
        return Path(payload['fr3_path'])
    newton.utils.download_asset = pinned_asset
    from force_bench.rig import Rig
    from force_bench.appendix_tasks.plug_in_charger_blocks import make_variant
    from force_bench.recorder import lookat_transform, _resolve_frame_kernel
    from newton.sensors import SensorContact, SensorTiledCamera
    orig_init, orig_finalize, orig_run = Rig.__init__, Rig.finalize, Rig.run
    orig_step = newton.solvers.SolverMuJoCo.step
    samples, substeps, gain_rows = [], [], []
    active = {}

    class Finished(Exception):
        pass

    def init(rig, *args, **kwargs):
        budget.reset()
        orig_init(rig, *args, **kwargs)

    def finalize(rig, probes, cam_pos, cam_target, cam2_pos=None, cam2_target=None, record=True):
        rig._p0_camera = (np.asarray(cam_pos), np.asarray(cam_target))
        # Avoid published video/QA output and multi-megapixel recorder allocation.
        return orig_finalize(rig, probes, cam_pos, cam_target, record=False)

    def step(solver, s0, s1, control, contacts, dt):
        budget.step(float(dt))  # Also counts upstream constructor/pre-roll work.
        answer = orig_step(solver, s0, s1, control, contacts, dt)
        if active:
            solver.update_contacts(contacts, s1)
            active['fingers'].update(s1, contacts)
            active['environment'].update(s1, contacts)
            raw = active['fingers'].total_force.numpy()
            # total_force includes all counterparts; only force_matrix selects
            # the environment shapes and excludes fingertip pinch forces.
            env = active['environment'].force_matrix.numpy()[0].sum(axis=0)
            ncon = int(np.max(solver.mjw_data.ncon.numpy()))
            rigid = int(np.max(contacts.rigid_contact_count.numpy()))
            if ncon >= 8000 or rigid >= 20000:
                raise RuntimeError('Contact capacity reached; cannot certify force samples')
            if not np.isfinite(raw).all() or not np.isfinite(env).all():
                raise RuntimeError('Non-finite contact force')
            substeps.append([budget.sim_seconds, *raw.ravel().tolist(), *env.tolist(), ncon, rigid])
        return answer

    def gain(rig, alpha):
        kp, kd = rig.model.joint_target_ke.numpy(), rig.model.joint_target_kd.numpy()
        kp[:7], kd[:7] = 12000 * alpha, 900 * math.sqrt(alpha)
        rig.model.joint_target_ke.assign(kp)
        rig.model.joint_target_kd.assign(kd)
        rig.solver.notify_model_changed(newton.ModelFlags.JOINT_DOF_PROPERTIES)
        wp.synchronize()
        mapping = rig.solver.mjc_actuator_to_newton_idx.numpy()
        source = rig.solver.mjc_actuator_ctrl_source.numpy()
        gains = rig.solver.mjw_model.actuator_gainprm.numpy()[0]
        bias = rig.solver.mjw_model.actuator_biasprm.numpy()[0]
        modes = rig.model.joint_target_mode.numpy()
        rows = []
        for dof in range(9):
            indices = np.flatnonzero((source == 0) & (mapping == dof))
            if len(indices) != 1 or modes[dof] != int(newton.JointTargetMode.POSITION):
                raise RuntimeError('Expected one position actuator per robot DOF; review mapping')
            i = int(indices[0])
            expected_kp = 12000 * alpha if dof < 7 else 3000
            expected_kd = 900 * math.sqrt(alpha) if dof < 7 else 40
            if not np.allclose([gains[i, 0], bias[i, 1], bias[i, 2]],
                               [expected_kp, -expected_kp, -expected_kd], rtol=1e-5, atol=1e-3):
                raise RuntimeError('MuJoCo actuator gain/bias did not match requested gain')
            rows.append([dof, i, float(gains[i, 0]), float(bias[i, 1]), float(bias[i, 2])])
        gain_rows.append(dict(t=budget.sim_seconds, alpha=alpha, actuators=rows))

    def run(rig, duration, control_cb, extra_forces_cb=None, print_every=20):
        # Deliberately do NOT call expert callbacks, variant ending or criteria.
        if rig.fps != 60 or rig.substeps != 24 or rig.solver.use_mujoco_cpu:
            raise RuntimeError('Unexpected clock or CPU solver')
        labels = list(rig.model.body_label)
        plug = labels.index('plug')
        parents, children = rig.model.joint_parent.numpy(), rig.model.joint_child.numpy()
        if any(c == plug and p >= 0 and labels[int(p)].startswith('fr3/') for p, c in zip(parents, children)):
            raise RuntimeError('Unexpected robot-object weld/stabilizer')
        effort = rig.model.joint_effort_limit.numpy().copy()
        if not np.allclose(effort[:7], [87, 87, 87, 87, 12, 12, 12]):
            raise RuntimeError('FR3 effort limits differ from expected source; review asset')
        result['effort_limits'] = effort[:9].tolist()
        result['solver_options'] = rig.solver._force_bench_effective_options
        if result['solver_options'].get('iterations') != 30 or result['solver_options'].get('impratio') != 10:
            raise RuntimeError('Unexpected task solver options')
        finger_ids = [labels.index('fr3/fr3_leftfinger'), labels.index('fr3/fr3_rightfinger')]
        active['fingers'] = SensorContact(rig.model, sensing_bodies=finger_ids, measure_total=True)
        body_of_shape = rig.model.shape_body.numpy()
        fixture_shapes = [i for i, b in enumerate(body_of_shape)
                          if b != plug and (b < 0 or not labels[int(b)].startswith('fr3/'))]
        if not fixture_shapes:
            raise RuntimeError('No environment counterpart shapes')
        active['environment'] = SensorContact(rig.model, sensing_bodies=['plug'],
                                               counterpart_shapes=fixture_shapes, measure_total=True)
        cam = SensorTiledCamera(model=rig.model)
        cam.utils.create_default_light(enable_shadows=True)
        rays = cam.utils.compute_camera_rays_pinhole(224, 224, camera_fovs=np.radians([40.0]))
        color = cam.utils.create_color_image_output(224, 224, 1)
        sidx = cam.utils.create_shape_index_image_output(224, 224, 1)
        rgb_out = wp.zeros((224, 224, 3), dtype=wp.uint8)
        cam_pos, cam_target = rig._p0_camera
        cam_tf = wp.array([[lookat_transform(cam_pos, cam_target)]], dtype=wp.transformf)
        result['camera'] = dict(pos=cam_pos.tolist(), target=cam_target.tolist(), width=224, height=224, fov_deg=40)
        alpha, previous = 1.0, None
        force_frames = []
        rot = wp.transform_get_rotation(rig.robot_base)
        every_substep = rig.effective_collide_every_substep()
        result['collide_every_substep'] = every_substep
        # Gain-only fixture: hold original post-pre-roll joint position target.
        # Does not implement the N2 Cartesian action decoder or train a policy.
        target = rig.control.joint_target_q.numpy().copy()
        gain(rig, alpha)
        for fi in range(84):
            if fi % 6 == 0:
                alpha = limited_gain(alpha, 0.5 if fi < 42 else 1.0)
                gain(rig, alpha)
            if not every_substep:
                rig.s0.clear_forces()
                rig.pipeline.collide(rig.s0, rig.contacts)
            for _ in range(rig.substeps):
                if every_substep:
                    rig.s0.clear_forces()
                    rig.pipeline.collide(rig.s0, rig.contacts)
                rig.solver.step(rig.s0, rig.s1, rig.control, rig.contacts, 1 / 1440)
                rig.s0, rig.s1 = rig.s1, rig.s0
            f_world = active['fingers'].total_force.numpy()
            force = np.array([list(wp.quat_rotate_inv(rot, wp.vec3(*f))) for f in f_world]).ravel()
            force_frames.append(force)
            if not np.isfinite(rig.s0.body_q.numpy()).all() or not np.isfinite(rig.s0.body_qd.numpy()).all():
                raise RuntimeError('Non-finite physics state')
            if not np.array_equal(target, rig.control.joint_target_q.numpy()) or not np.array_equal(effort, rig.model.joint_effort_limit.numpy()):
                raise RuntimeError('Gain fixture changed targets or effort limits')
            if (fi + 1) % 6 == 0:
                now_force = np.mean(force_frames[-6:], axis=0).tolist()
                state32 = actor_state(rig.s0.joint_q.numpy()[:9], rig.s0.joint_qd.numpy()[:9], now_force, previous, alpha)
                rig.model.bvh_refit_shapes(rig.s0)
                cam.update(rig.s0, cam_tf, rays, color_image=color, shape_index_image=sidx,
                           clear_data=type(cam).GRAY_CLEAR_DATA)
                wp.launch(_resolve_frame_kernel, dim=(224, 224),
                          inputs=[color, sidx, rgb_out, 1, 224, wp.vec3f(0.15, 0.17, 0.21),
                                  wp.vec3f(0.42, 0.45, 0.51), 0, 0])
                rgb = rgb_out.numpy()
                if rgb.shape != (224, 224, 3) or int(rgb.max()) == int(rgb.min()):
                    raise RuntimeError('Empty/invalid RGB frame')
                if not samples or fi == 83:
                    from PIL import Image
                    Image.fromarray(rgb).save('/results/rgb_first.png' if not samples else '/results/rgb_last.png')
                samples.append(dict(t=budget.sim_seconds, rgb_t=budget.sim_seconds,
                                    force_window_end=budget.sim_seconds, state32=state32,
                                    rgb_sha256=hashlib.sha256(rgb.tobytes()).hexdigest()))
                previous = now_force
        if max(np.linalg.norm(np.asarray(force_frames).reshape(-1, 2, 3), axis=-1).ravel()) <= 0:
            raise RuntimeError('No fingertip contact witness; force path inconclusive')
        if not any(abs(r['alpha'] - 0.5) < 1e-6 for r in gain_rows) or not any(abs(r['alpha'] - 1) < 1e-6 for r in gain_rows[1:]):
            raise RuntimeError('Gain endpoints not reached')
        result.update(status='WIRING_CHECKS_PASS_VISUAL_REVIEW_PENDING',
                      actor_samples=samples, gains=gain_rows, fixture='joint-target hold with gain ramp',
                      physics_force_rows=len(substeps), task_success_evaluated=False,
                      pending=['manual RGB task visibility','environment load/normal-force calibration',
                               'target SFT/normalizer','Cartesian actor decoder','VLA IO','RL comparison'])
        np.savez_compressed('/results/substep_forces.npz',
                            rows=np.asarray(substeps),
                            columns=np.array(['t', 'Lfx', 'Lfy', 'Lfz', 'Rfx', 'Rfy', 'Rfz',
                                              'envfx', 'envfy', 'envfz', 'mj_ncon', 'rigid_ncon']))
        raise Finished

    Rig.__init__, Rig.finalize, Rig.run = init, finalize, run
    newton.solvers.SolverMuJoCo.step = step
    variant = make_variant(1, spring=0.4)
    mod = __import__(variant.source, fromlist=['main'])
    argv = sys.argv
    try:
        np.random.seed(plan['fixture']['seed'])
        import random
        random.seed(plan['fixture']['seed'])
        variant.configure(mod)
        sys.argv = [variant.source]
        mod.main()
        raise RuntimeError('Expected P0 loop interception did not occur')
    except Finished:
        pass
    finally:
        variant.cleanup(mod)
        Rig.__init__, Rig.finalize, Rig.run = orig_init, orig_finalize, orig_run
        newton.solvers.SolverMuJoCo.step = orig_step
        sys.argv = argv
        result['attempted_physics_steps_including_preroll'] = budget.physics
        result['equivalent_control_frames_including_preroll'] = math.ceil(budget.sim_seconds * 60 - 1e-7)
        result['resets_including_constructor'] = budget.resets
        result['partial_actor_samples'] = len(samples)


def main():
    require_container()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('stage', choices=['prepare', 'p0'])
    args = ap.parse_args()
    plan = json.loads((HERE / 'P0_PLAN.json').read_text())
    budget = Budget(plan['caps'])
    result = dict(stage=args.stage, status='STARTED',
                  packet_fingerprint=os.environ['CONTACT_P0_FINGERPRINT'],
                  image_id=os.environ['CONTACT_P0_IMAGE_ID'],
                  vla_queries=0, optimizer_updates=0, weight_downloads=0)
    exit_code = 0
    try:
        Path('/cache/tmp').mkdir(parents=True, exist_ok=True)
        if os.environ.get('TB_ARM_EFFORT') or os.environ.get('TB_STABILIZER') != '0':
            raise RuntimeError('Unexpected effort/stabilizer override')
        if args.stage == 'prepare':
            prepare(plan, result)
        else:
            native(plan, result, budget)
    except Exception as exc:
        result.update(status='FAILED_OR_INCONCLUSIVE', error=f'{type(exc).__name__}: {exc}')
        exit_code = 4
    finally:
        result['elapsed_seconds'] = time.monotonic() - budget.started
        result['attempted_physics_steps_including_preroll'] = budget.physics
        result['resets_including_constructor'] = budget.resets
        Path('/results/' + args.stage + '.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('stage', 'status', 'elapsed_seconds')}))
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
