"""Reanalyse recorded evidence in Docker; never starts a simulator rollout."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

if not Path('/.dockerenv').exists():
    raise SystemExit('Docker only.')
from analyse import run

source=Path('/recorded');output=Path('/output')
frozen=json.loads((source/'FROZEN_RUN.json').read_text())
assert hashlib.sha256(Path('analyse.py').read_bytes()).hexdigest()==frozen['analysis_sha256']
with tempfile.TemporaryDirectory(prefix='p4_reanalysis_',dir='/tmp') as tmp:
    dest=Path(tmp)
    for name in ['episodes.json','prefix_failures.json','compact_traces.jsonl.gz']:
        shutil.copyfile(source/name,dest/name)
    run(dest)
    expected=(source/'analysis.json').read_bytes();actual=(dest/'analysis.json').read_bytes()
    if expected!=actual:
        raise SystemExit('Saved analysis differs; preserve evidence and investigate, do not overwrite.')
    shutil.copyfile(dest/'analysis.json',output/'analysis.json')
    (output/'replay_report.json').write_text(json.dumps(dict(status='PASS',bit_identical_analysis=True,
        analysis_sha256=hashlib.sha256(actual).hexdigest(),new_rollouts=0,
        source_hashes={name:hashlib.sha256((source/name).read_bytes()).hexdigest()
                       for name in ['episodes.json','prefix_failures.json','compact_traces.jsonl.gz']}),indent=2)+'\n')
