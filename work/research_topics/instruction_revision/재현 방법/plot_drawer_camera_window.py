"""Plot exact single-camera matches and all paired first-contact changes."""
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def plot(folder,output):
    report=json.loads((folder/'verification.json').read_bytes())
    data=[report['groups'][f'{i}/{pos}-bottom'] for i in (2,3) for pos in ('native','crossed')]
    labels=['2 · original','2 · moved','3 · original','3 · moved']
    fig,(left,right)=plt.subplots(1,2,figsize=(11,4.1),gridspec_kw={'width_ratios':[1.15,1]})
    fig.subplots_adjust(top=.73,bottom=.23,left=.14,right=.97,wspace=.38)
    fig.suptitle('Which camera reproduces the change in first contact?',fontsize=16,y=.97)
    fig.text(.5,.86,'The bottom drawer stays open ≈160 mm. Assigned views show 76 mm from 0.5 to 1.0 s.',
             ha='center',fontsize=10)
    cats=[('external_only','External only','#176a70'),('wrist_only','Wrist only','#cc7941'),
          ('both_match','Either alone','#79aaa0'),('neither_match','Neither alone','#546275')]
    for y,row in enumerate(data):
        start=0
        for key,title,color in cats:
            n=row['primary'][key]
            left.barh(y,n,left=start,color=color,height=.55,label=title if y==0 else None)
            if n:
                left.text(start+n/2,y,str(n),color='white' if key!='both_match' else 'black',va='center',ha='center',fontsize=9)
            start+=n
        left.text(start+.6,y,f'{start} eligible',fontsize=8,va='center')
    left.set(yticks=range(4),yticklabels=labels,xlim=(0,41),ylim=(3.6,-.6),xticks=[0,8,16,24,32],
             xlabel='Cases with a different target in both-view vs own-width control')
    left.set_title('Exact match to the both-view target',fontsize=11)
    left.legend(loc='upper center',bbox_to_anchor=(.44,-.31),ncol=2,fontsize=8,frameon=False)
    x=np.arange(len(labels))
    for j,(v,legend,color,marker) in enumerate([('external','External','#176a70','o'),('wrist','Wrist','#cc7941','s'),('both','Both views','#263c55','D')]):
        xs=[r['changed_from_self'][v]['contact'] for r in data]
        right.scatter(xs,x+(j-1)*.2,marker=marker,s=42,color=color,label=legend)
    right.set(yticks=range(4),yticklabels=labels,xlim=(-1.2,33.2),ylim=(3.6,-.6),xticks=[0,8,16,24,32],
              xlabel='Cases changed from own-width control (out of 32)')
    right.set_title('All starts, including control agreement',fontsize=11)
    right.legend(loc='upper center',bbox_to_anchor=(.5,-.31),ncol=3,fontsize=8,frameon=False)
    for axis in (left,right):
        axis.spines[['top','right','left']].set_visible(False)
        axis.tick_params(axis='y',length=0)
    fig.savefig(output,dpi=170,bbox_inches='tight',facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    plot(Path(sys.argv[1]),Path(sys.argv[2]))
