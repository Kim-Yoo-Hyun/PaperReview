# No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=P4o9akekdf.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/111453. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://openreview.net/forum?id=P4o9akekdf
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/111453
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The performance gap stems from their sequential process of alternating between pose estimation and scene reconstruction.를 문제로 두고, The main contributions of this work are: • We propose NoPoSplat, a feed-forward network that reconstructs 3D scenes parameterized by 3D Gaussians from unposed sparse-view inputs, and demonstrate that it can be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We introduce NoPoSplat, a feed-forward model capable of reconstructing 3D scenes parameterized by 3D Gaussians from unposed sparse multi-view images.
- **p. 1 / ABSTRACT - extractive body cue:** Our model, trained exclusively with photometric loss, achieves real-time 3D Gaussian reconstruction during inference.
- **p. 1 / ABSTRACT - extractive body cue:** To eliminate the need for accurate pose input during reconstruction, we anchor one input view's local camera coordinates as the canonical space and train the ...
- **p. 1 / ABSTRACT - extractive body cue:** This approach obviates the need to transform Gaussian primitives from local coordinates into a global coordinate system, thus avoiding errors associated with per-frame Gaussians and ...
- **p. 1 / ABSTRACT - extractive body cue:** To resolve scale ambiguity, we design and compare various intrinsic embedding methods, ultimately opting to convert camera intrinsics into a token embedding and concatenate it ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The performance gap stems from their sequential process of alternating between pose estimation and scene reconstruction.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent methods (Chen & Lee, 2023; Smith et al., 2023; Hong et al., 2024a) aim to address this challenge by integrating pose estimation and 3D ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** The main contributions of this work are: • We propose NoPoSplat, a feed-forward network that reconstructs 3D scenes parameterized by 3D Gaussians from unposed sparse-view ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Since our method does not require camera poses for input images, it can be applied to user-provided images to reconstruct the underlying 3D scene and ...
- **p. 4 / 3 METHOD - extractive body cue:** By training on large-scale datasets, our method can generalize to novel scenes without any optimization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For pose estimation, we introduce a two-stage pipeline: first, we obtain an initial pose estimate by applying the PnP algorithm (Hartley & Zisserman, 2003) to ...
- **p. 4 / 3 METHOD - extractive body cue:** 3.2 PIPELINE Our method, illustrated in Fig.
- **p. 5 / 3 METHOD - extractive body cue:** Next, the output features from the encoder are fed into a ViT decoder module, where features from each view interact with those from all other ...
- **p. 5 / 3 METHOD - extractive body cue:** The first head focuses on predicting the Gaussian center positions and utilizes features extracted exclusively from the transformer decoder.
- **p. 6 / 3 METHOD - extractive body cue:** Next, while keeping Gaussian parameters frozen, we refine the initial pose from the first step by optimizing the same photometric losses used for model training, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.3 ANALYSIS OF THE OUTPUT GAUSSIAN SPACE While our method shares a similar spirit with previous works (Charatan et al., 2024; Zheng et al., 2024; Szymanowicz et al., 2024) in predicting pixelwise ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| State/latent | ANALYSIS, OUTPUT, GAUSSIAN, SPACE, While, shares, similar, spirit, previous, works, Charatan, Zheng | geometry, map, object/relationship state | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 15 (A MORE IMPLEMENTATION DETAILS) |
| Output/action | First, we estimate the initial related camera pose of the input two views using the PnP algorithm (Hartley & Zisserman, 2003) with RANSAC (Fischler & Bolles, 1981), given the Gaussian centers of ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 METHOD), p. 15 (A MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| Objective/outcome | Both encoder and decoder utilize pure Vision Transformer (ViT) structures, without injecting any geometric priors (e.g. epipolar constraints employed in pixelSplat (Charatan et al., 2024), or cost volumes in MVSplat (Chen et ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** The main contributions of this work are: • We propose NoPoSplat, a feed-forward network that reconstructs 3D scenes parameterized by 3D Gaussians from unposed sparse-view ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Since our method does not require camera poses for input images, it can be applied to user-provided images to reconstruct the underlying 3D scene and ...
- **p. 4 / 3 METHOD - extractive body cue:** By training on large-scale datasets, our method can generalize to novel scenes without any optimization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For pose estimation, we introduce a two-stage pipeline: first, we obtain an initial pose estimate by applying the PnP algorithm (Hartley & Zisserman, 2003) to ...
- **p. 4 / 3 METHOD - extractive body cue:** 3.2 PIPELINE Our method, illustrated in Fig.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** On the other hand, we achieve competitive performance over SOTA pose-required methods (Charatan et al., 2024; Chen et al., 2024), and even outperform them when ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 13, the performance significantly improves with the inclusion of the additional view.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4, NoPoSplat significantly outperforms all SOTA pose-free approaches.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Embodiment/environment | Small Medium Large Average Method PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓ PoseRequired pixelNeRF 19.376 0.535 0.564 20.339 0.561 0.537 20.826 0.576 0.509 20.323 0.561 0.533 AttnRend 20.942 0.616 0.398 24.004 0.7 ... | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | To further scale up our model (denoted as Ours*), we also combine RE10K with DL3DV (Ling et al., 2024), which is an outdoor dataset containing 10K videos, which includes a wider variety ... | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | For pose estimation, we report the area under the cumulative pose error curve (AUC) with thresholds of 5◦, 10◦, 20◦(Sarlin et al., 2020; Edstedt et al., 2024). | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | Compared to baselines, we obtain: 1) more coherent fusion from input views, 2) superior reconstruction from limited image overlap, 3) enhanced geometry reconstruction in non-overlapping regions. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 16 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: RealEstate10k performance with different number of input views. Addtional Comparison with Splatt3R. In Tab.1 of the main paper, we compare our method with ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** While our method currently applies only to static scenes, extending our pipeline to dynamic scenarios presents an interesting direction for future work.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Note that DUSt3R (and MASt3R) struggle to fuse input views coherently due to their reliance on per-pixel depth loss, a limitation Splatt3R also inherits from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Comparison with pose-required sparse-view 3D Gaussian splatting pipeline. Previ- ous methods first generate Gaussians in each local camera coordinate system and then transform ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Furthermore, our method does not require an explicit matching loss during training, meaning no ground truth depth is necessary.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** These issues are largely due to the noises introduced in their transform-then-fuse pipeline.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Our model can better zero-shot transfer to out-ofdistribution data than SOTA pose-required methods. strates superior performance on out-of-distribution data compared to SOTA pose-required methods.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The performance gap stems from their sequential process of alternating between pose estimation and scene reconstruction.를 문제로 두고, The main contributions of this work are: • We propose NoPoSplat, a feed-forward network that reconstructs 3D scenes parameterized by 3D Gaussians from unposed sparse-view inputs, and demonstrate that it can be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
