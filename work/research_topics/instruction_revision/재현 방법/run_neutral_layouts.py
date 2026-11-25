"""Run neutral B/T continuations from two previously sealed R1 layouts."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

from inside import artifacts, write_json
from run_atomic import utc
from run_layouts import INPUTS, base_inputs, layout_spec, prefix_gate
from run_r1 import digest, run_path
from verify_atomic import PACKET, read


STUDY = 'R1_NEUTRAL_LAYOUTS.json'


def inputs():
    design = read(PACKET/STUDY)
    reference = PACKET/design['reference']['archive']
    for name, expected in design['reference']['files'].items():
        assert digest(reference/name) == expected, name
    mention = PACKET/design['mention_protocol']
    assert digest(mention) == design['mention_sha256']
    _, base, original = base_inputs()
    return design, reference, read(mention), base, original


def protocol(design, mention, base, seed):
    key = str(seed)
    spec = layout_spec(base, seed, design['reference']['prefix_sha256'][key])
    spec.update(arms={arm:mention['arms'][arm] for arm in ('B', 'T')}, words=mention['words'],
                run_order=design['order'][key], neutral_study=STUDY)
    for arm, referent in zip(('B', 'T'), spec['words']['objects']):
        assert spec['arms'][arm] == base['arms']['A']+' '+spec['words']['template'].format(referent)
    assert all(sorted(order) == sorted(spec['arms']) for order in spec['run_order'])
    return spec


def run_condition(folder, run_order, frozen_at, qualification, image_id, hashes, record_server=False):
    record = {'frozen_at':frozen_at, 'image_id':image_id, 'qualification':qualification,
              'input_sha256':hashes, 'frozen_calibration_sha256':digest(folder/'calibration.json'),
              'status':'STARTED', 'paths':[]}
    tokens = [sys.executable, str(PACKET/'run_r1.py'), 'tokens', str(folder)]
    subprocess.run([*tokens, 'before'], check=True)
    for repeat, order in enumerate(run_order, 1):
        for arm in order:
            entry = {'arm':arm, 'repeat':repeat, 'started_at':utc()}
            record['paths'].append(entry)
            write_json(folder/'run.json', record)
            print(f'Running {folder.name}, {arm}, repeat {repeat}', flush=True)
            run_path(folder, arm, repeat, record_server=record_server)
            entry['finished_at'] = utc()
    subprocess.run([*tokens, 'after'], check=True)
    record.update(status='COMPLETED', finished_at=utc())
    write_json(folder/'run.json', record)


def run(out):
    assert Path('/.dockerenv').is_file()
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    design, reference, mention, base, original = inputs()
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
    names = (*INPUTS, STUDY, design['mention_protocol'], 'run_neutral_layouts.py')
    hashes = {name:digest(PACKET/name) for name in names}
    for name in hashes:
        shutil.copyfile(PACKET/name, sources/name)

    with zipfile.ZipFile(reference/'study.zip') as saved:
        (out/'gates.json').write_bytes(saved.read('gates.json'))
        gates = read(out/'gates.json')
        for seed in design['seeds']:
            key = str(seed)
            folder = out/f'seed-{seed}'
            (folder/'frames').mkdir(parents=True)
            (folder/'logs').mkdir()
            spec = protocol(design, mention, base, seed)
            for name in ('calibration.json', 'prefix.json'):
                (folder/name).write_bytes(saved.read(f'seed-{seed}/{name}'))
            gate = prefix_gate(folder, spec, read(folder/'calibration.json'))
            assert gate == gates['prefixes'][key] and gate['eligible'] and gates['layouts'][key]['layout_eligible']
            assert gate['prefix_sha256'] == spec['source_replay']['file_sha256']
            write_json(folder/'protocol.json', spec)
            shutil.copyfile(runtime, folder/'runtime_manifest.json')
    frozen_at = utc()
    for seed in design['seeds']:
        folder = out/f'seed-{seed}'
        run_condition(folder, design['order'][str(seed)], frozen_at, qualification, meta['image_id'], hashes)
    write_json(out/'run.json', {'status':'COMPLETED', 'input_sha256':hashes, 'frozen_at':frozen_at,
                                'finished_at':utc(), 'jax_memory_fraction':os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION']})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('out', type=Path)
    run(parser.parse_args().out)
