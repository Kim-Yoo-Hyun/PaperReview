"""Bounded expert-action codec diagnostic. Run only inside local Docker."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import platform
import signal
import time
import urllib.request

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from scipy.fft import dct, idct
from transformers import PreTrainedTokenizerFast


ROOT = Path('/app')
OUT = Path('/output')
CONTRACT = json.loads((ROOT / 'CONTRACT.json').read_text())
ASSETS = []
DOWNLOADED = 0


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(url):
    global DOWNLOADED
    remaining = CONTRACT['budget']['payload_limit_bytes'] - DOWNLOADED
    with urllib.request.urlopen(url, timeout=45) as r:
        data = r.read(remaining + 1)
    if len(data) > remaining:
        raise RuntimeError('payload budget exceeded')
    DOWNLOADED += len(data)
    ASSETS.append({'url': url, 'bytes': len(data), 'sha256': sha(data)})
    return data


def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False) + '\n')


def load_codec():
    cfg = CONTRACT['fast']
    folder = Path('/tmp/fast')
    folder.mkdir()
    for name in cfg['files']:
        (folder / name).write_bytes(fetch(f"https://huggingface.co/{cfg['repo']}/resolve/{cfg['revision']}/{name}"))
    spec = importlib.util.spec_from_file_location('reviewed_fast', folder / 'processing_action_tokenizer.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    metadata = json.loads((folder / 'processor_config.json').read_text())
    tokenizer = PreTrainedTokenizerFast.from_pretrained(str(folder), local_files_only=True)
    codec = mod.UniversalActionProcessor(tokenizer, scale=cfg['scale'], min_token=metadata['min_token'], vocab_size=metadata['vocab_size'])
    return codec, metadata


def reconstruct(codec, x):
    coeff = np.around(dct(x, axis=0, norm='ortho') * codec.scale)
    if np.any(coeff < codec.min_token):
        raise ValueError('official coefficient floor would clip')
    tokens = codec(x)[0]
    y = codec.decode([tokens], time_horizon=len(x), action_dim=x.shape[1])[0]
    expected = idct(coeff / codec.scale, axis=0, norm='ortho')
    parity = float(np.max(np.abs(expected - y)))
    if y.shape != x.shape or not np.all(np.isfinite(y)) or parity > 1e-10:
        raise ValueError(f'official decode / independent DCT parity failed: {parity}')
    # Also catches silent all-zero fallback on a nonzero encoded chunk.
    return y, len(tokens), parity


def mse(x):
    return float(np.mean(np.square(x)))


def disagreement(a, b):
    return bool(abs(a) > 1e-12 and abs(b) > 1e-12 and a * b < 0)


def summarize(records):
    keys = ['full_short_mse', 'full_long_mse', 'prefix_short_mse', 'prefix_long_mse',
            'prefix_delta_rms', 'pointwise_prefix_mse', 'tokens_short', 'tokens_long',
            'pointwise_prefix_delta_rms', 'identity_mse']
    out = {k: float(np.mean([r[k] for r in records])) for k in keys}
    out['windows'] = len(records)
    out['window_preference_disagreements'] = sum(r['preference_disagreement'] for r in records)
    out['mean_preference_disagreement'] = disagreement(out['full_long_mse'] - out['full_short_mse'], out['prefix_long_mse'] - out['prefix_short_mse'])
    out['prefix_delta_rms_max'] = max(r['prefix_delta_rms'] for r in records)
    out['prefix_delta_rms_gt_001'] = sum(r['prefix_delta_rms'] > 0.01 for r in records)
    return out


def study(ds, codec):
    base = f"https://huggingface.co/datasets/{ds['repo']}/resolve/{ds['revision']}"
    info = json.loads(fetch(base + '/meta/info.json'))
    assert info['fps'] == ds['fps']
    assert info['features']['action']['shape'] == [ds['action_dim']]
    tables = [pq.read_table(io.BytesIO(fetch(base + '/' + f)), columns=['action', 'episode_index', 'frame_index']) for f in ds['files']]
    table = pa.concat_tables(tables)
    episode_ids = np.array(table['episode_index'].to_pylist())
    frames = np.array(table['frame_index'].to_pylist())
    actions = np.array(table['action'].to_pylist(), dtype=np.float64)
    if not np.all(np.isfinite(actions)):
        raise ValueError('nonfinite actions')
    selected = CONTRACT['sampling']['normalizer_episode_ids'] + CONTRACT['sampling']['diagnostic_episode_ids']
    episodes = {}
    for eid in selected:
        indices = np.flatnonzero(episode_ids == eid)
        indices = indices[np.argsort(frames[indices])]
        assert len(indices) and np.array_equal(frames[indices], np.arange(len(indices))), f'noncontiguous episode {eid}'
        episodes[eid] = actions[indices]
    calibration = np.concatenate([episodes[eid] for eid in CONTRACT['sampling']['normalizer_episode_ids']])
    low, high = np.quantile(calibration, [0.01, 0.99], axis=0)
    width = high - low
    if np.any(width <= 1e-12):
        raise ValueError('degenerate normalizer dimension')
    normalizer = {'q01': low.tolist(), 'q99': high.tolist(), 'fit_episodes': CONTRACT['sampling']['normalizer_episode_ids'], 'clip': False}
    h1, h2, e = ds['short_horizon'], ds['long_horizon'], ds['execution_prefix']
    records, by_episode = [], []
    max_parity, out_of_range, values = 0.0, 0, 0
    for eid in CONTRACT['sampling']['diagnostic_episode_ids']:
        raw = episodes[eid]
        normalized = 2 * (raw - low) / width - 1
        out_of_range += int(np.count_nonzero(np.abs(normalized) > 1))
        values += normalized.size
        local = []
        for start in list(range(0, len(raw) - h2 + 1, h2))[:8]:
            long = normalized[start:start + h2]
            short = long[:h1]
            y1, t1, p1 = reconstruct(codec, short)
            y2, t2, p2 = reconstruct(codec, long)
            max_parity = max(max_parity, p1, p2)
            q1, q2 = np.round(short * 10) / 10, np.round(long * 10) / 10
            identity_error = mse(long.copy() - long)
            pointwise_delta = mse(q1[:e] - q2[:e]) ** 0.5
            assert identity_error == 0 and pointwise_delta == 0
            err1, err2 = y1 - short, y2 - long
            row = {'episode': eid, 'frame': start, 'full_short_mse': mse(err1), 'full_long_mse': mse(err2),
                   'prefix_short_mse': mse(err1[:e]), 'prefix_long_mse': mse(err2[:e]),
                   'prefix_delta_rms': mse(y1[:e] - y2[:e]) ** 0.5,
                   'pointwise_prefix_mse': mse(q1[:e] - short[:e]), 'pointwise_prefix_delta_rms': pointwise_delta,
                   'identity_mse': identity_error, 'tokens_short': t1, 'tokens_long': t2,
                   'nominal_bits_short': float(t1 * np.log2(codec.vocab_size)),
                   'nominal_bits_long': float(t2 * np.log2(codec.vocab_size)),
                   'prefix_raw_mae_short': np.mean(np.abs(err1[:e]) * width / 2, axis=0).tolist(),
                   'prefix_raw_mae_long': np.mean(np.abs(err2[:e]) * width / 2, axis=0).tolist(),
                   'prefix_dimension_mse_short': np.mean(err1[:e] ** 2, axis=0).tolist(),
                   'prefix_dimension_mse_long': np.mean(err2[:e] ** 2, axis=0).tolist(),
                   'action_window_sha256': sha(raw[start:start + h2].astype('<f8').tobytes())}
            row['preference_disagreement'] = disagreement(row['full_long_mse'] - row['full_short_mse'], row['prefix_long_mse'] - row['prefix_short_mse'])
            records.append(row)
            local.append(row)
        if not local:
            raise ValueError(f'episode {eid} has no complete long window')
        by_episode.append({'episode': eid, **summarize(local)})
    avg_keys = ['full_short_mse', 'full_long_mse', 'prefix_short_mse', 'prefix_long_mse', 'prefix_delta_rms', 'tokens_short', 'tokens_long']
    equal_episode = {k: float(np.mean([r[k] for r in by_episode])) for k in avg_keys}
    equal_episode.update({'episode_count': len(by_episode), 'window_count': len(records),
                          'episodes_with_preference_disagreement': sum(r['mean_preference_disagreement'] for r in by_episode),
                          'windows_with_preference_disagreement': sum(r['preference_disagreement'] for r in records),
                          'max_official_dct_parity_error': max_parity, 'normalized_out_of_range_fraction': out_of_range / values,
                          'coefficient_floor_clips': 0, 'decode_failures': 0,
                          'prefix_delta_rms_gt_001_windows': sum(r['prefix_delta_rms'] > 0.01 for r in records)})
    return {'repo': ds['repo'], 'revision': ds['revision'], 'source_info': info,
            'episode_lengths': {str(eid): len(episodes[eid]) for eid in selected},
            'normalizer': normalizer, 'summary': equal_episode, 'episodes': by_episode, 'windows': records}


def main():
    if not Path('/.dockerenv').exists():
        raise SystemExit('Docker-only probe')
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('run budget exceeded')))
    signal.alarm(CONTRACT['budget']['run_timeout_seconds'])
    OUT.mkdir(exist_ok=True)
    started = time.time()
    result = {'id': CONTRACT['id'], 'status': 'RUNNING', 'contract_sha256': sha((ROOT / 'CONTRACT.json').read_bytes()),
              'probe_sha256': sha(Path(__file__).read_bytes()), 'python': platform.python_version(), 'machine': platform.machine(),
              'libraries': Path('/python-packages.txt').read_text(), 'datasets': [], 'assets': ASSETS}
    try:
        codec, metadata = load_codec()
        result['processor_config'] = metadata
        for ds in CONTRACT['datasets']:
            print('Auditing ' + ds['repo'], flush=True)
            result['datasets'].append(study(ds, codec))
        result['status'] = 'PASSED_OFFLINE_CODEC_DIAGNOSTIC'
    except Exception as exc:
        result['status'] = 'FAILED'
        result['error'] = type(exc).__name__ + ': ' + str(exc)
        raise
    finally:
        result['downloaded_bytes'] = DOWNLOADED
        result['wall_seconds'] = time.time() - started
        dump('results.json', result)
        print(json.dumps({'status': result['status'], 'datasets': [d['summary'] for d in result['datasets']]}), flush=True)


if __name__ == '__main__':
    main()
