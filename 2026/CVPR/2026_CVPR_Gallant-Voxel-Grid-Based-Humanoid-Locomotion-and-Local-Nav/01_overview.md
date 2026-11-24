# Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Qingwei Ben, Botian Xu, Kailin Li, Feiyu Jia, Wentao Zhang, Jingping Wang, Jingbo Wang, Dahua Lin, Jiangmiao Pang
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, perceptive locomotion, LiDAR, 3D navigation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf
- Code/Project: https://gallantloco.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Gallant는 라이다 점군을 3차원 복셀로 표현해 휴머노이드의 보행과 가까운 장애물 회피를 한 정책에서 제어한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust humanoid locomotion requires accurate and globally consistent perception of the surrounding 3D environment.
- **p. 1 / Abstract - extractive body cue:** However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture ...
- **p. 1 / Abstract - extractive body cue:** This paper presents Gallant, a voxel-grid-based framework for humanoid locomotion and local navigation in 3D constrained terrains.
- **p. 1 / Abstract - extractive body cue:** It leverages voxelized LiDAR data as a lightweight and structured perceptual representation, and employs a z-grouped 2D CNN to map this representation to the control ...
- **p. 1 / Abstract - extractive body cue:** A high-fidelity LiDAR simulation that dynamically generates realistic observations is developed to support scalable, LiDAR-based training and ensure sim-to-real consistency.
- **p. 2 / 1. Introduction - extractive body cue:** While recent systems have progressed from lab prototypes to real-world deployment [17, 23], ensuring operational safety remains a key challenge.
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we introduce Gallant, a voxel-grid-based perception-learning framework for humanoid locomotion and loco-navigation across 3D constrained terrains.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose voxel grid as a lightweight yet geometrypreserving representation for humanoid locomotion and loco-navigation [31] in 3D-constrained environments.
- **p. 3 / 3. Method - extractive body cue:** We introduce Gallant, a voxel-grid-based perceptive learning framework for humanoid locomotion and local navigation [31] in 3D constrained environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) and train an ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In contrast, 3D LiDAR provides detailed scene geometry with a wide FoV, but its raw point clouds are sparse and noisy, which bottlenecks sample-efficient policy learning and real-time inference. | proprioception, reference pose/motion, visual or language command | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| State/latent | contrast, LiDAR, provides, detailed, scene, geometry, wide, FoV, point, clouds, sparse, noisy | whole-body pose, balance/contact state와 skill/mode | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3. Method) |
| Output/action | Actor and critic share all features except privileged inputs, which are critic-only. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (3.1. Problem Formulation), p. 3 (3. Method), p. 2 (1. Introduction) |
| Objective/outcome | The objective is to maximize expected return J(π) = E[PH-1 t=0 γtrt]. | tracking, balance, skill/task success와 recovery | p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation) |

## Main Claims and Actual Contribution

- 높이 방향으로 나눈 복셀 특징을 2차원 합성곱으로 처리하고 시뮬레이션에서 라이다 관측과 정책을 함께 학습한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf#page=4)
- 시뮬레이션 절제 실험과 실물 통과 실험으로 위쪽 장애물·측면 제약·단차가 포함된 지형에서 평가한다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2.3. Result), p. 7 (4.2.3. Result) |
| Embodiment/environment | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ... | hardware/simulator version and reset protocol | p. 5 (4.2.1. Metrics), p. 8 (4.4. Further Analyses) |
| Dataset/benchmark | (a) The humanoid crouches to traverse under a low ceiling; (b) Voxel grid from LiDAR simulation that includes dynamic objects captures the robot's own links; (c) LiDAR simulation restricted to static objects ... | role, split, size and leakage | p. 5 (4.2.1. Metrics), p. 8 (4.4. Further Analyses), p. 7 (4.2.3. Result), p. 5 (4.1. Experimental Configuration) |
| Metric | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ... | definition, denominator, direction and uncertainty | p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 7 (4.2.3. Result) |
| Baseline/ablation | Gallant consistently outperforms both baselines across all real-world terrains. | fair input/data/compute/action matching | p. 8 (4.3.2. Ablation), p. 5 (4.1. Experimental Configuration), p. 6 (4.2.3. Result) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 7 / 4.2.3. Result - extractive body cue:** 1, using only a height map as the perceptual representation for policy cannot represent multilayer structure; consequently, Only-Height-Map fails on terrains such as Ceiling.
- **p. 8 / 4.4. Further Analyses - extractive body cue:** On other terrains-especially Platforms and Stairs, previously considered unstable due to collision risk [21]-Gallant achieves high success by proactively adjusting foot trajectories.
- **p. 8 / 5. Conclusion - extractive body cue:** In real-world tests, a single LiDAR policy covers the ground obstacles handled by elevation-map controllers while also tackling lateral and overhead structures, and on ground-only ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. (a) Curriculum-based training over 8 representative terrains enhances generalization, and realistic voxel path alignment achieved via efficient LiDAR simulation with domain-randomized ...
- **p. 6 / 4.2.3. Result - extractive body cue:** 5 (b)) correctly include the robot's legs, which occupy voxels and induce occlusion "holes" along LiDAR rays to the distant floor.
- **p. 6 / 4.2.3. Result - extractive body cue:** Because real LiDAR returns from all visible objects, omitting dynamics makes the voxel grid out-of-distribution (OOD) in postures where the body is not fully upright ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 6 (4.2.3. Result), p. 7 (4.2.3. Result)이다.
