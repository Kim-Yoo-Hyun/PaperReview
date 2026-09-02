#!/usr/bin/env python3
"""Register paper metadata and curation notes; never download PDFs."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

try:
    import build_lit_survey as survey
    from normalize_taxonomy import registry
    from registry_schema import enrich_record, extract_identifiers, next_paper_id
    from taxonomy import canonicalize
except ModuleNotFoundError:
    from . import build_lit_survey as survey
    from .normalize_taxonomy import registry
    from .registry_schema import enrich_record, extract_identifiers, next_paper_id
    from .taxonomy import canonicalize


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
REGISTRY_META = ROOT / "work" / "sources" / "registry_meta.json"
NOTE_NAMES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]
REQUIRED = {"title", "year", "venue", "category", "tags", "page"}


def title_key(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def notes(item: dict) -> dict[str, str]:
    aliases = item.get("aliases") or []
    common = f"""- Year/Venue: {item['year']} / {item['venue']}
- Category: {item['category']}
- Tags: {', '.join(item['tags'])}
- Aliases: {', '.join(aliases) if aliases else 'none recorded'}
- Official paper: {item['page']}
- Code/Project: {item.get('project', 'not identified')}
- Source audit: {item.get('source_audit', 'metadata registration only; full-text claims are UNVERIFIED.')}
"""
    evidence = item.get("evidence", "CURATION_ONLY")
    evidence_note = (
        " Full-text reading is not implied."
        if evidence in {"CURATION_ONLY", "ABSTRACT_CHECKED"}
        else ""
    )
    warning = f"> Evidence maturity: `{evidence}`.{evidence_note}\n"
    evidence_boundary = {
        "FULL_TEXT_CHECKED": "본문의 method/evaluation을 수동 확인한 근거만 paper-supported conclusion으로 확정한다.",
        "EXPERIMENT_CHECKED": "핵심 실험까지 확인한 근거만 paper-supported conclusion으로 확정한다.",
        "ABSTRACT_CHECKED": "공식 abstract/project 수준만 확인됐다. 상세 method, exact metric, failure는 full-text 확인 전까지 확정하지 않는다.",
        "CURATION_ONLY": "registry와 curation cue만 확인됐다. 자동 추출이나 local PDF 보유를 수동 정독으로 간주하지 않는다.",
    }.get(evidence, "현재 source 범위를 먼저 확인하고 본문 근거가 있는 claim만 확정한다.")
    note_header = (
        f"> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.{evidence_note}\n"
    )
    problem = item.get("problem", "UNVERIFIED — official abstract/full text에서 확인한다.")
    method = item.get("method", "UNVERIFIED — method section에서 확인한다.")
    interface = item.get(
        "interface",
        "UNVERIFIED — observation/state/action/control interface를 확인한다.",
    )
    assumptions = item.get(
        "assumptions",
        "UNVERIFIED — state, dynamics, sensing, contact와 distribution-shift 가정을 확인한다.",
    )
    evaluation = item.get(
        "evaluation",
        "UNVERIFIED — embodiment, task, data, metrics와 baselines를 확인한다.",
    )
    limitations = item.get(
        "limitations",
        "UNVERIFIED — failure condition, negative result와 재현성 제약을 full text에서 확인한다.",
    )
    lineage = item.get(
        "lineage",
        "UNVERIFIED — 어떤 foundation에서 출발하고 어떤 후속 연구로 이어지는지 확인한다.",
    )
    return {
        "01_overview.md": f"# {item['title']}\n\n{warning}\n{common}\n## Why This Paper Is Here\n\n{item.get('role', 'Registry admission rationale must be verified during reading.')}\n\n## Problem\n\n{problem}\n\n## Core Idea\n\n{method}\n\n## Interface\n\n{interface}\n\n## Evaluation Scope\n\n{evaluation}\n",
        "02_problem.md": f"""# Problem — {item['title']}

{note_header}> Analysis basis: metadata registration only; exact formulation은 본문 확인 필요. tracker의 reading status/evidence는 자동으로 올리지 않는다.

## Problem in One Sentence

{problem}

## System and Scope

- **Object / environment:** {item.get('role', '논문이 정의한 robot/embodied environment; 상세 조건은 본문 확인 필요.')}
- **Observation / input:** {interface}
- **Latent state / decision variable:** state/decision variable은 본문 확인 필요.
- **Output / action:** output/action/control interface는 위 input cue만으로 확정하지 않으며 본문 확인 필요.
- **Horizon / evaluation target:** task horizon과 primary evaluation target은 본문 확인 필요.

