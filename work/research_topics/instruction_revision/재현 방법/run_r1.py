"""Execute the calibrated R1 comparison with the released openpi server on local Docker."""
import dataclasses
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from urllib.request import urlopen

from inside import artifacts, write_json
from run_atomic import POLICY, SIM_PYTHON, utc


PACKET = Path(__file__).resolve().parent
SPEC = json.loads((PACKET/'R1_CONTROL.json').read_bytes())
CHECKPOINT = Path('/data/checkpoints/pi05_libero')
MODEL = 'pi05_libero'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def token_audit(out, stage, path_names=None):
    import numpy as np
    from PIL import Image
    from openpi import transforms
    from openpi.models.tokenizer import PaligemmaTokenizer
    from openpi.training import checkpoints, config

    spec = json.loads((out/'protocol.json').read_bytes())
    cfg = config.get_config(MODEL)
    data = cfg.data.create(cfg.assets_dirs,cfg.model)
    norm = checkpoints.load_norm_stats(CHECKPOINT/'assets',data.asset_id)
    native = [transforms.InjectDefaultPrompt(None),*data.data_transforms.inputs,
              transforms.Normalize(norm,use_quantiles=data.use_quantile_norm),*data.model_transforms.inputs]
    token_index, = [i for i,f in enumerate(native) if isinstance(f,transforms.TokenizePrompt)]
    tokenizer = native[token_index]
    unbounded = dataclasses.replace(tokenizer,tokenizer=PaligemmaTokenizer(max_len=4096))
    limit = cfg.model.max_token_len
    def audit(query):
        for transform in native[:token_index]:
            query = transform(query)
        limited = tokenizer(dict(query))
        full = unbounded(dict(query))
        ids = limited['tokenized_prompt'][limited['tokenized_prompt_mask']]
        all_ids = full['tokenized_prompt'][full['tokenized_prompt_mask']]
        assert len(ids) <= limit < 4096 and np.array_equal(ids,all_ids)
        record = {'tokens':len(ids),'ids_sha256':hashlib.sha256(ids.astype('<i4').tobytes()).hexdigest()}
        if stage == 'before' and ('words' in spec or 'first_view' in spec or spec['case']=='R4' or 'raw' in spec['arms']):
            record['ids'] = ids.tolist()
        return record
    records = {}
    if stage == 'before':
        blank = np.zeros((224,224,3),dtype=np.uint8)
        for name,prompt in {'source':spec['source_prompt'],**spec['arms']}.items():
            records[name] = [audit({'observation/image':blank,'observation/wrist_image':blank,
                                    'observation/state':np.zeros(8),'prompt':prompt})]
        if 'words' in spec:
            names = ('BB','TT') if 'branch_donors' in spec else ('B','T')
            left,right = [records[name][0]['ids'] for name in names]
            assert len(left) == len(right) == spec['words']['expected_tokens']
            assert [i for i,(a,b) in enumerate(zip(left,right)) if a != b] == spec['words']['differing_token_indices_zero_based']
    else:
        if path_names is None:
            path_names = [f'{arm}_{rep}' for rep in range(1,spec['repetitions']+1) for arm in spec['arms']]
        for name in path_names:
            records[name] = []
            for q in json.loads((out/f'{name}.json').read_bytes())['queries']:
                query = {'observation/state':np.asarray(q['proprioception']),'prompt':q['prompt']}
                for key,sha in q['rgb_sha256'].items():
                    with Image.open(out/'frames'/f'{sha}.png') as img:
                        query[key] = np.asarray(img)
                records[name].append(audit(query))
    write_json(out/f'tokens_{stage}.json',{'model':MODEL,'limit':limit,'discrete_state_input':tokenizer.discrete_state_input,
                                         'full_vs_native_ids_exact':True,'records':records})


