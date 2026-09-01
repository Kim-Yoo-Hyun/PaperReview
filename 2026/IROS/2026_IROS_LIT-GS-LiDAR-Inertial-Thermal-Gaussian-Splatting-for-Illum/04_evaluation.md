# Evaluation - LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.20424; PDF retrieval source: https://arxiv.org/pdf/2606.20424. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)): To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated 3D points with frame-wise, anchor-aware geometric ...

## Evaluation Body Digest

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated 3D ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** (1) To adapt the anchor/non-anchor balance to the motion state of the current frame, we compute a normalized motion score from the linear and angular ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Comparison of renderings on private datasets. Data collection times (left to right) are 12:00 p.m., 10:00 p.m., 2:00 p.m., 7:00 p.m., and 6:00 ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Comparison of renderings on public datasets. and distorted surface structures in LIV-GaussMap. Similarly, in the Tree-stump scene, the reconstructed trunk surfaces appear noticeably ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Under illumination changes or texture-deficient scenes, photometric cues become unstable, degrading correspondence quality and pose estimation [4].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS AND RESULTS (p. 5); 1) Evaluation of Learned Feature Matching under Low (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| III. METHODOLOGY | EMPIRICAL / REAL-ROBOT OR HARDWARE | To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated ... | p. 3 (III. METHODOLOGY) |
| III. METHODOLOGY | EMPIRICAL / REAL-ROBOT OR HARDWARE | Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig. | p. 3 (III. METHODOLOGY) |

## Dataset / Benchmark Role

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Hardware setup of LIT-GS. (a1) thermal observations of the FAST-Calib target under strong sunlight; (a2) thermal observations of the camera's internal reference target; ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. System overview of LIT-GS. • We propose LIT-GS, a LiDAR-inertial-thermal Gaus- sian Splatting framework that couples LiDAR plane constraints into both pose/structure refinement ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Comparison of renderings on private datasets. Data collection times (left to right) are 12:00 p.m., 10:00 p.m., 2:00 p.m., 7:00 p.m., and 6:00 ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Comparison of renderings on public datasets. and distorted surface structures in LIV-GaussMap. Similarly, in the Tree-stump scene, the reconstructed trunk surfaces appear noticeably ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with the unrefined perspectives ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated. | embodiment, simulator version and control stack | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Task/environment | Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig. | reset, timeout, object/scene variation | p. 3 (III. METHODOLOGY) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated ... | definition/direction/unit from same section | p. 3 (III. METHODOLOGY) |
| (1) To adapt the anchor/non-anchor balance to the motion state of the current frame, we compute a normalized motion score from the linear and ... | definition/direction/unit from same section | p. 3 (III. METHODOLOGY) |
| Fig. 3. Comparison of renderings on private datasets. Data collection times (left to right) are 12:00 p.m., 10:00 p.m., 2:00 p.m., 7:00 p.m., and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 4. Comparison of renderings on public datasets. and distorted surface structures in LIV-GaussMap. Similarly, in the Tree-stump scene, the reconstructed trunk surfaces appear ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with the unrefined ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 3. Comparison of renderings on private datasets. Data collection times (left to right) are 12:00 p.m., 10:00 p.m., 2:00 p.m., 7:00 p.m., and ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Fig. 4. Comparison of renderings on public datasets. and distorted surface structures in LIV-GaussMap. Similarly, in the Tree-stump scene, the reconstructed trunk surfaces appear ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with the unrefined ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator ... | component/input/data sensitivity | p. 3 (III. METHODOLOGY) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting. | To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses and triangulated ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Primary metric/result | Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig. | numeric claim only at cited anchor | p. 3 (III. METHODOLOGY) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Reliance on visible imagery poses a fundamental limitation. | p. 1 (I. INTRODUCTION) |
| body limitation/failure cue | Under illumination changes or texture-deficient scenes, photometric cues become unstable, degrading correspondence quality and pose estimation [4]. | p. 1 (I. INTRODUCTION) |
| body limitation/failure cue | In contrast, LIT-GS combines illuminationrobust thermal supervision [8, 9] with persistent LiDAR | p. 2 (II. RELATED WORKS) |
| body limitation/failure cue | Learning-based methods improve robustness by jointly learning detection and description, as exemplified by D2-Net [17]. | p. 2 (II. RELATED WORKS) |
| body limitation/failure cue | 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting. | p. 3 (III. METHODOLOGY) |
| body limitation/failure cue | SuperPoint+SuperGlue matches generate additional nonanchor points that complement anchors by improving spatial coverage and graph connectivity, especially in thermally homogeneous regions, but may contain ... | p. 3 (III. METHODOLOGY) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated. | p. 3 (III. METHODOLOGY) |
| Hardware synchronization is achieved via PPS triggers from a microcontroller, ensuring consistent timestamp alignment among the LiDAR, IMU, and thermal camera (Fig. | p. 3 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Under illumination changes or texture-deficient scenes, photometric cues become unstable, degrading correspondence quality and pose estimation [4].
- **p. 2 / II. RELATED WORKS - extractive PDF cue:** In contrast, LIT-GS combines illuminationrobust thermal supervision [8, 9] with persistent LiDAR
- **p. 2 / II. RELATED WORKS - extractive PDF cue:** Learning-based methods improve robustness by jointly learning detection and description, as exemplified by D2-Net [17].
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** SuperPoint+SuperGlue matches generate additional nonanchor points that complement anchors by improving spatial coverage and graph connectivity, especially in thermally homogeneous regions, but may contain higher ...

- **PDF anchors reviewed:** datasets p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), metrics p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
