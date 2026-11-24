# Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (54 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1126/scirobotics.ads5033.
> PDF retrieval source: https://arxiv.org/pdf/2410.21845. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / Science Robotics
- Authors: Jianlan Luo, Charles Xu, Jeffrey Wu, Sergey Levine
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, human-in-the-loop, real-world RL, dexterous manipulation, recovery
- Official paper: https://api.crossref.org/works/10.1126/scirobotics.ads5033
- Full-text retrieval: https://arxiv.org/pdf/2410.21845
- Code/Project: https://github.com/rail-berkeley/hil-serl
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (54 pages; PyMuPDF text; title-token overlap first two pages=1.0)


> Publication metadata update (2026-10-25): [Science Robotics 2025](https://www.science.org/doi/10.1126/scirobotics.ads5033), [publisher-deposited metadata](https://api.crossref.org/works/10.1126/scirobotics.ads5033). 아래 본문·페이지 근거는 기존 arXiv PDF review를 보존한다. Journal 본문 재정독이나 reading status 변경은 아니다.

## Why This Paper Is Here

실물 로봇에서 시연과 사람의 개입을 시각 기반 강화학습에 결합해 정밀 조작 정책을 개선한다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** Manipulation is one of the foundational problems in robotics, and achieving human-level performance on dynamic, dexterous manipulation tasks is a longstanding pursuit in the field ...
- **p. 1 / 1. Introduction - extractive body cue:** Reinforcement learning (RL) holds the promise of enabling autonomous acquisition of complex and dexterous robotic skills.
- **p. 1 / 1. Introduction - extractive body cue:** By learning through trial and error, an effective RL method should in principle be able to acquire highly proficient skills that are tailored to the ...
- **p. 1 / 1. Introduction - extractive body cue:** This could result in performance that not only exceeds that of hand-designed controllers but also surpasses human teleoperation.
- **p. 1 / 1. Introduction - extractive body cue:** However, realizing this promise in real-world settings has been challenging due to issues with sample complexity, assumptions (e.g., accurate reward functions), and optimization stability.
- **p. 1 / 1. Introduction - extractive body cue:** However, developing general-purpose vision-based methods that can efficiently acquire physically complex skills, with proficiency exceeding imitation learning and hand-designed controllers, has been comparatively difficult.
- **p. 1 / 1. Introduction - extractive body cue:** Our system, named Human-in-the-Loop SampleEfficient Robotic Reinforcement Learning (HIL-SERL), addresses the previously mentioned challenges by integrating a number of components that enable fast and highly ...

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** To assess the effectiveness of our system, we compare it against several state-of-the-art RL methods and conduct ablation studies to understand the contribution of each ...
- **p. 3 / 1. Introduction - extractive body cue:** In summary, our contributions demonstrate that with the appropriate system-level design choices, RL can effectively solve a wide range of dexterous and complex vision-based manipulation ...
- **p. 1 / 1. Introduction - extractive body cue:** However, developing general-purpose vision-based methods that can efficiently acquire physically complex skills, with proficiency exceeding imitation learning and hand-designed controllers, has been comparatively difficult.
- **p. 1 / 1. Introduction - extractive body cue:** This could result in performance that not only exceeds that of hand-designed controllers but also surpasses human teleoperation.
- **p. 2 / 1. Introduction - extractive body cue:** A subset of tasks considered in this paper, they include whipping out a Jenga block from its tower, flipping an object in a pan, assembling ...
- **p. 9 / 3.5. Training Process - extractive body cue:** Finally, we start the policy training process.
- **p. 9 / 3.5. Training Process - extractive body cue:** Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which can result in ...
- **p. 8 / 3.5. Training Process - extractive body cue:** This is approximately equivalent to 10 human trajectories, assuming each trajectory takes about 10 seconds.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | $\mathcal M=\{\mathcal S,\mathcal A,\rho,\mathcal P,r,\gamma\}$에서 관측 $s\in\mathcal S$의 예는 영상과 로봇의 고유수용감각이다. 행동 $a\in\mathcal A$의 예는 말단장치의 목표 트위스트(선속도·각속도)다. | 영상과 고유수용감각 | [§3.1 MDP 정의 · PDF 4쪽](https://arxiv.org/pdf/2410.21845v3#page=4) |
| State/latent | Robotic, reinforcement, learning, tasks, defined, MDP, where, state, observation, image, combination, robot | shared representation, embodiment/task identity와 data distribution | p. 4 (3.1. Preliminaries and Problem Statement), p. 5 (3.1. Preliminaries and Problem Statement), p. 5 (3.1. Preliminaries and Problem Statement) |
| Output/action | 카메라 영상과 로봇 고유수용감각으로 관측 공간 $\mathcal S$를 정한다. 행동 공간 $\mathcal A$와 저수준 제어기의 선택은 정책의 명령이 실제 로봇에 어떻게 적용되는지를 결정한다. | 말단장치 목표 트위스트 | [§3.1 관측·행동 공간 · PDF 5쪽](https://arxiv.org/pdf/2410.21845v3#page=5) |
| Objective/outcome | Additionally, we may collect extra data to address any false negative and false positive issues with the reward classifier. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 8 (3.5. Training Process), p. 8 (3.5. Training Process), p. 9 (3.5. Training Process) |

## Main Claims and Actual Contribution

- 시연, 실행 중 교정, 표본 효율적인 강화학습과 실물 시스템 설계를 하나의 학습 절차로 통합한다.
- 정밀 조립·동적 조작·양팔 협응에서 학습 시간, 작업 성공과 실행 속도를 기준 방법과 비교한다.

[저자 원문](https://arxiv.org/html/2410.21845)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (4.3. Experimental Results), p. 15 (4.3. Experimental Results) |
| Embodiment/environment | Each task also uses either a scripted robot motion or manually human reset to randomize the initial state of the task. | hardware/simulator version and reset protocol | p. 9 (4.1. Overview of Experiments), p. 9 (4.1. Overview of Experiments) |
| Dataset/benchmark | For all tasks, BC baselines were trained using HG-DAgger with the same number of episodes and interventions as RL. | role, split, size and leakage | p. 9 (4.1. Overview of Experiments), p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results), p. 13 (4.3. Experimental Results) |
| Metric | Figure 3: This diagram illustrates the process for training HIL-SERL. First, we tele-operate the robot to collect positive and negative samples and train a binary reward classifier. We then collect a small ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 17 (5. Result Analysis), p. 18 (5.1. Reliability of the Learned Policies) |
| Baseline/ablation | In the remainder of this section, we will first describe each task in detail, and present relevant results as well as comparisons to other state-of-the-art methods. | fair input/data/compute/action matching | p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results), p. 13 (4.3. Experimental Results) |

## Explicit Limitations and Failure Boundary

- **p. 21 / 6. Discussion - extractive body cue:** We also see some limitations of our approach.
- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** For all tasks, unless otherwise noted, we trained a binary classifier as reward detector, it takes images from wrist and/or side cameras as inputs, and ...
- **p. 18 / 5.1. Reliability of the Learned Policies - extractive body cue:** We argue this reliability comes from reinforcement learning's inherent ability to self-correct through policy sampling, allowing the agent to continuously improve by learning from both ...
- **p. 21 / 6. Discussion - extractive body cue:** We see a number of opportunities for future work.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Robustness evaluation for policies learned by our method. (A) RAM insertion under external perturbations, such as a moving motherboard. (B) Retrying behavior during ...
- **p. 14 / 4.3. Experimental Results - extractive body cue:** For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses.
- **p. 14 / 4.3. Experimental Results - extractive body cue:** Additionally, the intervention rate does not consistently decrease over time, indicating that the policy is not steadily improving.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 9 (3.5. Training Process)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (54 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, developing general-purpose vision-based methods that can efficiently acquire physically complex skills, with proficiency exceeding imitation learning and hand-designed controllers, has been comparatively difficult. (p. 1, 1. Introduction).
- **Actual contribution:** In summary, our contributions demonstrate that with the appropriate system-level design choices, RL can effectively solve a wide range of dexterous and complex vision-based manipulation tasks in the real world. (p. 3, 1. Introduction).
- **Evaluation boundary:** Table 1: Experiment results. (a) HIL-SERL against imitation learning baselines. (b) HIL-SERL against various other baselines. In this subsection, we present the experimental results for all the tasks mentioned above. ... (p. 13, Figure/Table caption).
- **Explicit failure boundary:** For all tasks, unless otherwise noted, we trained a binary classifier as reward detector, it takes images from wrist and/or side cameras as inputs, and predicts whether the current state ... (p. 9, 4.1. Overview of Experiments).
