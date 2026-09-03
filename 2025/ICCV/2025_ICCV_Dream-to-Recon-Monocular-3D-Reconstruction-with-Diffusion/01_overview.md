# Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, depth, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, such 3D ground truth is difficult and expensive to obtain, e.g. by accumulating Lidar scans from a This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, Furthermore, we show that our method has unique advantages when it comes to dynamic scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Volumetric scene reconstruction from a single image is crucial for a broad range of applications like autonomous driving and robotics.
- **p. 1 / Abstract - extractive body cue:** Recent volumetric reconstruction methods achieve impressive results, but generally require expensive 3D ground truth or multi-view supervision.
- **p. 1 / Abstract - extractive body cue:** We propose to leverage pre-trained 2D diffusion models and depth prediction models to generate synthetic scene geometry from a single image.
- **p. 1 / Abstract - extractive body cue:** This can then be used to distill a feed-forward scene reconstruction model.
- **p. 1 / Abstract - extractive body cue:** Our experiments on the challenging KITTI-360 and Waymo datasets demonstrate that our method matches or outperforms state-of-the-art baselines that use multi-view supervision, and offers unique ...
- **p. 1 / 1. Introduction - extractive body cue:** However, such 3D ground truth is difficult and expensive to obtain, e.g. by accumulating Lidar scans from a This ICCV paper is the Open Access ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the generated geometry, which is important for many downstream tasks, is still lacking in quality.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our method has unique advantages when it comes to dynamic scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • A specialized view completion model that inpaints and refines synthetic novel views and which can be trained using only a single ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For a given scene, our method receives as input a single image Iin ∈([0, 1]3)Ω, where Ω= {1, . . . , H} × {1, ...
- **p. 1 / 1. Introduction - extractive body cue:** A dense reconstruction of the environment enables machines to react to their surroundings and to reason about further actions such as path planning.
- **p. 4 / 3.3. Synthesizing Scene Geometry - extractive body cue:** Throughout our approach, we consider a continuous synthetic occupancy field ΘV(x) : R3 →{0, 1}, which maps every point x ∈R3 in the scene to ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction ...
- **p. 5 / 3.4. Distilling into a Scene Reconstruction Model - extractive body cue:** The loss term provides training signals to the surface areas of the predicted density field, which are particularly hard to learn. \mat h c al ...
- **p. 4 / 3.2. Training the View Completion Model - extractive body cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an input image Iin and predicted depth DIin, we first warp the pixels into a virtual novel view with a random camera pose. | conditioning observation와 noisy/intermediate sample | p. 3 (3.2. Training the View Completion Model), p. 4 (3.2. Training the View Completion Model) |
| State/latent | Given, input, image, Iin, predicted, depth, DIin, first, warp, pixels, virtual, novel | latent/noise variable와 conditional distribution | p. 3 (3.2. Training the View Completion Model), p. 4 (3.2. Training the View Completion Model), p. 2 (1. Introduction) |
| Output/action | Training uses only a single view per scene and leverages forward-backward warping for data generation. b) The VCM is applied iteratively alongside a depth prediction network to synthesize virtual novel views, enabling ... | generated sample, action chunk 또는 trajectory | p. 4 (3.2. Training the View Completion Model), p. 2 (1. Introduction), p. 3 (3.2. Training the View Completion Model) |
| Objective/outcome | We then directly supervise them via the depth predictions Di from V using a Gaussian Negative Log-Likelihood (GNLL) loss, as proposed in [46]. | distribution fit, multimodality, sample quality와 latency | p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model), p. 4 (3.3. Synthesizing Scene Geometry) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our method has unique advantages when it comes to dynamic scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • A specialized view completion model that inpaints and refines synthetic novel views and which can be trained using only a single ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For a given scene, our method receives as input a single image Iin ∈([0, 1]3)Ω, where Ω= {1, . . . , H} × {1, ...
- **p. 1 / 1. Introduction - extractive body cue:** A dense reconstruction of the environment enables machines to react to their surroundings and to reason about further actions such as path planning.
- **p. 4 / 3.3. Synthesizing Scene Geometry - extractive body cue:** Throughout our approach, we consider a continuous synthetic occupancy field ΘV(x) : R3 →{0, 1}, which maps every point x ∈R3 in the scene to ...
- **p. 6 / 4.2. Scene Reconstruction - extractive body cue:** We contend that, despite being slightly outperformed in quantitative metrics by the directly synthesized geometry, the distilled model is more reliable and significantly faster.
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive body cue:** A camera rig with eight predefined poses and random rotations achieves the best performance. leverages two-way optical flow between the input and novel views to ...
- **p. 6 / 4.2. Scene Reconstruction - extractive body cue:** We hypothesize that this lack of improvement stems from the strong depth cues already inherent in multi-view data.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.2. Occlusion detection in novel views) |
| Embodiment/environment | Both datasets contain scenes with complex layouts and possibly dynamic objects. | hardware/simulator version and reset protocol | p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction) |
| Dataset/benchmark | We test our method on the challenging KITTI-360 [31] and Waymo [54] self-driving datasets. | role, split, size and leakage | p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction), p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction) |
| Metric | The accuracy and robustness of our occlusion detection strategy directly influence the effectiveness of refining incomplete novel views using VCM. | definition, denominator, direction and uncertainty | p. 7 (4.3.2. Occlusion detection in novel views), p. 6 (4.1. Setup), p. 6 (4.1. Setup) |
| Baseline/ablation | Here, the state-of-the-art volumetric reconstruction methods Behind the Scenes (BTS) [60] and Know Your Neighbor (KYN) [27] serve as baselines. | fair input/data/compute/action matching | p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM), p. 6 (4.1. Setup) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Scene Reconstruction - extractive body cue:** This failure stems from their use of multi-view data across multiple timesteps, which introduces inconsistency when the object is in motion.
- **p. 6 / 4.2. Scene Reconstruction - extractive body cue:** Since depth prediction cannot reason about occluded areas, we do not report the IEacc and IErec metrics.
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive body cue:** The fused strategy mitigates some of the false positives compared to optical flow alone but still inherits many of its limitations.
- **p. 7 / 4.3.2. Occlusion detection in novel views - extractive body cue:** The accuracy and robustness of our occlusion detection strategy directly influence the effectiveness of refining incomplete novel views using VCM.
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive body cue:** 5, the depth gradient method robustly captures occlusions without requiring extensive post-filtering.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, such 3D ground truth is difficult and expensive to obtain, e.g. by accumulating Lidar scans from a This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, Furthermore, we show that our method has unique advantages when it comes to dynamic scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Training the View Completion Model), p. 5 (3.4. Distilling into a Scene Reconstruction Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
