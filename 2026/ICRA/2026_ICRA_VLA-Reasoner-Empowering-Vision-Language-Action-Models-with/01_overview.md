# VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html.
> PDF retrieval source: https://arxiv.org/pdf/2509.22643. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html
- Full-text retrieval: https://arxiv.org/pdf/2509.22643
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, current VLAs also face critical limitations.를 문제로 두고, Our contributions are summarized as follows: • We propose a plug-in framework named VLA-Reasoner that empowers VLAs with structured reasoning to address their incremental deviations during deployment. • We adapt a modified ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action models (VLAs) achieve strong performance in general robotic manipulation tasks by scaling imitation learning.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs are limited to predicting short-sighted next-action, which struggle with long-horizon trajectory tasks due to incremental deviations.
- **p. 1 / Abstract - extractive body cue:** To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time ...
- **p. 1 / Abstract - extractive body cue:** Specifically, VLA-Reasoner samples and rolls out possible action trajectories where involved actions are rationales to generate future states via a world model, which enables VLA-Reasoner ...
- **p. 1 / Abstract - extractive body cue:** We further leverage Monte Carlo Tree Search (MCTS) to improve search efficiency in large action spaces, where stepwise VLA predictions seed the root.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current VLAs also face critical limitations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce a KDE-based confidence distribution that samples candidates in MCTS from an expert-like prior, reducing redundant VLA queries while preserving exploration.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • We propose a plug-in framework named VLA-Reasoner that empowers VLAs with structured reasoning to address their incremental deviations ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce a KDE-based confidence distribution that samples candidates in MCTS from an expert-like prior, reducing redundant VLA queries while preserving exploration.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This raises a core question: "Can VLAs explore the longhorizon future influence of actions at test time, and decide the optimal action?" To this end, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method delivers consistent gains in both simulation and on real robots.
- **p. 3 / III. METHOD - extractive body cue:** In this section, we first show the pipeline of our framework as Figure 2, and then present the formulation of our work (Section III-A).
- **p. 4 / III. METHOD - extractive body cue:** The whole process constructs an independent Monte Carlo Tree of current robot states as we use a world model to dictate the transitions.
- **p. 4 / III. METHOD - extractive body cue:** With a dataset of actions {a1, a2, . . . , an}, the KDE can be formulated as: πKDE θ (a) = 1 N N ...
- **p. 3 / III. METHOD - extractive body cue:** The simulation formulates: si+1 = W(ai, si) (3) where the world model rolls out the next state si+1 under a given action ai and current ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input : VLA proposal aVLA t , current state st Output : final action at 1 Init: Create root node o(0) with s(0) ←st, a(0) ←aVLA t . ; 2 for depth ... | image/video, language instruction, proprioception과 history | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | Input, VLA, proposal, aVLA, current, state, Output, final, action, Init, Create, root | language-grounded task state와 action-policy context | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Problem Statement VLAs aim to generalize robot manipulation by mapping multimodal inputs (states from the environment st, language instructions of the task l) to actions aV LA t . | continuous action, pose 또는 action chunk | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective/outcome | Input : VLA proposal aVLA t , current state st Output : final action at 1 Init: Create root node o(0) with s(0) ←st, a(0) ←aVLA t . ; 2 for depth ... | instruction following, task success, generalization과 latency | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • We propose a plug-in framework named VLA-Reasoner that empowers VLAs with structured reasoning to address their incremental deviations ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce a KDE-based confidence distribution that samples candidates in MCTS from an expert-like prior, reducing redundant VLA queries while preserving exploration.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This raises a core question: "Can VLAs explore the longhorizon future influence of actions at test time, and decide the optimal action?" To this end, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method delivers consistent gains in both simulation and on real robots.
- **p. 3 / III. METHOD - extractive body cue:** In this section, we first show the pipeline of our framework as Figure 2, and then present the formulation of our work (Section III-A).
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** As the success rate is the primary metric of evaluation in two benchmarks, our method improves the absolute task-set performance on OpenVLA-SFT by 5% on ...
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** It averages an improvement of OpenVLA with an absolute gain of 19%, a relative gain of 86.4%, as the baseline shows a poor performance of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In real-world deployments, our approach achieves higher success rates compared to popular VLAs fine-tuned with a few demonstrations, indicating stronger generalization and adaptivity at test ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Embodiment/environment | Deployment in Real-world Environment a) Experiment Setup: To evaluate the performance of the VLA-Reasoner in the real world with real robots. | hardware/simulator version and reset protocol | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (2 Cups) |
| Dataset/benchmark | For Q1, we conduct experiments in 2 simulation environment (LIBERO [39] and SimplerEnv [40]) with 8 specific tasks based on 3 popular general robot policies. | role, split, size and leakage | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (2 Cups), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 3 (III. METHOD) |
| Metric | Baseline Gaussian Noise KDE (Ours) 80.0% 85.0% 90.0% 95.0% 100.0% Success Rate (%) 82.0% 85.0% 91.5% Strategies of Action Sampling Baseline Token Reward Image Reward (Ours) 82.0% 87.0% 91.5% Methods of Reward ... | definition, denominator, direction and uncertainty | p. 7 (2 Cups), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Baseline/ablation | It is noticeable that compared to those variants developed from OpenVLA, our plug-and-play method can directly improve the performance of the backbone to the state-of-the-art level without large-scale and skillful post-training, which ... | fair input/data/compute/action matching | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSION - extractive body cue:** We identified a core limitation of current short-sighted VLA deployment and introduced VLA-Reasoner, a plug-in framework that injects test-time reasoning into off-the-shelf VLAs, to mitigate ...
- **p. 4 / III. METHOD - extractive body cue:** For the world model, we additionally collect a small set of failure demonstrations to finetune it for predicting failure cases.
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** For the world model, we additionally supplement its training with a small set of failure demonstrations collected from the rollouts of the pretrained VLA itself, ...
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** The training phases use the same datasets, and we collect 10 failure cases for each task to supplement the training of the world model.
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** Besides the strengths shown in Section IV-A, we find that injecting a directional future-conditioned feedback to action can improve the awareness of current execution, and ...
- **p. 7 / V. CONCLUSION - extractive body cue:** We expect future work to build on VLA-Reasoner and explore scalable test-time computation 7
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** As our method captures future deviations caused by current actions, the backpropagation offers a look-ahead evaluation, bringing the Markovian deployment with a longer horizon to ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, current VLAs also face critical limitations.를 문제로 두고, Our contributions are summarized as follows: • We propose a plug-in framework named VLA-Reasoner that empowers VLAs with structured reasoning to address their incremental deviations during deployment. • We adapt a modified ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
