"""Display native camera inputs, bowl destinations and the upper-goal command crossover."""
import argparse
from contextlib import nullcontext
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def counts_panel(ax, counts, totals, xlabels, ylabels, title, xlabel, ylabel):
    for i,row in enumerate(counts):
        for j,value in enumerate(row):
            n = totals[i][j]
            ax.text(j,i,f'{value}/{n}',ha='center',va='center',weight='bold',fontsize=11,
                    color='white' if value/n>.52 else '#172f45')
    ax.imshow(np.asarray(counts)/np.asarray(totals),cmap='Blues',vmin=0,vmax=1,aspect='auto')
    ax.set(title=title,xticks=range(len(xlabels)),xticklabels=xlabels,yticks=range(len(ylabels)),yticklabels=ylabels,
           xlabel=xlabel,ylabel=ylabel)


def plot(folder, proof_file, output):
    result = json.loads((folder/'verification.json').read_bytes())
    cross = json.loads(proof_file.read_bytes())['crossover']
    bundle = folder/'study.zip'
    fig = plt.figure(figsize=(12.6,8.4),layout='constrained')
    sections = fig.subfigures(2,1,hspace=.06)
    with (ZipFile(bundle) if bundle.is_file() else nullcontext()) as store:
        def data(name):
            return store.read(name) if store else (folder/name).read_bytes()
        def read(name):
            return json.loads(data(name))
        entries = list(read('sessions.json').values())
        modes = read('design.json')['modes']
        labels = ['Closed','Middle','Bottom']
        for section,arr in zip(sections,('partial','full')):
            width = result['clearance'][arr]['width_m']
            if width is None:
                width = result['physical_starts'][arr][entries[0]['arm']]['opening_m']
            caption = 'Original tabletop positions' if arr=='partial' else 'Clearance-adjusted tabletop positions'
            section.suptitle(f'{caption}    •    {width*1000:.0f} mm drawer travel',fontsize=13,weight='bold')
            grid = section.add_gridspec(2,5,width_ratios=(.85,.85,.85,2.55,2.15),wspace=.08)
            counts, totals = [],[]
            for col,m in enumerate(modes):
                subset = [e for e in entries if e['mode']==arr+'-'+m]
                e = next(e for e in subset if e['arm']==entries[0]['arm'] and e['block']==1 and e['key']==0)
                images = read('paths/'+e['session']+'.json')['queries'][0]['live']
                for row,(cam,view) in enumerate([('observation/image','External'),('observation/wrist_image','Wrist')]):
                    ax = section.add_subplot(grid[row,col])
                    with Image.open(BytesIO(data('frames/'+images[cam]+'.png'))) as img:
                        ax.imshow(np.asarray(img))
                    ax.set(xticks=[],yticks=[])
                    ax.spines[:].set_visible(False)
                    if row==0:
                        ax.set_title(labels[col],fontsize=10)
                    if col==0:
                        ax.set_ylabel(view)
                values = [result['outcomes'][e['session']]['600'] for e in subset]
                flags = [[v[l+'_in'] for l in ('top','middle','bottom')] for v in values]
                assert all(sum(row)<=1 for row in flags)
                counts.append([sum(s) for s in zip(*flags)]+[sum(not any(s) for s in flags)])
                totals.append([len(subset)]*4)
            counts_panel(section.add_subplot(grid[:,3]),counts,totals,['Upper','Middle','Bottom','None'],labels,
                         'Native placement at 30 s','Bowl destination','Pulled drawer')
            cell = cross[arr]['all']['600']
            counts = [[cell[s][m]['counts']['top_in'] for m in modes] for s in modes]
            totals = [[cell[s][m]['paths'] for m in modes] for s in modes]
            counts_panel(section.add_subplot(grid[:,4]),counts,totals,labels,labels,'Upper goal at 30 s',
                         'Physical drawer condition','Commands from')
    fig.suptitle('LIBERO-Goal    |    Open the top drawer and put the bowl inside',fontsize=16,weight='bold')
    fig.savefig(output,dpi=155,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--replay',type=Path)
    args=parser.parse_args()
    plot(args.folder,args.replay or args.folder/'physical_replay.json',args.output)
