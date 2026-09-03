# LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.20424.
> PDF retrieval source: https://arxiv.org/pdf/2606.20424. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting
- Official paper: https://arxiv.org/abs/2606.20424
- Full-text retrieval: https://arxiv.org/pdf/2606.20424
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Reliance on visible imagery poses a fundamental limitation.를 문제로 두고, 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR-inertial-visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their ...
- **p. 1 / Abstract - extractive body cue:** We present LIT-GS, a LiDAR-inertial-thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization.
- **p. 1 / Abstract - extractive body cue:** Specifically, we exploit LIV visual map points as confidence-aware cross-modal anchors to establish reliable thermal-LiDAR associations, and incorporate weighted LiDAR point-to-plane residuals into bundle adjustment ...
- **p. 1 / Abstract - extractive body cue:** Building on the refined structure, we further introduce a LiDAR-plane-regularized differentiable splatting objective that constrains rendered 3D points to align with locally observed planes, mitigating ...
- **p. 1 / Abstract - extractive body cue:** Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although LiDAR provides metric geometry, existing LiDAR-inertial-visual Gaus- *

## Core Idea

- **p. 3 / III. METHODOLOGY - extractive body cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.
- **p. 3 / III. METHODOLOGY - extractive body cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** 2) Thermal feature extraction and matching: For frameto-frame registration and scene-graph construction, we employ SuperPoint [15] for keypoint detection and description and SuperGlue [16] for ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In each frame, anchors are enforced to contribute a fraction αt of the total geometric weight, while the remaining weight is distributed to non-anchor points according to their spatial proximity to the ... | camera/depth stream, pose, map와 language goal | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| State/latent | frame, anchors, enforced, contribute, fraction, total, geometric, weight, while, remaining, distributed, non-anchor | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Output/action | (1) To adapt the anchor/non-anchor balance to the motion state of the current frame, we compute a normalized motion score from the linear and angular speeds using datasetlevel statistics, and map it ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Given synchronized LiDAR, inertial, and thermal measurements, it jointly estimates camera poses, 3D structure, and Gaussian parameters by minimizing a differentiable objective that couples thermal photometric residuals with LiDAR-derive ... | goal reach, safety, localization error와 replanning latency | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 3 / III. METHODOLOGY - extractive body cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Embodiment/environment | Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated. | hardware/simulator version and reset protocol | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Dataset/benchmark | Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated. | role, split, size and leakage | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Metric | To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated 3D points with frame-wise, anchor-aware geometric we ... | definition, denominator, direction and uncertainty | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (Figure/Table caption) |
| Baseline/ablation | Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with the unrefined perspectives (b1-b4). The unrefined perspective structure is no ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Under illumination changes or texture-deficient scenes, photometric cues become unstable, degrading correspondence quality and pose estimation [4].
- **p. 2 / II. RELATED WORKS - extractive body cue:** In contrast, LIT-GS combines illuminationrobust thermal supervision [8, 9] with persistent LiDAR
- **p. 2 / II. RELATED WORKS - extractive body cue:** Learning-based methods improve robustness by jointly learning detection and description, as exemplified by D2-Net [17].
- **p. 3 / III. METHODOLOGY - extractive body cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.
- **p. 3 / III. METHODOLOGY - extractive body cue:** SuperPoint+SuperGlue matches generate additional nonanchor points that complement anchors by improving spatial coverage and graph connectivity, especially in thermally homogeneous regions, but may contain higher ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Comparison of renderings on public datasets. and distorted surface structures in LIV-GaussMap. Similarly, in the Tree-stump scene, the reconstructed trunk surfaces appear noticeably ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Reliance on visible imagery poses a fundamental limitation.를 문제로 두고, 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
