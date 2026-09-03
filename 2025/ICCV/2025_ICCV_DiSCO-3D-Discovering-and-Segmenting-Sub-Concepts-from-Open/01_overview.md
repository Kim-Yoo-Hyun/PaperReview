# DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) and 3D USS (when no query is ...를 문제로 두고, Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as long as two conditions are met.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D semantic segmentation provides high-level scene understanding for applications in robotics, autonomous systems, etc.
- **p. 1 / Abstract - extractive body cue:** Traditional methods adapt exclusively to either task-specific goals (open-vocabulary segmentation) or scene content (unsupervised semantic segmentation).
- **p. 1 / Abstract - extractive body cue:** We propose DiSCO-3D, the first method addressing the broader problem of 3D Open-Vocabulary Sub-concepts Discovery, which aims to provide a 3D semantic segmentation that adapts ...
- **p. 1 / Abstract - extractive body cue:** We build DiSCO3D on Neural Fields representations, combining unsupervised segmentation with weak open-vocabulary guidance.
- **p. 1 / Abstract - extractive body cue:** Our evaluations demonstrate that DiSCO-3D achieves effective performance in Open-Vocabulary Sub-concepts Discovery and exhibits state-of-the-art results in the edge cases of both open-vocabulary and unsupervised ...
- **p. 2 / 1. Introduction - extractive body cue:** As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) ...
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...

## Core Idea

- **p. 5 / 3.5. Method extensions - extractive body cue:** Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** In the following, we present our method in three parts.
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce 3D OV-SD, a new 3D semantic segmentation task providing adaptive segmentations based on scene context and user-defined queries.
- **p. 8 / 4.3.1. Open-Vocabulary Segmentation - extractive body cue:** We present quantitative outcomes in Table 3, first analyzing results for classes, followed by concepts.
- **p. 5 / 3.5. Method extensions - extractive body cue:** First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders).
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs.
- **p. 5 / 3.5. Method extensions - extractive body cue:** Given these conditions, the input 3D representations and query modalities can vary widely-from a single feature field satisfying both requirements (e.g.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Regarding GrowSP, although it succeeds in performing accurate segmentation, the global performances are lower, probably due to the input data modalities, as the discrete nature of point clouds may limit their expressiveness ... | RGB-D, image set, point cloud, depth와 camera pose | p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction) |
| State/latent | Regarding, GrowSP, although, succeeds, performing, accurate, segmentation, global, performances, lower, probably, input | geometry, map, object/relationship state | p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview) |
| Output/action | We evaluate DiSCO-3D on both real and synthetic data, demonstrating better performance than hand-designed naive baselines on the proposed OV-SD task and experimentally show that our solution produces state-of-the-art performances on the ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview), p. 3 (3.2. Preliminaries) |
| Objective/outcome | While the losses Lproj and Lproto remain unchanged, a loss Lqi irr is added for each query qi following Equation 4. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions) |

## Main Claims and Actual Contribution

- **p. 5 / 3.5. Method extensions - extractive body cue:** Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** In the following, we present our method in three parts.
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce 3D OV-SD, a new 3D semantic segmentation task providing adaptive segmentations based on scene context and user-defined queries.
- **p. 8 / 4.3.1. Open-Vocabulary Segmentation - extractive body cue:** We present quantitative outcomes in Table 3, first analyzing results for classes, followed by concepts.
- **p. 6 / 4.2.1. Evaluated methods - extractive body cue:** Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas the latters achieve ...
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** To evaluate the ability of the produced CLIP prototypes to achieve semantic matching, we evaluate the OV-SD performance by replacing the prototypes matching by a ...
- **p. 5 / 4.1. Implementation and evaluation details - extractive body cue:** We implemented our method in the Nerfstudio [34] framework and every evaluation is based on the same Nerfacto model, a grid-based NeRF method coupled with ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies) |
| Embodiment/environment | We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), feature fields (LeRF and OpenNeRF), types of queries (textual, visual ... | hardware/simulator version and reset protocol | p. 7 (4.2.2. Results), p. 6 (4.1. Implementation and evaluation details) |
| Dataset/benchmark | However, the benchmark is still far from being saturated, showing the difficulty of the task and the room for future improvements. | role, split, size and leakage | p. 7 (4.2.2. Results), p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results), p. 5 (4. Experimental evaluations) |
| Metric | First, we observe that the complete model's performance remains stable in both segmentation accuracy and the numFF Method PCLIP Hungarian PQ ↑ mIoU ↑ mAcc ↑ PQ ↑ mIoU ↑ mAcc ↑ ... | definition, denominator, direction and uncertainty | p. 7 (4.2.3. Ablations studies), p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.3. Ablations studies) |
| Baseline/ablation | All quantitative experiments, including DiSCO3D and the comparative baselines, use the same pre-trained Nerfacto models and feature fields as input. | fair input/data/compute/action matching | p. 5 (4.1. Implementation and evaluation details), p. 5 (4. Experimental evaluations), p. 6 (4.2.1. Evaluated methods) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4. Experimental evaluations - extractive body cue:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** The last column refers to the main experiment where the number of prototypes is fixed and does not depend on NGT .

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) and 3D USS (when no query is ...를 문제로 두고, Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as long as two conditions are met.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview), p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 5 (3.5. Method extensions) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
