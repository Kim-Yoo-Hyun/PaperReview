#!/usr/bin/env python3
"""Register paper metadata and curation notes; never download PDFs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

try:
    import build_lit_survey as survey
    from normalize_taxonomy import registry
    from registry_profiles import enrich_profiles
    from registry_schema import enrich_record, extract_identifiers, next_paper_id
    from taxonomy import canonicalize
except ModuleNotFoundError:
    from . import build_lit_survey as survey
    from .normalize_taxonomy import registry
    from .registry_profiles import enrich_profiles
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


def abstract_analysis_notes(item: dict) -> dict[str, str]:
    """Render authored, paper-specific abstract analysis without implying a read."""
    required = ("problem", "method", "interface", "evaluation", "role", "lineage",
                "question", "minimal_experiment", "verification_questions")
    if any(not item.get(key) for key in required):
        raise ValueError(f"Incomplete abstract analysis: {item['title']}")
    if item.get("evidence") != "ABSTRACT_CHECKED":
        raise ValueError("abstract_analysis_v1 requires ABSTRACT_CHECKED evidence")
    sources = item.get("sources", {})
    code = (sources.get("code") or {}).get("url") or item.get("artifacts", {}).get("code_status", "not_identified")
    venue_source = (sources.get("venue_verification") or {}).get("url") or item["page"]
    header = f"""> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: {item['year']} / {item['venue']}
- Category: {item['category']}
- Primary track: {item['primary_track']}
- Tier: PENDING
- Tags: {', '.join(item['tags'])}
- Aliases: {', '.join(item.get('aliases', []))}
- Official paper: {item['page']}
- Venue verification: {venue_source}
- Code/Project: {item['project']}
- Code: {code}
- Source audit: {item['source_audit']}

"""
    header = "\n".join(line.rstrip() for line in header.split("\n"))
    evidence = f"[공식 paper/abstract]({item['page']})"
    project_url = (sources.get("project") or {}).get("url")
    if project_url:
        evidence += f" · [저자 project/code]({project_url})"
    code_url = (sources.get("code") or {}).get("url")
    if code_url and code_url != project_url:
        evidence += f" · [공식 code]({code_url})"
    unresolved = "not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다."
    bodies = {
        "01_overview.md": f"""## Problem and Importance

{item['problem']}

## Core Idea and Contribution

{item['method']}

## Observation–State–Action Interface

{item['interface']}

## Evaluation Scope and Claim Boundary

{item['evaluation']}

근거: {evidence}. 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

{item['role']}

## Verification Boundary

{item['verification_questions']}을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
""",
        "02_problem.md": f"""## Problem in One Sentence

{item['problem']}

## Bottleneck and Changed Formulation

{item['method']}

## System and Robotics Loop

{item['interface']}

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

{item['verification_questions']}.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

{item['evaluation']}

## Evidence Anchor

{evidence}. Exact objective, constraints, success definition은 본문 수동 확인 필요.
""",
        "03_method.md": f"""## Method in One Sentence

{item['method']}

## Observation–State–Action Interface

{item['interface']}

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: {item['verification_questions']}.

Source가 명시한 evaluation 범위: {item['evaluation']}

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

{item['minimal_experiment']}

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

{evidence}. 수식·세부 구현·코드 실행은 미검증이다.
""",
        "04_evaluation.md": f"""## Evaluation in One Sentence

{item['evaluation']}

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

{item['evaluation']}

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 {unresolved}

## Metrics and Success Definition

{unresolved}

## Baselines and Fairness

{unresolved} Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

{unresolved}

## Generalization and Failure Cases

{unresolved} 특히 {item['verification_questions']}을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 {unresolved}

## Proposed Evaluation — Researcher Interpretation

{item['minimal_experiment']}

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

{evidence}. Main table·appendix·negative result는 본문 수동 확인 필요.
""",
        "05_insights.md": f"""## Paper-supported conclusion

### What the Source Supports

{item['method']}

{item['evaluation']}

근거: {evidence}. 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 {item['verification_questions']}은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

{item['role']}

### Dependency and Evolution

{item['lineage']}.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

{item['minimal_experiment']}

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

{item['question']}

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
""",
    }
    pointer = (
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        "> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.\n"
        "> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.\n\n"
    )
    return {
        name: f"# {item['title']}\n\n{header if name == '01_overview.md' else pointer}{body}"
        for name, body in bodies.items()
    }


def notes(item: dict) -> dict[str, str]:
    if item.get("note_format") == "abstract_analysis_v1":
        return abstract_analysis_notes(item)
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
            migrated_on=str(date.today()),
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
        # These renderers emit the same declared evidence level in all five
        # newly created note headers. Record it without changing existing notes
        # or the user's reading status; the repository audit requires this map.
        item["provenance"]["note_evidence"] = {
            name: item["provenance"]["content_evidence"] for name in NOTE_NAMES
        }
    merged = existing + accepted
    # Registration is incremental: preserve the existing papers' manually
    # reviewed profiles and evidence dates; only initialize new entries.
    enrich_profiles(accepted, ROOT, reviewed_on=str(date.today()))
    for item in accepted:
        if item.get("note_format") == "abstract_analysis_v1":
            item["evaluation_profile"]["basis"] = (
                "Abstract/project-only note cues; detailed protocol remains not_recorded. "
                "Source claims are not full-text or experiment verification; catalog links are cue_only."
            )
            item["reproducibility"]["basis"] = (
                "Manifest artifact links and abstract/project-only note cues; "
                "full-text protocol and reproducible execution have not been checked."
            )
    MANIFEST.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if REGISTRY_META.exists():
        meta = json.loads(REGISTRY_META.read_text(encoding="utf-8"))
        meta["paper_count"] = len(merged)
        meta["generated_on"] = date.today().isoformat()
        meta["metadata_profile_version"] = "1.0"
        meta["metadata_profile_reviewed_on"] = date.today().isoformat()
        meta["evaluation_profile_count"] = len(merged)
        meta["reproducibility_profile_count"] = len(merged)
        meta["lineage_profile_count"] = len(merged)
        meta["manifest_sha256"] = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
        meta["relation_count"] = sum(len(paper.get("relations", [])) for paper in merged)
        REGISTRY_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "PAPER.md").write_text(registry(merged), encoding="utf-8")


if __name__ == "__main__":
    main()
