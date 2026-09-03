# Habitat: A Platform for Embodied AI Research

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.01201.
> PDF retrieval source: https://arxiv.org/pdf/1904.01201. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Benchmarks and Datasets
- Tier: REFERENCE
- Tags: Robotics, Navigation, Embodied AI, Benchmark
- Official paper: https://arxiv.org/abs/1904.01201
- Full-text retrieval: https://arxiv.org/pdf/1904.01201
- Code/Project: https://aihabitat.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Benchmarks and Datasets의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time and cannot be parallelized), dangerous (poorly-trained agents can unwittingly injure ...를 문제로 두고, Specifically, Habitat consists of the following: 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).
- **p. 1 / Abstract - extractive body cue:** Habitat enables training embodied agents (virtual robots) in highly efficient photorealistic 3D simulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, Habitat consists of: (i) Habitat-Sim: a flexible, high-performance 3D simulator with configurable agents, sensors, and generic 3D dataset handling.
- **p. 1 / Abstract - extractive body cue:** Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can reach over 10,000 ...
- **p. 1 / Abstract - extractive body cue:** (ii) Habitat-API: a modular high-level library for end-toend development of embodied AI algorithms - defining tasks (e.g. navigation, instruction following, question answering), configuring, training, and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time and cannot be ...
- **p. 2 / 1. Introduction - extractive body cue:** In the context of embodied AI, simulators help overcome the aforementioned challenges - they can run orders of magnitude faster than real-time and can be ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Specifically, Habitat consists of the following: 1.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 1 / Abstract - extractive body cue:** Habitat enables training embodied agents (virtual robots) in highly efficient photorealistic 3D simulation.
- **p. 5 / 4. PointGoal Navigation at Scale - extractive body cue:** In Habitat and our experiments, we use a more realistic collision model - the agent navigates in a continuous state space4 and motion can produce ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** When training learning-based agents, we first divide the scenes in the training set equally among 8 (Gibson), 6 (Matterport3D) concurrently running simulator worker threads.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - Implementation: C++ backend with Python API and ... | standardized observation, action, task state와 evaluation split | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale) |
| State/latent | RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task, API, allows | benchmark state/goal와 method decision | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction) |
| Output/action | The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy optimization [25]. | policy/controller trajectory 또는 measured result | p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction), p. 4 (3. Habitat Platform) |
| Objective/outcome | RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - Implementation: C++ backend with Python API and ... | success metric, robustness, generalization과 reproducibility | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 6 (4. PointGoal Navigation at Scale) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Specifically, Habitat consists of the following: 1.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 1 / Abstract - extractive body cue:** Habitat enables training embodied agents (virtual robots) in highly efficient photorealistic 3D simulation.
- **p. 7 / 5. Results and Findings - extractive body cue:** Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors.
- **p. 8 / 5. Results and Findings - extractive body cue:** Our findings so far are that RL (PPO) agents significantly outperform SLAM [20].
- **p. 7 / 5. Results and Findings - extractive body cue:** All RL (PPO) agents start out with far worse SPL, but RL (PPO) Depth, in particular, improves dramatically and matches the classic baseline at approximately ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5. Results and Findings), p. 8 (5. Results and Findings) |
| Embodiment/environment | In contrast, RGB sensors provide a high-dimensional complex signal that may be prone to overfitting to train environments due to the variety across scenes (even within the same dataset). | hardware/simulator version and reset protocol | p. 7 (5. Results and Findings), p. 7 (5. Results and Findings) |
| Dataset/benchmark | We believe the reason is the previously noted observation that Gibson scenes are smaller and episodes are shorter (lower GDSP) than Matterport3D. | role, split, size and leakage | p. 7 (5. Results and Findings), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings), p. 8 (5. Results and Findings) |
| Metric | The differences are about an order of magnitude larger than the standard deviation of average SPL for all cases (e.g. on the Gibson dataset errors are, Depth: ±0.015, RGB: ±0.055, RGBD: ±0.028, ... | definition, denominator, direction and uncertainty | p. 7 (5. Results and Findings), p. 7 (Figure/Table caption), p. 8 (5. Results and Findings) |
| Baseline/ablation | Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance at 5-10 million steps. Interesting trends emerge with more experience: ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (5. Results and Findings), p. 8 (5. Results and Findings) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 7. Future Work - extractive body cue:** Another planned avenue of future work involves procedural generation of 3D environments by leveraging a combination of 3D reconstruction and virtual object datasets.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the RL (PPO) baseline agent on test set ...
- **p. 7 / 5. Results and Findings - extractive body cue:** SLAM [20] does not require training and thus has a constant performance (0.59 on Gibson, 0.42 on Matterport3D).
- **p. 8 / 5. Results and Findings - extractive body cue:** RGB and RGBD agents suffer a significant performance degradation, while the Blind agent is least affected (as we would expect).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: Performance of Habitat-Sim under different sensor frame memory transfer strategies for increasing image resolution. We see that ‘GPU->GPU' is unaffected by image resolution ...

## Why Read It

Benchmarks and Datasets의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time and cannot be parallelized), dangerous (poorly-trained agents can unwittingly injure ...를 문제로 두고, Specifically, Habitat consists of the following: 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4. PointGoal Navigation at Scale), p. 4 (3. Habitat Platform) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
