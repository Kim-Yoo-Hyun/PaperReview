#!/usr/bin/env python3
"""Upgrade CORE notes without pretending that UNREAD papers were close-read.

The operation is idempotent. It preserves paper-specific extracted material in
01-04, labels unresolved extraction fields as UNVERIFIED, and replaces the old
generic 05_insights template with a paper-specific dependency/research audit.
"""

from __future__ import annotations

import csv
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "research" / "READING_STATUS.csv"

STANDARD_FILES = [
    "01_overview.md",
    "02_problem.md",
    "03_method.md",
    "04_evaluation.md",
    "05_insights.md",
]

TRACK_AUDIT = {
    "Planning, control, and whole-body foundations": {
        "why": "feasibility, constraint handling, search/optimization, and feedback control을 구분하기 위한 robotics 좌표계",
        "verify": "state와 dynamics model, decision variable, constraint, convergence/completeness 성질, planning/control rate, failure case",
        "reuse": "학습 정책이 맡을 부분과 명시적 planner/controller가 유지해야 할 부분을 분리한다.",
        "experiment": "대표 저차원 task에서 feasible rate, solve time, trajectory cost와 disturbance 후 replanning을 비교한다.",
        "gap": "G-01 / G-09",
    },
    "RL, IL, and policy learning foundations": {
        "why": "data distribution, policy objective, value/sequence/generative action interface를 비교하기 위한 robot-learning 기반",
        "verify": "learning setting, objective, policy/value representation, data source, interaction budget, generalization split, optimization failure",
        "reuse": "성능 향상이 objective, data coverage, architecture 중 어디에서 오는지 분리한다.",
        "experiment": "동일 observation/action/data split에서 objective만 바꾸고 success, OOD degradation와 calibration을 비교한다.",
        "gap": "G-06 / G-08 / G-12",
    },
    "Manipulation, contact, tactile, and dexterity": {
        "why": "geometry와 contact mechanics가 sensing, planning, learned control에 들어가는 방식을 비교하기 위한 physical-interaction 기반",
        "verify": "contact model/state, sensor, action/control mode, embodiment, contact regime, peak force/slip/failure와 real-robot protocol",
        "reuse": "명시적 contact structure와 learned feedback의 책임 경계를 설계한다.",
        "experiment": "동일 contact-rich task에서 success뿐 아니라 peak force, slip, reaction latency와 recovery를 측정한다.",
        "gap": "G-01 / G-03 / G-05",
    },
    "VLA and generalist robot policies": {
        "why": "vision-language prior를 robot state와 action으로 연결하는 data, architecture, action representation의 기준점",
        "verify": "input/state, action representation, data/embodiment scale, control rate, horizon, fine-tuning protocol, unseen-task evaluation와 recovery",
        "reuse": "semantic generalization과 low-level control 성능의 기여를 분리한다.",
        "experiment": "동일 robot/task split에서 representation, action head와 data recipe를 분리해 success, latency와 intervention을 비교한다.",
        "gap": "G-01 / G-02 / G-10 / G-12",
    },
    "Safety and robot world models": {
        "why": "prediction, uncertainty, constraint, monitoring와 recovery를 서로 다른 safety interface로 구분하기 위한 기반",
        "verify": "model state/target, uncertainty definition, horizon, policy/planner coupling, calibration, intervention와 recovery outcome",
        "reuse": "예측 정확도나 detector score를 실제 action selection과 safety constraint로 연결한다.",
        "experiment": "통제된 perturbation에서 calibration, unsafe proposal, intervention cost와 최종 recovery success를 함께 측정한다.",
        "gap": "G-02 / G-07 / G-08",
    },
    "Locomotion, mobile manipulation, and humanoid systems": {
        "why": "dynamics adaptation, contact-rich locomotion, whole-body coupling과 embodiment-specific deployment를 비교하기 위한 기반",
        "verify": "state/action level, dynamics/contact handling, reward/reference, adaptation signal, sim-to-real protocol, stability와 task metric",
        "reuse": "learned skill과 model-based whole-body constraint 사이의 interface를 설계한다.",
        "experiment": "동일 disturbance set에서 task completion, fall/contact violation, recovery time와 energy를 함께 측정한다.",
        "gap": "G-09 / G-11",
    },
    "Robotics-enabling 3D perception": {
        "why": "3D representation과 state estimation이 downstream planning/control에 주는 실질적 효과를 판별하기 위한 기반",
        "verify": "input/representation, temporal update, calibration, latency, uncertainty, downstream robot interface와 task-level metric",
        "reuse": "perception score와 closed-loop robot performance 사이의 causal link를 검증한다.",
        "experiment": "동일 policy와 sensor budget에서 representation만 바꾸고 success, collision, latency와 stale-state failure를 비교한다.",
        "gap": "G-03 / G-04 / G-13",
    },
}


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S
    )
    return match.group(1).strip() if match else ""