def run_path(out,arm,repeat,mode='rollout',record_server=False):
    name = 'prefix' if mode=='prefix' else f'{arm}_{repeat}'
    with (out/'logs'/f'{name}_server.log').open('w') as log:
        cmd = [sys.executable,str(POLICY/'scripts/serve_policy.py'),'--port','8000','policy:checkpoint',
               f'--policy.config={MODEL}',f'--policy.dir={CHECKPOINT}']
        if record_server:
            cmd = [sys.executable, str(PACKET/'serve_first_view.py'), str(out/f'{name}_receipts.jsonl')]
        server = subprocess.Popen(cmd,cwd='/opt/resteer',stdout=log,stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic()+420
            while server.poll() is None:
                try:
                    with urlopen('http://127.0.0.1:8000/healthz',timeout=1) as reply:
                        if reply.status == 200:
                            break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise TimeoutError(f'{name} server startup')
                    time.sleep(1)
            else:
                raise RuntimeError(f'{name} server exited {server.returncode}')
            with (out/'logs'/f'{name}_sim.log').open('w') as sim_log:
                subprocess.run([SIM_PYTHON,str(PACKET/'r1_motion.py'),mode,str(out),arm,str(repeat)],
                               cwd='/opt/resteer',stdout=sim_log,stderr=subprocess.STDOUT,timeout=1200,check=True)
        finally:
            if server.poll() is None:
                server.terminate()
                try:
                    server.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    server.kill()
                    server.wait()


def main(out,protocol_file):
    spec = json.loads((PACKET/protocol_file).read_bytes())
    assert Path('/.dockerenv').is_file() and spec['policy'] == MODEL
    out.mkdir(parents=True,exist_ok=False)
    (out/'frames').mkdir()
    (out/'logs').mkdir()
    latest = Path('/prior/LATEST').read_text().strip()
    assert latest and Path(latest).name == latest
    runtime = Path('/prior')/latest/'runtime_manifest.json'
    qualification = json.loads(runtime.read_bytes())
    base = json.loads((PACKET/'ATOMIC_CONTROL.json').read_bytes())
    assert qualification['status'] == 'PASS_IO_ONLY' and qualification['image_id'] == os.environ['REVISION_IMAGE_ID']
    assert [qualification[k] for k in ('resteer_revision','openpi_revision')] == [base['source_commit'],base['openpi_commit']]
    case, = [c for c in json.loads((PACKET/'SEMANTIC_CASES.json').read_text())['cases'] if c['case_id'] == 'R1']
    assert spec['source_prompt'] == case['initial_utterance']
    assert SPEC['arms']['O'] == case['oracle_policy_prompt']
    if 'reference' in spec:
        reference = PACKET/spec['reference']['archive']
        for name,expected in spec['reference']['files'].items():
            assert digest(reference/name) == expected, name
        fixed = ('case','policy','policy_rng_seed','python_hash_seed','scene_seed','calibration_seed','warmup_controls',
                 'horizon','switch','replan_controls','repetitions','source_prompt','goal_key','protected_body','calibration')
        assert all(spec[k] == SPEC[k] for k in fixed)
        previous = json.loads((reference/'runtime_manifest.json').read_bytes())
        assert previous['artifacts']['files'] == qualification['artifacts']['files']
        if 'words' in spec:
            names = ('BB','TT') if 'branch_donors' in spec else ('B','T')
            for arm,referent in zip(names,spec['words']['objects']):
                assert spec['arms'][arm] == SPEC['arms']['A']+' '+spec['words']['template'].format(referent)
        if 'raw' in spec['arms']:
            assert spec['arms'] == {'raw':case['revision_utterance'], 'O':case['oracle_policy_prompt'], 'A':SPEC['arms']['A']}
        if 'branch_donors' in spec:
            donor_spec = json.loads((reference/'protocol.json').read_bytes())
            for arm,donor_name in spec['branch_donors'].items():
                assert donor_name == arm[0]+'_1.json' and spec['arms'][arm] == donor_spec['arms'][arm[1]]
        if 'run_order' in spec:
            assert all(sorted(order)==sorted(spec['arms']) for order in spec['run_order'])
            assert len(spec['run_order'])==spec['repetitions']
        if 'source_replay' in spec:
            assert all(spec['arms'][k] == SPEC['arms'][k] for k in ('O','A'))
    shutil.copyfile(runtime,out/'runtime_manifest.json')
    shutil.copyfile(PACKET/protocol_file,out/'protocol.json')
    files = ('R1_CONTROL.json','ATOMIC_CONTROL.json','SEMANTIC_CASES.json','atomic_control.py',
             'r1_motion.py','inside.py','run_atomic.py','run_r1.py')
    if protocol_file not in files:
        files += (protocol_file,)
    if 'branch_donors' in spec:
        files += ('replay_r1.py','verify_atomic.py',spec['base_protocol'])
    report = {'started_at':utc(),'image_id':qualification['image_id'],'qualification':latest,
              'input_sha256':{name:digest(PACKET/name) for name in files},'paths':[],'status':'STARTED'}
    try:
        assert artifacts(download=False)['files'] == qualification['artifacts']['files']
        if 'reference' in spec:
            shutil.copyfile(reference/'calibration.json',out/'calibration.json')
        else:
            subprocess.run([SIM_PYTHON,str(PACKET/'r1_motion.py'),'calibrate',str(out/'calibration.json')],check=True)
        report['frozen_calibration_sha256'] = digest(out/'calibration.json')
        report['frozen_at'] = utc()
        if 'branch_donors' in spec:
            subprocess.run([SIM_PYTHON,str(PACKET/'replay_r1.py'),str(out),'--prepare-donors'],check=True)
            report['donor_states_sha256'] = digest(out/'donor_states.json')
        subprocess.run([sys.executable,__file__,'tokens',str(out),'before'],check=True)
        for repeat in range(1,spec['repetitions']+1):
            order = spec['run_order'][repeat-1] if 'run_order' in spec else spec['arms']
            for arm in order:
                entry = {'arm':arm,'repeat':repeat,'started_at':utc()}
                report['paths'].append(entry)
                write_json(out/'run.json',report)
                print(f'Starting {arm} repetition {repeat}',flush=True)
                run_path(out,arm,repeat)
                entry['finished_at'] = utc()
                print(f'Completed {arm} repetition {repeat}',flush=True)
        subprocess.run([sys.executable,__file__,'tokens',str(out),'after'],check=True)
        assert digest(out/'calibration.json') == report['frozen_calibration_sha256']
        report['status'] = 'COMPLETED'
    except Exception as error:
        report.update(status='FAILED',error=f'{type(error).__name__}: {error}')
        raise
    finally:
        report['finished_at'] = utc()
        write_json(out/'run.json',report)


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == 'tokens':
        token_audit(Path(sys.argv[2]),sys.argv[3])
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('out',type=Path)
        parser.add_argument('--protocol',choices=('R1_CONTROL.json','R1_MENTION.json','R1_MENTION_MATCHED.json','R1_POST_RELEASE.json','R1_RAW_UPDATE.json'),
                            default='R1_CONTROL.json')
        args = parser.parse_args()
        main(args.out,args.protocol)
