"""Pinned public inputs; run inside the dedicated Docker container only."""
import concurrent.futures
import hashlib
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path('/tmp/c3_logits')
ROOT.mkdir(exist_ok=True)
MODEL = 'Haozhan72/Openvla-oft-SFT-libero10-trajall'
REV = '97d6e58bc5fbc402e85bab382e4206bb8e5f0db0'
CODE = '7c51662df27b586f9e8a1ab35fcf849f2b8852f9'
DATA = 'a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4'


def get(url, path, expected=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    h = hashlib.sha256()
    count = 0
    with urllib.request.urlopen(url, timeout=120) as resp, path.with_suffix(path.suffix+'.partial').open('wb') as out:
        while chunk := resp.read(4*1024*1024):
            out.write(chunk)
            h.update(chunk)
            count += len(chunk)
    digest = h.hexdigest()
    if expected:
        assert digest == expected, (path.name, digest, expected)
    path.with_suffix(path.suffix+'.partial').rename(path)
    rec = {'url':url, 'path':str(path.relative_to(ROOT)), 'bytes':count,
           'sha256':digest, 'seconds':time.monotonic()-start}
    print(json.dumps({'downloaded':rec}), flush=True)
    return rec


if __name__ == '__main__':
    api = f'https://huggingface.co/api/models/{MODEL}/revision/{REV}?blobs=true'
    info = json.load(urllib.request.urlopen(api))
    assert info['sha'] == REV
    names = [x for x in info['siblings'] if x['rfilename'].endswith(('.json','.model','.safetensors'))]
    receipts = []
    # Code is taken from the paper's pinned runtime override, not HF's bundled variant.
    folder = ROOT/'native'
    folder.mkdir(exist_ok=True)
    (folder/'__init__.py').write_text('')
    for name in ['configuration_prismatic.py','modeling_prismatic.py','processing_prismatic.py','constants.py','train_utils.py']:
        url = f'https://raw.githubusercontent.com/PRIME-RL/SimpleVLA-RL/{CODE}/verl/utils/vla_utils/openvla_oft/{name}'
        receipts.append(get(url, folder/name))
    for name in ['verl/workers/rollout/rob_rollout.py','verl/workers/actor/dp_rob.py',
                 'verl/workers/fsdp_workers.py','verl/utils/libero_utils.py',
                 'examples/run_openvla_oft_rl_libero.sh','examples/overwrite_vla_ckpt_utils.sh']:
        receipts.append(get(f'https://raw.githubusercontent.com/PRIME-RL/SimpleVLA-RL/{CODE}/{name}',ROOT/name.split('/')[-1]))
    libero_revision='8f1084e3132a39270c3a13ebe37270a43ece2a01'
    libero_url=f'https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/{libero_revision}/libero/libero/benchmark/libero_suite_task_map.py'
    receipts.append(get(libero_url,ROOT/'libero_suite_task_map.py'))
    (ROOT/'libero_revision.json').write_text(json.dumps({'revision':libero_revision,'url':libero_url}))
    lerobot_revision='afbf3f14a13bdad3e5990e2bed629c6539605658'
    for name in ['docs/source/libero.mdx','docs/source/env_processor.mdx','src/lerobot/processor/env_processor.py']:
        receipts.append(get(f'https://raw.githubusercontent.com/huggingface/lerobot/{lerobot_revision}/{name}',ROOT/('lerobot_'+name.split('/')[-1])))
    (ROOT/'lerobot_revision.json').write_text(json.dumps({'revision':lerobot_revision}))
    def job(entry):
        name=entry['rfilename']
        return get(f'https://huggingface.co/{MODEL}/resolve/{REV}/{name}',ROOT/'model'/name,entry.get('lfs',{}).get('sha256'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for rec in ex.map(job,names):
            receipts.append(rec)
            (ROOT/'download_receipts.json').write_text(json.dumps(receipts,indent=2))
    (ROOT/'weight_receipts.json').write_text(json.dumps([r for r in receipts if r['path'].endswith('.safetensors')],indent=2))
    for name in ['info.json','tasks.parquet']:
        receipts.append(get(f'https://huggingface.co/datasets/lerobot/libero/resolve/{DATA}/meta/{name}',ROOT/'data_meta'/name))
    receipts.append(get(f'https://huggingface.co/datasets/lerobot/libero/resolve/{DATA}/meta/episodes/chunk-000/file-000.parquet',ROOT/'data_meta/episodes.parquet'))
    (ROOT/'download_receipts.json').write_text(json.dumps(receipts,indent=2))
    print('FETCH COMPLETE',flush=True)
