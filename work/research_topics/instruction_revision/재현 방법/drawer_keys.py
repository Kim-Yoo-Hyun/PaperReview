"""Secondary test of the two natural frames under eight paired native noise streams."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np

from inside import write_json
from verify_atomic import CAMERAS, read
from verify_drawer import D, PERIOD, command_sha, pixels, tape
from verify_layouts import unpack


SEEDS = range(8)


def forward(out, process, anchors):
    import jax
    from openpi.policies import policy_config
    from openpi.training import config
    from run_r1 import CHECKPOINT, MODEL
    from serve_first_view import ObservedPolicy

    policy = policy_config.create_trained_policy(config.get_config(MODEL), str(CHECKPOINT), default_prompt=None)
    samples = []
    for pair in read(out / 'selection.json')['pairs']:
        i = pair['tick'] // PERIOD
        q = tape(anchors, f"direct-1-{pair['start']}")['queries'][i]
        for seed in SEEDS:
            key = jax.random.key(seed)
            for _ in range(i):
                key, _ = jax.random.split(key)
            for arm in (('A', 'B') if process == 1 else ('B', 'A')):
                obs = {k: pixels(out, pair[arm][k]) for k in CAMERAS}
                obs.update({'observation/state':np.array(q['state']), 'prompt':D['prompt']})
                policy._rng = key
                receipt = io.StringIO()
                reply = ObservedPolicy(policy, receipt).infer(obs)['actions']
                samples.append(dict(pair=pair['id'], seed=seed, arm=arm,
                                    receipt=json.loads(receipt.getvalue()), reply=np.asarray(reply).tolist()))
    return samples


def evaluate(out, runs, anchors):
    pairs = read(out / 'selection.json')['pairs']
    indexed = [{(x['pair'], x['seed'], x['arm']):x for x in run} for run in runs]
    assert len(runs) == 2 and all(len(r) == len(pairs) * len(SEEDS) * 2 for r in runs)
    assert indexed[0] == indexed[1]
    scores = {}
    for p in pairs:
        by_seed = []
        index = p['tick'] // PERIOD
        state = tape(anchors, f"direct-1-{p['start']}")['queries'][index]['state']
        assert len({tuple(indexed[0][p['id'],seed,'A']['receipt']['rng_before']) for seed in SEEDS}) == len(SEEDS)
        for seed in SEEDS:
            a, b = [indexed[0][p['id'], seed, arm] for arm in ('A', 'B')]
            assert a['receipt']['rng_before'] == b['receipt']['rng_before']
            for v in (a,b):
                rec = v['receipt']
                assert rec['actions_sha256'] == command_sha(v['reply']) and rec['rgb_sha256'] == p[v['arm']]
                assert rec['proprioception'] == state and rec['prompt'] == D['prompt']
                if seed == 0:
                    t = tape(out, f"branch-1-{p['id']}-{v['arm']}")
                    assert t['queries'][index]['reply'] == v['reply']
            delta = np.abs(np.subtract(a['reply'], b['reply']))
            by_seed.append(dict(seed=seed, first=float(delta[0].max()), first_five=float(delta[:PERIOD].max()),
                                chunk=float(delta.max())))
        scores[p['id']] = by_seed
    return dict(seeds=list(SEEDS), exact_across_fresh_processes=len(indexed[0]), differences=scores)


def main(source, destination, anchors):
    assert Path('/.dockerenv').is_file()
    destination.mkdir()
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    with unpack(source) as out:
        assert read(out / 'selection.json')['pairs']
        for process in (1, 2):
            target = destination / f'forward-{process}.json'
            subprocess.run([sys.executable, __file__, str(out), str(target), '--process', str(process),
                            '--anchors', str(anchors)], check=True)
        runs = [read(destination / f'forward-{i}.json') for i in (1, 2)]
        write_json(destination / 'verification.json', dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   image=os.environ['REVISION_IMAGE_ID'], **evaluate(out, runs, anchors)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('source', type=Path)
    ap.add_argument('destination', type=Path)
    ap.add_argument('--process', type=int, choices=[1,2])
    ap.add_argument('--anchors', type=Path, required=True)
    args = ap.parse_args()
    if args.process:
        write_json(args.destination, forward(args.source, args.process, args.anchors))
    else:
        main(args.source, args.destination, args.anchors)
