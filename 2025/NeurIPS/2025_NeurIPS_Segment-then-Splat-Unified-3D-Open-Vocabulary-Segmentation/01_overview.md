# Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ycPVp0577R.
> PDF retrieval source: https://arxiv.org/pdf/2503.22204.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, semantic
- Official paper: https://openreview.net/forum?id=ycPVp0577R
- Full-text retrieval: https://arxiv.org/pdf/2503.22204.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied to dynamic scenes.를 문제로 두고, In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary querying in 3D space is crucial for enabling more intelligent perception in applications such as robotics, autonomous systems, and augmented reality.
- **p. 1 / Abstract - extractive body cue:** However, most existing methods rely on 2D pixel-level parsing, leading to multi-view inconsistencies and poor 3D object retrieval.
- **p. 1 / Abstract - extractive body cue:** Moreover, they are limited to static scenes and struggle with dynamic scenes due to the complexities of motion modeling.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** Segment then Splat reverses the long established approach of "segmentation after reconstruction" by dividing Gaussians into distinct object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied ...
- **p. 1 / 1 Introduction - extractive body cue:** 2) Failure to capture true 3D object information, complicating 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This enables unified static/dynamic open-vocabulary segmentation, eliminates auxiliary language fields, and significantly reduces training complexity. • Our framework features a robust object tracking module that ...
- **p. 4 / 3 Method - extractive body cue:** We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 5 / 3 Method - extractive body cue:** To capture newly appearing objects, we introduce a detection mechanism at fixed intervals of ∆t.
- **p. 6 / 3 Method - extractive body cue:** To robustly address this, we propose a partial mask filtering strategy applied at the end of training.
- **p. 4 / 3 Method - extractive body cue:** Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents ...
- **p. 6 / 3 Method - extractive body cue:** 1 101 2 101 3 101 4 102 5 102 6 102 : Small-Level ID : Mid-Level ID Optimize small-level first Supervise Small-level Objects 1 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | "Chopsticks" Initialized Objectspecific Gaussians Reconstruction Rasterize Object Query Result Trained Objectspecific Gaussians "Chopsticks" Gaussians CLIP Rasterize Rendered Image & 2D Feature Map Queried 2D Mask Object Query Result Sf ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 4 (3 Method) |
| State/latent | Chopsticks, Initialized, Objectspecific, Gaussians, Reconstruction, Rasterize, Object, Query, Result, Trained, CLIP, Rendered | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method) |
| Output/action | Following Deformable 3D Gaussian Splatting [17], we incorporate a deformation field to capture scene dynamics: (δx, δr, δs) = Fθ(γ(x), γ(t)), (3) where Fθ represents deformation field, which takes Gaussian mean x ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | Given an input text prompt, we perform open vocabulary query following the below strategy: fq = CLIPt(q), (10) qreturn = arg max p cos(fq, fp), (11) where fq is the CLIP embedding ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This enables unified static/dynamic open-vocabulary segmentation, eliminates auxiliary language fields, and significantly reduces training complexity. • Our framework features a robust object tracking module that ...
- **p. 4 / 3 Method - extractive body cue:** We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 5 / 3 Method - extractive body cue:** To capture newly appearing objects, we introduce a detection mechanism at fixed intervals of ∆t.
- **p. 8 / 4 Experiments - extractive body cue:** Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results.
- **p. 9 / 4 Experiments - extractive body cue:** In addition, our method achieves nearly a ten-fold improvement in optimization speed compared to DGD, as learning a dynamic language field is computationally intensive.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative comparison on dynamic scenes. As our method enforce object-Gaussian correspondence, it applies directly to dynamic scenes and performs well, whereas DGD and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 55.90 G-Grouping [36] 29.59 77.00 76.24 56.10 3D LangSplat [10] ... | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | In contrast, scenes with fewer objects (e.g., chickchicken, split-cookie) exhibit a smaller performance gain. | role, split, size and leakage | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments) |
| Metric | Leveraging ground-truth labels, we adopt two metrics: Object Recall Rate (ORR), defined as ORR = 1 k k X i=1 number of tracked objects number of GT objects , (12) where k ... | definition, denominator, direction and uncertainty | p. 10 (4 Experiments), p. 2 (Figure/Table caption), p. 8 (4 Experiments) |
| Baseline/ablation | Our method outperforms all baseline approaches. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 Conclusion - extractive body cue:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair ...
- **p. 10 / 4 Experiments - extractive body cue:** However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views.
- **p. 9 / 4 Experiments - extractive body cue:** Moreover, because DGD does not directly supervise the language embeddings of each Gaussian, Gaussians located far apart may share similar embeddings, further deteriorating segmentation quality.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Demonstration of Segment then Splat pipeline. We first extracts multi-view masks for each object through a robust tracking module, then object IDs are ...
- **p. 8 / 4 Experiments - extractive body cue:** The new object detection stride ∆t in the robust object tracking is set to 10.
- **p. 8 / 4 Experiments - extractive body cue:** Unlike 2D pixel-based methods, which are limited by occlusions, our approach can retrieve the complete object even from an occluded view.
- **p. 9 / 4 Experiments - extractive body cue:** Besides, both LSeg and DGD fail when retrieving relatively small objects (e.g., bunny painting).

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied to dynamic scenes.를 문제로 두고, In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
