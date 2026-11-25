"""Run the 2 × 2 base-scene by bottle-position experiment on the local revision image."""
import argparse
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import zipfile

import numpy as np

from inside import artifacts, write_json
from run_atomic import SIM_PYTHON, utc
from run_layouts import INPUTS, prefix_gate
from run_neutral_layouts import STUDY as NEUTRAL, inputs as neutral_inputs, protocol as neutral_protocol, run_condition
from run_r1 import digest
from verify_atomic import PACKET, read
from verify_r1 import check_calibration, prefix_signature


STUDY = 'R1_BOTTLE_XY.json'


def inputs():
    design = read(PACKET/STUDY)
    archive = PACKET/design['reference']['archive']
    for name, expected in design['reference']['files'].items():
        assert digest(archive/name) == expected, name
    neutral, _, mention, base, original = neutral_inputs()
    return design, archive, neutral, mention, base, original


def protocol(design, neutral, mention, base, scene, donor, frozen_prefix=None):
    spec = neutral_protocol(neutral, mention, base, scene)
    source = spec.pop('source_replay')
    key = f'{scene}-{donor}'
    spec.update(xy_study=STUDY, bottle_xy_seed=donor, archived_command_source=source['file_sha256'],
                run_order=design['order'][key], bottle_xy={'native':design['raw_reset_xy_m'][str(scene)],
                                                          'target':design['raw_reset_xy_m'][str(donor)]})
    if frozen_prefix is not None:
        spec['source_replay'] = dict(source, file_sha256=frozen_prefix)
    return spec


def max_difference(a, b):
    if a is None or b is None:
        assert a is b
        return 0.0
    left, right = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    assert left.shape == right.shape and np.isfinite(left).all() and np.isfinite(right).all()
    return float(np.max(np.abs(left-right)))


def partners(row, name, group):
    return {b if a in group else a for a,b in row[name+'_contacts']}


def qualify(folder, design, spec, native, donor):
    tape, cal, edit = (read(folder/name) for name in ('prefix.json', 'calibration.json', 'reset_edit.json'))
    assert digest(folder/'base_prefix.json') == tape['command_origin'] == spec['archived_command_source']
    assert read(folder/'base_prefix.json') == native and tape['policy_queries_for_prefix'] == 0
    assert tape['queries'][0]['reply'] == native['queries'][0]['reply']
    assert [r['dispatched'] for r in tape['rows']] == [r['dispatched'] for r in native['rows']]
    check_calibration(cal, spec)
    branch = prefix_gate(folder, spec, cal)
    start = edit['qpos_address']+1
    nq = edit['nq']
    before = edit['before']
    expected = before['integration_state'].copy()
    assert expected[start:start+2] == spec['bottle_xy']['native']
    expected[start:start+2] = spec['bottle_xy']['target']
    assert dict(before, integration_state=expected) == edit['after']
    assert len(tape['rows']) == spec['switch'] == 2
    trial = cal['check']
    support = trial['passive_support']
    table = trial['table_geom']
    assert len(support) == spec['horizon']+1 and support[0]['bowl_xyz'] == trial['bowl_xyz']
    bowl = set(tape['geometry']['contact_geoms']['bowl'].values())
    bottle = set(tape['bottle_geometry']['bottle'])
    assert table not in bowl | bottle and table >= 0
    both_supported = all(r['bowl_partners'] == r['bottle_partners'] == [table] for r in support)
    drift_mm = max(math.dist(support[0]['bowl_xyz'], r['bowl_xyz']) for r in support)*1000
    rows = [tape['initial_readout'], *tape['rows']]
    branch_supported = all(partners(r, 'bowl', bowl) == partners(r, 'bottle', bottle) == {table} for r in rows)
    snapshots = {}
    for index, tick in enumerate((0,spec['switch'])):
        actual = tape['snapshots'][str(tick)]
        prior = native['snapshots'][str(tick)]
        assert set(actual) == set(prior)
        assert all(actual[k] == prior[k] for k in actual if k not in ('integration_state','controller'))
        assert set(actual['controller']) == set(prior['controller'])
        ctl = max(max_difference(actual['controller'][k], prior['controller'][k]) for k in actual['controller'])
        state = np.asarray(actual['integration_state']) - prior['integration_state']
        state[start:start+2] = 0
        planned = donor['initial_readout'] if tick == 0 else donor['rows'][-1]
        old = native['initial_readout'] if tick == 0 else native['rows'][-1]
        view, old_view = tape['queries'][index], native['queries'][index]
        snapshots[str(tick)] = {
            'max_integration_except_xy':float(np.max(np.abs(state))),
            'max_qpos_except_xy':float(np.max(np.abs(state[1:1+nq]))),
            'max_controller':ctl, 'max_proprioception':max_difference(view['proprioception'],old_view['proprioception']),
            'max_bowl_plate_cabinet_xyz_m':max(max_difference(rows[tick][k],old[k]) for k in ('bowl_xyz','plate_xyz','cabinet_site_xyz')),
            'bottle_xy_error_m':max_difference(rows[tick]['bottle_pose']['xyz'][:2],planned['bottle_pose']['xyz'][:2]),
            'same_rgb_as_native':view['rgb_sha256'] == old_view['rgb_sha256']}
    unchanged = spec['scene_seed'] == spec['bottle_xy_seed']
    original_exact = prefix_signature(tape,2,5) == prefix_signature(native,2,5)
    matched = all(max(v['max_controller'], v['max_integration_except_xy'], v['max_proprioception']) <= design['state_tolerance']
                  and max(v['max_qpos_except_xy'],v['max_bowl_plate_cabinet_xyz_m'],v['bottle_xy_error_m']) <= design['position_tolerance_m']
                  for v in snapshots.values())
    return {'eligible':bool(branch['eligible'] and both_supported and branch_supported and matched
                            and drift_mm < cal['translation_m']*1000 and (not unchanged or original_exact)),
            'prefix_sha256':branch['prefix_sha256'], 'original_prefix_exact':original_exact,
            'before_edit_bottle_xy_m':spec['bottle_xy']['native'], 'after_edit_bottle_xy_m':spec['bottle_xy']['target'],
            'passive_states':len(support), 'passive_table_only':both_supported, 'passive_bowl_peak_mm':drift_mm,
            'prefix_table_only':branch_supported, 'branch':branch, 'snapshots':snapshots}


