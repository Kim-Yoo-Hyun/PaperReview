"""Test naturally occurring drawer image pairs recovered after the physical replay mismatch."""
import argparse
from collections import Counter
import hashlib
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from camera_extension import server
from drawer_recapture import DESIGN
from inside import write_json
from run_atomic import SIM_PYTHON
from verify_atomic import PACKET, read
from verify_drawer import D, TICKS, branch_results, physical, pixels, select, tape
from verify_layouts import unpack


def selection(anchors, out):
    n = DESIGN['batches'] * DESIGN['replays_per_start_per_batch']
    batches = [read(out / f'batch-{i}.json') for i in range(1, DESIGN['batches'] + 1)]
    assert [b['batch'] for b in batches] == list(range(1, DESIGN['batches'] + 1))
    assert all(b['paths'] == DESIGN['replays_per_start_per_batch'] * len(DESIGN['starts']) for b in batches)
    assert sum(b['paths'] for b in batches) == len(list((out/'survey').glob('*.json'))) == n * len(DESIGN['starts'])
    assert all(b['image'] == read(anchors/'runtime.json')['image'] and b['sources'] == batches[0]['sources'] for b in batches)
    chosen = select(out, anchors=anchors, count=n, width=3, priority={1:55})
    chosen['registered_pair_ids'] = [p['id'] for p in chosen['pairs']]
    # Added after seeing two different render ticks, before any branch inference.
    # Preserve the original window selection. Also test up to four other observed
    # single-camera pairs before first goal, by start, tick, then replay order.
    chosen['additional_rule'] = 'Up to four further distinct eligible pre-goal frame pairs, ordered by start, tick, replay; added before branch inference.'
    used = {(p['start'],p['tick'],p['camera'],p['B'][p['camera']]) for p in chosen['pairs']}
    extra = 0
    for start in DESIGN['starts']:
        anchor = tape(anchors, f'direct-1-{start}')
        outcome = physical(anchor)
        runs = [read(out/'survey'/f'render-{r:03d}-{start}.json') for r in range(1,n+1)]
        for i,q in enumerate(anchor['queries']):
            tick = q['tick']
            if outcome['first_goal'] is not None and tick >= outcome['first_goal']:
                break
            for run in runs:
                b = run['queries'][i]
                changed = [c for c in q['live'] if q['live'][c] != b['live'][c]]
                if len(changed) != 1:
                    continue
                cam = changed[0]
                key = (start,tick,cam,b['live'][cam])
                if key in used or extra == 4:
                    continue
                a_img, b_img = pixels(anchors,q['live'][cam]).astype(int), pixels(out,b['live'][cam]).astype(int)
                points = np.argwhere(np.any(a_img != b_img, axis=2))
                if len(points) > 4 or np.abs(a_img-b_img).max() > 1:
                    continue
                used.add(key)
                extra += 1
                chosen['pairs'].append(dict(id=f'{start}-additional-{tick}-{extra}',start=start,tick=tick,
                    phase='approach' if outcome['first_contact'] is None or tick < outcome['first_contact'] else 'contact',
                    replay=run['name'],camera=cam,A=q['live'],B=b['live'],
                    pixels=[dict(row=int(y),column=int(x),A=a_img[y,x].tolist(),B=b_img[y,x].tolist()) for y,x in points]))
    return chosen


def assessment(anchors, out):
    from drawer_keys import evaluate
    chosen = selection(anchors, out)
    assert chosen == read(out/'selection.json') and read(out/'design.json') == DESIGN
    results = branch_results(out, chosen, anchors)
    assert len(list((out/'paths').glob('*.json'))) == 2*DESIGN['branch_blocks']*len(chosen['pairs'])
    noise = None
    if chosen['pairs']:
        noise = evaluate(out, [read(out/'keys'/f'forward-{n}.json') for n in (1,2)], anchors)
        saved = read(out/'keys/verification.json')
        assert all(saved[k] == v for k,v in noise.items())
    references = {s: tape(anchors, f'direct-1-{s}')['queries'] for s in DESIGN['starts']}
    variants = Counter()
    for path in (out/'survey').glob('*.json'):
        trace = read(path)
        for a, b in zip(references[trace['start']], trace['queries']):
            for cam, original in a['live'].items():
                actual = b['live'][cam]
                if original != actual:
                    variants[trace['start'], a['tick'], cam, original, actual] += 1
    inventory = []
    for (start, tick, camera, original, actual), count in sorted(variants.items()):
        a, b = pixels(anchors, original).astype(int), pixels(out, actual).astype(int)
        positions = np.argwhere(np.any(a != b, axis=2))
        inventory.append(dict(start=start, tick=tick, camera=camera, reference=original, alternative=actual,
                              occurrences=count, changed_pixels=len(positions), max_abs=int(np.abs(a-b).max()),
                              coordinates_and_rgb=[[int(y),int(x),a[y,x].tolist(),b[y,x].tolist()] for y,x in positions[:4]]))
    return dict(selection=chosen, observed_variants=inventory, outcomes=results, noise=noise,
                closed_loop_paths=len(list((out/'paths').glob('*.json'))))


def policy_round(anchors, out, pairs, n):
    arms = ('A','B') if n % 2 else ('B','A')
    jobs = [(f"branch-{n}-{p['id']}-{a}", p, a) for p in (pairs if n % 2 else reversed(pairs)) for a in arms]
    plan = out/f'treatment-{n}.json'
    write_json(plan, [dict(session=name, receipts=f'receipts/{name}.jsonl', source=D['prompt'],
                           key=D['policy_seed'], queries=len(TICKS)) for name,_,_ in jobs])
    with server(plan, out/'logs'/f'treatment-{n}.log'):
        for name, pair, arm in jobs:
            with (out/'logs'/f'{name}.log').open('w') as log:
                subprocess.run([SIM_PYTHON,__file__,str(anchors),str(out),'--branch',name,pair['id'],arm],
                               cwd='/opt/resteer',stdout=log,stderr=subprocess.STDOUT,timeout=1200,check=True)
    print('Completed paired block', n, flush=True)


def run(source, out):
    assert Path('/.dockerenv').is_file()
    os.environ.update(XLA_PYTHON_CLIENT_MEM_FRACTION='0.50',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with unpack(source) as root:
        write_json(out/'design.json', DESIGN)
        hashes = {s: hashlib.sha256((PACKET/s).read_bytes()).hexdigest() for s in
                  ('drawer_pairs.py','drawer_keys.py','drawer_recapture.py','drawer_sim.py','verify_drawer.py',
                   'camera_server.py','serve_first_view.py','drawer/recapture.json','resume.sh')}
        write_json(out/'runtime.json',dict(image=os.environ['REVISION_IMAGE_ID'],sources=hashes))
        chosen = selection(root, out)
        write_json(out/'selection.json', chosen)
        pairs = chosen['pairs']
        print('Selected',len(pairs),'natural pairs',flush=True)
        if pairs:
            for n in range(1,DESIGN['branch_blocks']+1):
                policy_round(root,out,pairs,n)
            from drawer_keys import main as noise_probe
            noise_probe(out,out/'keys',root)
        write_json(out/'verification.json',assessment(root,out))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('source', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--branch', nargs=3)
    a = ap.parse_args()
    if a.branch:
        from drawer_sim import rollout
        name, pair_id, arm = a.branch
        pair = next(p for p in read(a.out/'selection.json')['pairs'] if p['id'] == pair_id)
        rollout(a.out,'branch',name,pair['start'],pair,arm,source_root=a.source)
    else:
        run(a.source,a.out)
