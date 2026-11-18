"""Container-only preparation, simulator instrumentation and bounded P0 runner."""
import argparse
import ast
import builtins
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import selectors
import shutil
import stat
import subprocess
import sys
import time
import traceback
import zipfile

HERE = Path(__file__).resolve().parent
PLAN = json.loads((HERE / 'PLAN.json').read_text())
RESULTS = Path('/results')
ARM = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(8 * 1024**2), b''):
            h.update(block)
    return h.hexdigest()


def plain(x):
    if isinstance(x, dict):
        return {str(k): plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [plain(v) for v in x]
    if hasattr(x, 'tolist'):
        return x.tolist()
    if isinstance(x, Path):
        return str(x)
    return x


def write(path, data):
    Path(path).write_text(json.dumps(plain(data), ensure_ascii=False, indent=2, allow_nan=False) + '\n')


class BudgetExceeded(BaseException):
    """Must not be swallowed by upstream broad Exception/TOPP retry handlers."""


class Budget:
    def __init__(self):
        self.total = self.phase_count = 0
        self.setup = self.control = 0
        self.phase = None
        self.completed = 0

    def begin(self, phase):
        if phase not in ('setup', 'control'):
            raise ValueError(phase)
        self.phase, self.phase_count = phase, 0

    def before_step(self):
        cap = PLAN['budget']['max_physics_per_setup_attempt' if self.phase == 'setup' else 'max_physics_per_command']
        if self.phase is None or self.total >= PLAN['budget']['max_total_physics_steps'] or self.phase_count >= cap:
            raise BudgetExceeded('physics budget exhausted before scene.step')
        self.total += 1
        self.phase_count += 1
        if self.phase == 'setup':
            self.setup += 1
        else:
            self.control += 1


def safe_extract(archive, destination):
    destination = Path(destination).resolve()
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            target = (destination / item.filename).resolve()
            if not target.is_relative_to(destination) or stat.S_ISLNK(item.external_attr >> 16):
                raise ValueError('Archive contains traversal or symlink')
        z.extractall(destination)


def prepare():
    from huggingface_hub import hf_hub_download
    model = PLAN['model']
    manifest = {'model': {}, 'assets': {}, 'prepared': False}
    for name, expected in [('model.safetensors', model['weight_sha256']), (model['normalizer_path'], model['normalizer_sha256'])]:
        file = Path(hf_hub_download(model['model_id'], name, revision=model['revision'], local_dir='/cache/model'))
        actual = sha(file)
        if actual != expected:
            raise ValueError('Payload hash mismatch: ' + name)
        manifest['model'][name] = actual
    asset_root = Path('/cache/assets')
    asset_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree('/opt/relation-src/robotwin/assets', asset_root, dirs_exist_ok=True)
    for item in PLAN['assets']['archives']:
        archive = Path(hf_hub_download(PLAN['assets']['dataset'], item['path'], repo_type='dataset',
            revision=PLAN['assets']['revision'], local_dir='/cache/archives'))
        actual = sha(archive)
        if actual != item['upstream_lfs']['sha256']:
            raise ValueError('Asset hash mismatch: ' + item['path'])
        marker = Path('/cache') / (item['path'] + '.extracted.json')
        if not marker.exists():
            # Extract only into a fresh staging tree. An interrupted extraction never gets a marker.
            stage = Path('/cache') / ('extract-' + item['path'])
            if stage.exists():
                shutil.rmtree(stage)
            stage.mkdir()
            safe_extract(archive, stage)
            expected_dir = stage / item['path'].removesuffix('.zip')
            if not expected_dir.is_dir():
                raise ValueError('Unexpected archive layout; inspect before changing paths: ' + item['path'])
            shutil.copytree(expected_dir, asset_root / expected_dir.name, dirs_exist_ok=True)
            write(marker, {'archive_sha256': actual})
            shutil.rmtree(stage)
        elif json.loads(marker.read_text())['archive_sha256'] != actual:
            raise ValueError('Stale extraction marker')
        manifest['assets'][item['path']] = actual
    if not (asset_root / 'embodiments/aloha-agilex/config.yml').is_file() or not (asset_root / 'objects').is_dir():
        raise ValueError('Required embodiment/object assets missing')
    from openpi.models.tokenizer import PaligemmaTokenizer
    PaligemmaTokenizer(200)  # Downloads tokenizer only, not a model.
    token = Path('/cache/openpi/big_vision/paligemma_tokenizer.model')
    manifest['tokenizer_sha256'] = sha(token)
    manifest['prepared'] = True
    manifest['model_revision'] = model['revision']
    manifest['assets_revision'] = PLAN['assets']['revision']
    write('/cache/payload.json', manifest)
    write(RESULTS / 'payload.json', manifest)


def environment():
    import torch
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError('CUDA/BF16 unavailable')
    uuid = subprocess.check_output(['nvidia-smi', '--query-gpu=uuid', '--format=csv,noheader'], text=True).strip()
    if uuid != os.environ['RELATION_GPU_UUID']:
        raise RuntimeError('Allocated device is not the selected GPU')
    x = torch.ones((16, 16), device='cuda', dtype=torch.bfloat16)
    if not torch.isfinite(x @ x).all():
        raise RuntimeError('CUDA arithmetic check failed')
    subprocess.run([PLAN['python']['simulator'], str(HERE / 'probe.py'), 'graphics-check'], check=True, timeout=120)
    write(RESULTS / 'environment.json', {'status': 'CUDA_BF16_GRAPHICS_PASS', 'gpu_uuid': uuid,
        'torch': torch.__version__, 'cuda': torch.version.cuda, 'packet': os.environ['RELATION_PACKET_SHA'],
        'packages': {name: (HERE / name).read_text() for name in ('actor-packages.txt', 'simulator-packages.txt', 'system-packages.txt')}})


def graphics_check():
    import sapien
    import numpy as np
    engine = sapien.Engine()
    engine.set_renderer(sapien.SapienRenderer())
    scene = engine.create_scene()
    scene.set_ambient_light([1, 1, 1])
    builder = scene.create_actor_builder()
    builder.add_box_visual(half_size=[0.1]*3, color=[1, 0, 0])
    box = builder.build_kinematic()
    box.set_pose(sapien.Pose([1, 0, 0]))
    cam = scene.add_camera('qualification', 32, 32, 1.0, 0.01, 10)
    cam.set_pose(sapien.Pose())
    scene.update_render()
    cam.take_picture()
    rgb = cam.get_picture('Color')[..., :3]
    if not np.isfinite(rgb).all() or not np.any(rgb > 0):
        raise RuntimeError('SAPIEN RGB render failed')
    write(RESULTS / 'graphics.json', {'status': 'RENDER_PASS', 'shape': list(rgb.shape), 'physics_steps': 0})


def instrument_sources(root):
    """Count every explicit physics step in envs without proxying native Scene objects."""
    edits = []
    class Steps(ast.NodeTransformer):
        def __init__(self):
            self.count = 0
        def visit_Call(self, node):
            self.generic_visit(node)
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr == 'step' and not node.args and not node.keywords:
                receiver = f.value
                is_scene = (isinstance(receiver, ast.Name) and receiver.id == 'scene') or (isinstance(receiver, ast.Attribute) and receiver.attr == 'scene')
                if is_scene:
                    self.count += 1
                    fn = ast.Attribute(value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[ast.Constant('builtins')], keywords=[]), attr='_relation_physics_step', ctx=ast.Load())
                    return ast.copy_location(ast.Call(func=fn, args=[receiver], keywords=[]), node)
            return node
    for path in (root / 'envs').rglob('*.py'):
        before = sha(path)
        if str(path.relative_to(root)) in PLAN['upstream_hashes'] and before != PLAN['upstream_hashes'][str(path.relative_to(root))]:
            raise ValueError('Upstream source hash mismatch')
        source = path.read_text()
        if path.relative_to(root).as_posix() == 'envs/camera/camera.py':
            if source.count('near, far = 0.1, 100') != 1:
                raise ValueError('Camera near-plane source changed')
            source = source.replace('near, far = 0.1, 100', 'near, far = 0.01, 100')
        tree = ast.parse(source)
        patch = Steps()
        tree = patch.visit(tree)
        if patch.count or source != path.read_text():
            path.write_text(ast.unparse(ast.fix_missing_locations(tree)) + '\n')
            edits.append({'path': str(path.relative_to(root)), 'before': before, 'after': sha(path), 'step_hooks': patch.count})
    if not any(e['path'] == 'envs/_base_task.py' and e['step_hooks'] >= 8 for e in edits):
        raise ValueError('Physics instrumentation incomplete')
    return edits


