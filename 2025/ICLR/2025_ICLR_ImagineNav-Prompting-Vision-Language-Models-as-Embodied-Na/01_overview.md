# ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=vQFw9ryKyK.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114907. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Navigation
- Official paper: https://openreview.net/forum?id=vQFw9ryKyK
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114907
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.를 문제로 두고, In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Visual navigation is an essential skill for home-assistance robots, providing the object-searching ability to accomplish long-horizon daily tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Many recent approaches use Large Language Models (LLMs) for commonsense inference to improve exploration efficiency.
- **p. 1 / ABSTRACT - extractive body cue:** However, the planning process of LLMs is limited within texts and it is difficult to represent the spatial occupancy and geometry layout only by texts.
- **p. 1 / ABSTRACT - extractive body cue:** Both are important for making rational navigation decisions.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we seek to unleash the spatial perception and planning ability of VisionLanguage Models (VLMs), and explore whether the VLM, with only on-board ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although such a pipeline achieves great success in recent years (Zhou et al., 2023; Kuang et al., 2024; Wu et al., 2024b; Zhang et al., ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also provide a detailed ablation analysis to help understand the important conclusions in our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new decision-making paradigm based on imagined imagery, wherein decisions are made on imaginations, enabling more nuanced, context-aware interactions that better harness VLMs' ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** To determine the execution actions at each step of the PointNav process, we use Variable Experience Rollout (VER) (Wijmans et al., 2022) as our underlying ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Subsequently, the visual observations at these locations are imagined by a NVS model.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Through the Where2Imagine module, our imagination model aligns with human navigation habits.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As illustrated in Figure 3, the VLM receives the synthesized observations at future navigation waypoints and the navigation goal as inputs. | camera/depth stream, pose, map와 language goal | p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION) |
| State/latent | illustrated, Figure, VLM, receives, synthesized, observations, future, navigation, waypoints, goal, inputs, Cap | robot pose, free-space/semantic map와 local goal | p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Output/action | Cap (Liang et al., 2023) generates robotic policy code directly from example language commands, enabling autonomous control and task execution based on natural language instructions. | collision-free trajectory 또는 velocity command | p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Objective/outcome | Compared to larger models (e.g., GPT-4o), GPT-4o-mini is lightweight and cost-effective. | goal reach, safety, localization error와 replanning latency | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also provide a detailed ablation analysis to help understand the important conclusions in our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new decision-making paradigm based on imagined imagery, wherein decisions are made on imaginations, enabling more nuanced, context-aware interactions that better harness VLMs' ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** On the HM3D dataset, ImagineNav achieves a success rate of 53.0% and a SPL of 23.8%, significantly outperforming most of the methods especially at success ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Moreover, ImagineNav achieves the highest success rate and SPL on the HSSD dataset.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Further incorporating Where2Image improve success rate from 55.0 to 64.0, and from 49.0 to 56.0 under settings of ‘NVS' and ‘w/o NVS', respectively.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | The HSSD dataset provides 40 high-quality synthetic scenes, comprising 110 training scenes and 40 validation scenes. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | First, some object instances are neglected for marking by the simulator, and therefore a successfully trajectory is wrongly considered as a failure (a.k.a. false failure) as shown in the bottom left of ... | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | We report the performance in terms of Success Rate (SR), defined as the proportion of episodes where the agent's distance to the target object is less than 1m after executing the STOP ... | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Baseline/ablation | Imagination Where2Imagine NVS HM3D Success Rate SPL ✗ ✗ Oracle 43.0 24.7 ✓ ✗ Oracle 55.0 27.6 ✓ ✓ Oracle 64.0 28.3 ✓ ✗ PolyOculus 49.0 23.3 ✓ ✓ PolyOculus 56.0 24.3 ... | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We also present some failure examples at the bottom of Figure 8
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We identified three key factors contributing to these navigation failures.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** First, some object instances are neglected for marking by the simulator, and therefore a successfully trajectory is wrongly considered as a failure (a.k.a. false failure) ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** Moving forward, we aim to enhance the quality of viewpoint generation and optimize the use of historical memory to further improve navigation performance and robustness.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: An example of the VLM analysis. By examining different future-view scenarios, the VLM pinpoints the direction most likely to incorporate the target object ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.5 ANALYSIS OF SUCCESSFUL AND FAILED TRAJECTORIES Figure 5 illustrates that our method achieves efficient path planning and navigation across different targets.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.를 문제로 두고, In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
