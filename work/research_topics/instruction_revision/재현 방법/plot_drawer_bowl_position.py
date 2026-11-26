"""Plot matched first-contact changes under a reciprocal bowl-position swap."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def plot(folder, output):
    layouts = json.loads((folder/'verification.json').read_bytes())['layouts']
    data = [layouts[i]['late'] for i in ('2','3')]
    fig, (bars, table) = plt.subplots(1, 2, figsize=(10.8, 3.8), gridspec_kw={'width_ratios':[1,1.15]})
    fig.subplots_adjust(left=.11, right=.98, top=.70, bottom=.24, wspace=.34)
    fig.suptitle('Does the first-contact effect follow the bowl position?', fontsize=16, y=.97)
    for i,(key,label,color) in enumerate([('native_changed','Original position','#216b70'),
                                          ('crossed_changed','Other layout’s position','#ba6030')]):
        for y,row in enumerate(data):
            count, n = row[key], row['pairs']
            pos = y + (i-.5)*.31
            bars.barh(pos,count,height=.25,color=color,label=label if y == 0 else None)
            bars.text(count+.45,pos,f'{count}/{n}',va='center',fontsize=9)
    bars.set(yticks=[0,1],yticklabels=['Layout 2','Layout 3'],xlim=(0,39),ylim=(1.5,-.5),
             xticks=[0,8,16,24,32],xlabel='Matched cases')
    bars.set_title('First target changed from own-width control', fontsize=10)
    bars.spines[['left','top','right']].set_visible(False)
    bars.tick_params(axis='y',length=0)
    bars.legend(loc='upper left',bbox_to_anchor=(0,-.26),ncol=2,fontsize=8,frameon=False)
    fields = ('native_only','crossed_only','both','neither')
    values = np.array([[row[f] for f in fields] for row in data])
    table.imshow(values,cmap='Blues',vmin=0,vmax=max(r['pairs'] for r in data),aspect='auto')
    table.set(xticks=range(4),xticklabels=['Original\nonly','Other\nonly','Both','Neither'],
              yticks=[0,1],yticklabels=['Layout 2','Layout 3'])
    for (i,j),n in np.ndenumerate(values):
        table.text(j,i,str(n),va='center',ha='center',weight='bold',color='white' if n>=18 else '#1a283d')
    table.set_title('Where the late exchange changed first contact',fontsize=10)
    fig.text(.5,.855,'Both cameras show 76 mm from 0.5 to 1.0 s while the bottom drawer is open ≈160 mm.',
             ha='center',fontsize=10)
    fig.savefig(output,dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder,args.output)
