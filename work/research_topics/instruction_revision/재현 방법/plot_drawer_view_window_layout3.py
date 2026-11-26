"""Compare matched first contacts by physical opening across two LIBERO layouts."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def plot(folder, output):
    layouts = json.loads((folder / 'verification.json').read_bytes())['layouts']
    modes = ('narrow-middle', 'full-middle', 'narrow-bottom', 'full-bottom')
    labels = ('Middle · 76 mm', 'Middle · 160 mm', 'Bottom · 76 mm', 'Bottom · 160 mm')
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 6.5), sharex=True)
    fig.subplots_adjust(top=.81, left=.16, right=.96, bottom=.11, hspace=.24, wspace=.16)
    fig.suptitle('When does the opposite opening change the first gripper contact?', y=.98, fontsize=16)
    for i, (layout, values) in enumerate(sorted(layouts.items())):
        rows = [values['by_mode'][m] for m in modes]
        for j, ax in enumerate(axes[i]):
            for view, color, offset in [('early', '#18827b', -.15), ('late', '#c16a28', .15)]:
                if j == 0:
                    nums = [r['contact_changes']['self_to_' + view] for r in rows]
                    dens = [r['pairs'] for r in rows]
                else:
                    nums = [r['alignment'][view]['four'] for r in rows]
                    dens = [r['alignment']['eligible'] for r in rows]
                ys = np.arange(len(rows)) + offset
                fractions = [n/d if d else 0 for n, d in zip(nums, dens)]
                ax.barh(ys, fractions, height=.25, color=color, label=view)
                for y, x, n, d in zip(ys, fractions, nums, dens):
                    ax.text(x+.015, y, f'{n}/{d}' if d else '—', va='center', fontsize=8)
            ax.set(yticks=range(4), yticklabels=labels if j == 0 else [], xlim=(0, 1.20), ylim=(3.55, -.55))
            ax.set_xticks([0,.25,.5,.75,1], ['0','25','50','75','100%'])
            ax.spines[['top','right','left']].set_visible(False)
            ax.tick_params(axis='y', length=0)
            if not j:
                ax.set_ylabel('Layout ' + layout, labelpad=9, weight='bold')
    axes[0,0].set_title('First target changed from own-width view', fontsize=11)
    axes[0,1].set_title('First target matched the full-second exchange¹', fontsize=11)
    fig.legend(*axes[0,0].get_legend_handles_labels(), loc='upper center', bbox_to_anchor=(.5,.93), ncol=2, frameon=False)
    fig.text(.12,.025,'¹ Only pairs where the own-width and full-second views produced different first targets.', fontsize=9)
    fig.savefig(output, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder, args.output)
