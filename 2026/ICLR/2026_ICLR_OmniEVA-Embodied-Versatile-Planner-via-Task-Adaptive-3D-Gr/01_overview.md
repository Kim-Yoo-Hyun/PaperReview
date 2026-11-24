# OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7b122d0a0dcb1a86ffa25ccba154652b-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247599. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Yuecheng Liu, DaFeng Chi, Shiguang Wu, Zhanguang Zhang, Yuzheng Zhuang, Bowen Yang, He Zhu, Lingfeng Zhang, Pengwei Xie, David Gamaliel Arcos Bravo, Yingxue Zhang, Jianye Hao, Xingyue Quan
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7b122d0a0dcb1a86ffa25ccba154652b-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf)

## Why This Paper Is Here

OmniEVA는 과제에 따라 3D 정보를 얼마나 쓸지 조절하고 팔의 도달 범위 같은 물리적 조건을 반영해 실행할 계획을 생성한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in multimodal large language models (MLLMs) have opened new opportunities for embodied intelligence, enabling multimodal understanding, reasoning, and interaction, as well as continuous ...
- **p. 1 / ABSTRACT - extractive body cue:** Nevertheless, current MLLM-based embodied systems face two critical limitations.
- **p. 1 / ABSTRACT - extractive body cue:** First, Geometric Adaptability Gap: models trained solely on 2D inputs or with hard-coded 3D geometry injection suffer from either insufficient spatial information or restricted 2D ...
- **p. 1 / ABSTRACT - extractive body cue:** Second, Embodiment Constraint Gap: prior work often neglects the physical constraints of real robots, resulting in task plans that are theoretically valid but practically infeasible.To ...
- **p. 1 / ABSTRACT - extractive body cue:** (2) an Embodiment-Aware Reasoning framework that incorporates task goals and physical constraints into the reasoning loop, ensuring executable plans.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, the absence of embodied long-horizon planning benchmarks that explicitly incorporate embodiment constraints makes it difficult to systematically evaluate the unique challenges they pose.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** OmniEVA is the first framework to dynamically integrate 2D and 3D inputs via taskconditioned feature selection, enabling versatile and executable embodied reasoning through two key ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Dynamic 3D Injection via Gated Routing Rather than applying 3D positional encoding uniformly for all tasks, we propose a Task-Adaptive Gated Router (TAGR) that selectively ...
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** This format enables precise object localization and descriptive annotation within a single image frame.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Left: The overall architecture of OmniEVA, featuring a novel task-adaptive gated router that dynamically incorporates 3D positional embeddings.
- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Examples of the Activation of Gated Router Task‐Adaptive Gated Router Sentence Transformer 384 concatenate MLP Network Gumbel Softmax Task Condition Scene Condition Plus 𝒈ൌ𝟎 𝒈ൌ𝟏 ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder with a learning ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into a sequence of discrete visual tokens, 2) ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| State/latent | OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components, vision, transformer | geometry, map, object/relationship state | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS) |
| Output/action | The model accepts a natural language instruction T, a sequence of RGB images or video frames (I1, I2, . . . , IN), and optionally, depth maps (D1, D2, . . . ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS) |
| Objective/outcome | Given a reward for the i-th response: ri,t(q, oi) = rformat i (oi) + racc i,t (q, oi) (11) 18 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 18 (A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |

## Main Claims and Actual Contribution

- 게이트로 3D 특징을 선택적으로 주입하고, 기구 조건에서 계획이 실행 가능한지 평가하는 보상을 후학습에 사용한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=6)
- 일반 2D 및 3D 추론 과제와 별개로, 학습에서 본 팔 길이와 새로운 팔 길이의 시뮬레이션 조건에서 계획 실행 성공률을 측정했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=10)

## Evaluation Scope

표 5의 OmniEVA-ER 성공률은 시뮬레이션에서 팔 길이가 학습에 등장한 조건 85.08%, 새로운 길이 80.52%다. 표 6의 실제 이동 로봇 두 대(팔 길이 75 cm와 70 cm)에서 측정한 결과는 별도로 보고했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/7b122d0a0dcb1a86ffa25ccba154652b-Paper-Conference.pdf#page=10)

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. First, the geometric adaptability gap: mod- els ...
- **p. 26 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Designed to overcome the limitations of traditional multimodal models-which primarily operate at the image-level or bounding box-level-it incorporates regional masks linked with precise language descriptions ...
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** To overcome these limitations, we introduce a 3D-aware planning framework that ingests sequential RGB-D observations and directly generates subgoals in continuous 3D coordinate space.
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Physical constraints, including object location, size, collision potential, must be considered, making this task highly relevant to the Mobile Placement (Easy) tasks. • Where2Approach: The ...
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** In addition, it incorporates critical physical constraints, including object dimensions, fit within the available space, and collision avoidance with other objects.
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The entire benchmark consists of 464 samples, including 200 generation tasks that require the model to output corresponding points, and 264 judgment tasks where the ...
- **p. 51 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Common-Sense Considerations: - A vacant area must not overlap any existing objects ... large enough to accommodate ... avoid edges or corners where objects might ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS)이다.
