# Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.13415.
> PDF retrieval source: https://arxiv.org/pdf/2103.13415. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: NeRF, 3D Vision, representation, geometry
- Official paper: https://arxiv.org/abs/2103.13415
- Full-text retrieval: https://arxiv.org/pdf/2103.13415
- Code/Project: https://jonbarron.info/mipnerf/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This is a generalization of NeRF's positional encoding (PE) that allows a region of space to be compactly featurized, as opposed to a single point in space.를 문제로 두고, To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are ...
- **p. 1 / Abstract - extractive body cue:** The straightforward solution of supersampling by rendering with multiple rays per pixel is impractical for NeRF, because rendering each ray requires querying a multilayer perceptron ...
- **p. 1 / Abstract - extractive body cue:** Our solution, which we call "mip-NeRF" (`a la "mipmap"), extends NeRF to represent the scene at a continuously-valued scale.
- **p. 1 / Abstract - extractive body cue:** By efficiently rendering anti-aliased conical frustums instead of rays, mip-NeRF reduces objectionable aliasing artifacts and significantly improves NeRF's ability to represent fine details, while also ...
- **p. 1 / Abstract - extractive body cue:** Compared to NeRF, mip-NeRF reduces average error rates by 17% on the dataset presented with NeRF and by 60% on a challenging multiscale variant of ...
- **p. 2 / 1. Introduction - extractive body cue:** This is a generalization of NeRF's positional encoding (PE) that allows a region of space to be compactly featurized, as opposed to a single point ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE).
- **p. 2 / 1. Introduction - extractive body cue:** On a challenging multiresolution benchmark we present, mip-NeRF is able to reduce error rates relative to NeRF by 60% on average (see Figure 2 for ...
- **p. 6 / 3.2. Architecture - extractive body cue:** See the supplement for additional details and some additional differences between JaxNeRF and mip-NeRF that do not affect performance significantly and are incidental to our ...
- **p. 1 / 1. Introduction - extractive body cue:** Neural volumetric representations such as neural radiance fields (NeRF) [30] have emerged as a compelling strategy for learning to represent 3D objects and scenes from ...
- **p. 4 / 3. Method - extractive body cue:** This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, ...
- **p. 6 / 3.2. Architecture - extractive body cue:** Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ sum _{\ray \in ...
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** To accomplish this, it is helpful to first rewrite the PE in Equation 1 as a Fourier feature [35, 44]:
- **p. 5 / 3.1. Cone Tracing and Positional Encoding - extractive body cue:** IPE features behave intuitively: If a particular frequency in the positional encoding has a period that is larger than the width of the interval being ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | But our cone casting and IPE features allow us to explicitly encode scale into our input features and thereby enable an MLP to learn a multiscale representation of the scene. | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.2. Architecture), p. 6 (3.2. Architecture) |
| State/latent | But, cone, casting, IPE, features, allow, explicitly, encode, scale, input, thereby, enable | geometry, map, object/relationship state | p. 6 (3.2. Architecture), p. 6 (3.2. Architecture), p. 1 (1. Introduction) |
| Output/action | By integrating PE features over each interval, the high frequency dimensions of IPE features shrink towards zero when the period of the frequency is small compared to the size of the interval ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3.2. Architecture), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Our optimization problem is: \ u n der s e t {\modelwei gh ts }{\ op eratorname { mi n}} \, \ sum _{\ray \in \mathcal {R}} \Big ( \lossmult \big \/ ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 6 (3.2. Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE).
- **p. 2 / 1. Introduction - extractive body cue:** On a challenging multiresolution benchmark we present, mip-NeRF is able to reduce error rates relative to NeRF by 60% on average (see Figure 2 for ...
- **p. 6 / 3.2. Architecture - extractive body cue:** See the supplement for additional details and some additional differences between JaxNeRF and mip-NeRF that do not affect performance significantly and are incidental to our ...
- **p. 1 / 1. Introduction - extractive body cue:** Neural volumetric representations such as neural radiance fields (NeRF) [30] have emerged as a compelling strategy for learning to represent 3D objects and scenes from ...
- **p. 4 / 3. Method - extractive body cue:** This use of conical frustums and IPE features also allows us to reduce NeRF's two separate "coarse" and "fine" MLPs into a single multiscale MLP, ...
- **p. 8 / 4. Results - extractive body cue:** [30], mip-NeRF significantly outperforms NeRF and our improved version of NeRF, particularly on small or thin objects such as the holes of the LEGO truck ...
- **p. 7 / 4. Results - extractive body cue:** Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels improves ...
- **p. 7 / 4. Results - extractive body cue:** Mip-NeRF outperforms NeRF and its improved version by a significant margin, both visually and quantitatively.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4. Results), p. 7 (4. Results) |
| Embodiment/environment | 0.709 0.910 0.931 0.663 0.863 0.959 0.971 0.881 0.940 0.979 0.989 0.978 0.448 0.562 0.696 0.906 0.525 0.633 0.794 0.918 0.785 0.837 0.861 0.975 Ground-Truth NeRF NeRF + Area, Center, Misc Mip-NeRF ... | hardware/simulator version and reset protocol | p. 7 (4. Results), p. 6 (4. Results) |
| Dataset/benchmark | We constructed our multiscale Blender benchmark because the original Blender dataset used by NeRF has a subtle but critical weakness: all cameras have the same focal length and resolution and are placed ... | role, split, size and leakage | p. 7 (4. Results), p. 6 (4. Results), p. 6 (4. Results), p. 8 (4. Results) |
| Metric | Mip-NeRF reduces average error by 60% on this task and outperforms NeRF by a large margin on all metrics and all scales. "Centering" pixels improves NeRF's performance substantially, but not enough to ... | definition, denominator, direction and uncertainty | p. 7 (4. Results), p. 6 (4. Results), p. 6 (4. Results) |
| Baseline/ablation | Table 2: A comparison of mip-NeRF and its ablations against several baseline algorithms and variants of NeRF on the single-scale Blender dataset of Mildenhall et al. [30]. Training times taken from prior ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4. Results - extractive body cue:** The limitation of this dataset is complemented by the limitations of NeRF: despite NeRF's tendency to produce aliased renderings, it is able to produce excellent ...
- **p. 7 / 4. Results - extractive body cue:** Removing IPE features causes mip-NeRF's performance to degrade to the performance of "Centered" NeRF, thereby demonstrating that cone-casting and IPE features are the primary factors ...
- **p. 8 / 4. Results - extractive body cue:** This baseline has an unfair advantage: we manually remove the low-resolution images in the multiscale dataset, which would otherwise degrade NeRF's performance as previously demonstrated.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This is a generalization of NeRF's positional encoding (PE) that allows a region of space to be compactly featurized, as opposed to a single point in space.를 문제로 두고, To encode a 3D position and its surrounding Gaussian region, we propose a new feature representation: an integrated positional encoding (IPE).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 4 (3. Method), p. 6 (3.2. Architecture), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 5 (3.1. Cone Tracing and Positional Encoding), p. 4 (3.1. Cone Tracing and Positional Encoding) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
