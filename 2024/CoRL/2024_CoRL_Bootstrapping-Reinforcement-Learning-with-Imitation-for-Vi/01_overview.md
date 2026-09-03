# Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=bt0PX0e4rE.
> PDF retrieval source: https://arxiv.org/pdf/2403.12203. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, aerial robotics, Reinforcement Learning, Imitation Learning
- Official paper: https://openreview.net/forum?id=bt0PX0e4rE
- Full-text retrieval: https://arxiv.org/pdf/2403.12203
- Code/Project: https://bootstrap-rl-with-il.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, learning from only visual inputs introduces a range of distinct challenges.를 문제로 두고, Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence of gates using solely gate corners or RGB ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1 Introduction - extractive body cue:** Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence of ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 2 / 1 Introduction - extractive body cue:** Although we validate our method using vision-based drone racing, our approach does not rely on task-specific adaptations that might limit its applicability to other robotic ...
- **p. 4 / 3 Methodology - extractive body cue:** To address this, we propose an algorithm that conditions exploration and network updates on the policy's performance, as shown in Algorithm 1.
- **p. 1 / 1 Introduction - extractive body cue:** Visuomotor policy learning enables robots to perform complex tasks by directly mapping visual information into action.
- **p. 15 / A.8 Unobservable States Illustration - extractive body cue:** The quantitative results, shown in 6, clearly indicate that our approach greatly improves policy performance, achieving lap times within a difference of 0.05s to that ...
- **p. 13 / A.6 Performance w/ Diff. History Length - extractive body cue:** More importantly, in all of these cases, our approach achieves both better performance and success rate.
- **p. 7 / 3 Methodology - extractive body cue:** Firstly, it is noteworthy that the direct RL from corners or pixels achieves a 0% success rate in all three tracks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, learning from only visual inputs introduces a range of distinct challenges.를 문제로 두고, Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence of gates using solely gate corners or RGB ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 4 (3 Methodology), p. 4 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
