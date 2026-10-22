"""Resume pinned weight downloads with verified HTTP ranges, inside Docker only."""
import concurrent.futures
import hashlib
import json
import os
import time
import urllib.request
from pathlib import Path
from fetch_assets import ROOT, MODEL, REV

info = json.load(urllib.request.urlopen(f'https://huggingface.co/api/models/{MODEL}/revision/{REV}?blobs=true'))
entries = [x for x in info['siblings'] if x['rfilename'].endswith('.safetensors')]
jobs = []
fds = {}
started = time.monotonic()
marker=ROOT/'range_download_in_progress.json'
assert not marker.exists(), 'A prior ranged run was interrupted: sparse file size is NOT a valid downloaded prefix. Recover verified ranges explicitly.'
for entry in entries:
    name = entry['rfilename']
    path = ROOT/'model'/name
    if path.exists():
        continue
    partial = path.with_suffix(path.suffix+'.partial')
    offset = partial.stat().st_size if partial.exists() else 0
    size = entry['lfs']['size']
    fds[name] = os.open(partial, os.O_WRONLY|os.O_CREAT, 0o600)
    for start in range(offset, size, 16*1024*1024):
        jobs.append((name, start, min(start+16*1024*1024, size)-1, size))
print(json.dumps({'remaining_bytes':sum(b-a+1 for _,a,b,_ in jobs),'ranges':len(jobs)}),flush=True)
marker.write_text(json.dumps({'prefixes_only':True,'planned_ranges':jobs}))

def get_range(job):
    name, start, end, size = job
    for attempt in range(5):
        try:
            # Distinct query avoids an intermediary reusing a differently ranged response.
            url = f'https://huggingface.co/{MODEL}/resolve/{REV}/{name}?range_start={start}'
            req = urllib.request.Request(url, headers={'Range':f'bytes={start}-{end}'})
            with urllib.request.urlopen(req, timeout=120) as response:
                assert response.status == 206
                assert response.headers['Content-Range'] == f'bytes {start}-{end}/{size}'
                data = response.read()
                assert len(data) == end-start+1
            assert os.pwrite(fds[name],data,start) == len(data)
            return len(data)
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1+attempt)

done=0
with concurrent.futures.ThreadPoolExecutor(max_workers=24) as pool:
    for i, size in enumerate(pool.map(get_range,jobs)):
        done+=size
        if i%12==0:
            print(json.dumps({'downloaded_new_bytes':done,'seconds':time.monotonic()-started}),flush=True)
for fd in fds.values():
    os.close(fd)
receipts=[]
for entry in entries:
    path=ROOT/'model'/entry['rfilename']
    target=path if path.exists() else path.with_suffix(path.suffix+'.partial')
    h=hashlib.sha256()
    with target.open('rb') as source:
        while data:=source.read(8*1024*1024):
            h.update(data)
    assert target.stat().st_size==entry['lfs']['size']
    assert h.hexdigest()==entry['lfs']['sha256']
    if target!=path:
        target.rename(path)
    receipts.append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,
                     'sha256':h.hexdigest(),'revision':REV})
(ROOT/'weight_receipts.json').write_text(json.dumps(receipts,indent=2))
marker.unlink()
print('ALL ORIGINAL WEIGHT SHAS VERIFIED',flush=True)