def task_config(root, task_name):
    import yaml
    with (root / 'task_config/demo_clean.yml').open() as f:
        cfg = yaml.safe_load(f)
    with (root / 'task_config/_embodiment_config.yml').open() as f:
        embodiments = yaml.safe_load(f)
    robot_dir = (root / embodiments['aloha-agilex']['file_path']).resolve()
    with (robot_dir / 'config.yml').open() as f:
        robot_cfg = yaml.safe_load(f)
    with (root / 'task_config/_camera_config.yml').open() as f:
        cameras = yaml.safe_load(f)
    cfg.update(task_name=task_name, task_config='demo_clean', eval_mode=True, eval_video_log=False,
        render_freq=0, collect_data=False, save_data=False, save_path='/tmp/relation-unused',
        left_robot_file=str(robot_dir), right_robot_file=str(robot_dir), dual_arm_embodied=True,
        left_embodiment_config=robot_cfg, right_embodiment_config=robot_cfg,
        planner_backend='mplib', timestep=0.004)
    cfg['head_camera_h'] = cameras[cfg['camera']['head_camera_type']]['h']
    cfg['head_camera_w'] = cameras[cfg['camera']['head_camera_type']]['w']
    return cfg


def measured(robot):
    import numpy as np
    q, limits = [], []
    for arm in ('left', 'right'):
        ent = getattr(robot, arm + '_entity')
        active = ent.get_active_joints()
        joints = getattr(robot, arm + '_arm_joints')
        if len(joints) != 6:
            raise ValueError('Expected six joints per arm')
        indices = [active.index(j) for j in joints]
        q.extend(ent.get_qpos()[indices])
        limits.extend(ent.get_qlimits()[indices])
    return np.array(q), np.array(limits)


