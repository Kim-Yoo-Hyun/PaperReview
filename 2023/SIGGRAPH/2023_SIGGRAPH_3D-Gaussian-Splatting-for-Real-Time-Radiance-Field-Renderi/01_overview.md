# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2308.04079.
> PDF retrieval source: https://arxiv.org/pdf/2308.04079. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / SIGGRAPH
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: Gaussian Splatting, 3D reconstruction, representation
- Official paper: https://arxiv.org/abs/2308.04079
- Full-text retrieval: https://arxiv.org/pdf/2308.04079
- Code/Project: https://github.com/graphdeco-inria/gaussian-splatting
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 2022], but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360 [Barron et al.를 문제로 두고, To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An optimization method of 3D Gaussian properties, interleaved with ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Meshes and points are the most common 3D scene representations because they are explicit and are a good fit for fast GPU/CUDA-based rasterization.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In contrast, recent Neural Radiance Field (NeRF) methods build on continuous scene representations, typically optimizing a Multi-Layer Perceptron (MLP) using volumetric ray-marching for novel-view synthesis ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Similarly, the most efficient radiance field solutions to date build on continuous representations by interpolating values stored in, e.g., voxel [Fridovich-Keil and Yu et al.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2022], but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360 [Barron et al.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An optimization ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (≥30 fps) ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We first introduce 3D Gaussians as a flexible and expressive scene representation.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also can achieve training speeds and quality similar to the fastest methods and importantly provide the first real-time rendering with high quality for novel-view ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| State/latent | demonstrate, state-of-the-art, visual, quality, real-time, rendering, several, established, datasets, achieve, similar, theirs | geometry, map, object/relationship state | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION) |
| Output/action | 2022], we achieve similar quality to theirs; while this is the maximum quality they reach, by training for 51min we achieve state-of-the-art quality, even slightly better than Mip-NeRF360 [Barron et al. | point map, pose, scene graph, affordance 또는 query result | p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1 INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An optimization ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (≥30 fps) ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Our method achieves real-time rendering of radiance fields with quality that equals the previous method with the best quality [Barron et al. 2022], ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2022], we achieve high-quality results with only SfM points as input.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our results on previously published datasets show that we can optimize our 3D Gaussians from multi-view captures and achieve equal or better quality than the ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Recent methods achieve fast training [Fridovich-Keil ACM Trans.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 2 (1 INTRODUCTION) |
| Embodiment/environment | For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. | hardware/simulator version and reset protocol | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| Dataset/benchmark | Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization. | role, split, size and leakage | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Metric | Table 2. PSNR scores for Synthetic NeRF, we start with 100K randomly initialized points. Competing metrics extracted from respective papers. Mic Chair Ship Materials Lego Drums | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Baseline/ablation | We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while our tile-based splatting solution ... | fair input/data/compute/action matching | p. 1 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 1 (Body text (section boundary not confidently recovered)) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 2 RELATED WORK - extractive body cue:** We observe that our method performs relatively well, avoiding complete failure even without the SfM points.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 9. If we limit the number of points that receive gradients, the effect on visual quality is significant. Left: limit of 10 Gaussians that ...
- **p. 11 / 2 RELATED WORK - extractive body cue:** Comparison of failure artifacts: Mip-NeRF360 has "floaters" and grainy appearance (left, foreground), while our method produces coarse, anisoptropic Gaussians resulting in low-detail visuals (right, background).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fast - but lower-quality - radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short ...
- **p. 9 / 2 RELATED WORK - extractive body cue:** Also in areas not well covered from training views, the random initialization method appears to have more floaters that cannot be removed by optimization.
- **p. 10 / 2 RELATED WORK - extractive body cue:** 7.4 Limitations Our method is not without limitations.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 2022], but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360 [Barron et al.를 문제로 두고, To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An optimization method of 3D Gaussian properties, interleaved with ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Meshes and points are the most common 3D scene representations because they are explicit and are a good fit for fast GPU/CUDA-based rasterization. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** To summarize, we provide the following contributions: • The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields. • An optimization method of 3D Gaussian properties, ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Table 1. Quantitative evaluation of our method compared to previous work, computed over three datasets. Results marked with dagger † have been directly adopted from the original paper, all others ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise. (p. 1, 1 INTRODUCTION).
