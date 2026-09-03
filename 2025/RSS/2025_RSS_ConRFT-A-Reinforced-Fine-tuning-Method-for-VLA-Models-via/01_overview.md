# ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p019.html.
> PDF retrieval source: https://arxiv.org/pdf/2502.05450. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Reinforcement Learning, human interventions, consistency policy, real-world manipulation, fine-tuning
- Official paper: https://www.roboticsproceedings.org/rss21/p019.html
- Full-text retrieval: https://arxiv.org/pdf/2502.05450
- Code/Project: https://cccedric.github.io/conrft/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.를 문제로 두고, Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency policy through ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based ...
- **p. 1 / Abstract - extractive body cue:** In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.
- **p. 1 / Abstract - extractive body cue:** In the online stage, the VLA model is further finetuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In the subsequent online stage, we solve two challenges of sample efficiency and real-world safety requirements by exploiting task-specific rewards with CPQL [18] under human ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To leverage the benefits of RL-based techniques for efficiently fine-tuning VLA models with online interaction data, we propose a reinforced fine-tuning (RFT) approach consisting of ...
- **p. 2 / IV. METHOD - extractive body cue:** The proposed pipline ConRFT consists of two stages: offline fine-tuning followed by online fine-tuning to optimize robotic policies, as shown in Fig.
- **p. 3 / IV. METHOD - extractive body cue:** To address this issue, we propose augmenting the offline training process by incorporating a BC loss.
- **p. 3 / IV. METHOD - extractive body cue:** Motivated by combining the BC loss with Q guidance under a consistency-based objective [18], we introduce Cal-ConRFT in the offline stage.
- **p. 4 / IV. METHOD - extractive body cue:** As a result, we use a standard Q loss for online critic updating: Lonline Q (θ) = E(s,a,s′)∼(D∪R)[(Qθ(s, a) -BπQ(s, a))2] (4) The consistency-based training ...
- **p. 4 / IV. METHOD - extractive body cue:** The consistency policy is a diffusion-model-based policy [46] that learns to map random actions sampled from the unit Gaussian to generate actions drawn from the ...
- **p. 5 / IV. METHOD - extractive body cue:** Specifically, HIL learning allows for timely interventions by a human operator who can provide corrective actions during the exploration process, which will then take over ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To address these issues, we formulate each robotic task as a Markov Decision Process (MDP), where the goal of RL is to find the optimal policy in the MDP, M = (S, ... | image/video, language instruction, proprioception과 history | p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD) |
| State/latent | address, issues, formulate, robotic, task, Markov, Decision, Process, MDP, where, goal, find | language-grounded task state와 action-policy context | p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD), p. 2 (III. PROBLEM SETUP AND PRELIMINARIES) |
| Output/action | The consistency policy is a diffusion-model-based policy [46] that learns to map random actions sampled from the unit Gaussian to generate actions drawn from the expert action distribution conditioned on the current ... | continuous action, pose 또는 action chunk | p. 4 (IV. METHOD), p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD) |
| Objective/outcome | The BC loss directly minimizes the difference between the actions generated by the policy and those from the demonstrations. | instruction following, task success, generalization과 latency | p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To leverage the benefits of RL-based techniques for efficiently fine-tuning VLA models with online interaction data, we propose a reinforced fine-tuning (RFT) approach consisting of ...
- **p. 2 / IV. METHOD - extractive body cue:** The proposed pipline ConRFT consists of two stages: offline fine-tuning followed by online fine-tuning to optimize robotic policies, as shown in Fig.
- **p. 3 / IV. METHOD - extractive body cue:** To address this issue, we propose augmenting the offline training process by incorporating a BC loss.
- **p. 3 / IV. METHOD - extractive body cue:** Motivated by combining the BC loss with Q guidance under a consistency-based objective [18], we introduce Cal-ConRFT in the offline stage.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** Meanwhile, RLDG achieves higher success rates using optimal data collected from RL policies, suggesting that the consistency of these RL-collected data can improve the final ...
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS) |
| Embodiment/environment | This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world tasks, displayed as a running average over ... | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS) |
| Dataset/benchmark | This stability and performance highlight the effectiveness of our approach in overcoming the limitations of existing fine-tuning methods in real-world robotic applications. | role, split, size and leakage | p. 6 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 5 (V. EXPERIMENT AND RESULTS) |
| Metric | This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and stable policy improvement with a small set ... | definition, denominator, direction and uncertainty | p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS) |
| Baseline/ablation | For the online stage, we compared HIL-ConRFT with multiple baselines, including HG-DAgger [19] that incorporates human corrections to fine-tune the policy through supervised learning, PA-RL [14] that optimized actions through a policy-a ... | fair input/data/compute/action matching | p. 6 (V. EXPERIMENT AND RESULTS), p. 6 (Figure/Table caption), p. 5 (V. EXPERIMENT AND RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. LIMITATIONS - extractive body cue:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant policy improvement and even experiences a performance ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** They also show the limitations of supervised methods in handling sub-optimal data and efficient policy exploration.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** However, it fails to improve the policy performance in contact-rich tasks that require precise, careful manipulation, such as Insert Wheel.
- **p. 8 / V. EXPERIMENT AND RESULTS - extractive body cue:** This indicates that simply adding more human-collected demonstrations with supervised learning does not necessarily guarantee higher performance due to the inconsistent and sub-optimal actions inherent ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.를 문제로 두고, Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency policy through ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency ... (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and stable policy improvement with a ... (p. 8, V. EXPERIMENT AND RESULTS).
- **Explicit failure boundary:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. (p. 8, VI. LIMITATIONS).
