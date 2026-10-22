"""Freeze demo selection and run the public image preprocessing inside Docker."""
import ast
import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

os.environ['USE_TF']='0'
os.environ['TOKENIZERS_PARALLELISM']='false'
ROOT=Path('/tmp/c3_logits')
sys.path.insert(0,str(ROOT))
from fetch_assets import DATA, get
import av
import numpy as np
import pyarrow.parquet as pq
from PIL import Image
import tensorflow as tf
import torch
from transformers import AutoTokenizer
from native.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor

receipts=[]
def fetch(name):
    path=ROOT/'dataset'/name
    if not path.exists():
        receipts.append(get(f'https://huggingface.co/datasets/lerobot/libero/resolve/{DATA}/{name}',path))
    return path

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

tasks=pq.read_table(ROOT/'data_meta/tasks.parquet').to_pydict()
instructions=dict(zip(tasks['task_index'],tasks['__index_level_0__']))
node=ast.parse((ROOT/'libero_suite_task_map.py').read_text()).body[0]
suite_map=ast.literal_eval(node.value)
native_names={re.sub(r'^(LIVING_ROOM|KITCHEN|STUDY)_SCENE\d+_', '',x).replace('_',' '):x for x in suite_map['libero_10']}
task_ids=[i for i in sorted(instructions) if instructions[i] in native_names][:2]
assert task_ids==[0,1]
episodes=pq.read_table(ROOT/'data_meta/episodes.parquet').to_pylist()
selected={i:[] for i in task_ids}
seen_files=set()
for episode in episodes:
    file_id=(episode['data/chunk_index'],episode['data/file_index'])
    if file_id in seen_files:
        continue
    seen_files.add(file_id)
    path=fetch('data/chunk-%03d/file-%03d.parquet'%file_id)
    table=pq.read_table(path).to_pydict()
    for eid in sorted(set(table['episode_index'])):
        inds=[k for k,x in enumerate(table['episode_index']) if x==eid]
        tids={table['task_index'][k] for k in inds}
        assert len(tids)==1
        tid=tids.pop()
        if tid in selected and len(selected[tid])<2:
            meta=episodes[eid]
            assert meta['episode_index']==eid and len(inds)==meta['length']
            assert [table['frame_index'][k] for k in inds]==list(range(meta['length']))
            selected[tid].append({'task_id':tid,'task':instructions[tid],
                'native_task':native_names[instructions[tid]], 'metadata':meta,
                'parquet':str(path.relative_to(ROOT)), 'parquet_sha256':digest(path)})
    if all(len(v)==2 for v in selected.values()):
        break
assert all(len(v)==2 for v in selected.values())
samples=[]
for tid in task_ids:
    for episode in selected[tid]:
        meta=episode['metadata']
        for fraction in [.1,.3,.6,.9]:
            frame=int((meta['length']-1)*fraction)
            samples.append({**episode,'fraction':fraction,'frame':frame,
                'video_time':meta['videos/observation.images.image/from_timestamp']+frame/10})
manifest={'dataset':'lerobot/libero','revision':DATA,'selection':'first 2 matched task IDs, first 2 episodes each; floor((length-1)*fraction)',
          'orientation':'already rotated 180 degrees vs simulator, per official LeRobot env_processor/libero docs; do not flip twice',
          'encoding':'AV1 yuv420p; lossy demo observations, not original RGB/on-policy states',
          'samples':samples}
evidence=ROOT/'evidence';evidence.mkdir(exist_ok=True)
(evidence/'observation_manifest.json').write_text(json.dumps(manifest,indent=2))
print('SELECTION FROZEN',[(s['task_id'],s['metadata']['episode_index'],s['frame']) for s in samples],flush=True)

# Execute only the audited, original pure preprocessing functions (no env/rollout imports).
scope={'np':np,'tf':tf,'Image':Image}
for filename,names in [('libero_utils.py',{'resize_image'}),('rob_rollout.py',{'crop_and_resize','center_crop_image'})]:
    tree=ast.parse((ROOT/filename).read_text())
    chosen=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in chosen}==names
    exec(compile(ast.Module(body=chosen,type_ignores=[]),filename,'exec'),scope)
processor=PrismaticProcessor(
    PrismaticImageProcessor.from_pretrained(ROOT/'model'),
    AutoTokenizer.from_pretrained(ROOT/'model',local_files_only=True))
videos={}
prepared=[]
for i,sample in enumerate(samples):
    meta=sample['metadata']
    key=(meta['videos/observation.images.image/chunk_index'],meta['videos/observation.images.image/file_index'])
    if key not in videos:
        videos[key]=fetch('videos/observation.images.image/chunk-%03d/file-%03d.mp4'%key)
    video=videos[key]
    with av.open(str(video)) as container:
        stream=container.streams.video[0]
        target=sample['video_time']
        container.seek(max(0,int((target-1)/float(stream.time_base))),stream=stream)
        candidates=[]
        for frame in container.decode(stream):
            if frame.time is None: continue
            if abs(frame.time-target)<.051: candidates.append(frame)
            if frame.time>target+.051: break
        assert candidates, (i,target)
        frame=min(candidates,key=lambda f:abs(f.time-target))
        assert abs(frame.time-target)<.002,(frame.time,target)
        rgb=frame.to_ndarray(format='rgb24')
    assert rgb.shape==(256,256,3)
    # The dataset camera is already in training orientation. Apply native JPEG/Lanczos and crop.
    resized=scope['resize_image'](rgb,(224,224))
    cropped=scope['center_crop_image'](Image.fromarray(resized))
    prompt=f"In: What action should the robot take to {sample['task'].lower()}?\nOut:"
    features=processor(prompt,cropped)
    if features['input_ids'][0,-1].item()!=29871:
        features['input_ids']=torch.cat([features['input_ids'],torch.tensor([[29871]])],dim=1)
        features['attention_mask']=torch.cat([features['attention_mask'],torch.ones((1,1),dtype=features['attention_mask'].dtype)],dim=1)
    prepared.append(dict(features))
    sample.update({'decoded_time':frame.time,'video':str(video.relative_to(ROOT)),
        'decoded_rgb_sha256':hashlib.sha256(rgb.tobytes()).hexdigest(),
        'pixels_sha256':hashlib.sha256(features['pixel_values'].numpy().tobytes()).hexdigest(),
        'prompt':prompt,'input_ids':features['input_ids'][0].tolist()})
    if i in [0,4,8,12]:
        Image.fromarray(rgb).save(ROOT/f'sample-{i}.png')
    print('PREPARED',i,flush=True)
for sample in samples:
    sample['video_sha256']=digest(ROOT/sample['video'])
torch.save(prepared,ROOT/'prepared_inputs.pt')
manifest['prepared_inputs_sha256']=digest(ROOT/'prepared_inputs.pt')
manifest['receipts']=receipts
(evidence/'observation_manifest.json').write_text(json.dumps(manifest,indent=2))
print('DATA READY',flush=True)
