# MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=efDNv5XvVo.
> PDF retrieval source: https://arxiv.org/pdf/2509.15548. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://openreview.net/forum?id=efDNv5XvVo
- Full-text retrieval: https://arxiv.org/pdf/2509.15548
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.를 문제로 두고, In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions to construct a dense point cloud initialization ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In-the-wild photo collections often contain limited volumes of imagery and exhibit multiple appearances, e.g., taken at different times of day or seasons, posing significant challenges ...
- **p. 1 / Abstract - extractive body cue:** Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present MS-GS, a novel framework designed with Multi-appearance capabilities in Sparse-view scenarios using 3DGS.
- **p. 1 / Abstract - extractive body cue:** To address the lack of support due to sparse initializations, our approach is built on the geometric priors elicited from monocular depth estimations.
- **p. 1 / Abstract - extractive body cue:** The key lies in extracting and utilizing local semantic regions with a Structure-from-Motion (SfM) points anchored algorithm for reliable alignment and geometry cues.
- **p. 2 / 1 Introduction - extractive body cue:** A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.
- **p. 2 / 1 Introduction - extractive body cue:** To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators [18, 19, 20] that ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, they synthesize overly smooth regions, while our method recovers fine details.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present MS-GS, which improves the robustness of 3DGS in dealing with unconstrained images when limited viewpoints and varying appearances exist, which ...
- **p. 3 / 1 Introduction - extractive body cue:** To this end, we introduce an unbounded drone dataset that features multi-view appearance.
- **p. 4 / 3 Method - extractive body cue:** To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by ...
- **p. 6 / 3 Method - extractive body cue:** A 3D point cloud is back-projected given a training view IT and its corresponding rendered depth DT , and then forward-projected onto the virtual view ...
- **p. 6 / 3 Method - extractive body cue:** Thus, we propose to use a coarse semantic feature supervision at the local patch level, i.e, the receptive field of each feature-map element.
- **p. 7 / 3 Method - extractive body cue:** Optimization Incorporating all the aforementioned techniques, the training objective of MS-GS is: Ltotal " λI }IT ´ I˚ T }1 ` p1 ´ λIqSSIMpIT , ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions to construct a dense point cloud initialization ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (1 Introduction), p. 4 (3 Method) |
| State/latent | summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths, local, regions | geometry, map, object/relationship state | p. 3 (1 Introduction), p. 4 (3 Method), p. 6 (3 Method) |
| Output/action | SfM-anchored alignment After camera calibration, we have a set of N images tIn/n " 1, 2, ..., Nu, an initial SfM point cloud X P RP ˆ3 and the camera poses. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | (1) is minimized, it's unclear whether regions without sufficient constraints, i.e. dsfm n , are properly aligned. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, they synthesize overly smooth regions, while our method recovers fine details.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present MS-GS, which improves the robustness of 3DGS in dealing with unconstrained images when limited viewpoints and varying appearances exist, which ...
- **p. 3 / 1 Introduction - extractive body cue:** To this end, we introduce an unbounded drone dataset that features multi-view appearance.
- **p. 4 / 3 Method - extractive body cue:** To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by ...
- **p. 9 / 4 Experiments - extractive body cue:** On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts LPIPS ...
- **p. 8 / 4 Experiments - extractive body cue:** We identify that incorporating our semantic depth alignment initialization significantly improved the metrics with 0.8 dB in PSNR, 0.046 in SSIM, -0.031 in LPIPS, and ...
- **p. 8 / 4 Experiments - extractive body cue:** All proposed components are complementary, and the best results are achieved when combined.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance and two with varying appearances. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Additionally, our dataset contains scenes with 360-degree coverage by perspective cameras, whereas Phototourism is covered by face-forward images. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 15 (A.1.2 Comparison with prior benchmark), p. 8 (4 Experiments) |
| Metric | Although SparseGS and FSGS improve the rendering quality through floater pruning, score distillation regularization, and the densification strategy. | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts LPIPS and DSIM by 33.8% and 65.6%, respectively, ... | fair input/data/compute/action matching | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 17 (A.3 Implementation details) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** Specific techniques have to be developed to solve these limitations, which we leave as future work.
- **p. 10 / 6 Conclusion - extractive body cue:** We identify that one of the limitations of 3DGS-based methods in sparse-view synthesis is the sparse point cloud initialization.
- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations First, MS-GS is not designed for handling transient objects, which is especially difficult under sparse views due to increased uncertainty and ambiguities in ...
- **p. 10 / 6 Conclusion - extractive body cue:** Jointly, MS-GS offers a robust solution under challenges of limited viewpoints and varying appearances that naturally arise in real-world data.
- **p. 19 / A.6 In-the-wild evaluation - extractive body cue:** A previous approach [11] has tried to perform re-triangulation based on known train poses, but does not account for pose inaccuracy.
- **p. 21 / A.6.2 Evaluation metrics - extractive body cue:** This analysis indicates that DSIM is an appropriate metric for in-the-wild evaluations: it avoids over-penalising inevitable alignment errors while still capturing real perceptual degradation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.를 문제로 두고, In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions to construct a dense point cloud initialization ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
