# π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://arxiv.org/html/2410.24164)
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p010.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p010.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

π₀는 시각·언어 사전학습에서 얻은 표현으로 여러 로봇의 연속 행동을 생성한다. 논문은 기본 정책과 태스크별 미세조정 정책의 조작 성능을 각각 평가한다. [원문](https://arxiv.org/html/2410.24164)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robot learning holds tremendous promise to untock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the ...
- **p. 1 / Abstract - extractive body cue:** However, bringing robot learning to the level of generality required for effective real-world systems faces major ‘obstacles in terms of data, gener m, and robustness.
- **p. 1 / Abstract - extractive body cue:** In this paper, we discuss how generalist robot policies (i., robot foundation models) can address these challenges, and how we ean ‘design effective generalist robot ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel flow matching architecture
- **p. 1 / Abstract - extractive body cue:** Physical Intelligence, San Francisco, California, USA.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Flexible and general-purpose models that can be tasked variety of robot behaviors have tremendous fications, but they may also offer solutions to some of the ...

## Core Idea

π₀는 사전학습한 시각언어 모델에 flow matching으로 학습하는 행동 모듈을 결합한다. 영상·언어 지시·로봇 상태를 조건으로 연속 행동 청크를 생성하며 여러 플랫폼의 조작 데이터로 정책을 학습한다. [원문](https://arxiv.org/html/2410.24164)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ~ 50 for our tasks), and 0 ... | image/video, language instruction, proprioception과 history | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL) |
| State/latent | Formally, want, model, data, distribution, where, corresponds, action, chunk, future, actions, tasks | language-grounded task state와 action-policy context | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION) |
| Output/action | We further augment this backbone with roboties-specific inputs and outputs - namely, proprioceptive state and robot actions. | continuous action, pose 또는 action chunk | p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective/outcome | Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow matching loss and tokens corresponding to discrete ... | instruction following, task success, generalization과 latency | p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model) |

## Main Claims and Actual Contribution

다양한 로봇에서 학습한 기본 정책을 직접 평가하고 고품질 시연으로 미세조정했다. 세탁물 접기는 평가 과제이며, 서론의 신발끈 묶기와 새우 요리는 선행 연구의 예시다. [원문](https://arxiv.org/html/2410.24164)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | We study this question by directly evaluating π₀, with comparisons to other robot foundation models. | hardware/simulator version and reset protocol | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | We study this question by directly evaluating π₀, with comparisons to other robot foundation models. | role, split, size and leakage | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Metric | Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") with a method that receives intermediate commands from ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption) |
| Baseline/ablation | Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates for baseline models, x-small, and three ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 11 / C. Learning new dexterous tasks - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK
- **p. 10 / C. Learning new dexterous tasks - extractive body cue:** This presents challenges due to the egg shape, slipperiness, and the need for careful placement.

## Why Read It

기본 정책에 지시를 주어 수행한 실험과 태스크별 시연으로 미세조정한 실험을 나누어 보면 복잡한 조작 성능의 조건을 비교할 수 있다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges. (p. 2, 1. INTRODUCTION).
- **Actual contribution:** π₀는 사전학습한 시각언어 모델에 flow matching으로 학습하는 행동 모듈을 결합한다. 영상·언어 지시·로봇 상태를 조건으로 연속 행동 청크를 생성하며 여러 플랫폼의 조작 데이터로 정책을 학습한다. [원문](https://arxiv.org/html/2410.24164)
- **Evaluation boundary:** Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates for baseline models, x-small, ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks. (p. 7, A. Evaluating the base model).