def relative_jacobian(robot):
    import numpy as np
    import transforms3d as t3d
    from scipy.spatial.transform import Rotation
    entries = []
    for arm in ('left', 'right'):
        ent = getattr(robot, arm + '_entity')
        joints = ent.get_active_joints()
        ee = getattr(robot, arm + '_ee')
        # RoboTwin's *_ee is a JOINT, not a link. Reconstruct its child-frame pose.
        entries.append((arm, ent, ent.create_pinocchio_model(), ent.get_links().index(ee.get_child_link()),
                        [joints.index(j) for j in getattr(robot, arm + '_arm_joints')]))
    q, _ = measured(robot)
    def tcp_poses(armq):
        output = []
        for arm, ent, model, ee_index, indices in entries:
            allq = ent.get_qpos().copy()
            # Aloha has both arms in one articulation. Apply every matching joint.
            for i, (_, other, _, _, ix) in enumerate(entries):
                if other == ent:
                    allq[ix] = armq[i*6:(i+1)*6]
            model.compute_forward_kinematics(allq)
            pose = ent.get_pose() * model.get_link_pose(ee_index) * getattr(robot, arm+'_ee').get_pose_in_child()
            mat = pose.to_transformation_matrix().astype(float)
            mat[:3, :3] = mat[:3, :3] @ getattr(robot, arm+'_global_trans_matrix') @ getattr(robot, arm+'_delta_matrix')
            mat[:3, 3] += mat[:3, :3] @ np.array([getattr(robot, arm+'_gripper_bias'), 0, 0])
            output.append(mat)
        return output
    actual = []
    for arm in ('left', 'right'):
        pose = getattr(robot, 'get_'+arm+'_tcp_pose')()
        m = np.eye(4)
        m[:3, 3], m[:3, :3] = pose[:3], t3d.quaternions.quat2mat(pose[3:])
        actual.append(m)
    base = tcp_poses(q)
    for computed, observed in zip(base, actual):
        if np.linalg.norm(computed[:3, 3]-observed[:3, 3]) > PLAN['physics']['fk_pose_atol_m'] or Rotation.from_matrix(computed[:3,:3].T@observed[:3,:3]).magnitude() > PLAN['physics']['fk_rotation_atol_rad']:
            raise ValueError('FK/TCP frame mismatch')
    rel0 = np.linalg.inv(base[0]) @ base[1]
    def tangent(poses):
        t = np.linalg.inv(rel0) @ np.linalg.inv(poses[0]) @ poses[1]
        omega = Rotation.from_matrix(t[:3, :3]).as_rotvec()
        theta = np.linalg.norm(omega)
        w = np.array([[0,-omega[2],omega[1]],[omega[2],0,-omega[0]],[-omega[1],omega[0],0]])
        a = 1/12 if theta < 1e-5 else (1 - theta/(2*np.tan(theta/2))) / theta**2
        rho = (np.eye(3)-w/2+a*w@w) @ t[:3,3]
        return np.r_[rho, omega]
    eps = PLAN['physics']['fk_eps_rad']
    jac = np.zeros((6,12))
    for i in range(12):
        dq = np.zeros(12); dq[i] = eps
        jac[:,i] = (tangent(tcp_poses(q+dq))-tangent(tcp_poses(q-dq))) / (2*eps)
    if not np.isfinite(jac).all():
        raise ValueError('Nonfinite Jacobian')
    return jac, actual


