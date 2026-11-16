"""Standard-library checks for a prepared packet, not policy/physics validation."""
import hashlib
import json
from pathlib import Path
import sys


RECIPE_FILES = (
    'Dockerfile', 'resume.sh', 'sim-requirements.in', 'RESUME_PLAN.json',
    'ARTIFACTS.json', 'inside.py', 'native_probe.py', 'packet_checks.py',
)


def recipe_hashes(root):
    root = Path(root)
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in RECIPE_FILES}


def verify_recipe(built_root, expected_root):
    built_root = Path(built_root)
    sealed = json.loads((built_root / 'recipe_sha256.json').read_text())
    built = recipe_hashes(built_root)
    if sealed != built:
        raise RuntimeError('Built recipe differs from its build receipt')
    expected = recipe_hashes(expected_root)
    changed = [name for name in RECIPE_FILES if expected[name] != built[name]]
    if changed:
        raise RuntimeError('Stale image; rebuild before assets/smoke: ' + ', '.join(changed))
    return built


def classify_probe(probe, client_exit_code):
    """Separate technical completion, native containment and research evidence."""
    result = {'stage': 'CLIENT_FAILED', 'native_rollouts_completed': 0,
              'native_containment_observed': False, 'research_effect_verified': False}
    if probe is None:
        result['failure_reason'] = 'No probe.json; no verified native completion'
        return result
    status = probe.get('status', 'MISSING_STATUS')
    result['probe_status'] = status
    completed = {'NATIVE_CONTAINMENT', 'STEP_BUDGET_EXHAUSTED', 'TERMINAL_WITHOUT_CONDITION'}
    if client_exit_code != 0 or status not in completed:
        result['failure_reason'] = f'Native client exit={client_exit_code}, status={status}'
        return result
    containment = status == 'NATIVE_CONTAINMENT'
    if probe.get('native_condition_met') is not containment:
        result['failure_reason'] = 'Contradictory status/native condition'
        return result
    result.update(stage='NATIVE_COMPLETED', native_rollouts_completed=1,
                  native_containment_observed=containment)
    return result


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'seal':
        root = Path(sys.argv[2])
        (root / 'recipe_sha256.json').write_text(json.dumps(recipe_hashes(root), indent=2) + '\n')
    else:
        raise SystemExit('Expected: packet_checks.py seal <recipe directory>')
