# Evaluation - FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.19190; PDF retrieval source: https://arxiv.org/pdf/2606.19190. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving optimal comprehensive performance acr ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our platform with hardware synchronization for data acquisition.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We benchmarked our method against SOTA open-source systems, including LIO-SAM [8], FAST-LIVO2 [3], and LIGO [21].
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our robust mechanism effectively filters these hidden errors to extract ultimate accuracy.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving optimal ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Schematic of the Time-Differenced Carrier Phase (TDCP) model. Consecutive epoch differencing provides precise relative position constraints (∆ρ) by eliminating integer ambiguities and mitigating ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Mapping results generated in complex LIDAR, Camera, and GNSS degenerated scenes. were severely occluded. Traditional schemes diverge easily here, but our strict outlier ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | p. 6 (V. EXPERIMENTAL RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6. Trajectory evaluation in the large-scale flight. (a) and (b) show ENU position estimates across different phases. Our method (green) tightly aligns with ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our platform with hardware synchronization for data acquisition.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We benchmarked our method against SOTA open-source systems, including LIO-SAM [8], FAST-LIVO2 [3], and LIGO [21].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 1. System overview of our proposed framework. the GNSS antenna is modeled as a rigid transformation. To enable tightly-coupled fusion with raw GNSS measurements, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Schematic of the Time-Differenced Carrier Phase (TDCP) model. Consecutive epoch differencing provides precise relative position constraints (∆ρ) by eliminating integer ambiguities and mitigating ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Our platform with hardware synchronization for data acquisition. (a) Handheld system, (b) Fixed-wing drone setup, (c) Drone top view, (d) Drone bottom view.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Trajectory overview of the large-scale fixed-wing UAV experiment overlaid on Google Maps. The path segments (a), (b), and (c) correspond to challenging maneuvering ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Trajectory evaluation in the large-scale flight. (a) and (b) show ENU position estimates across different phases. Our method (green) tightly aligns with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Mapping results generated in complex LIDAR, Camera, and GNSS degenerated scenes. were severely occluded. Traditional schemes diverge easily here, but our strict outlier ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Task/environment | Our platform with hardware synchronization for data acquisition. | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our robust mechanism effectively filters these hidden errors to extract ultimate accuracy. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 2. Schematic of the Time-Differenced Carrier Phase (TDCP) model. Consecutive epoch differencing provides precise relative position constraints (∆ρ) by eliminating integer ambiguities and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 7. Mapping results generated in complex LIDAR, Camera, and GNSS degenerated scenes. were severely occluded. Traditional schemes diverge easily here, but our strict ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 6. Trajectory evaluation in the large-scale flight. (a) and (b) show ENU position estimates across different phases. Our method (green) tightly aligns with ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL RESULTS) |
| We benchmarked our method against SOTA open-source systems, including LIO-SAM [8], FAST-LIVO2 [3], and LIGO [21]. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 5. Qualitative comparison of global point cloud maps. (a1, b1) Our method; (a2, b2) FAST-LIVO2. To further validate this improvement, Fig. 6 evaluates ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| An ablation variant, Ours w/o Rejection, was also evaluated by disabling the adaptive robust module and fusing all pre-screened GNSS observations. | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL RESULTS) |
| Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping ... | By sacrificing negligible accuracy in denied environments, our system gains significant global accuracy improvements in open areas and successfully prevents tightly-coupled system crashes, achieving ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, looser-coupled systems like LIO-SAM and LIGO generate meter-level errors but avoid complete failure. | p. 6 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | Under such harsh conditions, a critical finding is that the ablation version (Ours w/o Rejection) directly suffers from trajectory divergence and system failure (marked ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | When encountering feature degradation (e.g., textureless long corridors), the prior covariance bPk inflates. | p. 5 (IV. STATE ESTIMATION) |
| body limitation/failure cue | Signals with low Carrier-to-Noise density (C/N0 <35 dB-Hz) or low elevation angles (< 15◦) are physically filtered out. | p. 5 (IV. STATE ESTIMATION) |
| body limitation/failure cue | 2) Outdoor LIVO Degraded Scenario: In regions (a)-(c) of View 1 (Fig. | p. 7 (2) High-Precision Mapping in Large-Scale Highly Dy) |
| body limitation/failure cue | 1) Indoor GNSS Degraded Scenario: In the long indoor corridor (see region (d) in Fig. | p. 7 (2) High-Precision Mapping in Large-Scale Highly Dy) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our platform with hardware synchronization for data acquisition. | p. 6 (V. EXPERIMENTAL RESULTS) |
| 3, integrating a Livox Avia solid-state LiDAR, an industrialgrade global shutter RGB camera, and a Ublox ZED-F9P GNSS receiver. | p. 6 (V. EXPERIMENTAL RESULTS) |
| Since the GNSS receiver and LIVO system run on independent clocks, a time offset δtrI remains between the two data streams. | p. 3 (III. METHODOLOGY) |
| Preprocess 1) Temporal Calibration via DTW: Before GNSS alignment, the LIV subsystem is initialized independently: LiDAR, camera, and IMU timestamps are hardwaresynchronized, while the ... | p. 3 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In contrast, looser-coupled systems like LIO-SAM and LIGO generate meter-level errors but avoid complete failure.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Under such harsh conditions, a critical finding is that the ablation version (Ours w/o Rejection) directly suffers from trajectory divergence and system failure (marked as ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** When encountering feature degradation (e.g., textureless long corridors), the prior covariance bPk inflates.
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** Signals with low Carrier-to-Noise density (C/N0 <35 dB-Hz) or low elevation angles (< 15◦) are physically filtered out.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 2) Outdoor LIVO Degraded Scenario: In regions (a)-(c) of View 1 (Fig.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 1) Indoor GNSS Degraded Scenario: In the long indoor corridor (see region (d) in Fig.

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), metrics p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), results p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
