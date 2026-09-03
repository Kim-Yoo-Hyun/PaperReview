# DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We address this problem by introducing a novel Failureto-Prior paradigm.를 문제로 두고, Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can be mined into priors.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While 3D Gaussian Splatting (3DGS) achieves realtime photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency.
- **p. 1 / Abstract - extractive body cue:** Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks.
- **p. 1 / Abstract - extractive body cue:** We address this challenge with DualSplat, a Failure-toPrior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage.
- **p. 1 / Abstract - extractive body cue:** We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training.
- **p. 1 / Abstract - extractive body cue:** We exploit these failures to construct object-level pseudo-masks by combining photometric residuals, feature mismatches, and SAM2 instance boundaries.
- **p. 2 / 1. Introduction - extractive body cue:** We address this problem by introducing a novel Failureto-Prior paradigm.
- **p. 2 / 1. Introduction - extractive body cue:** These failure patterns can be explicitly mined as cues for transient discovery.

## Core Idea

- **p. 3 / 3.2. Overview - extractive body cue:** Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can be ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows:
- **p. 2 / 1. Introduction - extractive body cue:** We address this problem by introducing a novel Failureto-Prior paradigm.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** We use DINOv2 [17] as the feature extraction backbone.
- **p. 4 / 3.2. Overview - extractive body cue:** FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization.
- **p. 4 / 3.2. Overview - extractive body cue:** After the first training, Mask Filter produces confidence-weighted pseudo-masks.
- **p. 3 / 3.2. Overview - extractive body cue:** We begin by training an initial 3DGS model and comparing each rendered image with its ground-truth training view.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad flow Local Masks SAM2 Instance Masks First ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |
| State/latent | FiT3D, Training, images, Render, Cosine, Similarity, Threshold, Filtering, Pseudo-Masks, MLP, stop, grad | geometry, map, object/relationship state | p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 2 (1. Introduction) |
| Output/action | We therefore introduce a lightweight per-pixel MLP that predicts a transient probability map online during the second reconstruction: Mi = MLPmask(fi, di), (10) where fi denotes cached image features from the groundtruth ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 2 (1. Introduction), p. 4 (3.2. Overview) |
| Objective/outcome | The Gaussian parameters are optimized by minimizing the photometric reconstruction loss between the rendered image and its reference image: L = (1 -λD-SSIM) L1 + λD-SSIMLD-SSIM, (1) where λD-SSIM balances pixel-wise L1 ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 4 (3.2. Overview) |

## Main Claims and Actual Contribution

- **p. 3 / 3.2. Overview - extractive body cue:** Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can be ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows:
- **p. 2 / 1. Introduction - extractive body cue:** We address this problem by introducing a novel Failureto-Prior paradigm.
- **p. 6 / 4.2. Distractor-free 3D Reconstruction - extractive body cue:** DualSplat achieves the best overall average performance.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity and ...
- **p. 7 / 4.2. Distractor-free 3D Reconstruction - extractive body cue:** Although the margins are modest and some individual scenes are still led by competing methods, our method remains consistently competitive across all five scenes and ...
- **p. 2 / 4. We conduct comprehensive experiments on Robust - extractive body cue:** NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes.
- **p. 6 / 4.1. Setups - extractive body cue:** Qualitative results on Spot and Mountain from the NeRF On-the-go dataset.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption) |
| Embodiment/environment | These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality. | hardware/simulator version and reset protocol | p. 5 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction) |
| Dataset/benchmark | NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes. | role, split, size and leakage | p. 5 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust), p. 5 (4.1. Setups) |
| Metric | Table 6. Comparison of different feature extraction models. Methods Accuracy Precision Recall IoU Ours* 0.988 | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 2 (4. We conduct comprehensive experiments on Robust) |
| Baseline/ablation | 4.2, we compare our method against 3DGSbased baselines using both quantitative metrics and qualitative visualizations. | fair input/data/compute/action matching | p. 5 (4.1. Setups), p. 6 (4.2. Distractor-free 3D Reconstruction), p. 6 (4.2. Distractor-free 3D Reconstruction) |

## Explicit Limitations and Failure Boundary

- **p. 2 / 1. We propose a Failure-to-Prior paradigm for transient - extractive body cue:** robust 3DGS that breaks the circular dependency between transient detection and scene reconstruction by converting first-pass reconstruction failures into explicit priors.
- **p. 4 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** The primary objective of this step is to translate these firstpass failures into reliable object-level priors for the second reconstruction stage, rather than directly outputting ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. These failure patterns can be explicitly mined as cues for transient discovery. Specifically, we first perform a conservative 3DGS reconstruction to expose failure ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comparison of paradigms and mechanisms. Item Online suppression methods Ours(DualSplat) Paradigm Online Heuristic (Internal) Failure-to-Prior (External Guidance) Dependency
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (15) The final MLP objective is LMLP = λrobustLrobust + λpriorLprior + Lreg.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** These loss functions are combined as: Lrobust = exp  -max(0, Tdensify -t) βrobustness  (Lcos + Lres) .
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. DualSplat performs two-stage 3D Gaussian Splatting to suppress transient distractions. The first stage reconstructs a coarse static scene. After the first training, Mask ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We address this problem by introducing a novel Failureto-Prior paradigm.를 문제로 두고, Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can be mined into priors.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
