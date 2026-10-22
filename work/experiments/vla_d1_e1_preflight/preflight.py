"""Bounded D1-E1 resource/source probe. Run only inside Docker; stdlib only.

Fetches public source and small JSON metadata into memory. Never imports upstream
code, downloads model weights/data, installs packages, or runs a policy/simulator.
"""

import ast
import concurrent.futures
import datetime
import glob
import hashlib
import json
import math
import platform
import shutil
import urllib.request
from pathlib import Path


if not Path('/.dockerenv').is_file():
    raise SystemExit('Docker-only probe: refusing host execution')

CODE_REV = 'e4287e94541f459edc4feabc4e181f537cd569a8'
MODEL = 'moojink/openvla-7b-oft-finetuned-libero-goal'
MODEL_REV = 'c2d0f9fbbd82674683b397ff923168a12f6a307b'
LIMIT = 4 * 1024 * 1024
FETCHED_BLOBS = {}


def read_text(path):
    p = Path(path)
    return p.read_text().strip() if p.is_file() else None


def fetch(item):
    kind, name, url = item
    record = {'kind': kind, 'name': name, 'url': url}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'D1-E1-readonly-preflight'})
        with urllib.request.urlopen(req, timeout=30) as response:
            blob = response.read(LIMIT + 1)
            if len(blob) > LIMIT:
                raise ValueError('Metadata/source exceeds 4 MiB cap')
            record['http_status'] = response.status
        record.update(bytes=len(blob), sha256=hashlib.sha256(blob).hexdigest())
        FETCHED_BLOBS[name] = blob
        if kind == 'source':
            lines = blob.decode().splitlines()
            patterns = ['cuda', 'flash_attn', 'flash_attention', 'bfloat16', 'DEVICE', 'A100', 'torch==', 'transformers']
            record['matching_line_numbers'] = {
                token: [i for i, line in enumerate(lines, 1) if token in line]
                for token in patterns
            }
        else:
            data = json.loads(blob)
            if kind == 'model_api':
                record['repository_revision'] = data['sha']
                record['files'] = [
                    {k: f[k] for k in ['rfilename', 'size', 'blobId', 'lfs'] if k in f}
                    for f in data['siblings']
                ]
            elif kind == 'weight_index':
                record['advertised_tensor_bytes'] = data.get('metadata', {}).get('total_size')
                record['shards'] = sorted(set(data.get('weight_map', {}).values()))
                record['tensor_names_count'] = len(data.get('weight_map', {}))
            elif kind == 'normalizer':
                record['dataset_keys'] = sorted(data)
                record['fields'] = {
                    dataset: {
                        group: {key: len(val) if isinstance(val, list) else type(val).__name__
                                for key, val in values.items()}
                        for group, values in item.items() if isinstance(values, dict)
                    } for dataset, item in data.items()
                }
                record['static_checks'] = {}
                for dataset, entry in data.items():
                    checks = {}
                    for field, dim in [('action', 7), ('proprio', 8)]:
                        values = entry[field]
                        checks[field] = {
                            'dimensions_match': all(len(values[k]) == dim for k in ['mean', 'std', 'min', 'max', 'q01', 'q99']),
                            'all_finite': all(math.isfinite(v) for k in ['mean', 'std', 'min', 'max', 'q01', 'q99'] for v in values[k]),
                            'q99_ge_q01': all(hi >= lo for lo, hi in zip(values['q01'], values['q99'])),
                            'degenerate_quantile_indices': [i for i,(lo,hi) in enumerate(zip(values['q01'], values['q99'])) if hi == lo],
                        }
                    record['static_checks'][dataset] = checks
            elif kind == 'config':
                record['selected_config'] = {
                    key: data[key] for key in ['architectures', 'model_type', 'torch_dtype', 'transformers_version', 'auto_map',
                                              'hidden_size', 'image_sizes', 'norm_stats']
                    if key in data and key != 'norm_stats'
                }
                tc = data.get('text_config', {})
                record['text_config_summary'] = {
                    key: tc[key] for key in ['hidden_size', 'num_hidden_layers', 'num_attention_heads', 'torch_dtype']
                    if key in tc
                }
        return record
    except Exception as exc:
        record['error'] = f'{type(exc).__name__}: {exc}'
        return record


