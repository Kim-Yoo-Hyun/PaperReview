"""Exact finite-sum diagnostics on native logits; no actual RL updates implied."""
import ast
import hashlib
import json
import types
import urllib.request
from pathlib import Path
import numpy as np
import torch

ROOT=Path('/tmp/c3_logits'); E=ROOT/'evidence'
CODE='7c51662df27b586f9e8a1ab35fcf849f2b8852f9'
sources={}
for key,path in {'loss':'verl/trainer/ppo/core_algos.py','functional':'verl/utils/torch_functional.py'}.items():
    raw=urllib.request.urlopen(f'https://raw.githubusercontent.com/PRIME-RL/SimpleVLA-RL/{CODE}/{path}').read()
    (ROOT/(key+'.py')).write_bytes(raw)
    sources[key]=raw.decode()
sources['gripper']=(ROOT/'libero_utils.py').read_text()
namespace={'np':np,'torch':torch}
def load(key,name):
    node=next(n for n in ast.walk(ast.parse(sources[key])) if isinstance(n,ast.FunctionDef) and n.name==name)
    exec(compile(ast.Module(body=[node],type_ignores=[]),key,'exec'),namespace)
    return namespace[name]
namespace['verl_F']=types.SimpleNamespace(masked_mean=load('functional','masked_mean'))
loss=load('loss','compute_policy_loss')
normalize=load('gripper','normalize_gripper_action');invert=load('gripper','invert_gripper_action')
# Native discrete decoder assignments; native gripper norm mask is false.
stats=json.loads((ROOT/'model/dataset_statistics.json').read_text())
assert stats['libero_10_no_noops']['action']['mask'][-1] is False
method=next(n for n in ast.walk(ast.parse((ROOT/'native/modeling_prismatic.py').read_text()))
            if isinstance(n,ast.FunctionDef) and n.name=='_verl_discrete_prediction')
tail=[n for n in method.body if isinstance(n,ast.Assign) and 1742<=n.lineno<=1744]
assert len(tail)==3
bins=np.linspace(-1,1,256)
ns={'np':np,'self':types.SimpleNamespace(vocab_size=32000,bin_centers=(bins[:-1]+bins[1:])/2),
    'predicted_action_token_ids':np.arange(31744,32000)}
exec(compile(ast.Module(body=tail,type_ignores=[]),'native_decoder','exec'),ns)
actions=np.zeros((256,7));actions[:,-1]=ns['normalized_actions']
commands=invert(normalize(actions))[:,-1]
classes,label=np.unique(commands,return_inverse=True)
assert np.bincount(label).tolist()==[65,191]
raw=np.load(E/'native_logits.npz')
logits=raw['action_logits'][:,6::7,:].astype(np.float64)
hidden=raw['gripper_hidden'].astype(np.float64)
all_hidden_norm=raw['action_hidden_squared_norm'].astype(np.float64)
assert logits.shape==(16,8,256) and hidden.shape==(16,8,4096)
manifest=json.loads((E/'observation_manifest.json').read_text())

def summaries(rows,key):
    values=np.array([r[key] for r in rows])
    return {'mean':float(values.mean()),'median':float(np.median(values)),
            'min':float(values.min()),'max':float(values.max())}

result={'scope':'16 demo observations / 4 episodes / 2 tasks; 128 correlated gripper slots',
        'actual_rl_updates':0,'advantages':'none observed; clipping uses a declared binary-class reward counterfactual',
        'command_classes':classes.tolist(),'token_class_counts':np.bincount(label).tolist(),
        'clip_high':.28,'clip_low':.2,'temperatures':{},
        'native_loss_source_sha256':hashlib.sha256(sources['loss'].encode()).hexdigest()}
