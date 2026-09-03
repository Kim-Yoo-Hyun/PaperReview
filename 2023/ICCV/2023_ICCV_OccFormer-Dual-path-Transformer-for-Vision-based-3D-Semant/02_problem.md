# Problem - OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.05316; PDF retrieval source: https://arxiv.org/pdf/2304.05316. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, the 3D convolution suffers from several limitations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The vision-based perception for autonomous driving has undergone a transformation from the bird-eye-view (BEV) representations to the 3D semantic occupancy.
- **p. 1 / Abstract - extractive body cue:** Compared with the BEV planes, the 3D semantic occupancy further provides structural information along the vertical direction.
- **p. 1 / Abstract - extractive body cue:** This paper presents OccFormer, a dual-path transformer network to effectively process the 3D volume for semantic occupancy prediction.
- **p. 1 / Abstract - extractive body cue:** OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features.
- **p. 1 / Abstract - extractive body cue:** It is obtained by decomposing the heavy 3D processing into the local and global transformer pathways along the horizontal plane.
- **p. 1 / 1. Introduction - extractive body cue:** However, the 3D convolution suffers from several limitations.
- **p. 1 / 1. Introduction - extractive body cue:** Also, its spatial invariance cannot well process the sparse and discontinuous 3D features, generated from the state-of-the-art practices for image-to-3D transformation [40, 20, 29].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the 3D convolution suffers from several limitations. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The output of the image encoder is one fused feature map with 1 16 of the input resolution. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | output, image, encoder, fused, feature, input, resolution, Transformer, Occupancy, Decoder | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | multiview, camera, images, input, various, attempts, D-to3D, transformation | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: output, image, encoder, fused, feature, input, resolution, Transformer, Occupancy, Decoder | p. 2 (3.1. Overview), p. 3 (3.1. Overview), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: encoder, part, dual-path, transformer, block, unleash, capacity, selfattention | p. 1 (1. Introduction), p. 2 (3.1. Overview), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: matching, cost, includes, class, loss, binary, mask, optimal | p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.3. Transformer Occupancy Decoder) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.4. Main Results), p. 6 (4.3. Metrics), p. 7 (4.4. Main Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Also, its spatial invariance cannot well process the sparse and discontinuous 3D features, generated from the state-of-the-art practices for image-to-3D transformation [40, 20, 29].
- **p. 2 / 1. Introduction - extractive body cue:** Experimental results demonstrate the superiority of OccFormer over existing state-of-the-art methods.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (3.1. Overview), p. 2 (1. Introduction), p. 3 (3.2. Dual-path Transformer Encoder), p. 3 (3.2. Dual-path Transformer Encoder)): For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.

- **p. 2 / 3.1. Overview - extractive body cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 1. Introduction - extractive body cue:** Our method surpasses TPVFormer by 1.4% mIoU and generates more complete and realistic predictions for 3D semantic occupancy prediction.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** We introduce the dual-path processing with more details in the following paragraph.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** To pursue long-range, dynamic, and efficient processing of the 3D feature volumes, we propose the dual-path transformer block to build the 3D encoder.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | It indicates that the predicted semantic occupancy from TPVFormer, despite reasonable visualizations, fails to contain accurate 3D positions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Note that our method requires only one model to perform both the LiDAR segmentation and the semantic occupancy ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Second, we remove the windowed attention in the global path, whose weights are shared with the local path, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (3.1. Overview), p. 3 (3.1. Overview), p. 1 (1. Introduction), p. 2 (3.1. Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (3.1. Overview), p. 3 (3.1. Overview), p. 1 (1. Introduction), p. 2 (3.1. Overview), objective p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.3. Transformer Occupancy Decoder).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