def run(out):
    assert Path('/.dockerenv').is_file()
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    design, archive, neutral, mention, base, original = inputs()
    qualification = Path('/prior/LATEST').read_text().strip()
    assert qualification and Path(qualification).name == qualification
    runtime = Path('/prior')/qualification/'runtime_manifest.json'
    meta = read(runtime)
    assert meta['status'] == 'PASS_IO_ONLY' and meta['image_id'] == os.environ['REVISION_IMAGE_ID']
    assert meta['artifacts']['files'] == read(original/'runtime_manifest.json')['artifacts']['files'] == artifacts(download=False)['files']
    out.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(runtime, out/'runtime_manifest.json')
    shutil.copyfile(PACKET/STUDY, out/'study.json')
    sources = out/'executed_sources'
    sources.mkdir()
    names = (*INPUTS, NEUTRAL, STUDY, neutral['mention_protocol'], 'run_neutral_layouts.py',
             'run_bottle_xy.py', 'bottle_xy_sim.py')
    hashes = {name:digest(PACKET/name) for name in names}
    for name in hashes:
        shutil.copyfile(PACKET/name, sources/name)
    gates = {'started_at':utc(), 'prefixes':{}}
    edits = {}
    with zipfile.ZipFile(archive/'study.zip') as saved:
        for scene, donor in design['configurations']:
            key = f'{scene}-{donor}'
            folder = out/f'seed-{key}'
            (folder/'frames').mkdir(parents=True)
            (folder/'logs').mkdir()
            for old, name in [('prefix.json','base_prefix.json'),('calibration.json','calibration.json')]:
                (folder/name).write_bytes(saved.read(f'seed-{scene}/{old}'))
            shutil.copyfile(runtime, folder/'runtime_manifest.json')
            spec = protocol(design, neutral, mention, base, scene, donor)
            write_json(folder/'protocol.json', spec)
            subprocess.run([SIM_PYTHON, str(PACKET/'bottle_xy_sim.py'), str(folder)], check=True)
            native = read(folder/'base_prefix.json')
            other = json.loads(saved.read(f'seed-{donor}/prefix.json'))
            check = qualify(folder, design, spec, native, other)
            gates['prefixes'][key] = check
            before = read(folder/'reset_edit.json')['before']
            assert before == edits.setdefault(scene, before)
            if check['eligible']:
                write_json(folder/'protocol.json',protocol(design, neutral, mention, base, scene, donor, check['prefix_sha256']))
            print(f"Prepared {key}: eligible={check['eligible']}", flush=True)
    gates['frozen_at'] = utc()
    write_json(out/'gates.json',gates)
    for scene, donor in design['configurations']:
        key = f'{scene}-{donor}'
        if gates['prefixes'][key]['eligible']:
            run_condition(out/f'seed-{key}', design['order'][key], gates['frozen_at'], qualification, meta['image_id'], hashes)
    write_json(out/'run.json',{'status':'COMPLETED','input_sha256':hashes,'frozen_at':gates['frozen_at'],
                               'finished_at':utc(),'jax_memory_fraction':os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION']})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('out', type=Path)
    run(parser.parse_args().out)
