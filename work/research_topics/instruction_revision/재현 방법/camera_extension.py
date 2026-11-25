"""Prepare the registered geometry changes and run two independently restarted validation rounds."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys
import time
from urllib.request import urlopen

import numpy as np

from camera_protocol import DESIGN, cell_folder, contexts, eligibility, geometry, key, placements
from inside import write_json
from run_atomic import SIM_PYTHON, utc
from run_bottle_xy import qualify
from run_camera_factorial import install_cell, sources
from run_layouts import base_inputs, layout_spec
from run_r1 import digest, run_path
from verify_atomic import PACKET, read


def expected_shift(native,delta):
    def shifted(row):
        xy = np.array(row['bottle_pose']['xyz'][:2])+delta
        return {'bottle_pose':{'xyz':[*xy,row['bottle_pose']['xyz'][2]]}}
    return {'initial_readout':shifted(native['initial_readout']), 'rows':[shifted(native['rows'][-1])]}


def prepare_positions(out,d,gates):
    _,base,reference = base_inputs()
    limits = read(PACKET/'R1_BOTTLE_XY.json')
    for scene in [11,*d['new_scene_seeds']]:
        if scene == 11:
            source_path = geometry(out,scene,'o')/'base_prefix.json'
            raw_xy = d['positions']['o']
        else:
            origin = out/'origins'/str(scene)
            (origin/'frames').mkdir(parents=True,exist_ok=True)
            (origin/'logs').mkdir(exist_ok=True)
            subprocess.run([SIM_PYTHON,str(PACKET/'camera_geometry.py'),str(scene),str(origin/'raw_xy.json')],check=True)
            raw_xy = read(origin/'raw_xy.json')
            write_json(origin/'protocol.json',layout_spec(base,scene))
            source_path = origin/'prefix.json'
            if not source_path.exists():
                run_path(origin,'raw',1,mode='prefix')
            assert read(source_path)['status'] == 'PREFIX_ONLY'
        native = read(source_path)
        for label,target in placements(d,scene,raw_xy).items():
            name = f'{scene}-{label}'
            if name in gates:
                continue
            folder = geometry(out,scene,label)
            (folder/'frames').mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source_path,folder/'base_prefix.json')
            shutil.copyfile(reference/'calibration.json',folder/'calibration.json')
            spec = layout_spec(base,scene)
            spec.update(archived_command_source=digest(source_path),bottle_xy_seed=scene if target == raw_xy else label,
                        bottle_xy={'native':raw_xy,'target':target})
            write_json(folder/'protocol.json',spec)
            subprocess.run([SIM_PYTHON,str(PACKET/'bottle_xy_sim.py'),str(folder)],check=True)
            expected = expected_shift(native,np.array(target)-raw_xy)
            gate = qualify(folder,limits,spec,native,expected)
            spec['source_replay'] = dict(path='prefix.json',controls=2,file_sha256=gate['prefix_sha256'])
            write_json(folder/'protocol.json',spec)
            gates[name] = gate
            print(f'Qualified {name}: {gate["eligible"]}',flush=True)
    return gates


@contextmanager
def server(plan, log, script='camera_server.py'):
    with log.open('w') as output:
        proc = subprocess.Popen([sys.executable,str(PACKET/script),str(plan)],
                                cwd='/opt/resteer',stdout=output,stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic()+420
            while proc.poll() is None and time.monotonic() < deadline:
                try:
                    with urlopen('http://127.0.0.1:8000/healthz',timeout=2) as reply:
                        if reply.status == 200:
                            break
                except OSError:
                    time.sleep(1)
            else:
                raise RuntimeError(f'Policy server did not start; see {log}')
            yield
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()


def run_entry(out, entry):
    folder = out/entry['folder']
    arm,repeat = entry['wording'],entry['repeat']
    started = utc()
    with (folder/'logs'/f'{arm}_{repeat}_sim.log').open('w') as log:
        subprocess.run([SIM_PYTHON,str(PACKET/'r1_motion.py'),'rollout',str(folder),arm,str(repeat)],
                       env=dict(os.environ,CAMERA_STUDY_SESSION=entry['session']),cwd='/opt/resteer',
                       stdout=log,stderr=subprocess.STDOUT,timeout=1200,check=True)
    lines = (out/entry['receipts']).read_bytes().splitlines()
    assert len(lines) == 61 and read(folder/f'{arm}_{repeat}.json')['status'] == 'COMPLETED'
    print('Completed '+entry['session'],flush=True)
    return {'session':entry['session'],'started_at':started,'finished_at':utc()}


def extend(out):
    d,core = read(out/'study.json'),read(out/'core.json')
    assert d == read(PACKET/DESIGN) and core['status'] == 'COMPLETED'
    assert core['image_id'] == os.environ['REVISION_IMAGE_ID']
    if (out/'run.json').is_file():
        finished = read(out/'run.json')
        assert finished['status'] == 'COMPLETED'
        assert finished['paths'] == 8*sum(read(out/'gates.json')['accepted'].values())
        rounds = [read(out/f'round-{r}.json') for r in d['repeats']]
        assert all(v['status'] == 'COMPLETED' for v in rounds)
        assert len(core['paths'])+sum(len(v['paths']) for v in rounds) == finished['paths']
        return
    names = ['camera_extension.py','camera_geometry.py','camera_server.py','bottle_xy_sim.py','R1_BOTTLE_XY.json']
    if not (out/'gates.json').exists():
        hashes = sources(out/'extension_sources',names)
        gates = prepare_positions(out,d,read(out/'historical_gates.json'))
        accepted = {key(c):eligibility(out,c,gates) for c in contexts(d)}
        for c in contexts(d)[1:]:
            if accepted[key(c)]:
                for condition in d['camera_sources']:
                    install_cell(out,d,c,condition)
        write_json(out/'gates.json',dict(frozen_at=utc(),geometry=gates,accepted=accepted,input_sha256=hashes))
    gates = read(out/'gates.json')
    assert all(digest(PACKET/n) == h for n,h in gates['input_sha256'].items())
    ordered = [(c,cond) for c in contexts(d)[1:] if gates['accepted'][key(c)] for cond in d['camera_sources']]
    random.Random(d['round_order_seed']).shuffle(ordered)
    for repeat in d['repeats']:
        completion = out/f'round-{repeat}.json'
        if completion.exists():
            assert read(completion)['status'] == 'COMPLETED'
            continue
        entries = []
        for c,cond in ordered if repeat == 1 else reversed(ordered):
            folder = cell_folder(out,c,cond)
            arm = c[3]
            entries.append(dict(session=f'{folder.name}-r{repeat}',key=c[4],wording=arm,repeat=repeat,
                                folder=str(folder.relative_to(out)),source=read(folder/'protocol.json')['source_prompt'],
                                receipts=str((folder/f'{arm}_{repeat}_receipts.jsonl').relative_to(out))))
        plan = out/f'plan-{repeat}.json'
        if plan.exists():
            assert read(plan) == entries
        write_json(plan,entries)
        # Completed paths survive an interrupted round. Partial receipts and logs are task-owned.
        done,pending = [],[]
        for entry in entries:
            folder = out/entry['folder']
            receipt = out/entry['receipts']
            tape = folder/f'{entry["wording"]}_{repeat}.json'
            mark = folder/f'finished-{repeat}.json'
            if mark.exists():
                assert tape.exists() and len(receipt.read_bytes().splitlines()) == 61
                done.append(read(mark))
            else:
                receipt.unlink(missing_ok=True)
                tape.unlink(missing_ok=True)
                pending.append(entry)
        def execute(entry):
            event = run_entry(out,entry)
            write_json(out/entry['folder']/f'finished-{repeat}.json',event)
            return event
        start = utc()
        if pending:
            with server(plan,out/f'round-{repeat}_server.log'), ThreadPoolExecutor(max_workers=3) as pool:
                done.extend(pool.map(execute,pending))
        write_json(completion,dict(status='COMPLETED',started_at=start,finished_at=utc(),paths=done))
    write_json(out/'run.json',dict(status='COMPLETED',finished_at=utc(),eligible_contexts=sum(gates['accepted'].values()),
                                   paths=8*sum(gates['accepted'].values())))
