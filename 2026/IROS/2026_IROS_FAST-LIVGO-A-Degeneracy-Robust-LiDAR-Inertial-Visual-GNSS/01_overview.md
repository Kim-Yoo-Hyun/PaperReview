# FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.19190.
> PDF retrieval source: https://arxiv.org/pdf/2606.19190. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Vision-Language
- Official paper: https://arxiv.org/abs/2606.19190
- Full-text retrieval: https://arxiv.org/pdf/2606.19190
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in large-scale field missions or high-speed Unmanned Aerial Vehicle (UAV) flights, pure LIVO systems still face critical limitations.를 문제로 두고, To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in highly dynamic scenarios and robust operation in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust state estimation and mapping in long-term, large-scale, and highly dynamic environments remains a key challenge in robotics.
- **p. 1 / Abstract - extractive body cue:** Existing LiDAR-Inertial-Visual Odometry (LIVO) systems achieve strong local accuracy but suffer from accumulated drift over long distances and may fail in geometrically degraded or textureless ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, GNSS-aided fusion frameworks often rely on LiDAR or visual odometry for state prediction and outlier rejection, making them vulnerable when odometry degenerates.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose a tightly coupled LiDAR-Inertial-Visual-GNSS fusion framework based on an Error-State Iterated Kalman Filter.
- **p. 1 / Abstract - extractive body cue:** An online spatiotemporal alignment module using Dynamic Time Warping is introduced for highly dynamic conditions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, in large-scale field missions or high-speed Unmanned Aerial Vehicle (UAV) flights, pure LIVO systems still face critical limitations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing loosely-coupled schemes underutilize the high precision of GNSS carrier phases, while traditional tightly-coupled frameworks lack adaptive integrity monitoring under alternating LIVO and GNSS degradation.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contributions are summarized as follows: • A tightly-coupled LiDAR-Inertial-Visual-GNSS fusion framework based on ESIKF.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The resulting optimal time lag δtrI is then compensated when utilizing GNSS observations.
- **p. 2 / III. METHODOLOGY - extractive body cue:** Notation and State Transition Model We define the full system state vector x in continuous time as an element of the manifold M.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We construct the following objective function to solve for the

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To unify spatial references, GNSS ephemeris and observations (e.g., position, velocity) are transformed from the EarthCentered, Earth-Fixed (ECEF) frame to the local East-NorthUp (ENU) frame during preprocessing, which serves as the def ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| State/latent | unify, spatial, references, GNSS, ephemeris, observations, position, velocity, transformed, EarthCentered, Earth-Fixed, ECEF | geometry, map, object/relationship state | p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/action | This lightweight approach successfully avoids state augmentation while fully exploiting the submillimeter relative precision of carrier phase observations. | point map, pose, scene graph, affordance 또는 query result | p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Following initialization, the ESIKF state is updated using two types of residuals: • Doppler Residual: Directly constrains the instantaneous velocity and the receiver clock drift ( ˙δt). • Time-Differenced Carrier Phase (TDCP) ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contributions are summarized as follows: • A tightly-coupled LiDAR-Inertial-Visual-GNSS fusion framework based on ESIKF.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving optimal ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Trajectory evaluation in the large-scale flight. (a) and (b) show ENU position estimates across different phases. Our method (green) tightly aligns with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | We benchmarked our method against SOTA open-source systems, including LIO-SAM [8], FAST-LIVO2 [3], and LIGO [21]. | role, split, size and leakage | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Metric | Our robust mechanism effectively filters these hidden errors to extract ultimate accuracy. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption) |
| Baseline/ablation | Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In contrast, looser-coupled systems like LIO-SAM and LIGO generate meter-level errors but avoid complete failure.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Under such harsh conditions, a critical finding is that the ablation version (Ours w/o Rejection) directly suffers from trajectory divergence and system failure (marked as ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** When encountering feature degradation (e.g., textureless long corridors), the prior covariance bPk inflates.
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** Signals with low Carrier-to-Noise density (C/N0 <35 dB-Hz) or low elevation angles (< 15◦) are physically filtered out.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 2) Outdoor LIVO Degraded Scenario: In regions (a)-(c) of View 1 (Fig.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 1) Indoor GNSS Degraded Scenario: In the long indoor corridor (see region (d) in Fig.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in large-scale field missions or high-speed Unmanned Aerial Vehicle (UAV) flights, pure LIVO systems still face critical limitations.를 문제로 두고, To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in highly dynamic scenarios and robust operation in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
