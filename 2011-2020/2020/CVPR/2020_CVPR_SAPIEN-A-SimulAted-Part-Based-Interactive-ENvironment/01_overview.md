# SAPIEN: A SimulAted Part-Based Interactive ENvironment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao Zhu, Fangchen Liu, Minghua Liu, Hanxiao Jiang, Yifu Yuan, He Wang, Li Yi, Angel X. Chang, Leonidas J. Guibas, Hao Su
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, simulation, articulated objects, physics, manipulation, 3D interaction
- Official paper: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf
- Code/Project: https://sapien.ucsd.edu/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf) 기준이다.

## Why This Paper Is Here

SAPIEN은 관절이 있는 생활 물체의 부품 기하와 움직임을 표현해 시각 인식 및 물체 조작을 평가하는 물리 시뮬레이션 환경이다. [PDF 1쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=1)

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
| Observation/input | In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud as inputs, the method needs to develop ... | 인식용 영상·점군 또는 조작 조건별로 제공한 장면·물체 상태 | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| State/latent | factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks, image/point-cloud, inputs | 물체 부품의 자세·관절과 그리퍼 상태 | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Output/action | We provide three different state representations: 1) raw state of the whole scene (raw-exp), consisting of current positions and velocities of all the parts; 2) mobility-based representation (mobility-exp), with 6D pose of ... | 부품 운동 예측 또는 그리퍼의 관절 물체 조작 | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction) |
| Objective/outcome | During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper falls off the handle. | 부품·운동 속성 인식과 문·서랍 열기 성공 | p. 8 (4.2. Robotic Interaction) |

## Main Claims and Actual Contribution

- PartNet-Mobility의 관절 물체 자산을 센서 렌더링·물리 상호작용과 연결해 부품 수준의 학습 데이터를 생성한다. [PDF 3쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=5)
- 움직이는 부품 검출과 운동 속성 추정을 평가하고 휴리스틱 및 강화학습 기반의 물체 상호작용을 시연했다. [PDF 6쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=8)

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

## 검색 태그 근거

PartNet-Mobility의 관절 물체로 영상·점군 기반 부품 인식과 모의 그리퍼의 문·서랍 열기를 평가한다. 인식기의 RGB·점군 입력과 상호작용 정책의 상태 표현은 서로 다른 실험에 쓰인다. [원문 6쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=6) · [원문 8쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf#page=8)

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction)이다.
