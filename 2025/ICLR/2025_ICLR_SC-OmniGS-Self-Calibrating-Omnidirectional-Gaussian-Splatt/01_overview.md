# SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=7idCpuEAiR.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/113436. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://openreview.net/forum?id=7idCpuEAiR
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/113436
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need for a framework that calibrates the omnidirectional ...를 문제로 두고, To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera models. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 360-degree cameras streamline data collection for radiance field 3D reconstruction by capturing comprehensive scene data.
- **p. 1 / ABSTRACT - extractive body cue:** However, traditional radiance field methods do not address the specific challenges inherent to 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Rather than converting 360-degree images to cube maps and performing perspective image calibration, we treat 360-degree images as a whole sphere and derive a mathematical ...
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing methods for recovering 3D information from 360-degree images, including structure-from-motion (SfM) systems (Moulon et al., 2013; Huang & Yeung, 2022), rely on an idealized ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SC-OmniGS, a novel system that self-calibrates the omnidirectional camera model and poses along with omnidirectional radiance field reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, considering omnidirectional images in the equirectangular projection have an unbalanced spatial resolution, we introduce weighted spherical photometric loss to ensure the spatially equivalent optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To rectify distortion patterns in the input image, we propose a differentiable omnidirectional camera model comprising a learnable 3D spherical grid to regress the camera distortion. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | rectify, distortion, patterns, input, image, differentiable, omnidirectional, camera, model, comprising, learnable, spherical | geometry, map, object/relationship state | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | (2023b), have demonstrated the feasibility and efficiency of reconstructing omnidirectional radiance fields in large scenes using sparse and wide-baseline 360-degree image inputs. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Objective/outcome | Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SC-OmniGS, a novel system that self-calibrates the omnidirectional camera model and poses along with omnidirectional radiance field reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and test view synthesis.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Despite a slight decrease in rendering quality, the results demonstrate that our method still exhibits significant performance improvements compared to baseline methods.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our results outperform in both rendering quality and camera accuracy. † indicates training from scratch.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Embodiment/environment | We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et al., 2022) each with on average 110 training views and ... | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Dataset/benchmark | 5.2 EVALUATION ON SINGLE-ROOM SYNTHETIC DATASET We conducted experiments on three synthetic scenes from OmniBlender (Choi et al., 2023), namely Barbershop, Classroom, and Flat. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Metric | Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors. | definition, denominator, direction and uncertainty | p. 10 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |
| Baseline/ablation | Furthermore, when compared to other calibration baselines (see Barbershop in Table 1), SC-OmniGS consistently outperforms them with most increased rotation noise scales. | fair input/data/compute/action matching | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 19 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** However, we cannot apply a similar modification to 3D-GS based methods.
- **p. 10 / 6 CONCLUSION - extractive body cue:** With the differentiable omnidirectional camera model and Gaussian splatting procedure, our approach jointly optimizes 3D Gaussians, omnidirectional camera poses and camera model, leading to robust ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** OmniBlender dataset provides noise-free camera poses and depth maps.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Additionally, since point cloud initialization is demanded by 3D-GS based methods, we conducted experiments using different initialization strategies to further verify our system's robustness and ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To verify SC-OmniGS flexibility and robustness, we utilized an omnidirectional monocular depth estimation method, e.g.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Ablation study of weighted spherical photometric loss Lwsp. Without using Lwsp, the estimated poses of some cameras suffer obvious errors leading to performance ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need for a framework that calibrates the omnidirectional ...를 문제로 두고, To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera models. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
