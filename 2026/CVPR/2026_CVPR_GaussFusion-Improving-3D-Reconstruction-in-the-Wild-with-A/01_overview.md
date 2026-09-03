# GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by generating dense novel-view images.를 문제로 두고, Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction pipelines. • A comprehensive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- **p. 1 / Abstract - extractive body cue:** GaussFusion mitigates common 3DGS artifacts, including floaters, flickering, and blur caused by camera pose errors, incomplete coverage, and noisy geometry initialization.
- **p. 1 / Abstract - extractive body cue:** Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometryinformed video-to-video generator that refines 3DGS renderings across both optimization-based and ...
- **p. 1 / Abstract - extractive body cue:** Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, ...
- **p. 1 / Abstract - extractive body cue:** We further introduce an artifact synthesis pipeline that simulates diverse degradation patterns, ensuring robustness and generalization.
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by ...
- **p. 2 / 1. Introduction - extractive body cue:** Similarly, MVSplat360 [7] refines feed-forward reconstructions but fails to generalize to optimization-based pipelines, as it is tightly coupled to a specific feed-forward model [6].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** We present GaussFusion, a video-to-video generative model for robust 3D reconstruction that features as key component the GP-Buffer, a pixel-aligned video representation that encodes multi-modal ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The contribution γi is the product of the learned opacity αi and the 2D Gaussian function evaluated at the pixel center u with projected mean ...
- **p. 1 / 1. Introduction - extractive body cue:** Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous driving, and robotics.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** 3.3) along this trajectory to obtain novel renderings, which are then refined by our geometry-aware video generator to produce artifactfree frames.
- **p. 5 / 3.4. 3D Reconstruction Updating - extractive body cue:** Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2) Feed-Forward 3DGS Reconstruction Models learn to directly predict a complete set of 3D Gaussian parameters from a small set of posed/unposed input images [4, 58, 60, 68]. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries) |
| State/latent | Feed-Forward, DGS, Reconstruction, Models, learn, directly, predict, complete, Gaussian, parameters, small, posed/unposed | geometry, map, object/relationship state | p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 5 (3.4. 3D Reconstruction Updating) |
| Output/action | Given a target sample x1 (e.g., image or video), random noise x0 ∼N(0, I), and a timestep t ∈[0, 1], the intermediate latent xt is defined by: xt = tx1 + (1 ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminaries), p. 5 (3.4. 3D Reconstruction Updating), p. 2 (1. Introduction) |
| Objective/outcome | Finally, we merge the generated novel views with the original inputs and optimize the 3D Gaussian splats using the standard photometric loss (Eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** We present GaussFusion, a video-to-video generative model for robust 3D reconstruction that features as key component the GP-Buffer, a pixel-aligned video representation that encodes multi-modal ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The contribution γi is the product of the learned opacity αi and the 2D Gaussian function evaluated at the pixel center u with projected mean ...
- **p. 1 / 1. Introduction - extractive body cue:** Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous driving, and robotics.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...
- **p. 6 / 15.11 FPS - extractive body cue:** The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with significantly ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization or ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative Comparison on 3D Reconstruction. We show the novel-view renderings from the improved 3D reconstruc- tion refined using enhanced views from different methods. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (15.11 FPS), p. 1 (Figure/Table caption) |
| Embodiment/environment | Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training. | hardware/simulator version and reset protocol | p. 6 (15.11 FPS), p. 7 (5.1. Results) |
| Dataset/benchmark | Rendering Refinement Performance on DL3DV and RE10K Datasets. | role, split, size and leakage | p. 6 (15.11 FPS), p. 7 (5.1. Results), p. 6 (15.11 FPS), p. 7 (5.1. Results) |
| Metric | A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and minor loss of high-frequency details. | definition, denominator, direction and uncertainty | p. 7 (5.1. Results), p. 7 (5.1. Results), p. 8 (5.2. Ablation Studies) |
| Baseline/ablation | The model trained exclusively on DL3DV outperforms all baselines trained on the same dataset by a substantial margin in terms of image quality. | fair input/data/compute/action matching | p. 6 (5.1. Results), p. 8 (5.1. Results), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** We discuss our limitations and future work in Supp.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization or ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising color, ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** 4), which combines optimization- and feed-forward degradations while injecting pose and coverage diversity.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by generating dense novel-view images.를 문제로 두고, Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction pipelines. • A comprehensive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
