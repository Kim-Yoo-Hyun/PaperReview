"""Measure whether the response to late drawer images transfers with the tool start."""
from functools import partial
from itertools import islice

from drawer_bowl_position import agreement, collect, main, run_path, score as score_positions, sessions
from drawer_gripper_position_starts import (DESIGN, DESIGN_FILE, HOSTS, LAYOUT, SCRIPT, branch, check_first,
    checked_inputs, prepare, prepare_start, validate)
from verify_atomic import PACKET, read
from verify_stove import sha
from verify_stove_layouts import digest


def score(out):
    result = score_positions(out, design_file=DESIGN_FILE, inputs_fn=partial(checked_inputs,validate_fn=validate))
    path = (PACKET/DESIGN['parent']).with_name('verification.json')
    assert sha(path) == DESIGN['parent_verification_sha256']
    parent = read(path)['paths_by_session']
    entries = sessions()
    runs = result['paths_by_session']
    for layout, report in result['layouts'].items():
        comparisons, controls = {}, {}
        for name, entry in entries.items():
            if entry['layout'] != int(layout):
                continue
            view = entry['view']
            if entry['mode'] == HOSTS[0]:
                comparisons.setdefault(view,[]).append((runs[name],parent[name]))
            if view in ('self','late'):
                tape = read(out/'paths'/(name+'.json'))
                controls[name] = dict(actions=digest([r['action'] for r in islice(tape['rows'],10)]),
                    inputs=[(q['physics'],q['state'],q['render']['sent']) for q in tape['queries'][:2]])
        report['previous_native_agreement'] = {v:agreement(rows) for v,rows in comparisons.items()}
        paired = [(n,x,controls[n.replace('.self-','.late-')]) for n,x in controls.items() if '.self-' in n]
        report['before_late_window'] = dict(pairs=len(paired), same_inputs=sum(a['inputs']==b['inputs'] for n,a,b in paired),
            same_first_ten=sum(a['actions']==b['actions'] for n,a,b in paired),
            different_first_ten=[n for n,a,b in paired if a['actions']!=b['actions']])
    return result


if __name__ == '__main__':
    main(script=SCRIPT,label='gripper-position',prepare_cell=prepare_start,first_cell=partial(check_first,prepare_fn=branch),
         prepare_study=prepare,collect_study=partial(collect,design_file=DESIGN_FILE,script=SCRIPT,scorer=score,
            extra_sources=('drawer_gripper_position_starts.py',)),
         path_fn=partial(run_path,prepare_fn=branch),score_fn=score)