for temperature in [1.0,1.6]:
    rows=[]
    for observation in range(16):
        for slot in range(8):
            z=logits[observation,slot]/temperature
            p=np.exp(z-z.max());p/=p.sum()
            cp=np.bincount(label,weights=p)
            q=np.stack([p*(label==c)/cp[c] for c in range(2)])
            class_score=q-p
            raw_score=np.eye(256)-p
            raw_trace=float(p@np.square(raw_score).sum(1))
            class_trace=float(cp@np.square(class_score).sum(1))
            assert class_trace<=raw_trace+1e-12
            assert np.max(abs(p@raw_score))<1e-12
            assert np.max(abs(cp@class_score))<1e-12
            conditional_entropy=[float(-np.sum(qc[qc>0]*np.log(qc[qc>0]))) for qc in q]
            representative=[int(np.where(label==c)[0][p[label==c].argmax()]) for c in range(2)]
            alias_mask=np.ones(256,dtype=bool);alias_mask[representative]=False
            # Deterministic +/-60% alternating tilt, renormalized WITHIN each class.
            proposed=p.copy()
            for c in range(2):
                ix=np.where(label==c)[0]
                factors=np.where(np.arange(len(ix))%2==0,.4,1.6)
                proposed[ix]=p[ix]*factors
                proposed[ix]*=cp[c]/proposed[ix].sum()
            new_cp=np.bincount(label,weights=proposed)
            assert np.max(abs(new_cp-cp))<1e-12
            advantage=label.astype(float)-cp[1] # hypothetical centered close-command reward
            def replay(old,new):
                args=[torch.tensor(v[None],dtype=torch.float64) for v in [np.log(old),np.log(new),advantage,p]]
                return [v.item() for v in loss(*args,.28,.2)]
            token_loss=replay(p,proposed)
            class_loss=replay(cp[label],new_cp[label])
            assert abs(class_loss[0])<1e-10 and class_loss[1]<1e-10
            hidden_scale=float(hidden[observation,slot]@hidden[observation,slot]/temperature**2)
            row={'observation':observation,'episode':manifest['samples'][observation]['metadata']['episode_index'],
                 'task_id':manifest['samples'][observation]['task_id'],'slot':slot,
                 'class_mass':cp.tolist(),'top_token_ids':[i+31744 for i in representative],
                 'conditional_top1':[float(qc.max()) for qc in q],
                 'conditional_effective_aliases':np.exp(conditional_entropy).tolist(),
                 'alias_mass':float(p[alias_mask].sum()), # stable equivalent of 1-sum class maxima
                 'token_entropy':float(-p@np.log(p)),'class_entropy':float(-cp@np.log(cp)),
                 'within_class_entropy':float(cp@np.array(conditional_entropy)),
                 'raw_score_trace':raw_trace,'class_score_trace':class_trace,
                 'score_trace_reduction_percent':float(100*(raw_trace-class_trace)/raw_trace),
                 'head_raw_score_trace':raw_trace*hidden_scale,'head_class_score_trace':class_trace*hidden_scale,
                 'counterfactual_token_loss':token_loss[0],'counterfactual_class_loss':class_loss[0],
                 'counterfactual_weighted_native_clip_fraction':token_loss[1],
                 'counterfactual_ratio_outside_bounds_mass':float(p@((proposed/p<.8)|(proposed/p>1.28))),
                 'counterfactual_class_clip_fraction':class_loss[1],
                 'counterfactual_token_kl':float(p@np.log(p/proposed))}
            rows.append(row)
    keys=['alias_mass','token_entropy','class_entropy','within_class_entropy','raw_score_trace','class_score_trace',
          'score_trace_reduction_percent','head_raw_score_trace','head_class_score_trace',
          'counterfactual_token_loss','counterfactual_weighted_native_clip_fraction','counterfactual_ratio_outside_bounds_mass']
    total_raw=sum(r['raw_score_trace'] for r in rows)
    total_class=sum(r['class_score_trace'] for r in rows)
    total_head_raw=sum(r['head_raw_score_trace'] for r in rows)
    total_head_class=sum(r['head_class_score_trace'] for r in rows)
    all_z=raw['action_logits'].astype(np.float64)/temperature
    all_p=np.exp(all_z-all_z.max(-1,keepdims=True));all_p/=all_p.sum(-1,keepdims=True)
    all_score_trace=np.sum(all_p*(1-2*all_p+np.square(all_p).sum(-1,keepdims=True)),axis=-1)
    all_head_score_trace=all_score_trace*all_hidden_norm/temperature**2
    total_joint_head=float(all_head_score_trace.sum())
    result['temperatures'][str(temperature)]={
        'summary':{key:summaries(rows,key) for key in keys},
        'aggregate_score_trace_reduction_percent':100*(total_raw-total_class)/total_raw,
        'aggregate_head_score_trace_reduction_percent':100*(total_head_raw-total_head_class)/total_head_raw,
        'gripper_share_of_factorized_chunk_head_score_trace_percent':100*total_head_raw/total_joint_head,
        'factorized_chunk_head_score_trace_reduction_percent':100*(total_head_raw-total_head_class)/total_joint_head,
        'joint_scope':'Conditional independent 56-token draws through frozen final linear head; no reward weighting or backbone gradient.',
        'observations':[{'observation':i,**{k:float(np.mean([r[k] for r in rows if r['observation']==i])) for k in ['alias_mass','raw_score_trace','class_score_trace']}} for i in range(16)],
        'rows':rows}
    print(temperature,json.dumps({k:v for k,v in result['temperatures'][str(temperature)].items() if k not in ['rows','observations']}),flush=True)
(E/'logits_analysis.json').write_text(json.dumps(result,indent=2,allow_nan=False))