class ContactTrace:
    def __init__(self, task, name, path):
        self.task, self.name = task, name
        self.entities = []
        self.streak = {}
        self.samples = 0
        objects = {'lift_pot': ['pot'], 'handover_block': ['box'], 'pick_dual_bottles': ['bottle1', 'bottle2']}[name]
        for attr in objects:
            actor = getattr(task, attr).actor
            ents = [link.entity for link in actor.get_links()] if hasattr(actor, 'get_links') else [actor]
            self.entities.extend((e, 'object/'+attr) for e in ents)
        for arm in ('left', 'right'):
            fingers = getattr(task.robot, arm+'_gripper')
            links = [g[0].get_child_link().entity for g in fingers]
            unique = []
            for e in links:
                if e not in unique:
                    unique.append(e)
            if len(unique) != 2:
                raise ValueError('Exactly two distinct finger entities must be mapped per hand')
            self.entities.extend((e, arm+'/'+str(i)) for i,e in enumerate(unique))
        table = getattr(task, 'table', None)
        if table is not None:
            self.entities.append((getattr(table, 'actor', table), 'table'))
        write(path.with_suffix('.mapping.json'), [{'label': label, 'name': e.get_name()} for e,label in self.entities])
        self.file = path.open('w')

    def label(self, entity):
        matches = [label for e,label in self.entities if e == entity]
        if len(set(matches)) > 1:
            raise ValueError('Ambiguous contact identity')
        return matches[0] if matches else 'other/'+entity.get_name()

    def sample(self, tick, initial=False):
        import numpy as np
        contacts, active = [], set()
        for c in self.task.scene.get_contacts():
            labels = [self.label(b.entity) for b in c.bodies]
            points = [{'impulse': p.impulse, 'normal': p.normal, 'position': p.position, 'separation': p.separation} for p in c.points]
            contacts.append({'bodies': labels, 'points': points})
            force = sum(float(np.linalg.norm(p.impulse)) for p in c.points if p.separation <= .001) / .004
            if force > .05:
                active.add(tuple(sorted(labels)))
        if not initial:
            for pair in set(self.streak) | active:
                self.streak[pair] = self.streak.get(pair,0)+1 if pair in active else 0
        supported = [list(pair) for pair,n in self.streak.items() if n >= 10]
        q,_ = measured(self.task.robot)
        drives = [float(j.get_drive_target()[0]) for arm in ('left','right') for j in getattr(self.task.robot,arm+'_arm_joints')]
        fingers = {arm: [float(j[0].get_drive_target()[0]) for j in getattr(self.task.robot,arm+'_gripper')] for arm in ('left','right')}
        finger_q, finger_limits = {}, {}
        for arm in ('left', 'right'):
            ent = getattr(self.task.robot, arm+'_entity')
            joints = [g[0] for g in getattr(self.task.robot, arm+'_gripper')]
            active_joints = ent.get_active_joints()
            finger_q[arm] = [float(ent.get_qpos()[active_joints.index(j)]) for j in joints]
            finger_limits[arm] = [j.get_limits() for j in joints]
        poses = [{'label':label, 'entity':e.get_name(), 'pose':e.get_pose().to_transformation_matrix()}
                 for e,label in self.entities if label.startswith('object/') or label == 'table']
        row = {'tick':tick,'dt':.004,'contacts':contacts,'persistent_pairs_diagnostic':supported,
               'actual_q12':q,'drive_target12':drives,'finger_drive_targets':fingers,
               'actual_finger_qpos':finger_q,'finger_limits':finger_limits,'object_table_poses':poses,
               'tcp_world':{a:getattr(self.task.robot,'get_'+a+'_tcp_pose')() for a in ('left','right')},
               'witness_validated':False,'initial_observation':initial,
               'sampled_before_native_success_test':not initial}
        self.file.write(json.dumps(plain(row), allow_nan=False)+'\n')
        self.samples += 1


