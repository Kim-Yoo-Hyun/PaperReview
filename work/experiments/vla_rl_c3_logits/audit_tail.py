"""Post-hoc audit of last-slot concentration; run inside Docker after primary analysis."""
import ast
import difflib
import hashlib
import json
import urllib.request
from pathlib import Path
import numpy as np
import torch
from safetensors import safe_open

ROOT=Path('/tmp/c3_logits');E=ROOT/'evidence'
bundled=ROOT/'hf_bundled_modeling_prismatic.py'
url='https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero10-trajall/resolve/97d6e58bc5fbc402e85bab382e4206bb8e5f0db0/modeling_prismatic.py'
if not bundled.exists():bundled.write_bytes(urllib.request.urlopen(url).read())
native_tree=ast.parse((ROOT/'native/modeling_prismatic.py').read_text())
bundled_tree=ast.parse(bundled.read_text())
def method(tree,name):
    return [n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name==name][-1]
source_check={}
for name in ['_prepare_input_for_action_prediction','_prepare_labels_for_action_prediction','_verl_discrete_prediction','generate_action_verl','forward']:
    a,b=method(native_tree,name),method(bundled_tree,name)
    same=ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)
    source_check[name]={'same_ast':same,'diff':list(difflib.unified_diff(ast.unparse(b).splitlines(),ast.unparse(a).splitlines())) if not same else []}
assert all(source_check[n]['same_ast'] for n in ['_prepare_input_for_action_prediction','_prepare_labels_for_action_prediction','_verl_discrete_prediction'])
analysis=json.loads((E/'logits_analysis.json').read_text())
tail={'status':'post-hoc exploratory; prompted by concentration in slot 7',
      'bundled_source_url':url,'bundled_source_sha256':hashlib.sha256(bundled.read_bytes()).hexdigest(),
      'source_comparison':source_check,
      'diff_review':'forward/generate differ only in optional proprio projector plumbing; disabled in this recipe. SFT label/padding provenance remains unverified.',
      'temperatures':{}}
for temperature,data in analysis['temperatures'].items():
    rows=data['rows'];top=sorted(rows,key=lambda r:r['alias_mass'],reverse=True)
    removed=np.array([r['head_raw_score_trace']-r['head_class_score_trace'] for r in rows])
    final=np.array([r['slot']==7 for r in rows])
    share=float(removed[final].sum()/removed.sum())
    tail['temperatures'][temperature]={
        'alias_threshold_counts':{str(th):sum(r['alias_mass']>th for r in rows) for th in [1e-6,1e-3,.01,.1]},
        'top_rows':top[:8],
        'last_slot_share_of_removed_head_score_trace':share,
        'first_seven_slots_mean_alias_mass':float(np.mean([r['alias_mass'] for r in rows if r['slot']<7])),
        'last_slot_mean_alias_mass':float(np.mean([r['alias_mass'] for r in rows if r['slot']==7])),
        'whole_chunk_reduction_percent_if_only_first_seven_grippers_marginalized':data['factorized_chunk_head_score_trace_reduction_percent']*(1-share)}
(E/'tail_audit.json').write_text(json.dumps(tail,indent=2))

# Independent autograd check on actual saved hidden states and checkpoint head weights.
# It validates the restricted 256-token head Jacobian, not the whole backbone gradient.
torch.set_num_threads(2)
raw=np.load(E/'native_logits.npz')
with safe_open(str(ROOT/'model/model-00004-of-00004.safetensors'),framework='pt') as f:
    weight=f.get_slice('language_model.lm_head.weight')[31744:32000].to(torch.float64).requires_grad_()
checks=[]
for observation,slot in [(0,0),(1,7),(7,7),(9,7)]:
    h=torch.tensor(raw['gripper_hidden'][observation,slot],dtype=torch.float64)
    z=weight@h
    original=torch.tensor(raw['action_logits'][observation,7*slot+6],dtype=torch.float64)
    error=(z-original).abs().max().item()
    assert error<1e-4,error # floating-point GEMM batch-order tolerance
    scaled=z/1.6;p=scaled.softmax(0)
    token=int(p.argmax()); c=(torch.arange(256)>=65)==(token>=65)
    token_objective=scaled[token]-torch.logsumexp(scaled,dim=0)
    class_objective=torch.logsumexp(scaled[c],dim=0)-torch.logsumexp(scaled,dim=0)
    token_grad=torch.autograd.grad(token_objective,weight,retain_graph=True)[0]
    class_grad=torch.autograd.grad(class_objective,weight)[0]
    q=p.detach()*c/p.detach()[c].sum()
    score=torch.nn.functional.one_hot(torch.tensor(token),256)-p.detach()
    class_score=q-p.detach()
    token_expected=score[:,None]*h[None,:]/1.6
    class_expected=class_score[:,None]*h[None,:]/1.6
    tg=(token_grad-token_expected).abs().max().item()
    cg=(class_grad-class_expected).abs().max().item()
    assert max(tg,cg)<1e-10,(tg,cg)
    checks.append({'observation':observation,'slot':slot,'reconstructed_logit_max_abs_error':error,
        'token_gradient_max_abs_error':tg,'class_gradient_max_abs_error':cg})
(E/'numerical_validation.json').write_text(json.dumps({'scope':'actual checkpoint 256-row head weights and saved real hidden states; selected token/class logprob derivatives',
    'checks':checks,'all_passed':True,'backbone_gradient_checked':False},indent=2))
print(json.dumps({'tail':{t:{k:v for k,v in d.items() if k!='top_rows'} for t,d in tail['temperatures'].items()},'autograd_checks':checks}),flush=True)
