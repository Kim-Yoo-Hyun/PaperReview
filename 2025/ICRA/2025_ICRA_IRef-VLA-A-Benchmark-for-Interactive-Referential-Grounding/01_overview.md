# IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.17406.
> PDF retrieval source: https://arxiv.org/pdf/2503.17406v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Haochen Zhang, Nader Zantout, Pujith Kachana, Ji Zhang, Wenshan Wang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, 3D Vision, Benchmark
- Official paper: https://arxiv.org/abs/2503.17406
- Full-text retrieval: https://arxiv.org/pdf/2503.17406v1
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

IRef-VLA는 모호하거나 장면과 맞지 않는 언어 표현이 주어졌을 때 3차원 실내 장면에서 지시 대상을 찾는 능력을 평가하는 자료다. [PDF 1쪽](https://arxiv.org/pdf/2503.17406v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** With the recent rise of large language models, vision-language models, and other general foundation models, there is growing potential for multimodal, multi-task robotics that can ...
- **p. 1 / Abstract - extractive body cue:** One such application is indoor navigation using natural language instructions.
- **p. 1 / Abstract - extractive body cue:** However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required.
- **p. 1 / Abstract - extractive body cue:** Additionally, the language used may be imperfect or misaligned with the scene, further complicating the task.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we curate a benchmark dataset, IRef-VLA, for Interactive Referential Vision and Language-guided Action in 3D Scenes with imperfect references.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The pursuit of such agents that can identify and understand 3D scenes, consolidate visual input with language semantics, and display robust performance for real-world deployment, ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding ...
- **p. 1 / Abstract - extractive body cue:** With this benchmark, we aim to provide a resource for 3D scene understanding that aids the development of robust, interactive navigation systems.
- **p. 1 / Abstract - extractive body cue:** We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to demonstrate ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential objectgrounding task, and a novel extension of this ... | standardized observation, action, task state와 evaluation split | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| State/latent | advance, path, towards, more, intelligent, interaction, natural, language, navigation, IRef-VLA, dataset, benchmark | benchmark state/goal와 method decision | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Output/action | One such application is indoor navigation using natural language instructions. | policy/controller trajectory 또는 measured result | p. 1 (Abstract) |
| Objective/outcome | However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required. | success metric, robustness, generalization과 reproducibility | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- 실제 실내 스캔으로부터 물체·방 주석, 공간 관계와 이동 가능 영역을 구축하고 같은 장면에 올바른 표현 및 불완전한 표현을 생성했다. [PDF 2쪽](https://arxiv.org/pdf/2503.17406v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2503.17406v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2503.17406v1#page=4)
- 지시 대상 추정 모델과 장면 그래프 탐색 기준선을 평가하고, 원래 설명과 일치하는 물체가 없을 때 대안을 생성하는 경우도 조사했다. [PDF 4쪽](https://arxiv.org/pdf/2503.17406v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2503.17406v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2503.17406v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 1 (I. INTRODUCTION) |
| Embodiment/environment | First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans. | hardware/simulator version and reset protocol | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Dataset/benchmark | First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans. | role, split, size and leakage | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Metric | Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness needed for real-world deployment [13]. | definition, denominator, direction and uncertainty | p. 1 (I. INTRODUCTION), p. 3 (Figure/Table caption), p. 1 (Abstract) |
| Baseline/ablation | We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to demonstrate the performance bound and generation of alternatives ... | fair input/data/compute/action matching | p. 1 (Abstract), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, human referential language often involves spatial reasoning, implicit and explicit affordances, open-vocabulary language, and may even be incorrect or refer to something that does ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential losses ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 5 (Figure/Table caption)이다.
