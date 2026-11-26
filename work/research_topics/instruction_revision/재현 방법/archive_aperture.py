"""Bundle drawer measurements and losslessly record a second physical replay."""
import argparse
from collections import defaultdict
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


@contextmanager
def new_bundle(destination):
    if destination.exists():
        raise FileExistsError(destination)
    with tempfile.TemporaryDirectory(dir=destination.parent) as tmp:
        stage = Path(tmp)/'bundle'
        stage.mkdir()
        yield stage
        sums = [f'{sha(p.read_bytes())}  {p.name}\n' for p in sorted(stage.iterdir())]
        (stage/'SHA256SUMS').write_text(''.join(sums))
        stage.rename(destination)


def write_measurements(run, metadata_file, stage):
    metadata = read(metadata_file)
    logs = defaultdict(list)
    files = {}
    for p in sorted(run.rglob('*')):
        if not p.is_file() or p==run/'verification.json':
            continue
        name = p.relative_to(run).as_posix()
        if p.parent.name=='logs' and not p.name.startswith('policy-'):
            logs[sha(p.read_bytes())].append(name)
        else:
            files[name] = p
    for h,names in logs.items():
        files['logs/simulator-'+h+'.log'] = run/names[0]
    metadata['path_log_groups_sha256'] = dict(logs)
    metadata['archive_script_sha256'] = sha(Path(__file__).read_bytes())
    files['sources/archive_aperture.py'] = Path(__file__)
    archive = stage/'study.zip'
    with ZipFile(archive,'x',compression=ZIP_DEFLATED,compresslevel=9) as z:
        for name,p in sorted(files.items()):
            z.write(p,name)
        z.writestr('environment.json',json.dumps(metadata,indent=2)+'\n')
    with ZipFile(archive) as z:
        assert z.testzip() is None and set(z.namelist())==set(files)|{'environment.json'}
        assert all(z.read(name)==p.read_bytes() for name,p in files.items())
        assert json.loads(z.read('environment.json'))==metadata
    shutil.copyfile(run/'verification.json',stage/'verification.json')


def figure_filename(result):
    default = 'drawer_width.png' if 'width_comparisons' in result else 'middle_aperture.png'
    if 'changed_camera_pixels' in result:
        default = 'drawer_first_camera.png'
    name = result.get('figure_name', default)
    assert name in ('middle_aperture.png', 'drawer_location.png', 'drawer_width.png', 'drawer_first_camera.png',
                    'drawer_view_duration.png')
    return name


def add_replay(stage, proof_file, figure):
    result, proof = read(stage/'verification.json'), read(proof_file)
    assert result['paths']==proof['paths']==len(proof['runs'])
    if 'alternates' in proof['runs'][0]:
        controls = 0
        for run in proof['runs']:
            if 'alternatives_per_path' in proof:
                assert len(run['alternates']) == proof['alternatives_per_path']
            for alternate in run['alternates'].values():
                assert alternate['controls'] == run['policy_controls']
                controls += alternate['controls']
        assert proof['alternate_controls'] == controls
    elif 'changed_camera_pixels' in result:
        assert 'alternate_controls' not in proof
        assert all('alternates' not in r for r in proof['runs'])
        assert proof['total_controls'] == sum(r['lead'] + r['policy_controls'] for r in proof['runs'])
    else:
        assert proof['alternate_controls'] == sum(r['policy_controls'] for r in proof['runs'])
    figure_name = figure_filename(result)
    if 'standalone' in result:
        assert result['standalone']['paths']==proof['standalone']['paths']
    shutil.copyfile(proof_file,stage/'physical_replay.json')
    shutil.copyfile(figure,stage/figure_name)


def pack(run, proof_file, figure, metadata_file, destination):
    with new_bundle(destination) as stage:
        write_measurements(run, metadata_file, stage)
        add_replay(stage,proof_file,figure)


def attach(archive, proof_file, figure, destination):
    sums = {n:h for h,n in (line.split('  ',1) for line in (archive/'SHA256SUMS').read_text().splitlines())}
    assert set(sums)=={'study.zip','verification.json'}
    with new_bundle(destination) as stage:
        for n,h in sums.items():
            shutil.copyfile(archive/n,stage/n)
            assert sha((stage/n).read_bytes())==h
        add_replay(stage,proof_file,figure)


def rerender_differences(first, second):
    changes = {}
    for a,b in zip(first,second,strict=True):
        assert dict(a,changed_rgb_ticks=b['changed_rgb_ticks'])==b, a['session']
        if a['changed_rgb_ticks']!=b['changed_rgb_ticks']:
            changes[a['session']] = b['changed_rgb_ticks']
    return changes


def seal(archive, repeat_file, destination):
    checksums = {n:h for h,n in (line.split('  ',1) for line in (archive/'SHA256SUMS').read_text().splitlines())}
    figure_name = figure_filename(read(archive/'verification.json'))
    assert set(checksums)=={'study.zip','verification.json','physical_replay.json',figure_name}
    assert all(sha((archive/n).read_bytes())==h for n,h in checksums.items())
    first,second = read(archive/'physical_replay.json'),read(repeat_file)
    repeat_digest = sha(json.dumps(second,sort_keys=True,separators=(',',':')).encode())
    metadata = dict(source_zip_sha256=checksums['study.zip'], repeat_report_digest=repeat_digest,
                    rerender_overrides=rerender_differences(first['runs'],second['runs']))
    second['runs'] = first['runs']
    if 'standalone' in first:
        direct = first['standalone']['runs']
        metadata['standalone_rerender_overrides'] = rerender_differences(direct,second['standalone']['runs'])
        second['standalone']['runs'] = direct
    assert first==second
    first['archive_repeat'] = metadata
    with new_bundle(destination) as stage:
        for name in ('study.zip','verification.json',figure_name):
            shutil.copyfile(archive/name,stage/name)
        (stage/'physical_replay.json').write_text(json.dumps(first,indent=2)+'\n')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    stages = parser.add_subparsers(dest='stage',required=True)
    for name,fields in [('measurements',('run','metadata','destination')),('attach',('archive','proof','figure','destination')),
                        ('pack',('run','proof','figure','metadata','destination')),
                        ('seal',('archive','repeat','destination'))]:
        sub = stages.add_parser(name)
        for field in fields:
            sub.add_argument(field,type=Path)
    args = parser.parse_args()
    if args.stage=='measurements':
        with new_bundle(args.destination) as stage:
            write_measurements(args.run,args.metadata,stage)
    elif args.stage=='attach':
        attach(args.archive,args.proof,args.figure,args.destination)
    elif args.stage=='pack':
        pack(args.run,args.proof,args.figure,args.metadata,args.destination)
    else:
        seal(args.archive,args.repeat,args.destination)