## Formal Problem Formulation

- **State / model:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.
- **Objective / loss / cost:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.
- **Constraints / initial-boundary-terminal conditions:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.
- **Success / guarantee:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.

## Bottleneck in Prior Work

현재 확인된 problem cue는 다음과 같다: {problem}

## What the Paper Changes

{method}

## Assumptions and Failure Boundary

| Assumption | Why it is needed | Failure boundary |
|---|---|---|
| {assumptions} | problem formulation을 재현하기 위해 필요 | 원문 확인 전에는 failure boundary를 확정하지 않음 |

## Position in the Robotics Loop

{interface}

## Verification Questions

- **Evidence anchor:** 현재 등록된 problem/method/interface cue; source-specific location은 본문 확인 필요.
- **Still to verify:** state, objective, constraints, initial/terminal condition, success definition과 robotics closed-loop 위치를 원문에서 확정한다.
""",
        "03_method.md": f"""# Method — {item['title']}

{note_header}> Analysis basis: metadata/abstract cue 기반 scaffold; exact method detail은 본문 확인 필요. tracker의 reading status/evidence는 자동으로 올리지 않는다.

## Method in One Sentence

{method}

## Design Rationale

{problem}

## Source Evidence Cues

- Method cue: {method}
- Interface cue: {interface}

## Pipeline

| Module | Purpose | Input | Operation | Output | Interface / expected benefit | Evidence |
|---|---|---|---|---|---|---|
| Paper-specific method module | 본문에서 확인 | {interface} | {method} | output/action은 본문 확인 필요 | paper-specific benefit은 04와 대조 | abstract/metadata cue; exact section/page 확인 필요 |

## Objective / Update Rule

- **Objective/loss/control law:** 본문 확인 필요.
- **Optimization/update:** 본문 확인 필요.
- **Constraint/regularization:** {assumptions}

## Variables and Parameters

| Symbol / parameter | Type / unit | Meaning | Used in | Source |
|---|---|---|---|---|
| oₜ / xₜ | observation/state | paper input or state | representation | method section 확인 필요 |
| aₜ / yₜ | action/prediction | paper output | execution/evaluation | method section 확인 필요 |
| θ | parameters | learned/optimized quantities | update | method section 확인 필요 |

## Observation–State–Action Interface

- **Observation / input:** {interface}
- **State / latent representation:** 본문 확인 필요.
- **Action / output:** 본문 확인 필요.
- **Planner–controller / policy–environment interface:** 본문 확인 필요.

## Temporal and Runtime Contract

- **Horizon:** 본문 확인 필요.
- **Inference/control rate:** 본문 확인 필요.
- **History / memory:** 본문 확인 필요.
- **Compute / latency dependency:** representation, optimization/inference steps와 hardware dependency를 본문에서 확인한다.

## Training vs Inference

- **Training / offline setup:** 본문 확인 필요.
- **Inference / online execution:** 본문 확인 필요.
- **Boundary to keep separate:** training, inference, control rate, horizon과 memory를 구분한다.

## Method-Specific Formal Details

- Exact equation/loss/control law와 variable meaning은 본문 확인 필요.

## Evaluation Link

- **Module-to-evaluation link:** [04_evaluation.md](./04_evaluation.md)의 baseline/ablation이 위 method module을 어떻게 isolate하는지 확인한다.
- **Protocol/metric:** {evaluation}

## Failure and Ablation Link

- Strongest assumption, failure mode와 module ablation은 본문 및 04_evaluation.md에서 확인 필요.

## Reproduction Checklist

1. [ ] method section에서 module input/output와 exact objective를 확인한다.
2. [ ] variable/unit, horizon, rate, memory와 implementation dependency를 기록한다.
3. [ ] 04의 baseline, ablation, metric, split과 failure protocol을 대조한다.

## Verification Questions

- **Still to verify:** exact method equation, variable source, training/inference boundary, runtime contract과 module-level evaluation attribution.
""",
        "04_evaluation.md": f"""# Evaluation — {item['title']}

{note_header}> Analysis basis: registry/abstract cue 기반 evaluation scaffold; exact experiment detail은 본문 확인 필요. tracker의 reading status/evidence는 자동으로 올리지 않는다.

## Evaluation in One Sentence

{evaluation}

## Evaluation Type and Scope

