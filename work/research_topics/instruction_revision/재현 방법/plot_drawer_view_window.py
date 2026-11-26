"""Plot paired behavior when the same 0.50 s camera exchange starts earlier or later."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def counts(ax, values, totals, columns, rows, title, cmap):
    n, d = np.asarray(values), np.asarray(totals)[:, None]
    fraction = np.divide(n, d, out=np.zeros_like(n, dtype=float), where=d > 0)
    ax.imshow(fraction, aspect='auto', vmin=0, vmax=1, cmap=cmap)
    for i, row in enumerate(n):
        for j, v in enumerate(row):
            ax.text(j, i, f'{v}/{d[i, 0]}' if d[i, 0] else '—', ha='center', va='center',
                    color='white' if fraction[i,j] >= .55 else '#152d35', weight='semibold')
    ax.set(title=title, xticks=range(len(columns)), xticklabels=columns, yticks=range(len(rows)), yticklabels=rows)


def plot(folder, output):
    result = json.loads((folder / 'verification.json').read_bytes())
    groups = result['comparisons']['all']
    modes = ('narrow-middle', 'full-middle', 'narrow-bottom', 'full-bottom')
    rows = ('Middle 76 mm', 'Middle 160 mm', 'Bottom 76 mm', 'Bottom 160 mm')
    halves = ('early', 'late')
    pairs = [groups[m]['early_to_late'] for m in modes]
    totals = [g['pairs'] for g in pairs]
    alignment = [groups[m]['alignment'] for m in modes]
    fig, axes = plt.subplots(2, 2, figsize=(12.2, 7.4), layout='constrained')
    counts(axes[0,0], [[g[k]['changed'] for k in ('contact','at15','at30')] for g in pairs], totals,
           ('First contact','Drawer at 15 s','Drawer at 30 s'), rows, 'Pairs that change between the two halves', 'Blues')
    counts(axes[0,1], [[a[v]['four'] for v in halves] for a in alignment], [a['eligible'] for a in alignment],
           ('Early exchange','Late exchange'), rows, 'First contact matches the full 1 s exchange¹', 'Purples')
    ax = axes[1,0]
    for g, label, color in zip(pairs, rows, ('#086674','#bd5826','#53916c','#68468f')):
        delta = [v['max_abs_delta']['median'] for v in g['controls']['chunks']]
        ax.plot(range(4), delta, 'o-', color=color, label=label)
    ax.set(title='Effect on the first 20 commands', xticks=range(4),
           xticklabels=('0–0.25','0.25–0.50','0.50–0.75','0.75–1.00'),
           xlabel='Time since the first query (s)', ylabel='Median maximum |command difference|')
    ax.set_ylim(bottom=0)
    ax.legend(ncol=2, fontsize=8, frameon=False)
    placed = []
    for m in modes:
        row = []
        for view in ('self', 'early', 'late', 'four'):
            matched = [r for n, r in result['paths_by_session'].items() if f'-{m}.{view}-' in n]
            assert len(matched) == groups[m]['early_to_late']['pairs']
            row.append(sum(r['at30'] == 'top' for r in matched))
        placed.append(row)
    counts(axes[1,1], placed, totals, ('Sham','Early','Late','Full'), rows,
           'Bowl in the instructed upper drawer at 30 s', 'Greens')
    for ax in axes.flat:
        ax.spines[['right','top']].set_visible(False)
        ax.title.set_fontsize(12)
    fig.suptitle('Same 0.50 s camera exchange at 0–0.5 s or 0.5–1 s', fontsize=16)
    fig.supxlabel('¹ Only pairs with different first contacts under sham and full exposure are eligible.', fontsize=10)
    fig.savefig(output, dpi=155, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder, args.output)
