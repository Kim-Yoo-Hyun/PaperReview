"""Collect lossless observations from complete fixed-command replays in fresh EGL processes."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import os
from pathlib import Path
import subprocess
import sys

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack


DESIGN = read(PACKET / 'drawer/recapture.json')


def batch(source, out, number):
    assert Path('/.dockerenv').is_file() and 1 <= number <= DESIGN['batches']
    for subdir in ('frames', 'logs', 'survey', 'receipts', 'paths'):
        (out / subdir).mkdir(parents=True, exist_ok=True)
    count = DESIGN['replays_per_start_per_batch']
    with unpack(source) as root:
        assert read(root / 'gate.json')['passed']
        def launch(job):
            r, start = job
            name = f'render-{r:03d}-{start}'
            with (out / 'logs' / (name + '.log')).open('w') as log:
                subprocess.run([sys.executable, __file__, str(root), str(out), '--one', name, str(start)],
                               cwd='/opt/resteer', stdout=log, stderr=subprocess.STDOUT, check=True, timeout=300)
        jobs = [(r, s) for r in range((number - 1)*count + 1, number*count + 1) for s in DESIGN['starts']]
        with ThreadPoolExecutor(max_workers=DESIGN['parallel_simulators']) as pool:
            list(pool.map(launch, jobs))
    write_json(out / f'batch-{number}.json', dict(batch=number, paths=len(jobs), image=os.environ['REVISION_IMAGE_ID'],
               sources={s:hashlib.sha256((PACKET / s).read_bytes()).hexdigest() for s in
                        ('drawer_recapture.py','drawer_sim.py','drawer/recapture.json')}))
    print('Complete render batch', number, flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('source', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--batch', type=int)
    ap.add_argument('--one', nargs=2)
    a = ap.parse_args()
    if a.one:
        from drawer_sim import rollout
        rollout(a.out, 'survey', a.one[0], int(a.one[1]), source_root=a.source)
    else:
        batch(a.source, a.out, a.batch)
