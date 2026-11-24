# Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/xing25a.html.
> PDF retrieval source: https://arxiv.org/pdf/2403.12203. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: Jiaxu Xing, Angel Romero, Leonard Bauersfeld, Davide Scaramuzza
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, aerial robotics, Reinforcement Learning, Imitation Learning
- Official paper: https://proceedings.mlr.press/v270/xing25a.html
- Full-text retrieval: https://arxiv.org/pdf/2403.12203
- Code/Project: https://bootstrap-rl-with-il.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 시뮬레이터의 특권 상태로 학습한 레이싱 드론 교사 정책을 영상 기반 학생 정책의 출발점으로 사용한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/xing25a/xing25a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning visuomotor policies for agile quadrotor flight presents significant difficulties, primarily from inefficient policy exploration caused by highdimensional visual inputs and the need for precise ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose a novel approach that combines the performance of Reinforcement Learning (RL) and the sample efficiency of Imitation Learning (IL) ...
- **p. 1 / Abstract - extractive body cue:** While RL provides a framework for learning high-performance controllers through trial and error, it faces challenges with sample efficiency and computational demands due to the ...
- **p. 1 / Abstract - extractive body cue:** Conversely, IL efficiently learns from visual expert demonstrations, but it remains limited by the expert's performance and state distribution.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, our policy learning framework integrates the strengths of both approaches.
- **p. 1 / 1 Introduction - extractive body cue:** However, learning from only visual inputs introduces a range of distinct challenges.
- **p. 2 / 1 Introduction - extractive body cue:** However, IL faces several challenges, including the significant issue of covariate shift.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence of ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 2 / 1 Introduction - extractive body cue:** Although we validate our method using vision-based drone racing, our approach does not rely on task-specific adaptations that might limit its applicability to other robotic ...
- **p. 4 / 3 Methodology - extractive body cue:** To address this, we propose an algorithm that conditions exploration and network updates on the policy's performance, as shown in Algorithm 1.
- **p. 1 / 1 Introduction - extractive body cue:** Visuomotor policy learning enables robots to perform complex tasks by directly mapping visual information into action.
- **p. 4 / 3 Methodology - extractive body cue:** In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses corresponding perceptual observations ...
- **p. 7 / 3 Methodology - extractive body cue:** For (i) we train the RL policy using RGB images with 10M samples and our approach and baseline (ii) we use 5M data samples for ...
- **p. 7 / 3 Methodology - extractive body cue:** Training Effectiveness with different RL configurations To demonstrate the effectiveness of our visuomotor policy learning approach, we ablate the training performance of our approach with ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses corresponding perceptual observations and action outputs. | proprioception, reference pose/motion, visual or language command | p. 4 (3 Methodology), p. 3 (3 Methodology) |
| State/latent | case, state-based, teacher, policy, executed, fixed, number, steps, generating, dataset, encompasses, corresponding | whole-body pose, balance/contact state와 skill/mode | p. 4 (3 Methodology), p. 3 (3 Methodology), p. 8 (3 Methodology) |
| Output/action | The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output Collective Thrust and Bodyrates control Stage I: State-based RL ... | joint/whole-body action, motion target 또는 task trajectory | p. 3 (3 Methodology), p. 8 (3 Methodology), p. 4 (3 Methodology) |
| Objective/outcome | The drone racing task can be formulated as an optimization problem where the objective is to minimize the time required to navigate through a predefined sequence of gates [35], as illustrated in ... | tracking, balance, skill/task success와 recovery | p. 3 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology) |

## Main Claims and Actual Contribution

- 모방학습으로 교사의 행동을 학생에게 전달한 뒤 강화학습으로 학생 정책을 추가 조정한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/xing25a/xing25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/xing25a/xing25a.pdf#page=4)
- 시뮬레이션과 실제 경주 코스에서 경로·비행 성능을 비교해 모방만 사용한 경우와 추가 강화학습의 차이를 측정한다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/xing25a/xing25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/xing25a/xing25a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (A.8 Unobservable States Illustration), p. 13 (A.6 Performance w/ Diff. History Length) |
| Embodiment/environment | Realworld Experiments To demonstrate policy improvements, we validated our policy in real-world scenarios using Hardware-in-the-Loop (HIL) simulations, aided by a VICON motion capture system for perceptual inputs. | hardware/simulator version and reset protocol | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Dataset/benchmark | 4 in both simulation and real-world experiments, aiming to achieve optimal and smooth performance for the state-based policy. | role, split, size and leakage | p. 8 (3 Methodology), p. 8 (3 Methodology), p. 12 (A.2 Reward Formulations for RL Trainings), p. 5 (3 Methodology) |
| Metric | We use three evaluation metrics: success rate (SR), mean-gate-passing-error (MGE), and lap time (LT). | definition, denominator, direction and uncertainty | p. 5 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology) |
| Baseline/ablation | Table 5: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more history observations, that the policy improvement will get improved. Notably, ... | fair input/data/compute/action matching | p. 14 (Figure/Table caption), p. 7 (3 Methodology), p. 8 (3 Methodology) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3 Methodology - extractive body cue:** To simulate real-world scenarios, we include domain randomization such as gate scales, pixel position noise (10 pixels in both (u, v) in a 1280 × ...
- **p. 8 / 3 Methodology - extractive body cue:** To simulate realworld uncertainties, we conducted two experiments: i) random frame blackouts to mimic sensor failures like communication loss, and ii) random positional jumps during ...
- **p. 8 / 3 Methodology - extractive body cue:** One limitation is that our current setup is tested in the controlled lab settings, it will likely fail in an in-the-wild setup.
- **p. 6 / 3 Methodology - extractive body cue:** 4.2 Experiment Results Performance comparison to baseline approaches One inherent limitation of the student-teacher IL framework is to infer reasonable actions from partial information.
- **p. 13 / A.3 Training Configurations - extractive body cue:** Reward Name Symbol Value Progress reward λ1 0.5 Perception-aware reward λ2 0.025 Command smoothness reward λ3 2e-4 Body rate penalty λ4 5e-4 Gate passing reward ...
- **p. 5 / 3 Methodology - extractive body cue:** We believe this approach is easily generalizable to other platforms as it does not require task-specific information.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Long exposure image of real-world flights shows a blue trajectory for our approach and a red one for the imitation policy. Training on ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Methodology)이다.
