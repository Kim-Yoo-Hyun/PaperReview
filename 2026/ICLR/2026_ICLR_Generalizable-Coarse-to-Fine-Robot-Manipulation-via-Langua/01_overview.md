# Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/314129fede356d33eb7719d9edb01cc7-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/244660. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Jianshu Hu, Lidi Wang, Shujia Li, Yunpeng Jiang, Xiao Li, Paul Weng, Yutong Ban
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Imitation Learning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/314129fede356d33eb7719d9edb01cc7-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

CLAP는 언어 지시가 가리키는 3차원 키포인트로 작업 영역을 좁힌 뒤 정밀한 로봇팔 동작을 예측한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Hierarchical coarse-to-fine policy, where a coarse branch predicts a region of interest to guide a fine-grained action predictor, has demonstrated significant potential in robotic 3D ...
- **p. 1 / ABSTRACT - extractive body cue:** However, even augmented with pre-trained models, these hierarchical policies still suffer from generalization issues.
- **p. 1 / ABSTRACT - extractive body cue:** To enhance generalization to novel instructions and environment variations, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a framework that integrates three key components: 1) task ...
- **p. 1 / ABSTRACT - extractive body cue:** Through comprehensive experiments in simulation and on a real robot, we demonstrate its superior generalization capability.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, on GemBench, a benchmark designed for evaluating generalization, our approach achieves a 12% higher average success rate than the SOTA method while using only ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, scaling these methods to a broader range of real-world applications (e.g., industrial, service, or home robotics) requires enhancing both (G1) their generalization to environment ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** To mitigate this, we introduce two ideas.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation.
- **p. 5 / 4 METHOD - extractive body cue:** 4.1 COARSE TASK PLANNER Prior coarse-to-fine policies condition all actions within a trajectory on a single high-level task description, limiting compositional generalization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action. | image/video, language instruction, proprioception과 history | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD) |
| State/latent | fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images, outputs, addition | language-grounded task state와 action-policy context | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD) |
| Output/action | In addition to task decomposition done at the beginning, at every execution timestep, the VLM fθ is also exploited to predict both the step instruction ℓtk (used as a novel input of ... | continuous action, pose 또는 action chunk | p. 5 (4 METHOD), p. 6 (4 METHOD), p. 4 (3 BACKGROUND) |
| Objective/outcome | Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by training our model to first reason about ... | instruction following, task success, generalization과 latency | p. 6 (4 METHOD), p. 7 (4 METHOD) |

## Main Claims and Actual Contribution

- 복합 지시를 하위 과제로 나누고 VLM을 키포인트 예측에 맞게 학습해, 지역 3차원 표현을 쓰는 행동 모듈에 목표 영역을 전달한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=6)
- GemBench의 새로운 지시·환경 조건에서 비교하고, 실물에서는 과제별 시연 열 개로 훈련한 정책의 일반화를 평가했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/314129fede356d33eb7719d9edb01cc7-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS) |
| Embodiment/environment | It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | 5.2 REAL-WORLD EXPERIMENTS Experimental Setting We keep the training settings the same as in the simulation and list key modifications here. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% 50% 30% 40% 20% 50% 36.2% 50% put block in cup with same color ... | definition, denominator, direction and uncertainty | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et al., 2025b). ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.5 ADDITIONAL ABLATION STUDY - extractive body cue:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods fail consistently.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 5 (4 METHOD)이다.
