# MapDream: Task-Driven Map Learning for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/64902.
> PDF retrieval source: https://openreview.net/pdf/6e898fbe18f2ef7449852473b4a8ab53fd0fda57.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Guoxin Lian, Shuo Wang, Yucheng Wang, Yongcai Wang, Maiyue Chen, Kaihui Wang, Bo Zhang, Zhizhong Su, Deying Li, Zhaoxin Fan
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Navigation
- Official paper: https://icml.cc/virtual/2026/poster/64902
- Full-text retrieval: https://arxiv.org/pdf/2602.00222.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

문제 관련 발췌 — A central difficulty of VLN is partial observability.

방법 관련 발췌 — Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation objectives rather than fixed by expert design. • ...

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Navigation (VLN) requires agents to follow natural language instructions in partially observed 3D environments, motivating map representations that aggregate spatial context beyond local perception.
- **p. 1 / Abstract - extractive body cue:** However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy.
- **p. 1 / Abstract - extractive body cue:** We argue that maps should instead be learned representations shaped directly by navigation objectives rather than exhaustive reconstructions.
- **p. 1 / Abstract - extractive body cue:** Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird'seye-view (BEV) image synthesis.
- **p. 1 / Abstract - extractive body cue:** The framework jointly learns map generation and action prediction, distilling environmental context into a compact three-channel BEV map that preserves only navigation-critical affordances.
- **p. 1 / 1. Introduction - extractive body cue:** A central difficulty of VLN is partial observability.
- **p. 2 / 1. Introduction - extractive body cue:** The limitation of this approach is that map representations typically remain outside the learning loop that governs navigation behavior, preventing them from being refined through ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation objectives ...
- **p. 2 / 1. Introduction - extractive body cue:** Based on this insight, we propose MapDream, a framework that unifies spatial representation learning and decision making.
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.
- **p. 1 / 1. Introduction - extractive body cue:** Obs Inst VLN Policy Act Vanilla Obs Map Inst VLN Policy Map Module Act Expert-Designed Maps Map Inst Obs VLN Policy Map Module Act Task-Driven ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike previous approaches that either omit maps or rely on expert-designed representations, MapDream adopts a map-in-the-loop design that learns a task-driven generative map jointly with ...
- **p. 4 / 3.1. Overview - extractive body cue:** Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) ...
- **p. 5 / 3.4. Reinforcement Fine-tuning - extractive body cue:** The optimization objective follows a GRPO-style formulation: LVLN = -Ek " min
- **원문 대조:** GRPO의 ratio ρ(k)는 navigation-policy likelihood ratio와 BEV-map likelihood ratio의 곱이다. 두 모듈은 current/reference parameter를 각각 사용하며 관측 history·현재 frame·instruction에 조건화된다. 기존 cue는 식의 마지막 조건부 인자만 남아 있었다. ([PDF p. 5](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lian26c/lian26c.pdf#page=5), §3.4 Reinforcement Fine-tuning, Eq. (7)).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, the map-inthe-loop architecture comprises a task-driven map module and a VLN policy, where BEV maps are autoregressively generated from egocentric observation histories and language instructions and then provided to the policy ... | camera/depth stream, pose, map와 language goal | p. 2 (1. Introduction), p. 4 (3.1. Overview) |
| State/latent | First, map-inthe-loop, architecture, comprises, task-driven, module, VLN, policy, where, BEV, maps, autoregressively | robot pose, free-space/semantic map와 local goal | p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 1 (1. Introduction) |
| Output/action | Specifically, it features (1) a two-module system composed of a task-driven map module and a VLN policy for spatial representation learning and action prediction; (2) a supervised pre-training stage that establishes a ... | collision-free trajectory 또는 velocity command | p. 4 (3.1. Overview), p. 1 (1. Introduction), p. 4 (3.3.2. PRE-TRAINING THE MAP MODULE) |
| Pre-training objective | 원문 대조: VLN policy의 supervised pre-training은 예측 BEV map, 관측 history·현재 frame·instruction에 조건화한 multi-step expert action sequence의 negative log-likelihood를 최소화한다. ([PDF p. 4](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lian26c/lian26c.pdf#page=4), §3.3.3 Pre-training the VLN Policy, Eq. (3)) | Expert-action likelihood; navigation 성공률·안전 지표와 구분 | [PDF p. 4](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lian26c/lian26c.pdf#page=4), §3.3.3 Pre-training the VLN Policy, Eq. (3) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are: • We first introduce a task-driven perspective on map representations for VLN, reframing maps as representations shaped by downstream navigation objectives ...
- **p. 2 / 1. Introduction - extractive body cue:** Based on this insight, we propose MapDream, a framework that unifies spatial representation learning and decision making.
- **p. 4 / 3.3. Supervised Pre-training - extractive body cue:** It consists of three parts: task-driven map supervision, pre-training the map module, and pre-training the VLN policy.
- **p. 1 / 1. Introduction - extractive body cue:** Obs Inst VLN Policy Act Vanilla Obs Map Inst VLN Policy Map Module Act Expert-Designed Maps Map Inst Obs VLN Policy Map Module Act Task-Driven ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike previous approaches that either omit maps or rely on expert-designed representations, MapDream adopts a map-in-the-loop design that learns a task-driven generative map jointly with ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive body cue:** Across all settings, MapDream improves both success rate and path efficiency, which we attribute to its task-driven generative maps that are refined through two-stage optimization ...
- **p. 5 / 4.1.2. METRICS - extractive body cue:** We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle success ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive body cue:** As shown in Table 1, MapDream achieves the best overall performance among monocular approaches on both datasets, with the highest SR and SPL while reducing ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.1.2. METRICS) |
| Embodiment/environment | Notably, the model is trained only on the R2R-CE and RxR-CE simulators, yet transfers in a zeroshot manner to real-world, previously unseen indoor scenes. | hardware/simulator version and reset protocol | p. 8 (4.6. Real-world Generalization), p. 6 (4.2.2. TRAINING DETAILS) |
| Dataset/benchmark | Results are reported on the validation-unseen splits to assess generalization to novel environments. | role, split, size and leakage | p. 8 (4.6. Real-world Generalization), p. 6 (4.2.2. TRAINING DETAILS), p. 5 (4.1.1. EXPERIMENTAL ENVIRONMENTS), p. 8 (4.6. Real-world Generalization) |
| Metric | We adopt the standard VLN evaluation protocol (Krantz et al., 2020; Ku et al., 2020) to assess navigation performance using success rate (SR), oracle success rate (OSR), success weighted by path length ... | definition, denominator, direction and uncertainty | p. 5 (4.1.2. METRICS), p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 6 (4.3. Comparison with State-of-the-Art Methods) |
| Baseline/ablation | We evaluate the effect of two-stage training in MapDream by comparing three configurations: a baseline VLN policy without maps, the map-conditioned model after Stage 1 supervised pre-training, and the full two-stage system ... | fair input/data/compute/action matching | p. 7 (4.5.1. TWO-STAGE TRAINING), p. 5 (4.2.1. DATASET COLLECTION), p. 5 (4.1.2. METRICS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1.1. EXPERIMENTAL ENVIRONMENTS - extractive body cue:** We focus on the continuous-environment (CE) protocol because continuous control introduces fine motion granularity and realistic noise, making navigation sensitive to small geometric deviations.
- **p. 5 / 4.2.1. DATASET COLLECTION - extractive body cue:** Additionally, we generate 500K non-oracle samples through exploratory rollouts in the training environments, improving robustness to outof-distribution states and enhancing generalization across diverse scenarios.
- **p. 6 / 4.3. Comparison with State-of-the-Art Methods - extractive body cue:** These results empirically validate that learning spatial abstractions under navigation objectives leads to more robust decision making in continuous environments.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** We conduct three ablation studies on R2R-CE that jointly probe MapDream along complementary design dimensions: optimization strategy, robustness to map initialization, and representation capacity.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 4 (3.3. Supervised Pre-training)이다.
