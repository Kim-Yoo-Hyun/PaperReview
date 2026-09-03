# SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=GtImvTta8x.
> PDF retrieval source: https://arxiv.org/pdf/2507.02705. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=GtImvTta8x
- Full-text retrieval: https://arxiv.org/pdf/2507.02705
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the aforementioned approaches inherently have the following limitations due to the nature of 2D-to-3D feature alignment.를 문제로 두고, Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D cross-view masks, Mutual Benefit ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Simultaneous understanding and 3D reconstruction plays an important role in developing end-to-end embodied intelligent systems.
- **p. 1 / Abstract - extractive body cue:** To achieve this, recent approaches resort to 2D-to-3D feature alignment paradigm, which leads to limited 3D understanding capability and potential semantic information loss.
- **p. 1 / Abstract - extractive body cue:** In light of this, we propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction from unposed images.
- **p. 1 / Abstract - extractive body cue:** Specifically, SIU3R bridges reconstruction and understanding tasks via pixel-aligned 3D representation, and unifies multiple understanding (segmentation) tasks into a set of unified learnable queries, enabling ...
- **p. 1 / Abstract - extractive body cue:** To encourage collaboration between the two tasks with ∗Qi Xu and Dongxu Wei contributed equally; † Corresponding author; This work was performed when Qi Xu ...
- **p. 2 / 1 Introduction - extractive body cue:** However, the aforementioned approaches inherently have the following limitations due to the nature of 2D-to-3D feature alignment.
- **p. 2 / 1 Introduction - extractive body cue:** Despite their individual successes, a critical gap remains: current frameworks often treat reconstruction and understanding as separate tasks, hindering the development of end-to-end embodied intelligence ...

## Core Idea

- **p. 4 / 3 Methodology - extractive body cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions are as follows: • We propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction, which bridges ...
- **p. 6 / 3 Methodology - extractive body cue:** 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline.
- **p. 2 / 1 Introduction - extractive body cue:** To address the challenges outlined above, we propose SIU3R, a novel generalizable framework achieving SIMULTANEOUS UNDERSTANDING and 3D RECONSTRUCTION beyond feature alignment (Fig.1 b).
- **p. 3 / 1 Introduction - extractive body cue:** To encourage the bidirectional promotion between the two tasks, we incorporate two lightweight modules into our pipeline and achieve significant performance improvements in both tasks. ...
- **p. 6 / 3 Methodology - extractive body cue:** Specifically, we propose Multi-View Mask Aggregation module, which first lifts 2D semantic information (i.e., query logits M and C) from different views to the 3D ...
- **p. 6 / 3 Methodology - extractive body cue:** Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians Q, M, C ...
- **p. 4 / 3 Methodology - extractive body cue:** Moreover, to improve reconstruction by understanding, we introduce Mask-Guided Geometry Refinement module that leverages 2D masks to enforce intrainstance depth continuity for refining reconstructed 3D ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1 Pixel-aligned 2D-to-3D lifting for simultaneous understanding and 3D recontruction. /* Model forward pass */ G ←Gaussian Decoder ▷Pixel-aligned 3D Gaussians Q, M, C ←Unified Query Decoder ▷Last-layer hidden states of ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3 Methodology), p. 3 (3 Methodology) |
| State/latent | Algorithm, Pixel-aligned, D-to-3D, lifting, simultaneous, understanding, recontruction, Model, forward, pass, Gaussian, Decoder | geometry, map, object/relationship state | p. 6 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology) |
| Output/action | 3.1 Problem Formulation and Pipeline SIU3R processes sparse unposed multi-view images with corresponding camera intrinsics {Iv, Kv}V v=1, where V ≥2 in our setting and denotes the number of input context views, ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology) |
| Objective/outcome | 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology) |

## Main Claims and Actual Contribution

- **p. 4 / 3 Methodology - extractive body cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions are as follows: • We propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction, which bridges ...
- **p. 6 / 3 Methodology - extractive body cue:** 3.4 Training Objective Through holistic integration of components, our framework enables end-to-end optimization across the complete learning pipeline.
- **p. 2 / 1 Introduction - extractive body cue:** To address the challenges outlined above, we propose SIU3R, a novel generalizable framework achieving SIMULTANEOUS UNDERSTANDING and 3D RECONSTRUCTION beyond feature alignment (Fig.1 b).
- **p. 3 / 1 Introduction - extractive body cue:** To encourage the bidirectional promotion between the two tasks, we incorporate two lightweight modules into our pipeline and achieve significant performance improvements in both tasks. ...
- **p. 9 / 4 Experiments - extractive body cue:** We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ Figure 6: Ablation ...
- **p. 9 / 4 Experiments - extractive body cue:** As demonstrated in Fig.5 (b), thanks to our simultaneous task modeling and Multi-View Mask Aggregation mechanism, our method can effectively leverage geometric clues to improve ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative Results. that can achieve 3D-aware understanding is LSM. However, its understanding capability is restricted by its source 2D model (LSeg) due to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | We adopt the official training and validation dataset splitting of ScanNet, and then resize and crop original images to centered images at 256 × 256 resolution. | hardware/simulator version and reset protocol | p. 15 (A.1 Data Preprocessing), p. 7 (4 Experiments) |
| Dataset/benchmark | We also conduct experiments to validate the generalizability of our method to more input views, unseen data domains and real-world scenarios. | role, split, size and leakage | p. 15 (A.1 Data Preprocessing), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Metric | For 3D reconstruction, we evaluate the performance from two aspects: depth estimation and novel view synthesis, using depth accuracy metrics (i.e., AbsRel and RMSE) and image quality metrics (i.e., PSNR, SSIM and ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | Therefore, we evaluate our method against three types of baseline methods, all of which are state-of-the-arts on their respective tasks: 1) Sparse-view 3D reconstruction: pixelSplat[29], MVSplat[30], NoPoSplat[37]; 2) Scene understandin ... | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3 Methodology - extractive body cue:** In general, adjacent 2D pixels within the same object instance or semantic region should correspond to continuous positions in 3D space.
- **p. 6 / 3 Methodology - extractive body cue:** Leveraging this prior knowledge, we can use our mask predictions as semantic clues to refine the reconstructed 3D geometries.
- **p. 6 / 3 Methodology - extractive body cue:** We call this "Understanding Helps Reconstruction (U→R)".

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the aforementioned approaches inherently have the following limitations due to the nature of 2D-to-3D feature alignment.를 문제로 두고, Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D cross-view masks, Mutual Benefit ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
