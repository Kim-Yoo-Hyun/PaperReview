# Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b5c402bb7bd5e60bede6961d6fe39e-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2412.15109. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Yang Tian, Sizhe Yang, Jia Zeng, Ping Wang, Dahua Lin, Hao Dong, Jiangmiao Pang
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, inverse dynamics, world model, manipulation, Vision-Language-Action
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b5c402bb7bd5e60bede6961d6fe39e-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2412.15109
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Seer는 로봇의 미래 시각 상태를 예측하고 그 예측에 조건화한 역동역학으로 행동을 생성한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Current efforts to learn scalable policies in robotic manipulation primarily fall into two categories: one focuses on "action," which involves behavior cloning from extensive collections ...
- **p. 1 / ABSTRACT - extractive body cue:** This paper presents an end-to-end paradigm that predicts actions using inverse dynamics models conditioned on the robot's forecasted visual states, named Predictive Inverse Dynamics Models ...
- **p. 1 / ABSTRACT - extractive body cue:** By closing the loop between vision and action, the end-to-end PIDM can be a better scalable action learner.
- **p. 1 / ABSTRACT - extractive body cue:** In practice, we use Transformers to process both visual states and actions, naming the model Seer.
- **p. 1 / ABSTRACT - extractive body cue:** It is initially pretrained on large-scale robotic datasets, such as DROID, and can be adapted to realworld scenarios with a little fine-tuning data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, R3M (Nair et al., 2022) and MVP (Xiao et al., 2022) learn discriminative representations from large-scale video datasets such as Ego4D (Grauman et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our results further indicate superiority in long-horizon task completion, unseen scene generalization, and data efficiency.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a foresight token to predict future RGB images and an action token to estimate intermediate actions between current and predicted future observations.
- **p. 3 / 3 METHOD - extractive body cue:** Therefore, we propose conditional visual foresight ffore to effectively anticipate future visual representations.
- **p. 4 / 3 METHOD - extractive body cue:** Seer consists of three parts: Multi-Modal Encoder, Conditional Visual Foresight and Inverse Dynamics Prediction.
- **p. 5 / 3 METHOD - extractive body cue:** Our aim is to answer: 1) How does our method perform on challenging simulation benchmarks?
- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive body cue:** As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, action decoder and ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 4 / 3 METHOD - extractive body cue:** For language inputs, we first tokenize the text and then use a CLIP text encoder (Radford et al., 2021) to obtain text embeddings, which are ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and predicts the RGB images at the time step t+n, denoted ... | multi-view observation, language/task label과 action trajectory | p. 3 (3 METHOD), p. 15 (A.1 IMPLEMENTATION DETAILS) |
| State/latent | Seer, takes, input, goal, form, language, instructions, robot, states, along, historical, observations | shared representation, embodiment/task identity와 data distribution | p. 3 (3 METHOD), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| Output/action | Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay Cosine decay Training Epochs 30 (LIBERO & ... | dataset sample 또는 learned policy action | p. 15 (A.1 IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 3 (3 METHOD) |
| Objective/outcome | (3) The loss function Linv comprises the arm action loss Larm and the gripper action loss Lgripper Linv = Larm + λLgripper, (4) where Larm is a Smooth-L1 loss, Lgripper is a ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (3 METHOD), p. 8 (3 METHOD), p. 8 (3 METHOD) |

## Main Claims and Actual Contribution

- 하나의 트랜스포머에서 미래 관측 예측과 행동 예측을 함께 최적화하고 로봇 데이터 사전학습 후 목표 작업에 맞춘다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=5)
- LIBERO-LONG·CALVIN의 연속 작업과 실물 조작에서 정책을 비교하고 물체·조명 변화에 대한 결과를 보고한다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/e5b5c402bb7bd5e60bede6961d6fe39e-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |
| Embodiment/environment | LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, and LIBERO100. | hardware/simulator version and reset protocol | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Dataset/benchmark | We attribute marginal improvements in general manipulation tasks to the diversity of objects, tasks, scenes, and language instructions in OXE. | role, split, size and leakage | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 16 (A.5 CALVIN ABC-D EXPERIMENT DETAILS) |
| Metric | Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a Robotiq-2f-85 gripper and two RealSense D435i cameras. Right: We design four real-world manipulation tasks: ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 6 (Figure/Table caption) |
| Baseline/ablation | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures the average success rate across ten tasks. Seer ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 18 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) grasping the camera model, and (2) inserting successfully with no collision.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** Notably, both tasks require quite precise action predictions and collision-free interactions, showing our model's potential in high-precision and contact-rich tasks.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Specifically, [FRS] tokens are appended to extract representations for two views, and three [INV ] tokens are appended to predict actions across three steps, ensuring ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 16 (A.2 NETWORK ARCHITECTURE), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 4 (3 METHOD)이다.
