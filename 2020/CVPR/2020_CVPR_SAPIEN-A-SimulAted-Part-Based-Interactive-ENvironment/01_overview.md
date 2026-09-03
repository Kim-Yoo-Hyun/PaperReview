# SAPIEN: A SimulAted Part-Based Interactive ENvironment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, simulation, articulated objects, physics, manipulation, 3D interaction
- Official paper: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf
- Code/Project: https://sapien.ucsd.edu/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level.를 문제로 두고, The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and front of the arena respectively.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Building home assistant robots has long been a goal for vision and robotics researchers.
- **p. 1 / Abstract - extractive body cue:** To achieve this task, a simulated environment with physically realistic simulation, sufficient articulated objects, and transferability to the real robot is indispensable.
- **p. 1 / Abstract - extractive body cue:** Existing environments achieve these requirements for robotics simulation with different levels of simplification and focus.
- **p. 1 / Abstract - extractive body cue:** We take one step further in constructing an environment that supports household tasks for training robot learning algorithm.
- **p. 1 / Abstract - extractive body cue:** Our work, SAPIEN, is a realistic and physics-rich simulated environment that hosts a large-scale set of articulated objects.
- **p. 1 / 1. Introduction - extractive body cue:** It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level.
- **p. 1 / 1. Introduction - extractive body cue:** One direct way to address the problem is to train robots by interacting with the real environment [30, 4, 27].

## Core Idea

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and ...
- **p. 1 / 1. Introduction - extractive body cue:** We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic segmentation of motion parts, while a robot ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Also, this mode enables end-toend learning for perception and interactions (e.g., learning perception with a specific interaction target).
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Having both diverse object categories and rich intra-class instance variations allows us to perform such tasks on multiple object instances at category levels.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** To demonstrate our simulator in manipulation tasks, we first use manually designed heuristic pipelines to solve the tasks.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** Then we use velocity controller to pull it to the joint limit.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or drawers, and test ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud as inputs, the method needs to develop ... | standardized observation, action, task state와 evaluation split | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| State/latent | factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks, image/point-cloud, inputs | benchmark state/goal와 method decision | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Output/action | We provide three different state representations: 1) raw state of the whole scene (raw-exp), consisting of current positions and velocities of all the parts; 2) mobility-based representation (mobility-exp), with 6D pose of ... | policy/controller trajectory 또는 measured result | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction) |
| Objective/outcome | During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper falls off the handle. | success metric, robustness, generalization과 reproducibility | p. 8 (4.2. Robotic Interaction) |

## Main Claims and Actual Contribution

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and ...
- **p. 1 / 1. Introduction - extractive body cue:** We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic segmentation of motion parts, while a robot ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Also, this mode enables end-toend learning for perception and interactions (e.g., learning perception with a specific interaction target).
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Having both diverse object categories and rich intra-class instance variations allows us to perform such tasks on multiple object instances at category levels.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** To demonstrate our simulator in manipulation tasks, we first use manually designed heuristic pipelines to solve the tasks.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** This method (PBVS) achieves an 81.8% success rate for door opening.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** Using ground-truth visual information, we can achieve a 95.3% success rate.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Robotic Interaction tasks. We study two robotic interaction tasks: door-opening and drawer-pulling. architectures, loss designs, and training protocols. We summarize the experimental results ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Embodiment/environment | SAPIEN simulator, equipped with the PartNet-Mobility dataset, provides a platform for several robotic perception tasks. | hardware/simulator version and reset protocol | p. 5 (4.1. Robotic Perception), p. 7 (4.2. Robotic Interaction) |
| Dataset/benchmark | We demonstrate the versatile abilities of our simulator by demonstrating robotic perception and interaction tasks. | role, split, size and leakage | p. 5 (4.1. Robotic Perception), p. 7 (4.2. Robotic Interaction), p. 5 (4. Tasks and Benchmarks), p. 6 (4.1. Robotic Perception) |
| Metric | For door-opening, the RL agent tends to overfit the training objects, as when the number of training objects Tasks Door (Final Angle Degree) Drawer (Success Rate) 2 4 8 16 2 4 ... | definition, denominator, direction and uncertainty | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.1. Robotic Perception) |
| Baseline/ablation | We evaluate two baseline algorithms, ResNet-50 [17] and PointNet++ [39], that deals with the input RGB-D partial scans using either 2D or 3D formats. | fair input/data/compute/action matching | p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** If the agent cannot move the joint to the given threshold or move 11103
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** in the opposite direction, then it fails.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper ...

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level.를 문제로 두고, The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and front of the arena respectively.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
