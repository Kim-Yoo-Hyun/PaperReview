# SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=o1sF4XaFdY.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247825. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openreview.net/forum?id=o1sF4XaFdY
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247825
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.를 문제로 두고, In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian surfels from sparse inputs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Reconstructing 3D scenes from sparse images remains a challenging task due to the difficulty of recovering accurate geometry and texture without optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Recent approaches leverage generalizable models to generate 3D scenes using 3D Gaussian Splatting (3DGS) primitive.
- **p. 1 / ABSTRACT - extractive body cue:** However, they often fail to produce continuous surfaces and instead yield discrete, color-biased point clouds that appear plausible at normal resolution but reveal severe artifacts ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue, we present SurfSplat, a feedforward framework based on 2D Gaussian Splatting (2DGS) primitive, which provides stronger anisotropy and higher geometric precision.
- **p. 1 / ABSTRACT - extractive body cue:** By incorporating a surface continuity prior and a forced alpha blending strategy, SurfSplat reconstructs coherent geometry together with faithful textures.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, we observe that existing feedforward methods tend to generate degraded 3D scenes.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture.
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive body cue:** This module outputs multi-view-aware features  F i N i=1, where F i ∈R H s × W s ×C.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This behavior rapidly boosts image quality for near-input viewpoints, but under the alpha-blending rendering rule, occluded Gaussians contribute minimally to the output: C = X i∈N ciαi i-1 Y j=1 (1 -αj), ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| State/latent | behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering, rule, occluded | geometry, map, object/relationship state | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Output/action | Given a collection of V input images {Iv}V v=1 with corresponding camera intrinsics {kv}V v=1 and poses {Tv}V v=1, the network fθ predicts Gaussian parameters for each pixel as: fθ : {(Iv, ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |
| Objective/outcome | The fused features are subsequently used to construct cost volumes Chen et al. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Interestingly, this variant still achieves competitive novel view synthesis (NVS) performance at the original resolution, despite producing visually noisy and discontinuous surfaces.
- **p. 10 / 4 EXPERIMENT - extractive body cue:** From this comparison, we observe that our method produces more geometrically consistent results, highlighting the improved geometric coherence induced by the surface continuity prior.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Embodiment/environment | Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Dataset/benchmark | 4.1 MAIN RESULTS Table 1: Novel view synthesis performance on the RealEstate10k dataset. | role, split, size and leakage | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Metric | This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity is not enforced. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Baseline/ablation | We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan et al. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 CONCLUSION - extractive body cue:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.
- **p. 10 / 5 CONCLUSION - extractive body cue:** By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of previous approaches, eliminating surface discontinuities and overcoming ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** These artifacts reveal the limitations of previous feedforward 3DGS 8
- **p. 9 / 4 EXPERIMENT - extractive body cue:** This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Notably, DepthSplat, despite using the same encoder backbone as our method, fails to generate coherent geometry or consistent surface details, which highlights the effectiveness of ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.를 문제로 두고, In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian surfels from sparse inputs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 3 (1 INTRODUCTION), p. 4 (3.1 PRELIMINARIES) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
