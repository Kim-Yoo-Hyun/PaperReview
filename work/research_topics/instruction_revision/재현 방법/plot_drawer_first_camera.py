"""Plot measured action, contact and placement under a one-query camera exchange."""
import argparse
import json
from pathlib import Path

import numpy as np

from plot_drawer_location import counts_panel, plt


def plot(folder, output):
    result = json.loads((folder / 'verification.json').read_bytes())
    groups = result['comparisons']['all']
    modes = ('narrow-middle', 'full-middle', 'narrow-bottom', 'full-bottom')
    views = ('self', 'external', 'wrist', 'both')
    rows = ['Middle 76 mm', 'Middle ~160 mm', 'Bottom 76 mm', 'Bottom ~160 mm']
    cols = ['Self', 'External', 'Wrist', 'Both']
    cells = [[groups[m][v] for v in views] for m in modes]
    totals = [[s['paths'] for s in row] for row in cells]
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.5), layout='constrained')
    ax = axes[0, 0]
    magnitude = np.array([[s['first_action_delta_self']['median'] for s in row] for row in cells])
    ceiling = max(magnitude.max(), 1e-9)
    ax.imshow(magnitude, cmap='Purples', vmin=0, vmax=ceiling, aspect='auto')
    for i, row in enumerate(magnitude):
        for j, value in enumerate(row):
            ax.text(j, i, f'{value:.3f}', ha='center', va='center', weight='bold',
                    color='white' if value > 0.55 * ceiling else '#261d36')
    ax.set(title='First command change from self (median max |Δ|)',
           xticks=range(len(cols)), xticklabels=cols, yticks=range(len(rows)), yticklabels=rows)
    first = [[s['first_contact'].get('bowl', 0) for s in row] for row in cells]
    counts_panel(axes[0, 1], first, totals, cols, rows, 'Gripper touched bowl before a drawer', '', '')
    # Show upper-goal placement at 76 mm and placement in the pulled drawer at full width.
    destinations = ('top', 'middle', 'top', 'bottom')
    labels = [f"{label} → {'upper' if dest == 'top' else dest}" for label, dest in zip(rows, destinations)]
    for ax, tick, time in ((axes[1, 0], '300', 15), (axes[1, 1], '600', 30)):
        counts = [[s['destinations'][tick].get(dest, 0) for s in row] for row, dest in zip(cells, destinations)]
        counts_panel(ax, counts, totals, cols, labels, f'Bowl in indicated drawer at {time} s',
                     'First camera input exchanged', '')
    fig.suptitle('LIBERO-Goal   |   Same physical opening within each row', fontsize=15)
    fig.savefig(output, dpi=155, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder, args.output)
