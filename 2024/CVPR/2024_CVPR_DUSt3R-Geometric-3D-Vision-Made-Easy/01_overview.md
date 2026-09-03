# DUSt3R: Geometric 3D Vision Made Easy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2312.14132.
> PDF retrieval source: https://arxiv.org/pdf/2312.14132. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: 3D reconstruction, calibration, geometry
- Official paper: https://arxiv.org/abs/2312.14132
- Full-text retrieval: https://arxiv.org/pdf/2312.14132
- Code/Project: https://github.com/naver/dust3r
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The network learns strong geometric and shape priors, which are reminiscent of those commonly leveraged in MVS, like shape from texture, shading or contours [111].를 문제로 두고, Before delving into the details of our method, we introduce below the essential concept of pointmaps.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Multi-view stereo reconstruction (MVS) in the wild requires to first estimate the camera parameters e.g. intrinsic and extrinsic parameters.
- **p. 1 / Abstract - extractive body cue:** These are usually tedious and cumbersome to obtain, yet they are mandatory to triangulate corresponding pixels in 3D space, which is the core of all ...
- **p. 1 / Abstract - extractive body cue:** In this work, we take an opposite stance and introduce DUSt3R1, a radically novel paradigm for Dense and Unconstrained Stereo 3D Reconstruction of arbitrary image ...
- **p. 1 / Abstract - extractive body cue:** We cast the pairwise reconstruction problem as a regression of pointmaps, relaxing the hard constraints of usual projective camera models.
- **p. 1 / Abstract - extractive body cue:** In the case where more than two images are provided, we further propose a simple yet effective global alignment strategy that expresses all pairwise pointmaps ...
- **p. 2 / 1. Introduction - extractive body cue:** The network learns strong geometric and shape priors, which are reminiscent of those commonly leveraged in MVS, like shape from texture, shading or contours [111].
- **p. 2 / 1. Introduction - extractive body cue:** The main component is a network that can regress a dense and accurate scene representation solely from a pair of images, without prior information regarding ...

## Core Idea

