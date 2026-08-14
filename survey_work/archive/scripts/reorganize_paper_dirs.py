#!/usr/bin/env python3
"""Move existing paper folders into year/venue hierarchy."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from build_lit_survey import ROOT, WORK, folder_name


MANIFEST = WORK / "selected_papers.json"


def merge_or_move(src: Path, dst: Path) -> str:
    if src.resolve() == dst.resolve():
        return "already"
    if not src.exists():
        return "missing-source"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.move(str(src), str(dst))
        return "moved"

    # Idempotent safety path: merge files only when a partial destination exists.
    for child in src.iterdir():
        target = dst / child.name
        if target.exists():
            continue
        shutil.move(str(child), str(target))
    try:
        src.rmdir()
    except OSError:
        return "merged-source-not-empty"
    return "merged"


def main() -> None:
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    counts: dict[str, int] = {}
    missing: list[str] = []
    for paper in papers:
        src = ROOT / paper["folder"]
        dst = ROOT / folder_name(paper)
        result = merge_or_move(src, dst)
        counts[result] = counts.get(result, 0) + 1
        if result.startswith("missing"):
            missing.append(paper["folder"])

    print(counts)
    if missing:
        print("missing sources:")
        for item in missing[:20]:
            print("-", item)


if __name__ == "__main__":
    main()
