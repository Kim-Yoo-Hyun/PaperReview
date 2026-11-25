"""Transfer the preceding study's exact successful closed-scene commands to the new cabinet starts."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

from drawer_location import COHORT, DESIGN, FLAGS, TIMES
from inside import write_json
from replay_middle_aperture import play_commands, read_trace
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import BASE, outcome, summary
from verify_stove import sha
from verify_stove_layouts import digest


SCENES = ('partial-closed','partial-bottom','full-closed','full-bottom')


def old_path(z, name):
    return json.loads(z.read('paths/'+name+'.json'))


def one(out, prior, name):
    from drawer_location_sim import LocationCabinet,branch
    prep = partial(branch,corrections=read(out/'clearance.json')['arrangements'])
    with ZipFile(prior/'study.zip') as z:
        path = old_path(z,name)
    commands = [row['action'] for row in path['rows']]
    entry = dict(arm=path['arm'],lead=path['lead'])
    worlds = {m:play_commands(out,entry,commands,m,COHORT,LocationCabinet,prep,FLAGS) for m in SCENES}
    assert worlds['partial-closed']['final_physics']==path['final_physics']
    return worlds


def prior_report(out, prior):
    assert sha(prior/'study.zip')==DESIGN['parent_sha256']
    old = read(prior/'verification.json')
    representatives,paired = {},{}
    with ZipFile(prior/'study.zip') as z:
        plan = json.loads(z.read('sessions.json'))
        for n,e in plan.items():
            if e['mode']!='closed':
                continue
            assert e['arm'] in COHORT['arms'] and all(old['outcomes'][n][t]['top_in'] for t in ('300','600'))
            path = old_path(z,n)
            h = digest([v['action'] for v in path['rows']])
            paired[n] = representatives.setdefault((e['arm'],h),n)
    def worker(name):
        proc = subprocess.run([sys.executable,__file__,str(out),str(prior),'--one',name],
                              capture_output=True,text=True,timeout=360)
        if proc.returncode:
            raise RuntimeError(name+' '+proc.stderr[-1500:])
        return name,json.loads(proc.stdout.splitlines()[-1])
    with ThreadPoolExecutor(max_workers=3) as pool:
        worlds = dict(pool.map(worker,representatives.values()))
    scores = {}
    for name,cells in worlds.items():
        scores[name] = {}
        for mode,cell in cells.items():
            rows,touches = read_trace(cell['trace'],FLAGS)
            scores[name][mode] = {t:outcome(rows,touches,int(t)-BASE['lead']) for t in TIMES}
    for name,rep in paired.items():
        for t in TIMES:
            original = old['outcomes'][name][t]
            actual = scores[rep]['partial-closed'][t]
            assert {k:actual[k] for k in original}==original
    return dict(prior_zip_sha256=DESIGN['parent_sha256'], script_sha256=sha(Path(__file__)),
                native_successes=len(paired), distinct_donor_command_sequences=len(worlds),
                controls_per_sequence=next(iter(next(iter(worlds.values())).values()))['controls'],
                representatives=paired, worlds=worlds,
                by_time={t:{m:summary([scores[rep][m][t] for rep in paired.values()]) for m in SCENES} for t in TIMES})


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('study',type=Path)
    parser.add_argument('prior',type=Path,nargs='?',default=PACKET/Path(DESIGN['parent']).parent)
    parser.add_argument('--one')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.one:
        print(json.dumps(one(args.study,args.prior,args.one)))
    else:
        with unpack(args.study) as out:
            result=prior_report(out,args.prior)
        if args.output:
            if args.output.exists():
                raise FileExistsError(args.output)
            write_json(args.output,result)
        print('Replayed',result['distinct_donor_command_sequences'],'distinct historical command sequences on all four scenes')