- **p. 3 / 3. Method - extractive body cue:** Before delving into the details of our method, we introduce below the essential concept of pointmaps.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we introduce the pointmap representation for MVS applications, that enables the network to predict the 3D shape in a canonical frame, while preserving the ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DUSt3R, a radically novel approach for Dense Unconstrained Stereo 3D Reconstruction from un-calibrated and un-posed cameras.
- **p. 5 / 3.3. Downstream Applications - extractive body cue:** One possibility consists of obtaining 2D correspondences between IQ and IB, which in turn yields 2D-3D correspondences for IQ, and then running PnP-RANSAC [30, 52].
- **p. 5 / 3.4. Global Alignment - extractive body cue:** We now present a fast and simple post-processing optimization for entire scenes that enables the alignment of pointmaps predicted from multiple images into a joint ...
- **p. 4 / 3. Method - extractive body cue:** The resulting token representations F 1 and F 2 are then passed to two transformer decoders that constantly exchange information via cross-attention.
- **p. 4 / 3.1. Overview - extractive body cue:** To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, ...
- **p. 5 / 3.2. Training Objective - extractive body cue:** The final training objective is the confidence-weighted regression loss from Eq.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To that aim, we train a network F that takes as input 2 RGB images I1, I2 ∈RW ×H×3 and outputs 2 corresponding pointmaps X1,1, X2,1 ∈RW ×H×3 with associated confidence maps ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.1. Overview), p. 5 (3.2. Training Objective) |
| State/latent | train, network, takes, input, RGB, images, outputs, corresponding, pointmaps, associated, confidence, maps | geometry, map, object/relationship state | p. 4 (3.1. Overview), p. 5 (3.2. Training Objective), p. 2 (1. Introduction) |
| Output/action | Examples of input image pairs with their corresponding outputs are shown in Fig. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.2. Training Objective), p. 2 (1. Introduction), p. 4 (3.1. Overview) |
| Objective/outcome | The final training objective is the confidence-weighted regression loss from Eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Training Objective), p. 5 (3.3. Downstream Applications), p. 6 (3.4. Global Alignment) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Method - extractive body cue:** Before delving into the details of our method, we introduce below the essential concept of pointmaps.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we introduce the pointmap representation for MVS applications, that enables the network to predict the 3D shape in a canonical frame, while preserving the ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DUSt3R, a radically novel approach for Dense Unconstrained Stereo 3D Reconstruction from un-calibrated and un-posed cameras.
- **p. 5 / 3.3. Downstream Applications - extractive body cue:** One possibility consists of obtaining 2D correspondences between IQ and IB, which in turn yields 2D-3D correspondences for IQ, and then running PnP-RANSAC [30, 52].
- **p. 5 / 3.4. Global Alignment - extractive body cue:** We now present a fast and simple post-processing optimization for entire scenes that enables the alignment of pointmaps predicted from multiple images into a joint ...
- **p. 8 / 4.4. Multi-view Depth - extractive body cue:** We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using groundtruth camera poses.
- **p. 7 / 4.2. Multi-view Pose Estimation - extractive body cue:** As shown in Table 2, DUSt3R with global alignment achieves the best overall performance on the two datasets and significantly surpasses the state-of-the-art PoseDiffusion [140].
- **p. 7 / 4.1. Visual Localization - extractive body cue:** Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even managing ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Multi-view Depth), p. 7 (4.2. Multi-view Pose Estimation) |
| Embodiment/environment | These datasets feature diverse scenes types: indoor, outdoor, synthetic, real-world, object-centric, etc. | hardware/simulator version and reset protocol | p. 6 (4. Experiments with DUSt3R), p. 8 (4.4. Multi-view Depth) |
| Dataset/benchmark | In the remainder of this section, we benchmark DUSt3R on a representative set of classical 3D vision tasks, each time specifying datasets, metrics and comparing performance with existing state-of-the-art approaches. | role, split, size and leakage | p. 6 (4. Experiments with DUSt3R), p. 8 (4.4. Multi-view Depth), p. 6 (4. Experiments with DUSt3R), p. 7 (4.1. Visual Localization) |
| Metric | We use two metrics commonly used in the monocular depth evaluations [6, 117]: the absolute relative error AbsRel between target y and prediction ˆy, AbsRel = /y -ˆy//y, and the prediction threshold ... | definition, denominator, direction and uncertainty | p. 7 (4.3. Monocular Depth), p. 8 (4.5. 3D Reconstruction), p. 8 (4.5. 3D Reconstruction) |
| Baseline/ablation | Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even managing to outperform strong baselines like HLoc [101] ... | fair input/data/compute/action matching | p. 7 (4.1. Visual Localization), p. 7 (4.3. Monocular Depth), p. 8 (4.4. Multi-view Depth) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.5. 3D Reconstruction - extractive body cue:** Our method does not reach the accuracy levels of the best methods.
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** (1.7) 21.1 65.6 108.4 31.0 0.82 MVS2D ScanNet [160] ✓ × ✓ × 73.4 0.0 (4.5) (54.1) 30.7 14.4 5.0 57.9 56.4 11.1 34.0 27.5 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The network learns strong geometric and shape priors, which are reminiscent of those commonly leveraged in MVS, like shape from texture, shading or contours [111].를 문제로 두고, Before delving into the details of our method, we introduce below the essential concept of pointmaps.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 4 (3.1. Overview), p. 5 (3.2. Training Objective), p. 5 (3.2. Training Objective) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The network learns strong geometric and shape priors, which are reminiscent of those commonly leveraged in MVS, like shape from texture, shading or contours [111]. (p. 2, 1. Introduction).
- **Actual contribution:** In this paper, we present DUSt3R, a radically novel approach for Dense Unconstrained Stereo 3D Reconstruction from un-calibrated and un-posed cameras. (p. 2, 1. Introduction).
- **Evaluation boundary:** Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even managing to outperform strong baselines like ... (p. 7, 4.1. Visual Localization).
- **Explicit failure boundary:** Procrustes alignment is, unfortunately, sensitive to noise and outliers. (p. 5, 3.3. Downstream Applications).
