"""Plot first contact and bowl destinations recorded on the same tabletop."""
import argparse
from collections import Counter
import json
from pathlib import Path

from plot_drawer_location import counts_panel, plt


def plot(folder, output):
    result = json.loads((folder / 'verification.json').read_bytes())
    design = json.loads((Path(__file__).parent / 'drawer/drawer_width.json').read_bytes())
    modes = design['conditions']
    labels = ['Closed' if m == 'full-closed' else
              m.split('-')[1].title() + (' 76 mm' if m.startswith('narrow-') else ' 160 mm') for m in modes]
    grouped = [[ticks for name, ticks in result['outcomes'].items() if '-' + mode + '-b' in name] for mode in modes]
    assert sum(map(len, grouped)) == result['paths']
    contacts = [Counter(t['600']['first_external']['target'] for t in cases) for cases in grouped]
    panels = [('First external gripper contact', contacts)]
    for tick in (300, 600):
        dest = [Counter('+'.join(l for l in ('top', 'middle', 'bottom') if t[str(tick)][l + '_in']) or 'none'
                        for t in cases) for cases in grouped]
        panels.append((f'Bowl destination at {tick // 20} s', dest))
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), layout='constrained')
    for ax, (title, rows) in zip(axes, panels):
        present = set().union(*rows)
        ordered = [key for key in ('top', 'bowl', 'middle', 'bottom', 'other', 'none') if key in present]
        columns = ordered + sorted(present.difference(ordered))
        counts = [[row[col] for col in columns] for row in rows]
        totals = [[len(cases)] * len(columns) for cases in grouped]
        counts_panel(ax, counts, totals, [c.title() for c in columns], labels, title, '', '')
    fig.suptitle('LIBERO-Goal   |   Same tabletop and upper-drawer instruction', fontsize=15)
    fig.savefig(output, dpi=155, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    plot(args.folder, args.output)
