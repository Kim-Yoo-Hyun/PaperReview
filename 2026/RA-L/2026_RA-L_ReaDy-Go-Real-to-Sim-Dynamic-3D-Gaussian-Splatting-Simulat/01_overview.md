# ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2602.11575.
> PDF retrieval source: https://arxiv.org/pdf/2602.11575. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: Seungyeon Yoo, Youngseok Jang, Dabin Kim, Youngsoo Han, Seungwoo Jung, H. Jin Kim
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Navigation, Gaussian Splatting
- Official paper: https://arxiv.org/abs/2602.11575
- Full-text retrieval: https://arxiv.org/pdf/2602.11575
- Code/Project: https://syeon-yoo.github.io/ready-go-site/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

ReaDy-Go는 실제 장소의 정적 3차원 재구성에 움직이는 사람을 합성해 동적 장애물이 있는 환경의 시각 이동 정책을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2602.11575v3#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visual navigation models often struggle in realworld dynamic environments due to limited robustness to the sim-to-real gap and the difficulty of training policies tailored to ...
- **p. 1 / Abstract - extractive body cue:** Although real-to-sim navigation simulation using 3D Gaussian Splatting (GS) can mitigate these challenges, prior GS-based works have considered only static scenes or non-photorealistic human obstacles ...
- **p. 1 / Abstract - extractive body cue:** To address these issues, we propose ReaDy-Go, a novel real-to-sim simulation pipeline that synthesizes photorealistic dynamic scenarios in target environments by augmenting a reconstructed static ...
- **p. 1 / Abstract - extractive body cue:** The pipeline provides three key contributions: (1) a dynamic GS simulator that integrates static scene GS with a human animation module, enabling the insertion of ...
- **p. 1 / Abstract - extractive body cue:** ReaDy-Go outperforms baselines across target environments in both simulation and real-world experiments, demonstrating improved navigation performance even after sim-to-real transfer and in the presence of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Such limitations make it difficult to learn safe navigation in the presence of dynamic obstacles and to render photorealistic human appearances within reconstructed real-world environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the resulting sim-toreal distribution gap significantly degrades performance during deployment.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By reconstructing environments from RGB videos, GS enables high-fidelity rendering at fast frame rates, novel view synthesis, and simulation with an explicit 3D scene representation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are threefold. • Dynamic GS Simulator: We develop a photorealistic realto-sim dynamic 3D Gaussian Splatting simulator with human GS obstacles.
- **p. 3 / III. METHOD - extractive body cue:** GS is a representation that enables 3D geometry reconstruction, high-fidelity novel view synthesis, and fast training and rendering by fitting positions, rotations, scales, opacities, and ...
- **p. 3 / III. METHOD - extractive body cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...
- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 3 / III. METHOD - extractive body cue:** The human animation module places an animatable human GS model in the scene and then generates plausible human motion along a given obstacle trajectory.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy. | camera/depth stream, pose, map와 language goal | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | leveraging, simulator, planners, pipeline, collects, RGB, observations, actions, relative, goal, positions, training | robot pose, free-space/semantic map와 local goal | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Given a video of a static target deployment environment, ReaDy-Go generates photorealistic navigation datasets with moving human obstacles and trains an environment-specific navigation policy, as shown in Fig. | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Specifically, we employed PGSR [24] for 3D scene reconstruction, which achieves high-quality surface reconstruction and rendering by compressing 3D Gaussians into flat planes and using geometric regularization loss terms in addition to ... | goal reach, safety, localization error와 replanning latency | p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- 애니메이션이 가능한 사람 Gaussian을 정적 지도에 결합하고 사람·로봇 경로 계획기로 시연을 생성했다. [PDF 2쪽](https://arxiv.org/pdf/2602.11575v3#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2602.11575v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2602.11575v3#page=4)
- 시뮬레이션과 실제 이동을 별도로 비교하고 새로운 환경과 보행 장애물에 대한 배포 성능을 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2602.11575v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2602.11575v3#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Dataset/benchmark | The validation scenarios consist of 50 episodes for each environment, and we selected the checkpoint with the best validation performance, which is used for testing in simulation and the real world. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | 2) Evaluation metrics: We evaluate navigation performance using Success Rate (SR) and Average Reaching Time (ART). | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Baseline/ablation | For a fair comparison with image-goal navigation baselines (GNM, ViNT, and NoMaD), we provide them goal images captured at goal positions within 10 m of the start, with the camera oriented along ... | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go was more robust in situations involving dynamic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When a ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The robot should reach the goal without collisions within the scenario time limit.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These indicate that real-to-sim simulation with GS is a costeffective and scalable approach to achieve fewer collisions and faster task completion with only a video.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The proposed real-to-sim dynamic environment sim- ulation pipeline for visual navigation. ReaDy-Go generates photorealistic navigation datasets for dynamic scenarios and trains environment-specific visual ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For failed scenarios, we set the reaching time to the maximum scenario length.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD)이다.
