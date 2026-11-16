"""Run bounded contract checks inside Docker and save auditable artifacts."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import time
import unittest

import source_repair
import test_contract

HERE = Path(__file__).resolve().parent


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed_names = []

    def addSuccess(self, test):
        self.passed_names.append(test.id())
        super().addSuccess(test)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if any(args.output.iterdir()):
        raise ValueError('Output must be empty; preserve previous evidence')
    signal.alarm(60)
    started = time.monotonic()
    test_contract.SOURCE_ROOT = args.source
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_contract)
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult).run(suite)
    artifacts = {}
    if result.wasSuccessful():
        original, modified = source_repair.repair(args.source)
        patch = source_repair.patch_text(original, modified)
        (args.output / 'source_repair.patch').write_text(patch)
        protocol = json.loads((HERE / 'PROTOCOL.json').read_text())
        f = protocol['fixture']
        records = []
        for i, permutation in enumerate(f['permutations']):
            config = {k: f[k] for k in ['schema_version', 'group_id', 'split', 'scene_seed', 'target_color']}
            config['color_permutation'] = permutation
            records.append({'task': 'VideoUnmask', 'episode': i, 'seed': f['scene_seed'], 'difficulty': 'easy',
                            'status': 'PLANNED_NOT_COLLECTED', 'proxy_fixture': config})
        (args.output / 'fixture_plan.json').write_text(json.dumps({'env_id': 'VideoUnmask',
            'role': 'Three reset configurations for future qualification, not data or episode outcomes', 'records': records}, indent=2) + '\n')
        artifacts['modified_source_sha256'] = {path: hashlib.sha256(content.encode()).hexdigest() for path, content in modified.items()}
        artifacts['patch_sha256'] = hashlib.sha256(patch.encode()).hexdigest()
    report = {
        'task_id': 'GAP-N3', 'completed_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'PASS' if result.wasSuccessful() else 'FAIL', 'tests_run': result.testsRun,
        'passed_tests': result.passed_names, 'failures': [str(t) + '\n' + text for t, text in result.failures],
        'errors': [str(t) + '\n' + text for t, text in result.errors], 'skipped': result.skipped,
        'elapsed_seconds': time.monotonic() - started, 'python': platform.python_version(), 'machine': platform.machine(),
        'image_reference': os.environ.get('N3_IMAGE_REFERENCE'),
        'evidence_type': 'SYNTHETIC_CONTRACT_AND_ISOLATED_SOURCE_BINDING',
        'boundary': 'Upstream source parsed/compiled; selected AST call sites executed with stand-in actors/predicates. No simulator, renderer, native planner, learned model or tensor payload executed.',
        'upstream_sources': source_repair.source_lock(),
        'local_code_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.iterdir()) if p.suffix in {'.py', '.json', '.sh'}},
        'artifacts': artifacts,
        'gates': {'source_patch_and_contract': result.wasSuccessful(), 'native_fixture': False,
                  'hdf5_builder_integration': False, 'actual_model_input_and_memory': False,
                  'research_pilot': False},
        'policy_rollouts': 0, 'native_episodes': 0, 'training_steps': 0,
    }
    (args.output / 'contract_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'tests_run', 'elapsed_seconds', 'gates']}))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
