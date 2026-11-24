# RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2307.00595.
> PDF retrieval source: https://arxiv.org/pdf/2307.00595. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: Hao-Shu Fang, Hongjie Fang, Zhenyu Tang, Jirong Liu, Chenxi Wang, Junbo Wang, Haoyi Zhu, Cewu Lu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Dataset, multimodal sensing, robot manipulation, one-shot learning, cross-embodiment
- Official paper: https://arxiv.org/abs/2307.00595
- Full-text retrieval: https://arxiv.org/pdf/2307.00595
- Code/Project: https://rh20t.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2307.00595v2) 기준이다.

## Why This Paper Is Here

RH20T는 접촉이 많은 실물 조작에서 시각·힘·소리·로봇 행동을 수집하고 대응하는 사람 시연 및 언어 설명을 제공한다. [PDF 1쪽](https://arxiv.org/pdf/2307.00595v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A key challenge for robotic manipulation in open domains is how to acquire diverse and generalizable skills for robots.
- **p. 1 / Abstract - extractive body cue:** Recent progress in one-shot imitation learning and robotic foundation models have shown promise in transferring trained policies to new tasks based on demonstrations.
- **p. 1 / Abstract - extractive body cue:** This feature is attractive for enabling robots to acquire new skills and improve their manipulative ability.
- **p. 1 / Abstract - extractive body cue:** However, due to limitations in the training dataset, the current focus of the community has mainly been on simple cases, such as push or pick-place ...
- **p. 1 / Abstract - extractive body cue:** In reality, there are many complex skills, some of which may even require both visual and tactile perception to solve.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Firstly, there is a lack of large and diverse robotic manipulation datasets in this field [B]], despite the community's long-standing eagerness for such datasets.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These challenges include the arduous task of configuring diverse robot platforms, creating varied environments, and gathering manipulation trajectories, which require significant effort and resources.

## Core Idea

- **p. 3 / III. RH20T DATASET - extractive body cue:** We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community.
- **p. 3 / III. RH20T DATASET - extractive body cue:** [TM1 c) Scale: Our dataset consists of over 110,000 robot sequences and an equal number of human sequences, with more than 50 million images collected ...
- **p. 3 / III. RH20T DATASET - extractive body cue:** To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in ...
- **p. 1 / Abstract - extractive body cue:** Each sequence in the dataset includes visual, force, audio, and action information.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these control methods are inefficient and pose safety risks when the robot engages in rich-contact interactions with the environment.
- **p. 3 / Dataset - extractive body cue:** #Traj. #Skills #Robots Human Demo Contact Rich Depth Sensing Camera Calib.
- **p. 4 / 200 Hz - extractive body cue:** Different force-torque sensors are tared carefully.
- **p. 4 / 200 Hz - extractive body cue:** The coordinate frame of all robots and force-torque sensors are aligned.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Proprioception encompasses joint angles/torques, end-effector Cartesian pose and gripper states. | multi-view observation, language/task label과 action trajectory | p. 3 (III. RH20T DATASET), p. 1 (Abstract) |
| State/latent | Proprioception, encompasses, joint, angles/torques, end-effector, Cartesian, pose, gripper, states, sequence, dataset, includes | shared representation, embodiment/task identity와 data distribution | p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Output/action | Each sequence in the dataset includes visual, force, audio, and action information. | dataset sample 또는 learned policy action | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (III. RH20T DATASET) |
| Objective/outcome | Properties of RH20T RH20T is designed with the objective of enabling general robotic manipulation, which means that the robot can perform various skills based on a task description, typically a human demonstration ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- 서로 다른 로봇·카메라의 좌표계와 센서를 보정해 다양한 관측을 같은 행동 기록에 연결한다. [PDF 3쪽](https://arxiv.org/pdf/2307.00595v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2307.00595v2#page=4)
- RH20T로 사전학습한 ACT를 새 환경에서 수집한 시연으로 미세조정한 뒤 실물 블록 옮기기에서 도달·파지·배치 성공률을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2307.00595v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2307.00595v2#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are synchronized in the temporal domain. the manipulation sequences from our ... | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET) |
| Dataset/benchmark | Additionally, the robot model is rendered in the scene based on the joint angles recorded in our dataset. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | We divide the task into 3 stages, namely whether the robot can reach the block, grasp it and place it on the weight, and measure the success rate at each stage. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. DISCUSSION AND CONCLUSION - extractive body cue:** The current limitations of this paper are that (i) the cost of data collection is expensive and (ii) the potential of robotic foundation models is ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These results demonstrate that leveraging the diverse training data from our dataset enhances the adaptability and robustness of the robotic manipulation model.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 3 (Dataset)이다.
