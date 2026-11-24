# SATA: Safe and Adaptive Torque-Based Locomotion Policies Inspired by Animal Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p124.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p124.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Li Peizhuo, Hongyi Li, Ge Sun, Jin Cheng, Xinrong Yang, Guillaume Bellegarda, Milad Shafiee Ashtiani, Yuhong Cao, Auke Ijspeert, Guillaume Adrien Sartoretti
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, safe locomotion, torque control
- Official paper: https://www.roboticsproceedings.org/rss21/p124.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p124.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

SATA는 관절 토크를 직접 출력하는 사족 보행 정책을 학습해 실제 로봇의 접촉 외란에 대응하게 한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p124.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Despite recent advances in learning-based con~ trollers for legged robots, deployments in human-centrie env ronments remain limited by safety concerns.
- **p. 1 / Abstract - extractive body cue:** Most of these approaches use position-based control, where policies output target joint angles that must be processed hy a low-level controller (e.g PD or impedance ...
- **p. 1 / Abstract - extractive body cue:** Although impressive results have been achieved in controlled real-world scenarios, these methods often struggle with compliance and adaptability when encountering environments or disturbances ‘unseen during ...
- **p. 1 / Abstract - extractive body cue:** Inspired by how animals achieve smooth and adaptive movements by controlling muscle extension and contraction, torque-based policies offer a promising alternative by enabling precise and ...
- **p. 1 / Abstract - extractive body cue:** In Principle, this approach facilitates more effective interactions
- **p. 1 / Abstract - extractive body cue:** However, challenges such as a highly nonlinear state ‘space and inefficient exploration during training have hindered their broader adoption, To address these limit
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, this simplicity limits the policy's capacity to explore fine-grained and dynamic behaviors, thereby reducing its adaptability and generalization to unseen challenges in real-world environments.

## Core Idea

- **p. 2 / 1. Iyrropuction - extractive body cue:** + Stable and Efficient Torque-Based Learning: We propose «novel framework for learning torque-based loco- ‘motion policies with a growth mechanism that gradually. unlocks torque limits, ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive body cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By directly controlling actuation in torque space, this approach enables finer interaction with the environment, leading to more dynamic and robust locomotion, Moreover. torque control ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** 1 of animals in nature, we propose a framework that addresses the challenges ‘of torque-based lecomosion learning achieving 2roshot sim-o-real tanser slong with exceptional compliance ...
- **p. 3 / 1. Iyrropuction - extractive body cue:** ‘To achieve robust and adaptive locomotion contro! in legged robots, we propose a bio-inspired neural architecture that em
- **p. 5 / A. Implementation of the Growth Mechanism - extractive body cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive body cue:** We utilize Proximal Policy Optimization (PPO) to train the control policy, The hyperparameters and neural network architecture are consistent with [33]. including a multilayer perceptron ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive body cue:** ‘Domain randomization is applied during training to simulate real-world variability. ‘The specific randomization settings are as follows: Added base mass: Randomly increased by up to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Learning-based controllers typically use position-based action spaces, where the policy directly outputs position com- ‘mands for the actuators. ‘These commands are subsequently converted to torque using a low-level (e... | proprioception, terrain/perception observation과 velocity command | p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet) |
| State/latent | Learning-based, controllers, typically, position-based, action, spaces, where, policy, directly, outputs, position, com- | body/contact state, foothold 또는 behavior mode | p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction) |
| Output/action | 1) Activation Model: Output by our policy network, the action signal a, first passes through the activation model [55]. | joint target, torque, footstep 또는 locomotion action | p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction), p. 3 (1. Iyrropuction) |
| Objective/outcome | Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives. | velocity/progress, stability, energy와 terrain generalization | p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING) |

## Main Claims and Actual Contribution

- 학습 초기에 사용할 수 있는 동작 능력을 제한했다가 점차 늘리는 성장 교육과정으로 토크 공간의 탐색을 돕는다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p124.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p124.pdf#page=6)
- 실물 밀기 외란과 부드러운 지면에서 안정성과 순응성을 시험해 토크 제어 정책의 대응 범위를 평가한다. [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p124.pdf#page=8) · [PDF 10쪽](https://www.roboticsproceedings.org/rss21/p124.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments) |
| Embodiment/environment | ‘To validate the effectiveness of our approach, we deployed it on a Unitree Go2 quadruped robot in real-world scenarios. | hardware/simulator version and reset protocol | p. 7 (B. Lab Level Experiments), p. 6 (A. Implementation of the Growth Mechanism) |
| Dataset/benchmark | During this disturbance (0.5 < ¢ < 1.58) the robot dynamically | role, split, size and leakage | p. 7 (B. Lab Level Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism) |
| Metric | Moreover, when comparing the cumulative reward of both scenarios under OOD velocity commands (vz = 1.8m/s) as in Fig. | definition, denominator, direction and uncertainty | p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 5 (A. Implementation of the Growth Mechanism) |
| Baseline/ablation | We also compared its performance against several baseline methods, including Unitree's built-in, MPC-based controller, | fair input/data/compute/action matching | p. 7 (B. Lab Level Experiments), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 1 Saco case - extractive body cue:** [Locomotion on wet slippery surfaces, showing both sucess (a) and failure (b), Even when the foot ofthe robot sip and fall down in Tile cases, ...
- **p. 9 / 1 Saco case - extractive body cue:** In contrast, Figure 11b shows a failure case, where the robot is given an abrupt command on the slippery surface.
- **p. 7 / A. Simulation Experiments - extractive body cue:** 2) Robustness to Single-Leg Failure: In this experiment, we simulate the failure of a single leg by abruptly reducing the maximum torque of its motor ...
- **p. 7 / A. Simulation Experiments - extractive body cue:** This dynamic redistribution of effort ensures continuous and stable locomotion even under single leg failures.
- **p. 8 / 4) Front eg sweep - extractive body cue:** 7, the robot's controller exhibited robust performance, successfully resisting these disturbances across all four legs ‘without overreacting.
- **p. 8 / 4) Front eg sweep - extractive body cue:** In the first subsection, we illustrate the compliance of our method during humanrobot interactions, while Sections V-B2 and V-B3 highlight its robustness against external disturbances.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive body cue:** Ablation study of the proposed framework. showing successful traning in green and failurofpremature convergence in red, SATA ts compared with varans that lack the Biomechanical ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 1 (1. Iyrropuction), p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), p. 5 (A. Implementation of the Growth Mechanism)이다.
