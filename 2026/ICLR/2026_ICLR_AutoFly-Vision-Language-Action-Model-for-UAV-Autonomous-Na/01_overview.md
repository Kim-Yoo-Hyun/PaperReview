# AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=88RKxlFUNY.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247860. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Navigation
- Official paper: https://openreview.net/forum?id=88RKxlFUNY
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247860
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.를 문제로 두고, This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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
| Output/action | For a stochastic policy, the target value y is calculated as: y = r + γ(1 -d)  min i=1,2 Qθ′ i(s′, a′) -α log πϕ(a′/s′)  , (6) where γ is ... | collision-free trajectory 또는 velocity command | p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 1 (1 INTRODUCTION), p. 4 (3 METHOD) |
| Objective/outcome | When d = 0 (episode continues), the target includes both the immediate reward r and the discounted estimate of future returns. | goal reach, safety, localization error와 replanning latency | p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** We utilize the same prism-siglip-7b backbone for consistency across VLM-based baselines, ensuring that performance differences reflect methodological contributions rather than backbone variations.
- **p. 22 / A.5.3 MODEL ACCELERATION - extractive body cue:** Additional CUDA operators are implemented for custom depth processing operations, while model parallelism enables distributed inference across multiple GPU processes to handle the computational demands ...
- **p. 19 / A.3.2 ABLATION EXPERIMENTS - extractive body cue:** Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by 1.4%.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the one ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% outdoors, with collision rates of 30% and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.를 문제로 두고, This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
