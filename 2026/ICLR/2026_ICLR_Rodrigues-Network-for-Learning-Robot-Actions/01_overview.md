# Rodrigues Network for Learning Robot Actions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/eb9b18ccb76a1156af5779ffdca1d91f-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2506.02618. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Jialiang Zhang, Haoran Geng, Yang You, Congyue Deng, Pieter Abbeel, Jitendra Malik, Leonidas Guibas
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, kinematics, action representation, Imitation Learning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/eb9b18ccb76a1156af5779ffdca1d91f-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2506.02618
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

RodriNet은 순기구학의 회전·연결 구조를 학습 가능한 연산에 반영해 관절형 시스템의 행동과 형상을 표현한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eb9b18ccb76a1156af5779ffdca1d91f-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Understanding and predicting articulated actions is important in robot learning.
- **p. 1 / ABSTRACT - extractive body cue:** However, common architectures such as MLPs and Transformers lack inductive biases that reflect the underlying kinematic structure of articulated systems.
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into ...
- **p. 1 / ABSTRACT - extractive body cue:** Building on this operator, we design the Rodrigues Network (RodriNet), a novel neural architecture specialized for processing actions.
- **p. 1 / ABSTRACT - extractive body cue:** We evaluate the expressivity of our network on two synthetic tasks on kinematic and motion prediction, showing significant improvements compared to standard backbones.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This gap raises our central question: Can we design a neural network for action learning that embeds articulated kinematics as an inductive bias?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We study the problem of understanding and predicting the actions of articulated actors.

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, our method derive a learnable operator from forward kinematics, thereby making the network kinematics-aware while maintaining the flexibility to learn high-level features.
- **p. 5 / 3.1 BACKGROUND - extractive body cue:** To achieve that, we propose a basic building block called Rodrigues Block (Figure 2), which comprises the following three components: (1) a Rodrigues Layer for ...
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** The global token enables the network to store and propagate task-wide information that is not tied to any specific joint or link.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, we showcase our effectiveness in realistic robot-learning scenarios with imitation learning on 5 robot manipulation tasks.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Other methods apply Cartesian-space loss functions after computing forward kinematics on network outputs (Pavllo et al., 2020; Jiang et al., 2021; Liu et al., 2020), ...
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** Refer to Section B of the supplementary for details on computing the first-layer features and task-specific outputs.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We then convert it into a neural operator by treating the state-dependent parameters as input features, and relaxing the state-independent coefficients into optimizable weights. | observation history와 expert trajectory/action | p. 2 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND) |
| State/latent | then, convert, neural, operator, treating, state-dependent, parameters, input, features, relaxing, state-independent, coefficients | behavior policy와 temporal action context | p. 2 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND) |
| Output/action | Based on this, we construct our Neural Rodrigues Operator for one single joint by replacing these fixed coefficients with learnable weights W bias, W cos, W sin ∈R4×4, resulting in: F out ... | predicted action 또는 action chunk | p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND) |
| Objective/outcome | Therefore, we can abbreviate Equation 2 as Pcj = Ppj(Tj ˜R(ˆωj, θj)), where ˜R(ˆωj, θj) ∈R4×4 is the homogeneous matrix of the rotation. | imitation error, task success, robustness와 compounding error | p. 3 (3.1 BACKGROUND), p. 3 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND) |

## Main Claims and Actual Contribution

- 회전축을 따르는 Rodrigues 연산을 학습 가능한 특징 변환으로 일반화하고 이를 블록으로 쌓는다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eb9b18ccb76a1156af5779ffdca1d91f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eb9b18ccb76a1156af5779ffdca1d91f-Paper-Conference.pdf#page=5)
- 합성 운동 예측 외에 Diffusion Policy를 쓰는 모방학습과 단일 영상의 3차원 손 복원에서 기존 신경망과 비교한다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eb9b18ccb76a1156af5779ffdca1d91f-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eb9b18ccb76a1156af5779ffdca1d91f-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Embodiment/environment | In real-world robot learning scenarios, neural backbones typically process observations in 3D Cartesian space (e.g., point clouds) and output control commands as target joint angles. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Dataset/benchmark | We evaluate our Rodrigues Network on a set of different tasks, ranging from forward kinematics and motion prediction (Section 5.1), to imitation learning in robotics (Section 5.2), to hand pose estimation for ... | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | Performance is measured by running 100 evaluation rollouts in simulation, and all models are trained with 5 random seeds to report the mean and standard deviation of success rates. | definition, denominator, direction and uncertainty | p. 8 (5 EXPERIMENTS), p. 9 (Figure/Table caption), p. 6 (5 EXPERIMENTS) |
| Baseline/ablation | Compared to the strongest baseline, HaMeR, our approach outperforms both the results reported in the original paper and our reproduced implementation. | fair input/data/compute/action matching | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and predicts the corresponding ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)이다.