- **Evaluation type:** provisional; theory, system, learning, simulation/real-robot 또는 benchmark 유형을 본문에서 확인한다.
- **Target system/task:** {item.get('role', 'paper-specific robot/system task')}
- **Input/observation boundary:** {interface}
- **Output/decision under evaluation:** paper-specific prediction, plan, control 또는 task outcome; 본문 확인 필요.
- **Primary target:** {evaluation}

## Experimental Matrix

| Experiment / claim | Type & setting | Dataset / split | Robot / system | Baseline | Metric / result cue | Trials / seeds | Source |
|---|---|---|---|---|---|---|---|
| paper-specific evaluation | setting, split, embodiment와 evaluation unit은 본문 확인 필요 | not reported | not reported | not reported | {evaluation} | not reported | experiment section 확인 필요 |

## Dataset / Benchmark Role

| Resource | Role | Split / size | Source |
|---|---|---|---|
| not found | dataset/benchmark role은 본문 확인 필요 | not reported | experiment section 확인 필요 |

## Embodiment / Environment

| Dimension | Recorded cue | Missing detail | Source |
|---|---|---|---|
| Robot / simulator / hardware | not reported | hardware, simulator/real 여부와 configuration 확인 필요 | experiment section 확인 필요 |
| Observation / sensor | {interface} | sensor, calibration와 preprocessing 확인 필요 | method/evaluation section 확인 필요 |
| Task / episode unit | not reported | task count, reset, timeout와 success denominator 확인 필요 | evaluation protocol 확인 필요 |
| Generalization split/variation | not reported | scene/object/instruction/embodiment split 확인 필요 | dataset/protocol 확인 필요 |

## Metrics and Success Definition

| Metric / success signal | Direction / unit | Status | Source |
|---|---|---|---|
| task-specific metric | not reported | exact metric, aggregation와 success definition 확인 필요 | evaluation table 확인 필요 |

- **Success/failure/timeout definition:** 본문 확인 필요.

## Baselines and Fairness

| Baseline / comparison cue | What it should isolate | Same data/observation/compute? | Source |
|---|---|---|---|
| not found | comparison identity와 configuration 확인 필요 | not reported | baseline table 확인 필요 |

**Baseline fairness audit**

| Fairness dimension | Current record | Required check |
|---|---|---|
| Observation/action interface | not reported | modality, action space와 preprocessing을 맞춘다 |
| Data/pretraining | not reported | demonstrations, pretraining과 additional labels를 맞춘다 |
| Compute/runtime | not reported | parameter budget, inference steps, latency와 control rate를 맞춘다 |
| Evaluation protocol | not reported | split, reset/timeout, seeds와 success denominator를 맞춘다 |

## Ablations and Sensitivity

| Ablation / sensitivity factor | Method component | Expected interpretation | Reported status / source |
|---|---|---|---|
| not reported | core method module | component attribution과 strongest assumption sensitivity 확인 필요 | ablation table 확인 필요 |

## Main Results / Claim–Evidence Map

| Claim / target | Evidence or result cue | Evaluation type | Strength | Source |
|---|---|---|---|---|
| primary evaluation claim | {evaluation} | provisional | registry/abstract cue; exact result와 condition은 본문 확인 필요 | result table/figure 확인 필요 |

## Generalization and Failure Cases

| Assumption / regime | Failure or stress test | Status | Source |
|---|---|---|---|
| {assumptions} | failure condition과 negative result은 본문 확인 필요 | unverified | limitations/evaluation section 확인 필요 |

## Statistics, Efficiency, and Reproducibility

| Reproducibility field | Recorded value/cue | Status | Source |
|---|---|---|---|
| Trials / episodes | not reported | count와 repeat unit 확인 필요 | protocol 확인 필요 |
| Random seeds / repeats | not reported | seed/repeat policy 확인 필요 | protocol 확인 필요 |
| Mean ± std / CI | not reported | uncertainty reporting 확인 필요 | result table 확인 필요 |
| Latency / throughput | not reported | inference/control runtime 확인 필요 | method/evaluation 확인 필요 |
| Compute / hardware dependency | not reported | hardware, checkpoint와 environment 확인 필요 | reproducibility section 확인 필요 |
| Train/eval split and leakage control | not reported | split, preprocessing와 leakage control 확인 필요 | dataset section 확인 필요 |
| Code / checkpoint / environment | canonical pointer는 01_overview.md 참조 | availability/configuration을 본문에서 확인 | 01_overview.md |

## Limitations and Verification Questions