def receive(worker, timeout=300):
    # Binary unbuffered pipe: readiness cannot hide a prefetched JSON line.
    with selectors.DefaultSelector() as selector:
        selector.register(worker.stdout, selectors.EVENT_READ)
        end = time.monotonic()+timeout
        buf = bytearray()
        while time.monotonic() < end:
            if selector.select(max(0,end-time.monotonic())):
                byte = os.read(worker.stdout.fileno(),1)
                if not byte:
                    raise RuntimeError('Actor worker exited before response')
                if byte == b'\n':
                    result = json.loads(buf)
                    if result.get('status') == 'FAILED':
                        raise RuntimeError(result)
                    return result
                buf.extend(byte)
        raise TimeoutError('Actor worker response timeout')


def request(worker, data):
    worker.stdin.write((json.dumps(data)+'\n').encode())
    worker.stdin.flush()
    return receive(worker)


def p0(backward=False):
    import numpy as np
    control = json.loads((Path('/cache') / ('control-'+os.environ['RELATION_PACKET_SHA']+'.json')).read_text())
    if not control['passed'] or control['packet'] != os.environ['RELATION_PACKET_SHA']:
        raise ValueError('Docker contract checks must pass for this exact packet before P0')
    write(RESULTS/'control-prerequisite.json', control)
    payload = json.loads(Path('/cache/payload.json').read_text())
    if not payload['prepared'] or payload['model_revision'] != PLAN['model']['revision'] or payload['assets_revision'] != PLAN['assets']['revision']:
        raise ValueError('Run prepare for these exact payload revisions')
    for name, expected in payload['model'].items():
        if sha(Path('/cache/model')/name) != expected:
            raise ValueError('Model/normalizer payload changed')
    if sha('/cache/openpi/big_vision/paligemma_tokenizer.model') != payload['tokenizer_sha256']:
        raise ValueError('Tokenizer payload changed')
    root = Path('/tmp/relation-robotwin')
    if root.exists():
        raise ValueError('Require a fresh container/work directory')
    shutil.copytree('/opt/relation-src/robotwin', root, ignore=shutil.ignore_patterns('.git','assets'))
    (root/'assets').symlink_to('/cache/assets', target_is_directory=True)
    write(RESULTS/'source_instrumentation.json', instrument_sources(root))
    os.chdir(root)
    sys.path.insert(0,str(root))
    budget = Budget()
    current_trace = None
    def physics_step(scene):
        if abs(float(scene.get_timestep())-.004) > 1e-9:
            raise ValueError('Unexpected simulator timestep')
        budget.before_step()
        scene.step()
        budget.completed += 1
        if current_trace is not None:
            current_trace.sample(budget.total)
    builtins._relation_physics_step = physics_step
    summary = {'status':'STARTED','cases':[],'native_policy_calls':0,'commands':0,'optimizer_steps':0,'backward':None}
    started = time.monotonic()
    worker = None
    log = (RESULTS/'actor-worker.log').open('wb')
    try:
        worker = subprocess.Popen([PLAN['python']['actor'],str(HERE/'actor.py')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=log,bufsize=0)
        write(RESULTS/'loader.json',receive(worker))
        for name in PLAN['budget']['tasks']:
            directory=RESULTS/name;directory.mkdir()
            case={'task':name,'requested_seed':0,'attempts':[],'status':'STARTED'}
            summary['cases'].append(case)
            task=None
            try:
                for seed in (0,1):
                    budget.begin('setup')
                    task=getattr(importlib.import_module('envs.'+name),name)()
                    try:
                        task.setup_demo(now_ep_num=0,seed=seed,**task_config(root,name))
                        case['attempts'].append({'seed':seed,'status':'SETUP_PASS','physics':budget.phase_count})
                        case['actual_seed']=seed
                        break
                    except BudgetExceeded:
                        raise
                    except Exception as e:
                        case['attempts'].append({'seed':seed,'status':'SETUP_FAILED','error':str(e),'physics':budget.phase_count})
                        try:
                            task.close_env()
                        except Exception:
                            pass
                        task=None
                if task is None:
                    case['status']='SETUP_FAILED'
                    continue
                from description.utils.generate_episode_instructions import generate_episode_descriptions
                descriptions=generate_episode_descriptions(name,[task.get_info()],1,case['actual_seed'])
                prompt=descriptions[0]['seen'][0]
                task.instruction=prompt
                case['prompt']=prompt
                obs=task.get_obs()
                q,limits=measured(task.robot)
                jac,tcp=relative_jacobian(task.robot)
                case['relative_fk_evaluations']=25
                case['urdf_hashes']={a:sha(getattr(task.robot,a+'_urdf_path')) for a in ('left','right')}
                images={dest:obs['observation'][src]['rgb'] for src,dest in [('head_camera','cam_high'),('left_camera','cam_left_wrist'),('right_camera','cam_right_wrist')]}
                if any(not np.any(x) for x in images.values()):
                    raise ValueError('Blank camera observation')
                state=np.asarray(obs['joint_action']['vector'])
                np.savez_compressed(directory/'observation.npz',**images,state=state,q=q,jacobian=jac,prompt=np.array(prompt),tcp=np.array(tcp),physics_tick=budget.total)
                case['observation_sha256']=sha(directory/'observation.npz')
                case['rgb_sha256']={k:hashlib.sha256(v.tobytes()).hexdigest() for k,v in images.items()}
                current_trace=ContactTrace(task,name,directory/'contacts.jsonl')
                current_trace.sample(budget.total,initial=True)
                summary['native_policy_calls']+=1
                response=request(worker,{'op':'query','directory':str(directory)})
                case['actor']=response
                command=np.array(response['command'])
                if command.shape!=(14,) or not np.isfinite(command).all():
                    raise ValueError('Invalid physical command')
                if np.any(command[ARM]<limits[:,0]) or np.any(command[ARM]>limits[:,1]) or np.max(np.abs(command[ARM]-state[ARM]))>.05:
                    case['status']='COMMAND_REJECTED_BY_P0_LIMIT'
                    continue
                # Keep native TOPP/compression behavior and record what it really does.
                controller=[]
                for arm in ('left','right'):
                    planner=getattr(task.robot,arm+'_mplib_planner')
                    original=planner.TOPP
                    def wrapped(path,*args,_original=original,_arm=arm,**kwargs):
                        entry={'arm':_arm,'path':path};controller.append(entry)
                        try:
                            result=_original(path,*args,**kwargs)
                            entry.update(points_before_downsample=len(result[1]),duration=result[4],status='RETURNED')
                            return result
                        except Exception as e:
                            entry.update(status='ERROR',error=str(e))
                            raise
                    planner.TOPP=wrapped
                case['controller_rng_before']=repr(np.random.get_state())
                budget.begin('control')
                summary['commands']+=1
                reward,terminated,truncated,info,raw_obs=task.gen_sparse_reward_data(command[None],collect_obs=True)
                last_obs=raw_obs[-1]
                np.savez_compressed(directory/'last_observation.npz',
                    **{dest:last_obs['observation'][src]['rgb'] for src,dest in [('head_camera','cam_high'),('left_camera','cam_left_wrist'),('right_camera','cam_right_wrist')]},
                    state=last_obs['joint_action']['vector'],physics_tick=budget.total)
                case.update(status='COMMAND_EXECUTED',reward=reward,terminated=terminated,truncated=truncated,info=info,
                    controller=controller,control_physics=budget.phase_count,contact_samples=current_trace.samples,
                    controller_rng_after=repr(np.random.get_state()),requested_command=command,
                    measured_after=measured(task.robot)[0],event_validation='API_TRACE_ONLY_NOT_POSITIVE_EVENT_VALIDATION',
                    partial_prefix=bool(info['executed_action_count'] < 1),
                    event_timestamps=None,event_timestamps_reason='Full-task event detector/calibration not implemented in P0')
                if info['executed_action_count'] < 1 or budget.phase_count == 0:
                    case['status']='COMMAND_NOT_FULLY_EXECUTED'
                if backward and summary['backward'] is None:
                    summary['backward']=request(worker,{'op':'backward'})
            except BudgetExceeded as e:
                case.update(status='BUDGET_STOP',error=str(e))
                raise
            except Exception as e:
                case.update(status='FAILED',error=str(e),exception_type=type(e).__name__)
                traceback.print_exc()
                # A structural interface failure is not a reason to collect other scenes.
                raise
            finally:
                if current_trace is not None:
                    current_trace.file.close();current_trace=None
                if task is not None:
                    try:
                        task.close_env()
                    except Exception as e:
                        case['cleanup_error']=str(e)
                write(directory/'case.json',case)
        summary['status']='P0_PASS' if all(c['status']=='COMMAND_EXECUTED' for c in summary['cases']) else 'P0_PARTIAL'
        return 0 if summary['status']=='P0_PASS' else 4
    except (Exception,BudgetExceeded) as e:
        summary.update(status='P0_FAILED',error=str(e),exception_type=type(e).__name__)
        traceback.print_exc()
        return 2
    finally:
        summary['physics']=vars(budget)
        summary['simulated_seconds']=budget.completed*.004
        summary['wall_seconds']=time.monotonic()-started
        summary['effect_measured']=False
        write(RESULTS/'p0.json',summary)
        if worker is not None:
            if worker.poll() is None:
                try:
                    worker.stdin.write(b'{"op":"close"}\n');worker.stdin.flush();worker.wait(timeout=15)
                except (BrokenPipeError,subprocess.TimeoutExpired):
                    worker.kill();worker.wait(timeout=10)
        log.close()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase',choices=('build-check','sim-import-check','environment','graphics-check','prepare','p0'))
    ap.add_argument('--backward',action='store_true')
    args=ap.parse_args()
    if not Path('/.dockerenv').exists():
        raise SystemExit('Docker-only; host model/simulation execution prohibited')
    if args.phase=='build-check':
        from transformers.models.siglip import check
        from openpi.models_pytorch.pi0_pytorch import PI0Pytorch
        assert check.check_whether_transformers_replace_is_installed_correctly()
        for key,value in PLAN['sources'].items():
            actual=subprocess.check_output(['git','-C','/opt/relation-src/'+key,'rev-parse','HEAD'],text=True).strip()
            assert actual==value['commit'],(key,actual)
        return 0
    if args.phase=='sim-import-check':
        import sapien, torch, mplib, toppra, yaml
        assert importlib.metadata.version('sapien').startswith('3.')
        return 0
    if os.environ.get('RELATION_IN_DOCKER')!='1':
        raise SystemExit('Use resume.py to establish run provenance')
    RESULTS.mkdir(exist_ok=True)
    if args.phase=='environment':
        environment()
    elif args.phase=='graphics-check':
        graphics_check()
    elif args.phase=='prepare':
        prepare()
    else:
        return p0(args.backward)
    return 0


if __name__=='__main__':
    sys.exit(main())
