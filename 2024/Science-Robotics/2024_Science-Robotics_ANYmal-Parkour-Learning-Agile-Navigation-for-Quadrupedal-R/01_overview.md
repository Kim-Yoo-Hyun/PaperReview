# ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.14874.
> PDF retrieval source: https://arxiv.org/pdf/2306.14874. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / Science Robotics
- Authors: David Hoeller, Nikita Rudin, Dhionis Sako, Marco Hutter
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, parkour, Navigation
- Official paper: https://arxiv.org/abs/2306.14874
- Full-text retrieval: https://arxiv.org/pdf/2306.14874
- Code/Project: https://anymal-parkour.ethz.ch/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

ANYmal Parkour는 사족 로봇이 여러 장애물을 연속으로 넘도록 학습된 이동 기술과 기술 선택 정책을 결합한다. [PDF 1쪽](https://arxiv.org/pdf/2306.14874v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Performing agile navigation with four-legged robots is a challenging task due to the highly dynamic motions, contacts with various parts of the robot, and the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a fully-learned approach to train such robots and conquer scenarios that are reminiscent of parkour challenges.
- **p. 1 / Abstract - extractive body cue:** The method involves training advanced locomotion skills for several types of obstacles, such as walking, jumping, climbing, and crouching, and then using a high-level policy ...
- **p. 1 / Abstract - extractive body cue:** Thanks to our hierarchical formulation, the navigation policy is aware of the capabilities of each skill, and it will adapt its behavior depending on the ...
- **p. 1 / Abstract - extractive body cue:** Additionally, a perception module is trained to reconstruct obstacles from highly occluded and noisy sensory data and endows the pipeline with scene understanding.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Method overview This work aims to solve the above-mentioned challenges and proposes a method to perform agile navigation with a quadrupedal robot in parkour-like settings ...

## Core Idea

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single ...
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** To the best of our knowledge, we propose the first system that can perform agile navigation with a quadrupedal robot in such challenging scenarios without ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We can summarize our contributions as follows:
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contributions In our experimental validation, we demonstrate the system's ability to solve the problem autonomously, resulting in behaviors not shown before with such platforms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This discipline requires years of practice to develop the necessary competencies, intuitions, and reflexes and is considered particularly dangerous.
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** This leads to the natural progression where the policy first learns to climb using its knees and then starts using its feet instead when possible. ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As input, the policies receive the current proprioceptive state, a local map of the surrounding terrain, an intermediate command, and output position commands to the motors. | proprioception, terrain/perception observation과 velocity command | p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that) |
| State/latent | input, policies, receive, current, proprioceptive, state, local, surrounding, terrain, intermediate, command, output | body/contact state, foothold 또는 behavior mode | p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS) |
| Output/action | While these approaches produce a separate representation, the exteroceptive measurements can also be directly provided as input to the policy [8], [40]. | joint target, torque, footstep 또는 locomotion action | p. 5 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS) |
| Objective/outcome | The occupancy output is trained using a binary cross-entropy loss, while the centroids are trained using the Euclidean distance to the ground truth. | velocity/progress, stability, energy와 terrain generalization | p. 14 (IV. MATERIALS AND METHODS), p. 14 (IV. MATERIALS AND METHODS), p. 4 (3) We develop a neural terrain reconstruction method that) |

## Main Claims and Actual Contribution

- 가려지고 잡음이 있는 관측에서 장애물을 복원하고 상위 정책이 지형과 하위 기술의 능력에 맞는 경로·기술을 고른다. [PDF 4쪽](https://arxiv.org/pdf/2306.14874v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2306.14874v1#page=5)
- 실제 로봇에서 장애물 연속 통과를 시연하고 대체 경로가 있을 때 기술 선택과 주행 경로가 어떻게 달라지는지 평가한다. [PDF 6쪽](https://arxiv.org/pdf/2306.14874v1#page=6) · [PDF 9쪽](https://arxiv.org/pdf/2306.14874v1#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Embodiment/environment | The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach a target across different arrangements of randomized ... | hardware/simulator version and reset protocol | p. 5 (II. RESULTS), p. 5 (II. RESULTS) |
| Dataset/benchmark | The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach a target across different arrangements of randomized ... | role, split, size and leakage | p. 5 (II. RESULTS), p. 5 (II. RESULTS) |
| Metric | Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill for obstacles ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 5 (II. RESULTS), p. 5 (II. RESULTS) |
| Baseline/ablation | The skill learns to turn on the spot in tight spaces and is more capable in such scenarios compared to other skills. | fair input/data/compute/action matching | p. 5 (II. RESULTS), p. 11 (Figure/Table caption), p. 5 (II. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 12 / A. Current Limitations - extractive body cue:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires ...
- **p. 12 / A. Current Limitations - extractive body cue:** We develop a specific curriculum to overcome this limitation.
- **p. 5 / II. RESULTS - extractive body cue:** 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch the fall of the robot during the ...
- **p. 5 / II. RESULTS - extractive body cue:** At this location, it has to perform precise foothold placement to pass the last step and prepare for the jump, despite the out-of-distribution scenario for ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** We can summarize our contributions as follows: (p. 3, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ... (p. 1, I. INTRODUCTION).
