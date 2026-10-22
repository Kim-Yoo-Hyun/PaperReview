"""C6 read-only provenance/structure audit; run only inside Docker.

No upstream execution, model inference, synthetic rollouts, or metric comparison.
Raw response bytes stay under /tmp/c6_sources in the container.
"""
import argparse
from collections import Counter
import datetime
import hashlib
import json
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path('/tmp/c6_sources')
CAP = 8 * 1024 * 1024


def fetch(url, destination):
    request = urllib.request.Request(url, headers={'User-Agent': 'C6-literature-audit'})
    with urllib.request.urlopen(request, timeout=40) as response:
        data = response.read(CAP + 1)
        headers = {k: response.headers.get(k) for k in ('ETag', 'Last-Modified')}
    if len(data) > CAP:
        raise ValueError('Bounded audit cap exceeded')
    path = ROOT / destination
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data, {'url': url, 'bytes': len(data),
                  'sha256': hashlib.sha256(data).hexdigest(),
                  'container_path': str(path), 'headers': headers}


def json_fetch(url, destination):
    data, meta = fetch(url, destination)
    return json.loads(data), meta


def structure(value, path='$', depth=0):
    """Record shape and all dictionary key names, not inferred trial counts."""
    rows = []
    if isinstance(value, dict):
        rows.append({'path': path, 'type': 'object', 'keys': list(value)})
        for key, child in value.items():
            if isinstance(child, (list, dict)):
                rows.extend(structure(child, path + '.' + key, depth + 1))
    elif isinstance(value, list):
        rows.append({'path': path, 'type': 'array', 'length': len(value),
                     'element_types': sorted({type(v).__name__ for v in value})})
        # All nested records are traversed so schema checks are not a sample.
        for index, child in enumerate(value):
            if isinstance(child, (list, dict)):
                rows.extend(structure(child, path + '[' + str(index) + ']', depth + 1))
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', required=True)
    args = parser.parse_args()
    specs = json.loads(pathlib.Path(args.sources).read_text())
    result = {'audited_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'upstream_code_executed': False, 'repositories': [], 'data': {}, 'errors': []}
    for repo, spec in specs.items():
        item = {'repository': repo, 'files': []}
        try:
            base = 'https://api.github.com/repos/' + repo
            sha = spec.get('commit')
            if not sha:
                head, _ = json_fetch(base + '/commits/HEAD', repo + '/head.json')
                sha = head['sha']
            tree, tree_meta = json_fetch(base + '/git/trees/' + sha + '?recursive=1', repo + '/tree.json')
            if tree.get('truncated'):
                raise ValueError('Truncated inventory')
            item.update(commit=sha, tree_metadata=tree_meta, tree_truncated=False,
                        blob_paths=[x['path'] for x in tree['tree'] if x['type'] == 'blob'])
            for path in spec['files']:
                data, meta = fetch('https://raw.githubusercontent.com/' + repo + '/' + sha + '/' + path,
                                   repo + '/' + path)
                meta.update(path=path, lines=len(data.splitlines()))
                item['files'].append(meta)
            item['status'] = 'source_inspected'
        except urllib.error.HTTPError as exc:
            item.update(status='http_unavailable', http_status=exc.code, url=exc.url)
        except Exception as exc:
            item.update(status='audit_error', error=str(exc))
            result['errors'].append({'repository': repo, 'error': str(exc)})
        result['repositories'].append(item)
    try:
        payload, meta = json_fetch('https://changyeon.site/race/data.json', 'race/data.json')
        summaries = {}
        for family, bundle in payload['real'].items():
            rows = bundle['raw']
            checkpoint_field = {'vla': 'step', 'dp': 'epoch'}[family]
            identities = [(row['task'], row[checkpoint_field]) for row in rows]
            summaries[family] = {
                'checkpoint_field': checkpoint_field,
                'checkpoint_measurement_rows': len(rows),
                'rows_per_task': dict(Counter(row['task'] for row in rows)),
                'duplicate_task_step_identities': len(identities) - len(set(identities)),
                'row_key_sets': sorted({tuple(sorted(row)) for row in rows}),
                'all_row_values_scalar': all(not isinstance(v, (list, dict))
                                             for row in rows for v in row.values()),
                'success_rate_range_as_stored': [min(r['success_rate'] for r in rows),
                                                 max(r['success_rate'] for r in rows)],
                'rows_with_aggregate_successes_and_trials': sum('successes' in r and 'trials' in r for r in rows)}
        result['data'] = {'metadata': meta, 'structure': structure(payload),
                          'real_measurement_summary': summaries,
                          'total_checkpoint_measurement_rows': sum(v['checkpoint_measurement_rows']
                                                                  for v in summaries.values()),
                          'sequential_selection_experiment_performed': False}
    except Exception as exc:
        result['errors'].append({'data': 'RACE', 'error': str(exc)})
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(result['errors'])


if __name__ == '__main__':
    raise SystemExit(main())