sources = [
    ('source', path, f'https://raw.githubusercontent.com/moojink/openvla-oft/{CODE_REV}/{path}')
    for path in ['SETUP.md', 'LIBERO.md', 'pyproject.toml', 'experiments/robot/openvla_utils.py',
                 'prismatic/extern/hf/modeling_prismatic.py']
]
assets = [
    ('model_api', 'model_metadata', f'https://huggingface.co/api/models/{MODEL}/revision/{MODEL_REV}?blobs=true'),
    ('weight_index', 'model.safetensors.index.json', f'https://huggingface.co/{MODEL}/resolve/{MODEL_REV}/model.safetensors.index.json'),
    ('normalizer', 'dataset_statistics.json', f'https://huggingface.co/{MODEL}/resolve/{MODEL_REV}/dataset_statistics.json'),
    ('config', 'config.json', f'https://huggingface.co/{MODEL}/resolve/{MODEL_REV}/config.json'),
    ('source', 'hf/modeling_prismatic.py', f'https://huggingface.co/{MODEL}/resolve/{MODEL_REV}/modeling_prismatic.py'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    fetched = list(pool.map(fetch, sources + assets))

static_comparison = {}
try:
    static_comparison['repo_and_hf_modeling_ast_equal'] = (
        ast.dump(ast.parse(FETCHED_BLOBS['prismatic/extern/hf/modeling_prismatic.py'])) ==
        ast.dump(ast.parse(FETCHED_BLOBS['hf/modeling_prismatic.py']))
    )
    config = json.loads(FETCHED_BLOBS['config.json'])
    stats = json.loads(FETCHED_BLOBS['dataset_statistics.json'])
    static_comparison['config_norm_stats_equals_statistics_file'] = config.get('norm_stats') == stats
    tree = ast.parse(FETCHED_BLOBS['experiments/robot/openvla_utils.py'])
    get_vla = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'get_vla')
    calls = [n for n in ast.walk(get_vla) if isinstance(n, ast.Call) and
             isinstance(n.func, ast.Attribute) and n.func.attr == 'from_pretrained']
    static_comparison['get_vla_from_pretrained_keyword_names'] = [[k.arg for k in n.keywords] for n in calls]
    static_comparison['explicit_active_attn_implementation_keyword'] = any(
        k.arg == 'attn_implementation' for call in calls for k in call.keywords
    )
except Exception as exc:
    static_comparison['error'] = f'{type(exc).__name__}: {exc}'

mem = {}
for line in Path('/proc/meminfo').read_text().splitlines():
    key, value = line.split(':', 1)
    if key in ['MemTotal', 'MemAvailable', 'SwapTotal']:
        mem[key + '_KiB'] = int(value.strip().split()[0])

report = {
    'schema': 'd1-e1-resource-probe-v2',
    'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Docker infrastructure and static source/small JSON audit only; not native OFT qualification.',
    'container': {
        'platform': platform.platform(), 'machine': platform.machine(),
        'python': platform.python_version(), 'docker_marker': True,
        'proc_meminfo': mem,
        'probe_cgroup_memory_max': read_text('/sys/fs/cgroup/memory.max'),
        'probe_cgroup_swap_max': read_text('/sys/fs/cgroup/memory.swap.max'),
        'device_nodes': {p: glob.glob(p) for p in ['/dev/nvidia*', '/dev/dri/*', '/dev/kfd']},
        'nvidia_smi_path': shutil.which('nvidia-smi'),
        'nvidia_driver_version': read_text('/proc/driver/nvidia/version'),
    },
    'policy_source_commit': CODE_REV,
    'model': MODEL, 'model_revision': MODEL_REV,
    'public_reads': fetched,
    'static_comparison': static_comparison,
    'downloads': {'weight_payload_bytes': 0, 'dataset_payload_bytes': 0, 'pdf_bytes': 0,
                  'source_and_small_json_bytes': sum(r.get('bytes', 0) for r in fetched)},
    'upstream_code_imported': False, 'dependencies_installed': False,
    'policy_forwards': 0, 'simulator_steps': 0, 'policy_episodes': 0,
    'torch_cuda_is_available_tested': False,
    'limitations': [
        'No PyTorch imported; absence of GPU device nodes is an infrastructure observation.',
        'Remote LFS metadata hashes are advertised identities, not locally verified weight hashes.',
        'Full-file hashes identify text; matching lines do not imply full code review.',
        'Probe cgroup memory limit is intentional and differs from Docker VM total memory.',
    ],
}
print(json.dumps(report, indent=2))
