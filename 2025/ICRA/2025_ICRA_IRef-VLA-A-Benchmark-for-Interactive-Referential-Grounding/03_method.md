# Method - IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.17406v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 1 (Abstract)): To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding task, and a novel extension ...

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding ...
- **p. 1 / Abstract - extractive body cue:** We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to demonstrate ...
- **p. 1 / Abstract - extractive body cue:** However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As we progress towards generalizable embodied intelligence, there is a need for methods that are capable of reasoning in 3Dspace and interacting with humans.
- **p. 1 / Abstract - extractive body cue:** One such application is indoor navigation using natural language instructions.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding ...
- **p. 1 / Abstract - extractive body cue:** With this benchmark, we aim to provide a resource for 3D scene understanding that aids the development of robust, interactive navigation systems.

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding ...
- **p. 1 / Abstract - extractive body cue:** We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to demonstrate ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both ... | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch ... | p. 1 (Abstract) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both ... | p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As we progress towards generalizable embodied intelligence, there is a need for methods that are capable of reasoning in 3Dspace and interacting with humans.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | advance, path, towards, more, intelligent, interaction, natural, language, navigation, IRef-VLA, dataset, benchmark, referential, objectgrounding | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | advance, path, towards, more, intelligent, interaction, natural, language, navigation, IRef-VLA | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | advance, path, towards, more, intelligent, interaction, natural, language, navigation, IRef-VLA | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | However, despite, recent, progress, problem, remains, challenging, spatial, reasoning, semantic | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding ...
- **p. 1 / Abstract - extractive body cue:** One such application is indoor navigation using natural language instructions.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | not recovered | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | not recovered | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** advance, path, towards, more, intelligent, interaction, natural, language, navigation, IRef-VLA, dataset, benchmark, referential, objectgrounding, task, novel, extension, call, grounding, imperfect.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans. | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Baseline harness | We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch ... | p. 1 (Abstract), p. 5 (Figure/Table caption) |
| Metric / failure reporting | Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. ... | p. 5 (Figure/Table caption), p. 1 (I. INTRODUCTION) |

## Failure and Ablation Link

- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, human referential language often involves spatial reasoning, implicit and explicit affordances, open-vocabulary language, and may even be incorrect or refer to something that does ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential losses ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 1 (Abstract), objective p. 1 (Abstract), p. 1 (I. INTRODUCTION), temporal 본문 anchor 없음.
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
