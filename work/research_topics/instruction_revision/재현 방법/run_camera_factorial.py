"""Run the four individually restarted primary camera conditions, then the prespecified extension."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from zipfile import ZipFile

from camera_protocol import DESIGN, cell_folder, contexts, eligibility, geometry, key, protocol
from inside import artifacts, write_json
from run_atomic import utc
from run_layouts import INPUTS, prefix_gate
from run_r1 import digest, run_path, token_audit
from verify_atomic import CAMERAS, PACKET, read
from verify_first_view import contact
from verify_r1 import check_calibration


def sources(out, names):
    out.mkdir(parents=True,exist_ok=True)
    hashes = {}
    for name in dict.fromkeys(names):
        if (out/name).exists():
            assert digest(out/name) == digest(PACKET/name), name
        else:
            shutil.copyfile(PACKET/name,out/name)
        hashes[name] = digest(out/name)
    assert set(hashes) == {p.name for p in out.iterdir()}
    return hashes


def install_cell(out,d,context,condition):
    scene,host,donor,_,_ = context
    folder = cell_folder(out,context,condition)
    (folder/'frames').mkdir(parents=True,exist_ok=True)
    (folder/'logs').mkdir(exist_ok=True)
    spec = protocol(out,d,context,condition)
    write_json(folder/'protocol.json',spec)
    def link(source,destination):
        if destination.exists():
            assert digest(destination) == digest(source)
        else:
            os.link(source,destination)
    link(geometry(out,scene,host)/'prefix.json',folder/'prefix.json')
    for cam,source in zip(CAMERAS,d['camera_sources'][condition]):
        name = spec['first_view']['rgb_sha256'][cam]+'.png'
        link(geometry(out,scene,donor if source else host)/'frames'/name,folder/'frames'/name)
    return folder


def historical(out, d):
    archive = PACKET/d['source']['archive']/'study.zip'
    assert digest(archive) == d['source']['sha256']
    gates = {}
    with ZipFile(archive) as z:
        previous = json.loads(z.read('runtime_manifest.json'))
        original_gates = json.loads(z.read('gates.json'))['prefixes']
        for scene in d['historical_scenes']:
            for pos,source in [('o',11),('s',19)]:
                folder = geometry(out,scene,pos)
                base = f'seed-{scene}-{source}/'
                (folder/'frames').mkdir(parents=True)
                for name in ('protocol.json','calibration.json','prefix.json','base_prefix.json','reset_edit.json'):
                    (folder/name).write_bytes(z.read(base+name))
                spec,prefix,cal = (read(folder/f) for f in ('protocol.json','prefix.json','calibration.json'))
                assert spec['bottle_xy']['target'] == d['positions'][pos]
                assert spec['source_replay']['file_sha256'] == digest(folder/'prefix.json')
                for query in prefix['queries']:
                    for checksum in query['rgb_sha256'].values():
                        name = 'frames/'+checksum+'.png'
                        (folder/name).write_bytes(z.read(base+name))
                gate = original_gates[f'{scene}-{source}']
                assert gate['eligible'] and gate['branch'] == prefix_gate(folder,spec,cal)
                gates[f'{scene}-{pos}'] = gate
    return previous,gates


def core(out):
    d = read(PACKET/DESIGN)
    prior = PACKET/d['previous']['file']
    assert digest(prior) == d['previous']['sha256'] and read(prior)['decision'] == d['previous']['decision']
    out.mkdir(parents=True,exist_ok=False)
    shutil.copyfile(PACKET/DESIGN,out/'study.json')
    previous,gates = historical(out,d)
    qualification = Path('/prior/LATEST').read_text().strip()
    assert Path(qualification).name == qualification
    runtime = Path('/prior')/qualification/'runtime_manifest.json'
    meta = read(runtime)
    assert meta['status'] == 'PASS_IO_ONLY' and meta['image_id'] == previous['image_id'] == os.environ['REVISION_IMAGE_ID']
    assert meta['artifacts']['files'] == previous['artifacts']['files'] == artifacts(download=False)['files']
    shutil.copyfile(runtime,out/'runtime_manifest.json')
    names = (*INPUTS,DESIGN,'R1_MENTION_MATCHED.json','run_camera_factorial.py','camera_protocol.py',
             'serve_first_view.py','verify_first_view.py','run_first_view.py','verify_command_cross.py',
             'verify_neutral_layouts.py','run_bottle_xy.py','verify_layouts.py','verify_mention.py',
             'verify_raw_update.py','run_neutral_layouts.py')
    hashes = sources(out/'executed_sources',names)
    write_json(out/'historical_gates.json',gates)
    primary = contexts(d)[0]
    assert eligibility(out,primary,gates)
    word_spec = protocol(out,d,primary,'own')
    word_spec['arms'] = {**read(PACKET/'R1_CONTROL.json')['arms'],**read(PACKET/'R1_MENTION_MATCHED.json')['arms']}
    write_json(out/'tokenizer'/'protocol.json',word_spec)
    token_audit(out/'tokenizer','before')
    record = dict(started_at=utc(),image_id=meta['image_id'],qualification=qualification,
                  input_sha256=hashes, paths=[],jax_memory_fraction=os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'])
    controls = {}
    for condition in d['camera_sources']:
        folder = install_cell(out,d,primary,condition)
        spec = read(folder/'protocol.json')
        for repeat in d['repeats']:
            entry = dict(condition=condition,repeat=repeat,started_at=utc())
            print(f'Primary {condition} {repeat}',flush=True)
            run_path(folder,'B',repeat,record_server=True)
            entry['finished_at'] = utc()
            record['paths'].append(entry)
        if condition in ('own','both'):
            cal = read(geometry(out,11,'s')/'calibration.json')
            limits,_ = check_calibration(cal,spec)
            controls[condition] = [contact(read(folder/f'B_{r}.json'),spec,limits)['selection'] for r in d['repeats']]
            if condition == 'both':
                write_json(out/'primary-controls.json',dict(checked_at=utc(),selections=controls))
    record.update(status='COMPLETED',finished_at=utc())
    write_json(out/'core.json',record)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('out',type=Path)
    parser.add_argument('--extend',action='store_true')
    args = parser.parse_args()
    assert Path('/.dockerenv').is_file()
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    if args.extend:
        from camera_extension import extend
        extend(args.out)
    else:
        core(args.out)
