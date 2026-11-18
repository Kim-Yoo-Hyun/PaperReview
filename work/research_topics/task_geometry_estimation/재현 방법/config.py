"""Stdlib-only manifest resolution; shared artifacts are pinned, never edited."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def shared_path(entry):
    path = (HERE / entry['path']).resolve()
    if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
        raise RuntimeError('Shared artifact changed; review before updating pin: ' + str(path))
    return path


def manifest():
    plan = json.loads((HERE / 'PLAN.json').read_text())
    if not plan.get('resolved'):
        shared = {k: shared_path(v) for k, v in plan['shared'].items()}
        parent = json.loads(shared['plan'].read_text())
        for key in plan['inherit']:
            plan[key] = parent[key]
        plan['resolved'] = True
    if plan['budgets'] != dict(physics_steps=10000, queries=8, model_steps=96,
                               tokens_per_query=12, vla_commands=0, optimizer_steps=0):
        raise RuntimeError('P0 bounds changed; explicitly review the probe contract')
    if len(plan['instructions']) != 2 or plan['conditions'] != [
            'original', 'identity', 'roi_bias', 'subpatch_permutation']:
        raise RuntimeError('Expected two instructions and four geometry conditions')
    if plan['model']['physical_normalizer'] is not None:
        raise RuntimeError('This probe never sends physical VLA commands')
    if (plan['geometry']['patch_size'], plan['geometry']['reso'],
            plan['scene']['width'], plan['scene']['height']) != (14, 2, 224, 224):
        raise RuntimeError('P0 spatial layout changed; review coordinate and pooling code')
    return plan


def build_context(destination):
    """Copy only authored source/config into a temporary Docker build context."""
    import shutil
    plan = manifest()
    raw = json.loads((HERE / 'PLAN.json').read_text())
    for name in ('Dockerfile', 'config.py', 'geometry.py', 'probe.py', 'checks.py'):
        shutil.copyfile(HERE / name, destination / name)
    shutil.copyfile(shared_path(raw['shared']['helper']), destination / 'shared_probe.py')
    shutil.copyfile(shared_path(raw['shared']['requirements']), destination / 'requirements.txt')
    (destination / 'PLAN.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
    return plan
