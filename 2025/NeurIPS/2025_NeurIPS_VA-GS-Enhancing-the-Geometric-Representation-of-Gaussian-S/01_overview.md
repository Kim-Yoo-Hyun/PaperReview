# VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ZnsR3waLUo.
> PDF retrieval source: https://arxiv.org/pdf/2510.11473. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=ZnsR3waLUo
- Full-text retrieval: https://arxiv.org/pdf/2510.11473
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, 2DGS has difficulty reconstructing background geometry and often produces incomplete or distorted surfaces in complex or unbounded scenes.를 문제로 두고, Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning the robust priors based on nor ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting has recently emerged as an efficient solution for highquality and real-time novel view synthesis.
- **p. 1 / Abstract - extractive body cue:** However, its capability for accurate surface reconstruction remains underexplored.
- **p. 1 / Abstract - extractive body cue:** Due to the discrete and unstructured nature of Gaussians, supervision based solely on image rendering loss often leads to inaccurate geometry and inconsistent multi-view alignment.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose a novel method that enhances the geometric representation of 3D Gaussians through view alignment (VA).
- **p. 1 / Abstract - extractive body cue:** Specifically, we incorporate edge-aware image cues into the rendering loss to improve surface boundary delineation.
- **p. 1 / 1 Introduction - extractive body cue:** However, 2DGS has difficulty reconstructing background geometry and often produces incomplete or distorted surfaces in complex or unbounded scenes.
- **p. 1 / 1 Introduction - extractive body cue:** This limitation stems from the inherent discrete and unstructured nature of Gaussians, which makes it difficult to enforce global surface consistency or capture fine geometric ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose a novel method for accurate and detailed surface reconstruction by enhancing the geometric representation of 3D Gaussians.
- **p. 4 / 4 Method - extractive body cue:** We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.
- **p. 4 / 4 Method - extractive body cue:** To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = ...
- **p. 6 / 4 Method - extractive body cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 6 / 4 Method - extractive body cue:** Then the pixel-wise feature alignment loss is defined as: Lf = 1 N X Fs∈{Fs,i} 1 V X pr∈Ir υrs(pr) · ω(pr) ·
- **p. 5 / 4 Method - extractive body cue:** To address these, we use a normal smoothing loss that encourages local continuity of surface normals by penalizing large discrepancies between adjacent pixels: Lns = ...
- **p. 5 / 4 Method - extractive body cue:** By introducing a photometric consistency loss based on plane patches, we leverage multi-view observations to resolve geometric ambiguities, particularly at object boundaries, and enhance reconstruction ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a set of posed RGB images, our goal is to learn a bunch of 3D Gaussian functions with associated attributes, such as color, opacity, position and shape, to represent the geometry ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4 Method), p. 5 (4 Method) |
| State/latent | Given, posed, RGB, images, goal, learn, bunch, Gaussian, functions, associated, attributes, color | geometry, map, object/relationship state | p. 4 (4 Method), p. 5 (4 Method), p. 2 (1 Introduction) |
| Output/action | 1 , (4) where δ = (1 -∇I)2 serves as a per-pixel weight [4] that downweights loss contributions from edge regions, and I denotes the set of image pixels. ˜ N is ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (4 Method), p. 2 (1 Introduction), p. 5 (4 Method) |
| Objective/outcome | To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = (1 -β1)L1( ˜I -I) + β1LSSIM( ˜I ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4 Method), p. 5 (4 Method), p. 4 (4 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose a novel method for accurate and detailed surface reconstruction by enhancing the geometric representation of 3D Gaussians.
- **p. 4 / 4 Method - extractive body cue:** We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.
- **p. 4 / 4 Method - extractive body cue:** To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = ...
- **p. 6 / 4 Method - extractive body cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 8 / 5 Experiments - extractive body cue:** Although our method is slightly slower than 3DGS [21] and 2DGS [16] due to the use of multi-view alignment, it achieves significant improvements in reconstruction ...
- **p. 8 / 5 Experiments - extractive body cue:** As shown in Table 2, our method achieves the best reconstruction performance among all competing approaches, including both implicit and explicit methods.
- **p. 7 / 5 Experiments - extractive body cue:** As shown in Table 1, our method achieves the lowest average Chamfer distance and ranks best across most scenes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Embodiment/environment | Following prior works [16, 56, 4, 57], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation. | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Dataset/benchmark | Consistent with our observations on the TNT dataset, our method recovers more accurate and complete surfaces in both foreground and background regions, whereas other methods suffer from noise, oversmoothing, or missing details, ... | role, split, size and leakage | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Metric | Precision ↑Recall ↑F1-score ↑ Only LI 0.09 0.23 0.13 w/o edge item 0.49 0.59 0.53 w/o weight δ 0.50 0.59 0.53 w/o Lnc 0.48 0.60 0.52 w/o Lns 0.47 0.58 0.51 w/o ... | definition, denominator, direction and uncertainty | p. 9 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments) |
| Baseline/ablation | We first compare our method with state-of-the-art implicit and explicit surface reconstruction approaches on the DTU dataset [18]. | fair input/data/compute/action matching | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Our method addresses illumination and boundary artifacts that previous methods fail to resolve. In this work, we propose a novel method for accurate ...
- **p. 5 / 4 Method - extractive body cue:** The definitions of υrs(pr) and ω(pr) are detailed in the following. • Due to viewpoint changes, a 2D pixel pr in the reference view may ...
- **p. 6 / 4 Method - extractive body cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visual comparison of surface reconstruction results on the Deep Blending dataset. Our method effectively handles the challenges posed by complex lighting conditions and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item υ ...
- **p. 6 / 4 Method - extractive body cue:** However, image-based losses are susceptible to noise, blur, and low-texture regions.
- **p. 8 / 5 Experiments - extractive body cue:** It also effectively mitigates the impact of shadows, whereas baseline methods often yield noisy meshes or fail to capture geometric details.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, 2DGS has difficulty reconstructing background geometry and often produces incomplete or distorted surfaces in complex or unbounded scenes.를 문제로 두고, Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • Aligning the robust priors based on nor ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (4 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
