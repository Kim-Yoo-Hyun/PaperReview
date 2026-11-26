"""Plot matched first actions, contact, and containment from the measured duration study."""
import argparse
import json
from pathlib import Path

import numpy as np

from plot_drawer_location import plt


def plot(folder, output):
    result = json.loads((folder / 'verification.json').read_bytes())
    records, groups = result['paths_by_session'], result['comparisons']['all']
    modes = ('narrow-middle', 'full-middle', 'narrow-bottom', 'full-bottom')
    labels = ('Middle 76 mm', 'Middle 160 mm', 'Bottom 76 mm', 'Bottom 160 mm')
    colors = ('#146b80', '#c06524', '#408864', '#74549b')
    fig, axes = plt.subplots(2, 2, figsize=(11.6, 7.1), layout='constrained')
    chunks, events = axes[0]
    comparisons = [groups[m]['one_to_four'] for m in modes]
    for label, color, group in zip(labels, colors, comparisons):
        values = [c['max_abs_delta']['median'] for c in group['controls']['chunks']]
        chunks.plot(np.arange(4), values, 'o-', lw=2, markersize=5, label=label, color=color)
    chunks.set(title='Effect on the first 20 controls', ylabel='Median largest |command difference|',
               xlabel='Time from first policy query (s)', xticks=np.arange(4),
               xticklabels=('0–0.25', '0.25–0.50', '0.50–0.75', '0.75–1.00'))
    chunks.set_ylim(bottom=0)
    chunks.legend(fontsize=8, ncol=2, frameon=False)
    counts = np.array([[c[f]['changed'] for f in ('contact', 'at15', 'at30')] for c in comparisons])
    totals = np.array([c['pairs'] for c in comparisons])
    events.imshow(counts / totals[:, None], cmap='Blues', vmin=0, vmax=1, aspect='auto')
    for i, row in enumerate(counts):
        for j, n in enumerate(row):
            events.text(j, i, f'{n}/{totals[i]}', ha='center', va='center', weight='bold',
                        color='white' if n > .54*totals[i] else '#1e3340')
    events.set(title='Pairs that changed category', xticks=range(3), yticks=range(4),
               xticklabels=('First contact', 'Drawer at 15 s', 'Drawer at 30 s'), yticklabels=labels)
    for ax, field, title in zip(axes[1], ('contact_tick', 'place_tick'),
                                ('Time to first drawer or bowl contact', 'Time to first containment in any drawer')):
        for i, (mode, color) in enumerate(zip(modes, colors)):
            pairs = [(x[field], records[n.replace('.one-', '.four-')][field]) for n, x in sorted(records.items())
                     if f'-{mode}.one-' in n]
            assert len(pairs) == totals[i]
            delta = sorted((b-a)/20 for a, b in pairs if a is not None and b is not None)
            if delta:
                ax.scatter(delta, i + np.linspace(-.17, .17, len(delta)), s=15, alpha=.65, color=color)
                ax.scatter([np.median(delta)], [i], s=44, marker='D', facecolors='white', edgecolor=color, zorder=3)
            ax.text(.985, i-.24, f'n={len(delta)}', transform=ax.get_yaxis_transform(), va='center',
                    ha='right', color='#455761', fontsize=8)
        ax.axvline(0, color='#59666e', lw=1, ls='--', zorder=0)
        ax.set(title=title, xlabel='Paired time difference, 1.00 s minus 0.25 s exposure (s)',
               yticks=range(4), yticklabels=labels, ylim=(3.55, -.55))
    for ax in axes.flat:
        ax.spines[['top', 'right']].set_visible(False)
        ax.title.set_fontsize(12)
    fig.suptitle('Both cameras show the opposite opening for 1.00 s versus 0.25 s',
                 fontsize=16, weight='semibold')
    fig.savefig(output, dpi=155, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder, args.output)