def first_meaningful(text: str) -> str:
    for line in text.splitlines():
        value = line.strip().lstrip("- ")
        if not value or value.startswith(("자동 추출", "UNVERIFIED")):
            continue
        return value
    return "UNVERIFIED — full-text close reading에서 paper-supported cue를 기록한다."


def clean_scaffold(text: str) -> str:
    replacements = {
        "자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.":
            "UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.",
        "자동 추출 없음.":
            "UNVERIFIED — abstract/full text에서 직접 확인한다.",
        "PDF/abstract 자동 추출에서 명확한 dataset 명칭을 찾지 못함. 본문의 experiment section 확인 필요.":
            "UNVERIFIED — dataset과 split은 experiment section에서 직접 확인한다.",
        "자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.":
            "UNVERIFIED — train/validation/test와 generalization split을 직접 확인한다.",
        "자동 추출 없음": "UNVERIFIED — 직접 확인 필요",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    banner = (
        "> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, "
        "정독 전에는 paper-supported conclusion으로 인용하지 않는다.\n\n"
    )
    if "Evidence maturity:" not in text:
        first_break = text.find("\n\n")
        if first_break >= 0:
            text = text[: first_break + 2] + banner + text[first_break + 2 :]
    return text


def insights(row: dict[str, str], rows: list[dict[str, str]], old: str, overview: str) -> str:
    track = row["track"]
    audit = TRACK_AUDIT[track]
    peers = [item for item in rows if item["track"] == track]
    idx = next(i for i, item in enumerate(peers) if item["overview_path"] == row["overview_path"])
    previous = peers[idx - 1]["title"] if idx else "이 track의 출발점"
    following = peers[idx + 1]["title"] if idx + 1 < len(peers) else "이 track의 frontier 연결"
    problem = first_meaningful(section(overview, "Problem") or section(old, "Problem cue"))
    method = first_meaningful(section(overview, "Core Idea") or section(old, "Method cue"))
    result = first_meaningful(section(old, "근거가 되는 논문 단서") or section(overview, "Main Claims"))
    return f"""# Insights — {row['title']}

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **{track}**에서 {audit['why']}로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: {problem}
- Method cue: {method}
- Result/evaluation cue: {result}

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`{previous} → {row['title']} → {following}`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- {audit['verify']}
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- {audit['reuse']}
- 연결 gap: `{audit['gap']}` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

{audit['experiment']}

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
"""


def main() -> None:
    with STATUS.open(newline="", encoding="utf-8") as handle:
        all_rows = list(csv.DictReader(handle))
    rows = [row for row in all_rows if row["tier"] == "CORE"]
    changed = 0
    for row in rows:
        folder = (ROOT / row["overview_path"].lstrip("./")).parent
        overview_path = folder / "01_overview.md"
        overview = overview_path.read_text(encoding="utf-8")
        old_insights = (folder / "05_insights.md").read_text(encoding="utf-8")
        for name in STANDARD_FILES[:4]:
            path = folder / name
            updated = clean_scaffold(path.read_text(encoding="utf-8"))
            if updated != path.read_text(encoding="utf-8"):
                path.write_text(updated, encoding="utf-8")
                changed += 1
        new_insights = insights(row, rows, old_insights, overview)
        if new_insights != old_insights:
            (folder / "05_insights.md").write_text(new_insights, encoding="utf-8")
            changed += 1
    print({"core_papers": len(rows), "files_changed": changed})


if __name__ == "__main__":
    main()