- **Current limitation cue:** {limitations}
- **Evidence boundary:** registry/abstract cue를 reported result로 승격하지 않는다. exact table/figure/page는 본문 확인이 필요하다.
- **Claim–condition check:** 모든 수치는 task, embodiment/simulator, input/action interface, metric, baseline와 trial/seed 조건을 함께 기록한다.
- **Reproduction check:** reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate와 failure handling을 별도로 확인한다.
""",
        "05_insights.md": f"""# Insights — {item['title']}

{note_header}
## Paper-supported conclusion

> **Evidence boundary:** {evidence_boundary}

### What was actually new

- **Problem cue:** {problem}
- **Method cue:** {method}
- **Evaluation cue:** {evaluation}

### Strongest assumption and failure boundary

- {limitations}
- Exact assumptions, negative results, and transfer limits remain to be checked against the full text.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** observation → state/world model → task decision → policy/control → feedback.
- {item.get('role', '정독 후 이 논문의 research relevance를 확정한다.')}

### Dependency and evolution

- {lineage}
- Direct citation and dependency claims require reference-level verification.

### Minimal reproduction

1. Confirm the paper-reported input, output, task, metric, baseline, and split from the full text.
2. Implement the smallest paper-specific component and compare it with a matched simpler baseline.
3. Report the primary metric together with failure rate, latency, and sensitivity to the strongest assumption.

## Falsifiable research question

At a matched data, compute, and action budget, does the paper's proposed interface improve its primary task metric and closed-loop robustness over a simpler baseline?

**Reject the hypothesis if** the primary metric does not improve or the method adds latency, failures, or assumption sensitivity without a compensating benefit.
""",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="JSON list of paper metadata")
    parser.add_argument("--apply", action="store_true", help="write changes; default is dry-run")
    args = parser.parse_args()
    incoming = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(incoming, list):
        raise SystemExit("input must be a JSON list")
    existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
    titles = {title_key(item["title"]) for item in existing}
    identifier_index: dict[tuple[str, str], str] = {}
    for old in existing:
        identifiers = old.get("identifiers") or extract_identifiers(old.get("page"), old.get("pdf"), old.get("project"))
        for namespace, identifier in identifiers.items():
            identifier_index[(namespace, identifier.casefold())] = old["title"]
    accepted = []
    skipped = []
    skipped_identifiers = []
    available_items = list(existing)
    for raw in incoming:
        missing = sorted(REQUIRED - raw.keys())
        if missing:
            raise SystemExit(f"{raw.get('title', '<untitled>')}: missing {missing}")
        item = canonicalize(dict(raw))
        if title_key(item["title"]) in titles:
            skipped.append(item["title"])
            continue
        item["folder"] = survey.folder_name(item)
        item.setdefault("pdf", "")
        item.setdefault("project", "not identified")
        item = enrich_record(
            item,
            paper_id=next_paper_id(available_items),
            root=ROOT,
        )
        collisions = [
            (namespace, identifier_index[(namespace, identifier.casefold())])
            for namespace, identifier in item.get("identifiers", {}).items()
            if (namespace, identifier.casefold()) in identifier_index
        ]
        if collisions:
            skipped_identifiers.append({"title": item["title"], "matches": collisions})
            continue
        accepted.append(item)
        available_items.append(item)
        titles.add(title_key(item["title"]))
        for namespace, identifier in item.get("identifiers", {}).items():
            identifier_index[(namespace, identifier.casefold())] = item["title"]
    print({"mode": "apply" if args.apply else "dry-run", "accepted": len(accepted), "skipped_existing": len(skipped), "skipped_identifier_collision": len(skipped_identifiers)})
    if not args.apply:
        for item in accepted:
            print(f"+ {item['title']} -> {item['folder']}")
        for collision in skipped_identifiers:
            print(f"! {collision['title']} -> identifier collision: {collision['matches']}")
        return
    for item in accepted:
        folder = ROOT / item["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, content in notes(item).items():
            path = folder / name
            if path.exists():
                raise SystemExit(f"refusing to overwrite {path}")
            path.write_text(content, encoding="utf-8")
    merged = existing + accepted
    MANIFEST.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if REGISTRY_META.exists():
        meta = json.loads(REGISTRY_META.read_text(encoding="utf-8"))
        meta["paper_count"] = len(merged)
        meta["generated_on"] = date.today().isoformat()
        REGISTRY_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "PAPER.md").write_text(registry(merged), encoding="utf-8")


if __name__ == "__main__":
    main()
