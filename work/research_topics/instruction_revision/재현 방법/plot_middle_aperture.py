"""Plot actual policy images, native placement over time and the fixed-command crossover."""
import argparse
from contextlib import nullcontext
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
from PIL import Image


def plot(folder, proof, output):
    colors = {'open':'#98522b', 'closed':'#12667d'}
    modes = list(colors)
    fig = plt.figure(figsize=(13.0,6.2),layout='constrained')
    grid = fig.add_gridspec(2,4,width_ratios=(1,1,2.3,1.55),wspace=.11)
    matrix = json.loads(proof.read_bytes())['crossover']['all']
    bundle = folder/'study.zip'
    with (ZipFile(bundle) if bundle.exists() else nullcontext()) as archive:
        def data(name):
            return archive.read(name) if archive else (folder/name).read_bytes()

        def read(name):
            return json.loads(data(name))

        base = read('sources/drawer/stove_layouts.json')
        task = read('sources/drawer/upper_bowl.json')
        design = read('design.json')
        entries = list(read('sessions.json').values())
        curves = {mode:[] for mode in modes}
        prep = {}
        for e in entries:
            arm,mode,lead = e['arm'],e['mode'],e['lead']
            if (arm,mode) not in prep:
                prep[arm,mode] = read(f'preparation/{arm}-{mode}-{lead}.json')['handoff']['upper']
            tape = read('paths/'+e['session']+'.json')
            rows = [prep[arm,mode],*tape['rows']]
            curves[mode].append([[r[k] for r in rows] for k in ('bowl_in','middle_in')])
            if arm==entries[0]['arm'] and e['key']==0 and e['block']==1:
                row = modes.index(mode)
                for col,(key,label) in enumerate([('observation/image','External camera'),('observation/wrist_image','Wrist camera')]):
                    ax = fig.add_subplot(grid[row,col])
                    with Image.open(BytesIO(data('frames/'+tape['queries'][0]['live'][key]+'.png'))) as img:
                        ax.imshow(np.asarray(img))
                    ax.set_xticks([])
                    ax.set_yticks([])
                    for spine in ax.spines.values():
                        spine.set_visible(False)
                    if row==0:
                        ax.set_title(label,fontsize=12)
                    if col==0:
                        ax.set_ylabel('Middle '+mode,fontsize=12,weight='bold',color=colors[mode])
        direct_curves = []
        if 'standalone' in design:
            direct_start = read('standalone/preparation/neutral-immediate-0.json')['handoff']['upper']
            for entry in read('standalone/sessions.json').values():
                tape = read('standalone/paths/'+entry['session']+'.json')
                rows = [direct_start,*tape['rows']]
                direct_curves.append([[r[k] for r in rows] for k in ('bowl_in','middle_in')])
    seconds = np.arange(base['lead'],task['extension']+1)/base['control_hz']
    for row,(region,title) in enumerate([('top','Upper drawer'),('middle','Middle drawer')]):
        axis = fig.add_subplot(grid[row,2])
        if direct_curves:
            times = np.arange(task['extension']+1)/base['control_hz']
            axis.step(times,np.mean(direct_curves,axis=0)[row],where='post',color='#626674',ls='--',lw=1.7,label='Standalone')
        for mode in modes:
            line = np.mean(curves[mode],axis=0)[row]
            axis.step(seconds,line,where='post',color=colors[mode],lw=2.2,label='Middle '+mode)
        axis.axvline(task['primary']/base['control_hz'],ls=':',lw=1,color='#565c61')
        axis.set(title=title+' placement over time',xlim=(3,30),ylim=(-.035,1.055),
                 xticks=[3,8,15,20,25,30],yticks=[0,.25,.5,.75,1])
        if direct_curves:
            axis.set(xlim=(0,30),xticks=[0,3,8,15,20,25,30])
        axis.yaxis.set_major_formatter(PercentFormatter(1,decimals=0))
        axis.grid(axis='y',color='#d6d8da',lw=.7)
        axis.spines[['top','right']].set_visible(False)
        if row==0:
            axis.legend(frameon=False,loc='center right',fontsize=9)
        else:
            axis.set_xlabel('Time from trial start (s)' if direct_curves else 'Time including 3 s posture return (s)')

        counts = [matrix[str(task['extension'])][src] for src in modes]
        totals = np.array([[cell[m]['paths'] for m in modes] for cell in counts])
        values = np.array([[cell[m]['counts'][region+'_in'] for m in modes] for cell in counts])
        heat = fig.add_subplot(grid[row,3])
        heat.imshow(values/totals,vmin=0,vmax=1,cmap='Blues',aspect='auto')
        heat.set_title(title+' at 30 s',fontsize=12)
        heat.set_xticks([0,1],['Open','Closed'])
        heat.set_yticks([0,1],['Open','Closed'])
        heat.set_ylabel('Commands from')
        if row==1:
            heat.set_xlabel('Physical middle drawer')
        for i,j in np.ndindex(values.shape):
            heat.text(j,i,f'{values[i,j]}/{totals[i,j]}',ha='center',va='center',fontsize=14,weight='bold',
                      color='white' if values[i,j]/totals[i,j]>.55 else '#193044')
    fig.suptitle(f"Middle-drawer aperture and bowl placement on LIBERO-Goal layout {design.get('layout',3)}",fontsize=16,weight='bold')
    fig.savefig(output,dpi=155,facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--replay',type=Path)
    args = parser.parse_args()
    plot(args.folder,args.replay or args.folder/'physical_replay.json',args.output)
