"""Original frozen VLA forward, with lossless layer streaming, inside Docker only.

The native forward code is not edited. Hooks load BF16 safetensor values as FP32
immediately before a module runs and release only its parameters afterwards.
"""
import gc
import hashlib
import json
import os
import resource
import sys
import time
from pathlib import Path
os.environ['USE_TF']='0'
os.environ['USE_FLAX']='0'
os.environ['TOKENIZERS_PARALLELISM']='false'
ROOT=Path('/tmp/c3_logits')
sys.path.insert(0,str(ROOT))
import numpy as np
import torch
from accelerate import init_empty_weights
from safetensors import safe_open
from native.configuration_prismatic import OpenVLAConfig
from native.modeling_prismatic import OpenVLAForActionPrediction

torch.set_num_threads(6)
torch.set_num_interop_threads(1)
torch.manual_seed(0)
torch.set_grad_enabled(False)
E=ROOT/'evidence';E.mkdir(exist_ok=True)
start=time.monotonic()
config=OpenVLAConfig.from_pretrained(ROOT/'model')
# These are the public fsdp_workers.py runtime overrides, not new model inputs.
config.use_proprio=False
config.proprio_dim=7
config._attn_implementation='sdpa'
config.text_config.use_cache=False
with init_empty_weights():
    model=OpenVLAForActionPrediction(config)
model.eval()
model.norm_stats=json.loads((ROOT/'model/dataset_statistics.json').read_text())
model.vision_backbone.set_num_images_in_input(1)
index=json.loads((ROOT/'model/model.safetensors.index.json').read_text())['weight_map']
params=dict(model.named_parameters())
assert set(model.state_dict())==set(index)==set(params)
assert (ROOT/'weight_receipts.json').exists(), 'All original SHA256 checks must complete first'
headers={name:safe_open(str(ROOT/'model'/name),framework='pt',device='cpu') for name in set(index.values())}
for key,parameter in params.items():
    assert list(parameter.shape)==headers[index[key]].get_slice(key).get_shape(),key
groups=['vision_backbone','projector','language_model.model.embed_tokens']
groups += [f'language_model.model.layers.{i}' for i in range(config.text_config.num_hidden_layers)]
groups += ['language_model.model.norm','language_model.lm_head']
assignments={name:[k for k in params if k.startswith(name+'.')] for name in groups}
flat=[k for keys in assignments.values() for k in keys]
assert len(flat)==len(set(flat))==len(params)
assert set(flat)==set(params)
events=[]
active_hidden=[]
active_head_norms=[]
current_positions=None
current_all_positions=None
first_layer_reference_checked=False
capture_full_logits=False
cached_lm_logits=[]

def parent_attr(key):
    parent,attr=key.rsplit('.',1)
    return model.get_submodule(parent),attr

def load_group(name):
    for key in assignments[name]:
        value=headers[index[key]].get_tensor(key)
        assert value.dtype==torch.bfloat16,(key,value.dtype)
        # BF16 -> FP32 exactly preserves every stored weight value.
        value=value.to(dtype=torch.float32,copy=True)
        parent,attr=parent_attr(key)
        setattr(parent,attr,torch.nn.Parameter(value,requires_grad=False))

def unload_group(name):
    for key in assignments[name]:
        parent,attr=parent_attr(key)
        setattr(parent,attr,torch.nn.Parameter(torch.empty(params[key].shape,device='meta',dtype=torch.float32),requires_grad=False))
    gc.collect()

def before(name):
    def hook(module,args,kwargs):
        load_group(name)
        module._probe_start=time.monotonic()
        if name=='language_model.lm_head':
            active_hidden.append(args[0][:,current_positions,:].detach().clone())
            active_head_norms.append(args[0][:,current_all_positions,:].double().square().sum(-1).cpu())
    return hook

