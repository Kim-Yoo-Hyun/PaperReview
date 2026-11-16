"""Supplementary fixed-horizon control; imports the immutable primary probe."""
import io
import json
from pathlib import Path
import signal
import time

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from scipy.fft import dct, idct

import probe as p


def main():
    assert Path('/.dockerenv').exists(), 'Docker only'
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('run budget exceeded')))
    signal.alarm(600)
    primary = json.loads((p.ROOT / 'results/verified/results.json').read_text())
    expected_assets = {a['url']: a['sha256'] for a in primary['assets']}
    started = time.time()
    report = {'id': 'GAP-CODEC1-SUFFIX', 'status': 'RUNNING', 'datasets': [],
              'primary_result_sha256': p.sha((p.ROOT / 'results/verified/results.json').read_bytes()),
              'contract_sha256': p.sha((p.ROOT / 'CONTRACT_SUFFIX.json').read_bytes()),
              'probe_sha256': p.sha(Path(__file__).read_bytes()), 'assets': p.ASSETS}
    try:
        codec, _ = p.load_codec()
        for ds, original in zip(p.CONTRACT['datasets'], primary['datasets']):
            assert ds['repo'] == original['repo']
            base = f"https://huggingface.co/datasets/{ds['repo']}/resolve/{ds['revision']}"
            tables = [pq.read_table(io.BytesIO(p.fetch(base + '/' + f)), columns=['action', 'episode_index', 'frame_index']) for f in ds['files']]
            table = pa.concat_tables(tables)
            acts = np.array(table['action'].to_pylist(), dtype=np.float64)
            ids = np.array(table['episode_index'].to_pylist())
            frames = np.array(table['frame_index'].to_pylist())
            low = np.array(original['normalizer']['q01']); high = np.array(original['normalizer']['q99'])
            h, e = ds['long_horizon'], ds['execution_prefix']
            rows = []
            for w in original['windows']:
                idx = np.flatnonzero(ids == w['episode']); idx = idx[np.argsort(frames[idx])]
                raw = acts[idx][w['frame']:w['frame'] + h]
                assert p.sha(raw.astype('<f8').tobytes()) == w['action_window_sha256']
                x = 2 * (raw - low) / (high - low) - 1
                held = x.copy(); held[e:] = x[e - 1]
                assert np.array_equal(x[:e], held[:e])
                y, _, _ = p.reconstruct(codec, x)
                z, _, _ = p.reconstruct(codec, held)
                no_q_x = idct(dct(x, axis=0, norm='ortho'), axis=0, norm='ortho')
                no_q_held = idct(dct(held, axis=0, norm='ortho'), axis=0, norm='ortho')
                no_q = p.mse(no_q_x[:e] - no_q_held[:e]) ** 0.5
                point = p.mse((np.round(x * 10) / 10)[:e] - (np.round(held * 10) / 10)[:e]) ** 0.5
                assert no_q < 1e-12 and point == 0
                rows.append({'episode': w['episode'], 'frame': w['frame'],
                             'fast_prefix_change_rms': p.mse(y[:e] - z[:e]) ** 0.5,
                             'no_quantization_change_rms': no_q, 'pointwise_change_rms': point,
                             'original_full_mse': p.mse(y - x), 'held_full_mse': p.mse(z - held),
                             'original_prefix_mse': p.mse(y[:e] - x[:e]), 'held_prefix_mse': p.mse(z[:e] - held[:e])})
            episodes = []
            for eid in p.CONTRACT['sampling']['diagnostic_episode_ids']:
                group = [r for r in rows if r['episode'] == eid]
                episodes.append({'episode': eid, 'prefix_change_rms': float(np.mean([r['fast_prefix_change_rms'] for r in group]))})
            report['datasets'].append({'repo': ds['repo'], 'summary': {
                'episodes': len(episodes), 'windows': len(rows),
                'equal_episode_mean_prefix_change_rms': float(np.mean([r['prefix_change_rms'] for r in episodes])),
                'max_unquantized_control': max(r['no_quantization_change_rms'] for r in rows),
                'max_pointwise_control': max(r['pointwise_change_rms'] for r in rows)},
                'episodes': episodes, 'windows': rows})
        assert all(expected_assets[a['url']] == a['sha256'] for a in p.ASSETS)
        report['status'] = 'PASSED_FIXED_HORIZON_SYNTHETIC_CONTROL'
        report['asset_parity_with_primary'] = True
    except Exception as exc:
        report['status'] = 'FAILED'; report['error'] = str(exc)
        raise
    finally:
        report['wall_seconds'] = time.time() - started
        report['downloaded_bytes'] = p.DOWNLOADED
        p.dump('results.json', report)
        print(json.dumps({'status': report['status'], 'datasets': [d['summary'] for d in report['datasets']]}))


if __name__ == '__main__':
    main()
