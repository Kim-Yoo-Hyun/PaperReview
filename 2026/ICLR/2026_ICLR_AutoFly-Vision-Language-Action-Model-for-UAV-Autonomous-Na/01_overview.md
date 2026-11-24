# AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2e9f9cde1b709281a06dd14f679e4c51-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247860. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Xiaolou Sun, Wufei Si, Wenhui Ni, Yuntian Li, Dongming Wu, Fei Xie, Runwei Guan, He-Yang Xu, Henghui Ding, Yuan Wu, Yutao Yue, Yongming Huang, Hui Xiong
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Navigation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2e9f9cde1b709281a06dd14f679e4c51-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4, 17. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

AutoFly는 실외 비행에서 자세한 경로 지시 없이 대략적인 위치·방향 지시와 카메라 관측으로 다음 이동을 선택하는 VLA다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.
- **p. 1 / ABSTRACT - extractive body cue:** Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes.
- **p. 1 / ABSTRACT - extractive body cue:** However, real-world outdoor exploration typically occurs in unknown environments where detailed navigation instructions are unavailable.
- **p. 1 / ABSTRACT - extractive body cue:** Instead, only coarse-grained positional or directional guidance can be provided, requiring UAVs to autonomously navigate through continuous planning and obstacle avoidance.
- **p. 1 / ABSTRACT - extractive body cue:** To bridge this gap, we propose AutoFly, an end-to-end Vision-Language-Action (VLA) model for autonomous UAV navigation.

## Core Idea

- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** We utilize the same prism-siglip-7b backbone for consistency across VLM-based baselines, ensuring that performance differences reflect methodological contributions rather than backbone variations.
- **p. 22 / A.5.3 MODEL ACCELERATION - extractive body cue:** Additional CUDA operators are implemented for custom depth processing operations, while model parallelism enables distributed inference across multiple GPU processes to handle the computational demands ...
- **p. 4 / 3 METHOD - extractive body cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We compare the following approaches against our baseline (we use the OpenVLA here) and the full AutoFly model: • Data Scaling.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and coarse positional or directional guidance encoded as ... | camera/depth stream, pose, map와 language goal | p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL) |
| State/latent | TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current, RGB, observation | robot pose, free-space/semantic map와 local goal | p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 1 (1 INTRODUCTION) |
| Output/action | Fig. 2는 high-level [v_xy,v_z,ω_yaw] action sequence를 나타낸다. | High-level velocity/yaw commands; RL Q-target과 분리 | PDF p. 4 Fig. 2; p. 17 Eq. (6)은 data-collection learner의 Q-target |
| Objective/outcome | When d = 0 (episode continues), the target includes both the immediate reward r and the discounted estimate of future returns. | goal reach, safety, localization error와 replanning latency | p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- RGB에서 깊이 단서를 추출하는 인코더를 결합하고 영상·언어를 비행 행동에 맞추는 두 단계 학습을 구성했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=5)
- 실제 비행과 시뮬레이션에서 수집한 탐색 자료를 바탕으로 제시된 경로를 따르는 방식과 비교하고 실외 내비게이션 성공을 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2e9f9cde1b709281a06dd14f679e4c51-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets. | hardware/simulator version and reset protocol | p. 16 (A.2.2 DATASET SPLIT), p. 15 (A.2.1 DATASET CONSTRUCTION) |
| Dataset/benchmark | Data Collection Framework: We employ a dual-source approach for dataset construction, combining simulation and real-world data acquisition. | role, split, size and leakage | p. 16 (A.2.2 DATASET SPLIT), p. 15 (A.2.1 DATASET CONSTRUCTION), p. 15 (A.2.1 DATASET CONSTRUCTION), p. 9 (4 EXPERIMENTS) |
| Metric | As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% outdoors, with collision rates of 30% and 35%, respectively. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.2 ABLATION EXPERIMENTS) |
| Baseline/ablation | The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the one without it (44%, 24.5%), which proves the ... | fair input/data/compute/action matching | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.2 ABLATION EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive body cue:** Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive body cue:** To address these limitations, we plan to enhance AutoFly's sensing capabilities through LiDAR integration, which will provide comprehensive 360◦environmental perception and improve robustness in complex ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive body cue:** Future work will integrate Reinforcement Learning to enable active interaction with dynamic environments, allowing the system to learn more robust reactive behaviors through trial-and-error exploration.
- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive body cue:** The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict their trajectories.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Analysis of previous methods and our AutoFly. Left: Previous methods (Lee et al., 2024; Liu et al., 2023b) rely on dedicated, step-by-step instructions ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** SR = /S//N, CR = /C//N, PER = /E///S/, (4) where S = {i : di ≤dτ, θi ≤θτ} denotes the set of successful trials, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Overall performance metrics for quadrotor (all values in %). Here, we report three metrics: Success Rate (SR↑), Collision Rate (CR↓), and Path Efficiency ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL)이다.
