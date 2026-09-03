# MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=5uw1GRBFoT&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=5uw1GRBFoT&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 These changes must, however, be put into perspective, as they do not fundamentally challenge the overall structure of the traditional pipeline.를 문제로 두고, We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Structure-from-Motion (SfM), a task aiming at jointly recovering camera poses and 3D geometry of a scene given a set of images, remains a hard problem ...
- **p. 1 / Abstract - extractive body cue:** The traditional solution for SfM consists of a complex pipeline of minimal solvers which tends to propagate errors and fails when images do not sufficiently ...
- **p. 1 / Abstract - extractive body cue:** Recent methods have attempted to revisit this paradigm, but we empirically show that they fall short of fixing these core issues.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose instead to build upon a recently released foundation model for 3D vision that can robustly produce local 3D reconstructions and ...
- **p. 1 / Abstract - extractive body cue:** We introduce a low-memory approach to accurately align these local reconstructions in a global coordinate system.
- **p. 1 / 1. Introduction - extractive body cue:** These changes must, however, be put into perspective, as they do not fundamentally challenge the overall structure of the traditional pipeline.
- **p. 1 / 1. Introduction - extractive body cue:** The presence of outliers, such as wrong pixel matches, poses additional challenges and compels existing methods to repeatedly resort to hypothesis formulation and verification at ...

## Core Idea

- **p. 4 / 4. Proposed Method - extractive body cue:** We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve linear complexity in the number of images, we show as second contribution how the encoder from MASt3R can be exploited for large-scale image ...
- **p. 2 / 1. Introduction - extractive body cue:** First, we propose MASt3R-SfM, a full-fledged SfM pipeline able to process unconstrained image collections.
- **p. 4 / 4.1. Scene graph - extractive body cue:** While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·).
- **p. 6 / 4.4. Refinement - extractive body cue:** We propose instead to form pseudo-tracks by creating anchor points and rigidly tying together every pixel with their closest anchor point.
- **p. 4 / 4.1. Scene graph - extractive body cue:** In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according to a codebook ...
- **p. 5 / 4.2. Local reconstruction - extractive body cue:** Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ViT decoder Dec(), ...
- **p. 5 / 4.2. Local reconstruction - extractive body cue:** (1) From it, we then recover the canonical depthmap ˜𝑍𝑛= ˜𝑋𝑛 :,:,3 and the focal length using Weiszfeld algorithm [64]: 𝑓∗= arg min 𝑓 ∑︁ ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The proposed method builds on the recently introduced MASt3R model which, given two input images 𝐼𝑛, 𝐼𝑚∈ ℝ𝐻×𝑊×3, performs joint local 3D reconstruction and pixelwise matching [27]. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Preliminaries), p. 2 (1. Introduction) |
| State/latent | builds, recently, introduced, MASt3R, model, given, input, images, performs, joint, local, reconstruction | geometry, map, object/relationship state | p. 3 (3. Preliminaries), p. 2 (1. Introduction), p. 3 (3. Preliminaries) |
| Output/action | In this work, we propose MASt3R-SfM, a fullyintegrated SfM pipeline that can handle completely unconstrained input image collections, i.e. ranging from a single view to large-scale scenes, possibly without any camera motion ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.1. Scene graph) |
| Objective/outcome | Global optimization proceeds with gradient descent of a matching loss in 3D space, followed by refinement in terms of 2D reprojection error. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4.3. Coarse alignment) |

## Main Claims and Actual Contribution

- **p. 4 / 4. Proposed Method - extractive body cue:** We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve linear complexity in the number of images, we show as second contribution how the encoder from MASt3R can be exploited for large-scale image ...
- **p. 2 / 1. Introduction - extractive body cue:** First, we propose MASt3R-SfM, a full-fledged SfM pipeline able to process unconstrained image collections.
- **p. 4 / 4.1. Scene graph - extractive body cue:** While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·).
- **p. 6 / 4.4. Refinement - extractive body cue:** We propose instead to form pseudo-tracks by creating anchor points and rigidly tying together every pixel with their closest anchor point.
- **p. 7 / 5.2. Comparison with the state of the art - extractive body cue:** MASt3R-SfM provides nearly constant performance for all ranges, significantly outperforming COLMAP, Ace-Zero, FlowMap and VGGSfM in all settings.
- **p. 7 / 5.2. Comparison with the state of the art - extractive body cue:** Results reported in table 3 shows that MASt3R-SfM outperforms all competing approaches by a large margin on average.
- **p. 8 / 8.4 GB - extractive body cue:** Slightly better results are achieved with the complete graph, but it is about 10x slower than retrieval-based graph and no scalable in general.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art) |
| Embodiment/environment | We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from LLFF, 14 from T&T and 2 from CO3Dv2), ... | hardware/simulator version and reset protocol | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup) |
| Dataset/benchmark | When reported at the dataset level, metrics are averaged over all scenes. | role, split, size and leakage | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup), p. 6 (5.1. Experimental setup), p. 7 (5.2. Comparison with the state of the art) |
| Metric | We report standard visual localization accuracy metrics, i.e. the percentages of images successfully localized within error thresholds of (0.25m, 2°) / (0.5m, 5°) / (5m, 10°) and (0.25m, 2°) / (0.5m, 10°) ... | definition, denominator, direction and uncertainty | p. 8 (8.4 GB), p. 15 (Figure/Table caption), p. 6 (5.1. Experimental setup) |
| Baseline/ablation | Overall, we find that combining short-range (𝑘-NN) and long-range (keyframes) connections is important for Method Aachen-Day-Night↑ InLoc↑ Day Night DUC1 DUC2 Kapture [21]+R2D2 [41] 91.3/97.0/99.5 78.5/91.6/100 41.4/60.1/73.7 47.3/67.2/ ... | fair input/data/compute/action matching | p. 8 (8.4 GB), p. 6 (5. Experimental Results), p. 7 (5.2. Comparison with the state of the art) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6. Conclusion - extractive body cue:** After analyzing the results, we observe that failures are due to the presence of outlier (false) matches between similar-looking structures.
- **p. 12 / 6. Conclusion - extractive body cue:** MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion 7154 false matches (30° azimut, 0° elevation) (240° azimut, 0° elevation) 6659 false matches (60° azimut, 30° elevation) ...
- **p. 10 / 6. Conclusion - extractive body cue:** In such cases, the triangulation step from traditional SfM pipeline becomes ill-defined and notoriously fails.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: In all failure cases that we have manually reviewed, the root cause of failure was the presence of wrong matches (outliers) between similar-looking ...
- **p. 9 / 6. Conclusion - extractive body cue:** Thanks to the strong priors encoded in the underlying MASt3R foundation model upon which our approach is based, it can even deal with cases without ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive body cue:** The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the end ...
- **p. 9 / 8.4 GB - extractive body cue:** As expected, refinement, a strongly non-convex bundle-adjustment problem, cannot recover from a random initialization (𝜈1 = 0).

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 These changes must, however, be put into perspective, as they do not fundamentally challenge the overall structure of the traditional pipeline.를 문제로 두고, We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Scene graph), p. 4 (4.1. Scene graph), p. 5 (4.2. Local reconstruction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
