# 3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, Vision-Language Navigation, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Additionally, existing methods are primarily trained in closed-vocabulary settings that lack the diversity to encompass the rich semantics and variaThis ICCV paper is the Open Access version, provided by the Computer Vision ...를 문제로 두고, In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set semantics. code online visual observations into the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language navigation (VLN) requires an agent to traverse complex 3D environments based on natural language instructions, necessitating a thorough scene understanding.
- **p. 1 / Abstract - extractive body cue:** While existing works equip agents with various scene representations to enhance spatial awareness, they often neglect the complex 3D geometry and rich semantics in VLN ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, this work proposes a 3D Gaussian Map that represents the environment as a set of differentiable 3D Gaussians and accordingly develops ...
- **p. 1 / Abstract - extractive body cue:** Specifically, Egocentric Scene Map is constructed online by initializing 3D Gaussians from sparse pseudo-lidar point clouds, providing informative geometric priors for scene understanding.
- **p. 1 / Abstract - extractive body cue:** Each Gaussian primitive is further enriched through Open-Set Semantic Grouping operation, which groups 3D Gaussians based on their membership in object instances or stuff categories ...
- **p. 1 / 1. Introduction - extractive body cue:** Additionally, existing methods are primarily trained in closed-vocabulary settings that lack the diversity to encompass the rich semantics and variaThis ICCV paper is the Open ...
- **p. 1 / 1. Introduction - extractive body cue:** Although topological graphs are effective to capture abstract spatial relations, they lack 3D transformation equivariance, resulting in inconsistent spatial reasoning across viewpoints [42, 73].

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method is evaluated on three public benchmarks: R2R [3], R4R [32], and REVERIE [56].
- **p. 4 / 3.3. Multi-Level Action Prediction (MAP) - extractive body cue:** The 3D Gaussian Map G, constructed by integrating ESM and OSG, consists of Gaussians gi parameterized by {µi, si, ri, αi, ci, σi}.
- **p. 4 / 3.2. Open-Set Semantic Grouping (OSG) - extractive body cue:** To bridge this gap, we introduce OSG operation, enriching ESM with open-set semantics by associating each Gaussian primitive with semantic properties derived from visual observations.
- **p. 2 / 1. Introduction - extractive body cue:** The solution enables the agent to i) construct 3D scene maps with geometric priors at each navigable point during navigation, ii) integrate open-set semantics into ...
- **p. 5 / 3.5. Implementation Details - extractive body cue:** For R2R [3] and R4R [32], Masked Language Modeling (MLM) [12, 36] and Single-step Action Prediction (SAP) [12, 30] are adopted as auxiliary objectives during ...
- **p. 5 / 3.3. Multi-Level Action Prediction (MAP) - extractive body cue:** These features are then stacked into a combined representation F i, followed by FMLT to generate the instance-level score pi: pi = Softmax(F MLT([F i, ...
- **p. 3 / 3. Method - extractive body cue:** Built upon this, the agent is required to learn a navigation policy that predicts the next step action at ∈ At.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on g, we design MAP strategy to predict action probabilities by aggregating spatial-semantic cues from candidate waypoints V, guided by the L-word instruction embedding X ∈RL×768. | camera/depth stream, pose, map와 language goal | p. 4 (3.3. Multi-Level Action Prediction (MAP)), p. 3 (3. Method) |
| State/latent | design, MAP, strategy, predict, action, probabilities, aggregating, spatial-semantic, cues, candidate, waypoints, guided | robot pose, free-space/semantic map와 local goal | p. 4 (3.3. Multi-Level Action Prediction (MAP)), p. 3 (3. Method), p. 3 (3. Method) |
| Output/action | Built upon this, the agent is required to learn a navigation policy that predicts the next step action at ∈ At. | collision-free trajectory 또는 velocity command | p. 3 (3. Method), p. 3 (3. Method), p. 1 (1. Introduction) |
| Objective/outcome | The differentiable rendering process enables gradients from pixel-level loss functions to backpropagate through the Gaussian parameters. | goal reach, safety, localization error와 replanning latency | p. 4 (3.1. Egocentric Scene Map (ESM)), p. 4 (3.1. Egocentric Scene Map (ESM)), p. 5 (3.5. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method is evaluated on three public benchmarks: R2R [3], R4R [32], and REVERIE [56].
- **p. 4 / 3.3. Multi-Level Action Prediction (MAP) - extractive body cue:** The 3D Gaussian Map G, constructed by integrating ESM and OSG, consists of Gaussians gi parameterized by {µi, si, ri, αi, ci, σi}.
- **p. 4 / 3.2. Open-Set Semantic Grouping (OSG) - extractive body cue:** To bridge this gap, we introduce OSG operation, enriching ESM with open-set semantics by associating each Gaussian primitive with semantic properties derived from visual observations.
- **p. 2 / 1. Introduction - extractive body cue:** The solution enables the agent to i) construct 3D scene maps with geometric priors at each navigable point during navigation, ii) integrate open-set semantics into ...
- **p. 6 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Our agent achieves consistent improvements across all splits, which outperforms BEVBert [1] by 2% in both SR and SPL on the val unseen split.
- **p. 6 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Specifically, compared to HAMT [12], our approach achieves improvements of 2% in SR, CLS, and nDTW, with 3% gain in SDTW.
- **p. 8 / 4.3. Diagnostic Experiment - extractive body cue:** From Table 5, we can observe that: i) Row #1 vs #2 vs #3 vs #4: Each level contributes to performance gain, and the Instance ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts) |
| Embodiment/environment | We evaluate our method on three benchmark datasets: R2R [3], R4R [32], and REVERIE [56]. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Qualitative results on R2R [3] val unseen split. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Comparison to State-of-the-Arts), p. 7 (4.2. Comparison to State-of-the-Arts) |
| Metric | The performance is evaluated using Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), and Success-weighted Path Length (SPL), following [46]. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 7 (4.2. Comparison to State-of-the-Arts) |
| Baseline/ablation | As shown in Table 3, our method maintains a strong performance on R4R, consistently outperforming existing approaches. | fair input/data/compute/action matching | p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** (b) Our agent precisely identifies and localizes the "bathroom" and "rug", while BEVBert [1] stops in the wrong place since critical landmarks cannot be identified, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dense Features vs 3D Gaussians. Recent VLN meth- ods [1, 47, 49, 78] rely on dense sampling to construct scene maps, which often ...
- **p. 6 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** These results further demonstrate the robustness of our method in main9257

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Additionally, existing methods are primarily trained in closed-vocabulary settings that lack the diversity to encompass the rich semantics and variaThis ICCV paper is the Open Access version, provided by the Computer Vision ...를 문제로 두고, In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating open-set semantics. code online visual observations into the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.5. Implementation Details), p. 5 (3.3. Multi-Level Action Prediction (MAP)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