def after(name):
    def hook(module,args,kwargs,result):
        global first_layer_reference_checked
        if name=='language_model.model.layers.0' and not first_layer_reference_checked:
            # Same real inputs/weights; direct resident forward bypasses streaming hooks.
            reference=module.forward(*args,**kwargs)
            difference=(result[0]-reference[0]).abs().max().item()
            assert difference==0.0,difference
            first_layer_reference_checked=True
            events.append({'resident_vs_streamed_first_layer_max_abs':difference})
        event={'module':name,'compute_seconds':time.monotonic()-module._probe_start,
               'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        events.append(event)
        print(json.dumps(event),flush=True)
        if name=='language_model.lm_head' and capture_full_logits:
            cached_lm_logits.append(result)
        unload_group(name)
    return hook

for name in groups:
    module=model.get_submodule(name)
    module.register_forward_pre_hook(before(name),with_kwargs=True)
    module.register_forward_hook(after(name),with_kwargs=True)

inputs=torch.load(ROOT/'prepared_inputs.pt',map_location='cpu',weights_only=True)
assert len(inputs)==16
batch_plan=[[0],list(range(1,8)),list(range(8,16))]
all_logits=[];all_hidden=[];all_head_norms=[];batch_records=[]
for ids in batch_plan:
    lengths={inputs[i]['input_ids'].shape[1] for i in ids}
    assert len(lengths)==1,'Within-task batches need no padding'
    values={k:torch.cat([inputs[i][k] for i in ids],dim=0) for k in ['input_ids','attention_mask','pixel_values']}
    assert values['input_ids'][:,-1].eq(29871).all()
    prompt_length=values['input_ids'].shape[1]
    current_positions=torch.arange(6,56,7)+256+prompt_length-1
    current_all_positions=torch.arange(56)+256+prompt_length-1
    active_hidden.clear()
    active_head_norms.clear()
    cached_lm_logits.clear()
    capture_full_logits=(ids==[0])
    batch_start=time.monotonic()
    with torch.inference_mode():
        logits=model(**values)
    assert logits.shape==(len(ids),56,32064),logits.shape
    action_logits=logits[:,:,-320:-64].clone().cpu()
    assert torch.isfinite(action_logits).all()
    assert len(active_hidden)==1
    hidden=active_hidden[0].cpu()
    assert hidden.shape==(len(ids),8,4096)
    if ids==[0]:
        # Independently execute the native rollout gather/argmax/decoder against the
        # actual LM output; avoids re-running the expensive vision/LLM computation.
        import types
        full=cached_lm_logits[0]
        stub=types.SimpleNamespace(vocab_size=model.vocab_size,bin_centers=model.bin_centers,
            _build_multimodal_attention=lambda a,b,c:(a,c),
            language_model=lambda **kw:types.SimpleNamespace(logits=full))
        decoded,token_ids=OpenVLAForActionPrediction._verl_discrete_prediction(
            stub,torch.zeros((1,1,1)),torch.zeros((1,1),dtype=torch.bool),
            torch.zeros((1,1,1)),torch.ones((1,1)),None,256,
            torch.tensor([prompt_length-1]),do_sample=False)
        assert torch.equal(token_ids,action_logits.argmax(-1)+31744)
        assert decoded.shape==(8,7)
        events.append({'native_rollout_vs_actor_action_token_ids_exact_match':True})
        del full,stub,decoded,token_ids
        cached_lm_logits.clear()
    all_logits.append(action_logits.numpy())
    all_hidden.append(hidden.numpy())
    all_head_norms.append(active_head_norms[0].numpy())
    record={'sample_ids':ids,'seconds':time.monotonic()-batch_start,
            'input_length':prompt_length,'gripper_hidden_positions':current_positions.tolist(),
            'finite':True,'min_logit':action_logits.min().item(),'max_logit':action_logits.max().item()}
    batch_records.append(record)
    np.savez_compressed(E/'native_logits.npz',action_logits=np.concatenate(all_logits),gripper_hidden=np.concatenate(all_hidden),action_hidden_squared_norm=np.concatenate(all_head_norms))
    (E/'forward_progress.json').write_text(json.dumps(batch_records,indent=2))
    print('FORWARD COMPLETE',json.dumps(record),flush=True)
    del logits,action_logits,hidden,values
    gc.collect()

source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
               for p in list((ROOT/'native').glob('*.py'))+list(ROOT.glob('*.py'))+list(ROOT.glob('*.sh'))}
runtime={'torch':torch.__version__,'execution':'original native forward with parameter load/release hooks',
    'storage_dtype':'bfloat16','compute_dtype':'float32','attention':'PyTorch SDPA, native causal semantics',
    'gpu_bf16_equivalence':'not verified','quantization':False,'parameters':sum(p.numel() for p in params.values()),
    'strict_parameter_keys_and_shapes':len(params),'missing_keys':[],'unexpected_keys':[],
    'training':False,'requires_grad':False,'on_policy_rollouts':0,'training_updates':0,
    'input_kind':'lossy AV1 demonstration frames','source_hashes':source_hashes,
    'weights':json.loads((ROOT/'weight_receipts.json').read_text()),'batch_records':batch_records,
    'events':events,'elapsed_seconds':time.monotonic()-start,
    'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'resident_first_layer_equivalence_checked':first_layer_reference_checked}
(E/'forward_runtime.json').write_text(json.dumps(runtime,indent=2))
print('ALL 16 NATIVE FORWARDS COMPLETE',flush=True)
