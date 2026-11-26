"""Verify wire inputs and compare four camera treatments within a matched rollout quartet."""
from collections import Counter

from drawer_bowl_position import agreement
from drawer_camera_window import (BASE, CAMERAS, CHANNELS, DESIGN, DESIGN_FILE, HOSTS, INDICES, LAYOUT,
    LIMIT, MODES, PACKET, PARENT, STUDIES, TASK, alternate, check_preflight, check_routing, sessions)
from drawer_view_duration import behavior_record, rendered_inputs
from drawer_width import tape_for
from verify_atomic import read
from verify_middle_aperture import check_donors, check_sessions, contact_geometry, path_outcomes
from verify_stove import sha
from verify_stove_layouts import check_freeze, digest

SINGLES=('external','wrist')
CATEGORIES=('external_only','wrist_only','both_match','neither_match')
ENDPOINTS=('contact','at15','at30')


def category(targets):
    if targets['self']==targets['both']:
        return 'controls_agree'
    ext=targets['external']==targets['both']
    wrist=targets['wrist']==targets['both']
    if ext and wrist:
        return 'both_match'
    if ext:
        return 'external_only'
    return 'wrist_only' if wrist else 'neither_match'


def profile(values):
    counts=Counter(category(v) for v in values)
    eligible=[v for v in values if v['self']!=v['both']]
    matches={}
    for single in SINGLES:
        where=Counter('both' if v[single]==v['both'] else 'self' if v[single]==v['self'] else 'third' for v in eligible)
        matches[single]={k:where[k] for k in ('self','both','third')}
    return dict(quartets=len(values),eligible=len(eligible),**{k:counts[k] for k in CATEGORIES},
                eligible_both_no_contact=sum(v['both']=='none' for v in eligible),
                single_target_when_eligible=matches)


def group_summary(cells):
    values=[c['targets'] for c in cells]
    same=[v for v in values if v['self']==v['both']]
    names=list(CHANNELS)
    transition={}
    for view in names:
        transition[view]={k:dict(Counter(c['outcomes']['self'][k]+'->'+c['outcomes'][view][k] for c in cells)) for k in ENDPOINTS}
    return dict(primary=profile(values),
        controls_both_contact=profile([v for v in values if v['self']!='none' and v['both']!='none']),
        matched_prefix=profile([c['targets'] for c in cells if c['matched_prefix']]),
        matched_switch_images=profile([c['targets'] for c in cells if c['matched_prefix'] and c['same_switch_native'] and c['same_switch_alternate']]),
        controls_agree=dict(count=len(same),singles_change={v:sum(c[v]!=c['self'] for c in same) for v in SINGLES},
                            either_changes=sum(any(c[v]!=c['self'] for v in SINGLES) for c in same)),
        outcomes={v:{k:dict(Counter(c['outcomes'][v][k] for c in cells)) for k in (*ENDPOINTS,'first_destination')} for v in names},
        changed_from_self={v:{k:sum(c['outcomes'][v][k]!=c['outcomes']['self'][k] for c in cells) for k in ENDPOINTS} for v in names},
        transitions_from_self=transition,
        from_self_via_single_to_both={v:dict(Counter('->'.join((c['self'],c[v],c['both'])) for c in values)) for v in SINGLES})


def path_score(out,entry,geo,preps,keys,seen):
    a,m,v=entry['arm'],entry['mode'],entry['view']
    host,other=preps[a,m],preps[a,alternate(m)]
    tape=read(out/'paths'/(entry['session']+'.json'))
    sent,swaps=rendered_inputs(tape,entry,host,other,geo,INDICES)
    values,_=path_outcomes(out,entry,host,geo,keys,seen,sent_by_tick=sent,tape=tape)
    raster=Counter()
    by_cam=Counter()
    for q in tape['queries'][:LIMIT]:
        r=q['render']
        selected=CHANNELS[v] if r['exchange'] else []
        check_routing(r,q['live'],selected)
        for cam in selected:
            by_cam[cam]+=1
            raster['pixel_identical_exchanges']+=int(r['sent'][cam]==q['live'][cam])
        rejected=r.get('reference_retries',[])
        raster['initial_reference_retries']+=len(rejected)
        for attempt in [*rejected,r]:
            missed=attempt.get('mismatches',[])
            raster['unmatched_renders']+=len(missed)
            raster['native_reacquisitions']+=attempt.get('native_reacquisitions',0)
            for bad in missed:
                raster['max_pixels_one_camera']=max(raster['max_pixels_one_camera'],*bad['pixels'].values())
    info=behavior_record(values,tape,swaps)
    actions=info.pop('controls')
    info['first_20_sha256']=digest(actions)
    info['final_physics']=tape['final_physics']
    pre=tape['queries'][:2]
    switch=tape['queries'][2]
    prefix=dict(inputs=digest([(q['physics'],q['state'],q['render']['sent']) for q in pre]),
        first_ten=digest(actions[:10]),switch_state=digest([switch['physics'],switch['state']]),
        switch_native=switch['live'],switch_alternate=switch['render']['narrow_rgb'])
    return info,prefix,by_cam,raster


