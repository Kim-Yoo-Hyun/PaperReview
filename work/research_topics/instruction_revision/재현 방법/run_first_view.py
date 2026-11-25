"""Use the assigned camera pair for one revised query on each sealed scene-11 prefix."""
import argparse
from io import BytesIO
import json
import os
from pathlib import Path
import shutil
from zipfile import ZipFile

import numpy as np
from PIL import Image

from inside import artifacts, write_json
from run_atomic import utc
from run_layouts import INPUTS
from run_neutral_layouts import run_condition
from run_r1 import digest
from verify_atomic import CAMERAS, PACKET, read, sha
from verify_command_cross import score_path
from verify_r1 import check_calibration


STUDY = 'R1_FIRST_VIEW.json'


def inputs():
    design = read(PACKET/STUDY)
    reference = PACKET/design['source']['archive']
    assert all(digest(reference/name) == checksum for name,checksum in design['source']['files'].items())
    fixed = PACKET/design['fixed_command_comparison']['file']
    assert digest(fixed) == design['fixed_command_comparison']['sha256']
    assert read(fixed)['decision'] == 'ENDPOINT_FOLLOWS_COMMAND_STREAM_BOTH_DIRECTIONS'
    cells = {}
    with ZipFile(reference/'study.zip') as archive:
        old_runtime = json.loads(archive.read('runtime_manifest.json'))
        gates = json.loads(archive.read('gates.json'))['prefixes']
        for position in (11,19):
            key = f'11-{position}'
            base = f'seed-{key}/'
            raw = {name:archive.read(base+name) for name in ('protocol.json','prefix.json','calibration.json','tokens_before.json')}
            spec, prefix = (json.loads(raw[name]) for name in ('protocol.json','prefix.json'))
            branch = prefix['queries'][1]
            pair = design['branch_rgb_sha256'][str(position)]
            assert branch['completed_controls'] == design['intervention_tick'] == spec['switch'] == 2
            assert spec['scene_seed'] == design['scene_seed'] and spec['bottle_xy_seed'] == position
            assert spec['policy_rng_seed'] == 0 and spec['replan_controls'] == 5
            assert sha(raw['prefix.json']) == gates[key]['prefix_sha256'] == spec['source_replay']['file_sha256']
            assert gates[key]['eligible'] and branch['rgb_sha256'] == pair and set(pair) == set(CAMERAS)
            images = {cam:archive.read(base+f'frames/{checksum}.png') for cam,checksum in pair.items()}
            for cam,png in images.items():
                with Image.open(BytesIO(png)) as image:
                    pixels = np.array(image)
                assert pixels.shape == (224,224,3) and pixels.dtype == np.uint8 and sha(pixels.tobytes()) == pair[cam]
            cells[position] = dict(raw=raw,spec=spec,prefix=prefix,images=images)
    a,b = cells[11],cells[19]
    assert a['prefix']['queries'][1]['proprioception'] == b['prefix']['queries'][1]['proprioception']
    assert all(a['images'][cam] != b['images'][cam] for cam in CAMERAS)
    assert a['spec']['arms']['B'] == b['spec']['arms']['B']
    assert [r['dispatched'] for r in a['prefix']['rows']] == [r['dispatched'] for r in b['prefix']['rows']]
    return design,cells,old_runtime


def protocol(design, cells, physical, donor):
    spec = dict(cells[physical]['spec'])
    del spec['words']
    spec.update(arms={'B':spec['arms']['B']}, run_order=[['B'] for _ in design['repeats']],
                first_view={'study':STUDY,'physical_position':physical,'image_position':donor,
                            'rgb_sha256':design['branch_rgb_sha256'][str(donor)]})
    return spec


def run(out):
    assert Path('/.dockerenv').is_file()
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    design,cells,previous = inputs()
    qualification = Path('/prior/LATEST').read_text().strip()
    assert qualification and Path(qualification).name == qualification
    runtime = Path('/prior')/qualification/'runtime_manifest.json'
    meta = read(runtime)
    assert meta['status'] == 'PASS_IO_ONLY' and meta['image_id'] == os.environ['REVISION_IMAGE_ID']
    assert meta['artifacts']['files'] == previous['artifacts']['files'] == artifacts(download=False)['files']
    out.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(runtime,out/'runtime_manifest.json')
    shutil.copyfile(PACKET/STUDY,out/'study.json')
    sources = out/'executed_sources'
    sources.mkdir()
    names = (*INPUTS,STUDY,'run_first_view.py','serve_first_view.py','run_neutral_layouts.py','run_bottle_xy.py',
             'verify_command_cross.py','verify_neutral_layouts.py','verify_layouts.py')
    hashes = {name:digest(PACKET/name) for name in names}
    for name in hashes:
        shutil.copyfile(PACKET/name,sources/name)
    gates = {'started_at':utc(),'prefixes':{}}
    for physical,donor in design['cells']:
        key = f'{physical}-{donor}'
        folder = out/f'seed-{key}'
        (folder/'frames').mkdir(parents=True)
        (folder/'logs').mkdir()
        spec = protocol(design,cells,physical,donor)
        write_json(folder/'protocol.json',spec)
        for name in ('calibration.json','prefix.json'):
            (folder/name).write_bytes(cells[physical]['raw'][name])
        for cam,digest_value in spec['first_view']['rgb_sha256'].items():
            (folder/'frames'/f'{digest_value}.png').write_bytes(cells[donor]['images'][cam])
        shutil.copyfile(runtime,folder/'runtime_manifest.json')
        gates['prefixes'][key] = dict(eligible=True,prefix_sha256=digest(folder/'prefix.json'))
    gates['frozen_at'] = utc()
    write_json(out/'gates.json',gates)
    controls = {}
    for physical,donor in design['cells']:
        folder = out/f'seed-{physical}-{donor}'
        spec = read(folder/'protocol.json')
        run_condition(folder,spec['run_order'],gates['frozen_at'],qualification,meta['image_id'],hashes,record_server=True)
        if physical == donor:
            limits,_ = check_calibration(read(folder/'calibration.json'),spec)
            receiver = dict(spec=spec,limits=limits)
            controls[str(physical)] = [score_path(read(folder/f'B_{r}.json'),receiver)['selection'] for r in design['repeats']]
            if len(controls) == 2:
                write_json(out/'controls.json',{'checked_at':utc(),'selections':controls})
    write_json(out/'run.json',{'status':'COMPLETED','input_sha256':hashes,'frozen_at':gates['frozen_at'],
                               'finished_at':utc(),'image_id':meta['image_id'],'qualification':qualification,
                               'jax_memory_fraction':os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION']})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('out',type=Path)
    run(parser.parse_args().out)
