# PointVLA: Injecting the 3D World into Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.07511.
> PDF retrieval source: https://arxiv.org/pdf/2503.07511. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: Chengmeng Li, Junjie Wen, Yaxin Peng, Yan Peng, Yichen Zhu
- 저자 판본 — RA-L 출판사 서지는 저자 5명, 저자 공개 PDF 표제면은 6명이다. 저자는 게재 서지를 따랐고, 방법·소속은 6인 판본 기준이다. Feifei Feng은 해당 저자판에만 있다. [게재 서지](https://api.crossref.org/works/10.1109/lra.2026.3653303) · [저자판](https://arxiv.org/pdf/2503.07511#page=1)
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: VLA, Vision-Language Model, 3D Vision, Imitation Learning
- Official paper: https://arxiv.org/abs/2503.07511
- Full-text retrieval: https://arxiv.org/pdf/2503.07511
- Code/Project: https://pointvla.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

PointVLA는 기존 VLA의 동작 예측기에 점군 정보를 더해 관측된 3차원 형상을 조작에 이용한다. [PDF 1쪽](https://arxiv.org/pdf/2503.07511#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models excel at robotic tasks by leveraging large-scale 2D vision-language pretraining, but their reliance on RGB images limits spatial reasoning critical for real-world ...
- **p. 1 / Abstract - extractive body cue:** Retraining these models with 3D data is computationally prohibitive, while discarding existing 2D datasets wastes valuable resources.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.
- **p. 1 / Abstract - extractive body cue:** Our method freezes the vanilla action expert and injects 3D features via a lightweight modular block.
- **p. 1 / Abstract - extractive body cue:** To identify the most effective way of integrating point cloud representations, we conduct a skip-block analysis to pinpoint less useful blocks in the vanilla action ...
- **p. 2 / 1. Introduction - extractive body cue:** This represents a crucial limitation because humans perceive and interact with the world in three dimensions.
- **p. 2 / 1. Introduction - extractive body cue:** The lack of comprehensive 3D spatial information in training data hinders a robot's ability to develop a deep understanding of its environment.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** To circumvent these issues, we propose a paradigm that treats 3D point cloud data as a complementary conditioning signal rather than a primary input modality.
- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** However, as this is not the core novelty of our approach, we leave it for future discussion.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an addition operation to ...
- **p. 3 / 3. Methodology - extractive body cue:** Subsequently, an 'action expert' module translates the VLM's state information into robot actions.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** The vanilla action expert remains frozen, while the new point cloud representation is integrated into the action expert through a modular network.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | PointVLA Framework Vision-Language Model Action Expert Point Cloud Injector Robot Action Block_12 Block_13 Block_16 Block_1 Injection Block_1 Injection Block_2 Injection Block_5 Zero Linear Adapter Zero Linear Point Cloud Injector Zero ... | image/video, language instruction, proprioception과 history | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| State/latent | PointVLA, Framework, Vision-Language, Model, Action, Expert, Point, Cloud, Injector, Robot, Block_12, Block_13 | language-grounded task state와 action-policy context | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA) |
| Output/action | The VLM acts as the model's 'brain,' processing instructions and current visual input to understand the task state. | continuous action, pose 또는 action chunk | p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| Objective/outcome | First, the computational cost would be prohibitively high due to the required conditioning blocks. | instruction following, task success, generalization과 latency | p. 4 (3.2. Injecting Point Cloud into VLA), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip) |

## Main Claims and Actual Contribution

- 기존 행동 전문가를 고정하고, 일부 블록을 건너뛰었을 때의 변화를 분석해 점군 특징을 넣을 위치를 고른다. [PDF 3쪽](https://arxiv.org/pdf/2503.07511#page=3) · [PDF 5쪽](https://arxiv.org/pdf/2503.07511#page=5)
- 가벼운 추가 모듈을 학습한 정책을 시뮬레이션과 실물에서 2차원 관측 기반 조작 정책과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2503.07511#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2503.07511#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench) |
| Embodiment/environment | Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment. | hardware/simulator version and reset protocol | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment) |
| Dataset/benchmark | These tasks assess the model's capability to manage both independent and coordinated robot movements across diverse scenarios. | role, split, size and leakage | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment), p. 6 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking) |
| Metric | The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | definition, denominator, direction and uncertainty | p. 8 (4.6. Experimental Results on Simulation Bench), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking) |
| Baseline/ablation | Figure 6. Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. We set chunk size to 50 for all tasks. Baseline. In our experiments, we ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (4.1. Implementation Details), p. 7 (4.2. Few-Shot Multi-Tasking) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space to ...
- **p. 8 / 4.4. Real-vs-Photo Discrimination - extractive body cue:** Since the model believes the object is present but continuously fails to grasp it, it enters a repetitive grasping loop.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Furthermore, even increasing the model size (ScaleDP-1B) does not lead to significant improvement.
- **p. 8 / 4.5. Height Adaptability - extractive body cue:** Our observations show that conventional 2D-based VLA models, such as OpenVLA [25], DP [9], ScaleDP-1B [57], and DexVLA [46] all failed in this scenario.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This represents a crucial limitation because humans perceive and interact with the world in three dimensions. (p. 2, 1. Introduction).
- **Actual contribution:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models. (p. 2, 1. Introduction).
- **Evaluation boundary:** We show experimental results on the bottom table. sented in Table 6, where our method outperforms all baselines in this scenario. (p. 7, 4.2. Few-Shot Multi-Tasking).
- **Explicit failure boundary:** Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space to become entangled-an observation consistent with ... (p. 7, 4.2. Few-Shot Multi-Tasking).