def make_quartet(names,paths,prefixes):
    assert set(names)==set(CHANNELS)
    prefix=[prefixes[n] for n in names.values()]
    cases={v:paths[n] for v,n in names.items()}
    targets={v:r['contact'] for v,r in cases.items()}
    checks={k:len({r[k] for r in prefix})==1 for k in ('inputs','first_ten','switch_state')}
    narrow=[prefixes[names[v]]['switch_alternate'] for v in ('external','wrist','both')]
    return dict(targets=targets,category=category(targets),outcomes=cases,matched_prefix=all(checks.values()),prefix_checks=checks,
                same_switch_native=all(r['switch_native']==prefix[0]['switch_native'] for r in prefix),
                same_switch_alternate=all(bool(d) and d==narrow[0] for d in narrow))


def score(out):
    src=out/'sources'
    runtime=read(out/'runtime.json')
    assert read(src/DESIGN_FILE)==DESIGN==read(out/'design.json')
    assert all(sha(src/n)==h for n,h in runtime['sources'].items())
    assert digest(runtime['checkpoint'])==BASE['checkpoint_manifest_sha256']
    check_freeze(src)
    for study in STUDIES.values():
        assert read(src/study['task_design'])==TASK and sha(src/TASK['bddl'])==TASK['bddl_sha256']
        check_donors(src,study)
    entries=sessions()
    check_sessions(out,entries,STUDIES[2]['blocks'])
    order=lambda e:(e['layout'],e['arm'],e['mode'],e['view'],e['key'])
    assert [order(e) for e in read(out/'block-1.json')]==[order(e) for e in reversed(read(out/'block-2.json'))]
    loads=read(out/'loads.json')
    assert [r['block'] for r in loads]==[1,2] and all(r['empty_before_load'] for r in loads) and loads[0]['cache']!=loads[1]['cache']
    assert loads[0]['started']<loads[0]['closed']<=loads[1]['started']<loads[1]['closed']
    keys=read(out/'rng.json')
    assert digest(keys)==DESIGN['rng_sha256']
    qual,bank,preflight=check_preflight(out)
    geo={i:contact_geometry(qual['geometry'][str(i)]) for i in STUDIES}
    preps={(a,m):tape_for(out,a,m) for a in LAYOUT for m in MODES}
    previous=PARENT.with_name('verification.json')
    assert sha(previous)==DESIGN['parent_verification_sha256']
    old=read(previous)['paths_by_session']
    paths,prefixes,index,history={},{},{},{}
    raster=Counter()
    delivered={v:Counter() for v in CHANNELS}
    seen=set()
    for n,e in entries.items():
        a,m,v=e['arm'],e['mode'],e['view']
        info,prefix,by_cam,counts=path_score(out,e,geo[e['layout']],preps,keys,seen)
        peak=max(raster['max_pixels_one_camera'],counts.pop('max_pixels_one_camera',0))
        raster.update(counts)
        raster['max_pixels_one_camera']=peak
        delivered[v].update(by_cam)
        paths[n],prefixes[n]=info,prefix
        index.setdefault((e['layout'],m,a,e['block'],e['key']),{})[v]=n
        if v in ('both','self'):
            prior=old[n.replace('.both-','.late-')]
            history.setdefault((e['layout'],m,v),[]).append((info,prior))
    cells={k:make_quartet(names,paths,prefixes) for k,names in index.items()}
    assert len(cells)==128
    groups,by_arm,prior,reloads={},{},{},{}
    for layout,study in STUDIES.items():
        for mode in HOSTS:
            label=f'{layout}/{mode}'
            subset=[c for (i,m,a,b,s),c in cells.items() if (i,m)==(layout,mode)]
            assert len(subset)==32
            groups[label]=group_summary(subset)
            prior[label]={v:agreement(history[layout,mode,v]) for v in ('self','both')}
            for arm in study['arms']:
                for block in study['blocks']:
                    vals=[cells[layout,mode,arm,block,k]['targets'] for k in BASE['stove_seeds']]
                    by_arm[f'{label}/{arm}/b{block}']=profile(vals)
            twins=[(cells[layout,mode,a,1,k],cells[layout,mode,a,2,k]) for a in study['arms'] for k in BASE['stove_seeds']]
            repeats=[(c['outcomes'][v],d['outcomes'][v]) for c,d in twins for v in CHANNELS]
            reloads[label]=dict(outcomes=agreement(repeats),same_category=sum(c['category']==d['category'] for c,d in twins),
                quartets=len(twins),final_physics=sum(a['final_physics']==b['final_physics'] for a,b in repeats),
                categories=dict(Counter(c['category']+'->'+d['category'] for c,d in twins)))
    detail={'/'.join(map(str,k)):{field:value for field,value in c.items() if field!='outcomes'} for k,c in cells.items()}
    return dict(figure_name=DESIGN['figure'],paths=len(entries),policy_queries=sum(e['queries'] for e in entries.values()),
        preflight_hosts=sum(len(item['views'])==len(CHANNELS) for records in preflight.values() for item in records.values()),
        changed_camera_pixels=bank['changed_pixels'],render_checks=len(entries)*LIMIT,raster=dict(raster),
        exchanged_queries=sum(len(r['exchanged']) for r in paths.values()),
        cutoffs=sum(paths[n]['exchanged']!=INDICES[e['view']] for n,e in entries.items()),
        delivered_channels={v:dict(counts) for v,counts in delivered.items()},
        groups=groups,posture_load=by_arm,parent_controls=prior,reloads=reloads,quartets=detail,paths_by_session=paths)
