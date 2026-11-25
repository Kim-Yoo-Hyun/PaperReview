"""Verify the direct-policy gate, naturally observed image pairs and drawer outcomes."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
from PIL import Image

from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_layouts import unpack


D = read(PACKET / 'drawer/protocol.json')
STARTS = D['public_start_indices']
PERIOD = D['replan_every']
TICKS = list(range(0, D['horizon'], PERIOD))


def tape(out, name):
    return read(out / 'paths' / (name + '.json'))


def receipts(out, name):
    return [json.loads(line) for line in (out / 'receipts' / (name + '.jsonl')).read_text().splitlines()]


def command_sha(actions):
    return hashlib.sha256(np.asarray(actions, dtype='<f8').tobytes()).hexdigest()


def pixels(out, signature):
    path = out / 'frames' / (signature + '.png')
    if not path.is_file() and out.name == 'recapture':
        path = out.parent / 'frames' / (signature + '.png')
    with Image.open(path) as source:
        a = np.array(source)
    assert a.shape == (224, 224, 3) and a.dtype == np.uint8 and hashlib.sha256(a.tobytes()).hexdigest() == signature
    return a


def physical(t, tick=0):
    rows = [t['initial'], *t['rows']]
    m = {int(i) for i in t['geometry']['drawer']}
    gripper = {int(i) for i in t['geometry']['gripper']}
    for r in rows:
        assert all(a in gripper for a, b in r['gripper_pairs'])
        assert r['target_contact'] == any(b in m for a, b in r['gripper_pairs'])
        assert r['goal'] == (r['joints'][1] < -0.14)
    contacts = [i for i, r in enumerate(rows) if r['target_contact']]
    goals = [i for i, r in enumerate(rows) if r['goal']]
    return dict(first_contact=next(iter(contacts), None), first_goal=next(iter(goals), None),
                first_post_query_contact=next((i for i in contacts if i > tick), None),
                contact_controls=len(contacts), terminal_contact=rows[-1]['target_contact'],
                terminal_gripper_pairs=rows[-1]['gripper_pairs'], terminal_goal=rows[-1]['goal'],
                travel_mm=round(1000 * (rows[0]['joints'][1] - rows[-1]['joints'][1]), 6),
                success=bool(contacts and rows[-1]['goal']))


def check_policy(out, name, anchor=None, pair=None):
    t = tape(out, name)
    qs, rs = t['queries'], receipts(out, name)
    assert len(qs) == len(rs) == len(TICKS) and len(t['rows']) == D['horizon']
    assert [r['tick'] for r in qs] == TICKS and rs[0]['rng_before'] == [0, D['policy_seed']]
    assert all(a['rng_after'] == b['rng_before'] for a, b in zip(rs, rs[1:]))
    for i, (q, rec) in enumerate(zip(qs, rs)):
        actions = np.asarray(q['reply'])
        assert actions.shape == (10, 7) and np.isfinite(actions).all()
        assert (q['state'], q['sent'], D['prompt'], command_sha(actions)) == (
            rec['proprioception'], rec['rgb_sha256'], rec['prompt'], rec['actions_sha256'])
        sent = pair[t['arm']] if pair and q['tick'] == pair['tick'] else q['live']
        assert sent == q['sent']
        offset = q['tick']
        if pair and offset <= pair['tick']:
            a = anchor['queries'][i]
            assert (q['physics'], q['state']) == (a['physics'], a['state'])
        rows = t['rows'][offset:offset + PERIOD]
        expected = ([row['action'] for row in anchor['rows'][offset:offset + PERIOD]]
                    if pair and offset < pair['tick'] else actions[:PERIOD].tolist())
        assert [row['action'] for row in rows] == expected
    if pair:
        assert t['rows'][:pair['tick']] == anchor['rows'][:pair['tick']]
    return t, rs, physical(t, pair['tick'] if pair else 0)


def gate(out):
    summaries, exact, total = {}, 0, 0
    for start in STARTS:
        base = f'direct-1-{start}'
        for block in range(1, D['direct_blocks'] + 1):
            name = f'direct-{block}-{start}'
            t, _, summaries[name] = check_policy(out, name)
            anchor = tape(out, base)
            assert t['initial_physics'] == anchor['initial_physics']
            expected = receipts(out, base)
            for r in (1, 2):
                probe = receipts(out, f'probe-{block}-{r}-{start}')
                assert len(probe) == len(expected)
                for a, b in zip(expected, probe):
                    assert all(a[k] == b[k] for k in ('prompt', 'proprioception', 'rgb_sha256', 'rng_before', 'rng_after'))
                    exact += a['actions_sha256'] == b['actions_sha256']
                    total += 1
    passed = sum(x['success'] for x in summaries.values()) >= 3 and all(
        any(summaries[f'direct-{b}-{s}']['success'] for b in (1, 2)) for s in STARTS)
    return dict(passed=bool(passed and exact == total), direct=summaries, competence=passed,
                identical_chunks=exact, reinserted_chunks=total, unique_reference_queries=len(TICKS) * len(STARTS))


def select(out, anchors=None, count=None, width=2, priority=None):
    counts, phases, pairs = Counter(), {}, []
    for start in STARTS:
        source = tape(anchors or out, f'direct-1-{start}')
        summary = physical(source)
        replays = [read(out / 'survey' / f'render-{r:0{width}d}-{start}.json')
                   for r in range(1, (count or D['render_replays_per_start']) + 1)]
        for run in replays:
            assert run['controls'] == D['horizon'] and run['final_physics'] == source['final_physics']
            assert len(run['queries']) == len(TICKS) and run['reference'] == source['name']
        chosen = set()
        queries = list(enumerate(source['queries']))
        if priority and start in priority:
            queries.sort(key=lambda item: (item[1]['tick'] != priority[start], item[1]['tick']))
        for i, q in queries:
            tick = q['tick']
            phase = ('after_goal' if summary['first_goal'] is not None and tick >= summary['first_goal']
                     else 'approach' if summary['first_contact'] is None or tick < summary['first_contact']
                     else 'contact')
            window = phases.setdefault(f'{start}-{phase}', Counter())
            window['query_states'] += 1
            for run in replays:
                b = run['queries'][i]
                assert all(q[k] == b[k] for k in ('state', 'physics', 'tick'))
                changed = [c for c in CAMERAS if q['live'][c] != b['live'][c]]
                counts['comparisons'] += 1
                window['comparisons'] += 1
                if not changed:
                    window['both_images_identical'] += 1
                    continue
                if len(changed) != 1:
                    window['both_cameras_changed'] += 1
                    continue
                camera = changed[0]
                a_img, b_img = [pixels(out, row['live'][camera]).astype(np.int16) for row in (q, b)]
                delta = b_img - a_img
                locations = np.argwhere(np.any(delta != 0, axis=2))
                if len(locations) > 4 or np.abs(delta).max() > 1:
                    window['outside_pixel_bounds'] += 1
                    continue
                window['eligible_' + camera.rsplit('/', 1)[-1]] += 1
                if phase == 'after_goal' or phase in chosen:
                    continue
                chosen.add(phase)
                values = [dict(row=int(y), column=int(x), A=a_img[y,x].tolist(), B=b_img[y,x].tolist())
                          for y,x in locations]
                pairs.append(dict(id=f'{start}-{phase}', start=start, phase=phase, tick=tick,
                                  replay=run['name'], camera=camera, A=q['live'], B=b['live'], pixels=values))
    return dict(comparisons=counts['comparisons'], windows=phases, pairs=pairs)


def score(out):
    assert read(out / 'design.json') == D
    g = gate(out)
    assert g == read(out / 'gate.json')
    selection, outcomes = None, {}
    if g['passed']:
        selection = select(out)
        assert selection == read(out / 'selection.json')
        outcomes = branch_results(out, selection, out)
    return dict(gate=g, selection=selection, outcomes=outcomes, closed_loop_paths=len(list((out/'paths').glob('*.json'))))


def branch_results(out, selection, anchors):
    outcomes = {}
    for pair in selection['pairs']:
        anchor = tape(anchors, f"direct-1-{pair['start']}")
        baseline_keys = [(x['rng_before'], x['rng_after']) for x in receipts(anchors, anchor['name'])]
        by_arm, first, chunks = {}, {}, {}
        for arm in ('A', 'B'):
            runs, commands, replies = [], [], []
            for n in range(1, D['branch_blocks'] + 1):
                t, rs, result = check_policy(out, f"branch-{n}-{pair['id']}-{arm}", anchor, pair)
                assert [(x['rng_before'], x['rng_after']) for x in rs] == baseline_keys
                i = pair['tick'] // PERIOD
                runs.append(result)
                commands.append(t['rows'][pair['tick']]['action'])
                replies.append(t['queries'][i]['reply'])
            by_arm[arm] = runs
            first[arm], chunks[arm] = commands, replies
        first_delta = [float(np.max(np.abs(np.subtract(a,b)))) for a,b in zip(first['A'],first['B'])]
        chunk_delta = [float(np.max(np.abs(np.subtract(a,b)))) for a,b in zip(chunks['A'],chunks['B'])]
        outcomes[pair['id']] = dict(arms=by_arm, first_command_max_abs=first_delta, full_chunk_max_abs=chunk_delta,
             within_arm_unique_chunks={a:len({command_sha(v) for v in c}) for a,c in chunks.items()})
    return outcomes


def replay_one(folder, source):
    from drawer_sim import rollout
    t = read(source)
    return rollout(folder, 'replay', 'verify-' + t['name'], t['start'], reference=t['name'])


def verify_evidence(root, stage):
    runtime = read(stage/'runtime.json')
    for name, signature in runtime['sources'].items():
        paths = [stage/'sources'/name, root/'sources'/name, PACKET/name]
        assert any(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == signature for p in paths), name
    hashes = set()
    for path in [*(stage/'paths').glob('direct-*.json'), *(stage/'survey').glob('*.json')]:
        for query in read(path)['queries']:
            hashes.update(query['live'].values())
    for signature in hashes:
        pixels(stage, signature)


def main(folder, phase, output):
    with unpack(folder) as out:
        if phase == 'replay':
            # Isolate EGL and process-global reset RNGs per physical replay.
            def invoke(path):
                cmd = [sys.executable, str(Path(__file__).resolve()), str(path.parent.parent), '_one', '--path', str(path)]
                line = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True).splitlines()[-1]
                return json.loads(line)
            with ThreadPoolExecutor(max_workers=4) as pool:
                paths = [*(out/'paths').glob('*.json'), *(out/'recapture/paths').glob('*.json')]
                result = list(pool.map(invoke, sorted(paths)))
            report = dict(paths=len(result), controls=sum(v['controls'] for v in result), runs=result)
            if output:
                write_json(output, report)
            print(json.dumps(report))
        elif phase == 'verify':
            result = score(out)
            verify_evidence(out, out)
            if (out/'recapture/selection.json').is_file():
                from drawer_pairs import assessment
                sub = out/'recapture'
                result['recapture'] = assessment(out, sub)
                if (sub/'verification.json').is_file():
                    assert result['recapture'] == read(sub/'verification.json')
                verify_evidence(out, sub)
            assert result == read(folder / 'verification.json')
            print('Verified', result['closed_loop_paths']+result.get('recapture',{}).get('closed_loop_paths',0), 'closed-loop paths')
        else:
            result = {'gate': gate, 'select': select, 'score': score}[phase](out)
            write_json(out / {'gate':'gate.json', 'select':'selection.json', 'score':'verification.json'}[phase], result)
            print(phase, 'complete', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('phase', nargs='?', default='verify', choices=['gate','select','score','verify','replay','_one'])
    parser.add_argument('--path', type=Path)
    parser.add_argument('--output', type=Path)
    a = parser.parse_args()
    if a.phase == '_one':
        print(json.dumps(replay_one(a.folder, a.path)))
    else:
        main(a.folder, a.phase, a.output)
