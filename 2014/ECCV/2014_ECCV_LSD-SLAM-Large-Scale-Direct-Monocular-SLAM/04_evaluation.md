# Evaluation - LSD-SLAM: Large-Scale Direct Monocular SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://cvg.cit.tum.de/research/vslam/lsdslam; PDF retrieval source: https://jakobengel.github.io/pdf/engel14eccv.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (4 Results), p. 13 (4 Results), p. 13 (4 Results), p. 14 (4 Results), p. 6 (Figure/Table caption)): 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes and major loop closures.

## Evaluation Body Digest

- **p. 13 / 4 Results - extractive PDF cue:** 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm).
- **p. 12 / 4 Results - extractive PDF cue:** 4.2 Quantitative Evaluation We evaluate LSD-SLAM on the publicly available RGB-D dataset [25].
- **p. 12 / 4 Results - extractive PDF cue:** Note that for monocular SLAM this is a very challenging benchmark, as it contains fast rotational movement, strong motion blur and rolling shutter artifacts.
- **p. 13 / 4 Results - extractive PDF cue:** The bottom row shows different close-ups of the scene.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different num- ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 5: Direct keyframe alignment on sim(3): (a)-(c): two keyframes with asso- ciated depth and depth variance. (d)-(f): photometric residual, depth residual and Huber weights, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Large-Scale Direct Monocular SLAM: LSD-SLAM generates a consistent global map, using direct image alignment and probabilistic, semi-dense depth maps instead of keypoints. Top: ...
- **p. 12 / 4 Results - extractive PDF cue:** We use the very first depth map to bootstrap the system and get the correct initial scale.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Results (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Results | EMPIRICAL / SIMULATION | 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes ... | p. 12 (4 Results) |
| 4 Results | EMPIRICAL / SIMULATION | 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm). | p. 13 (4 Results) |
| 4 Results | EMPIRICAL / SIMULATION | For comparison we show respective results from semi-dense mono-VO [9], keypoint-based mono-SLAM [15], direct RGB-D SLAM [14] and keypointbased RGB-D SLAM [7]. | p. 13 (4 Results) |
| 4 Results | EMPIRICAL / SIMULATION | 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different number ... | p. 14 (4 Results) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 13 / 4 Results - extractive PDF cue:** 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm).
- **p. 12 / 4 Results - extractive PDF cue:** 4.2 Quantitative Evaluation We evaluate LSD-SLAM on the publicly available RGB-D dataset [25].
- **p. 12 / 4 Results - extractive PDF cue:** Note that for monocular SLAM this is a very challenging benchmark, as it contains fast rotational movement, strong motion blur and rolling shutter artifacts.
- **p. 13 / 4 Results - extractive PDF cue:** The bottom row shows different close-ups of the scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Large-Scale Direct Monocular SLAM: LSD-SLAM generates a consistent global map, using direct image alignment and probabilistic, semi-dense depth maps instead of keypoints. Top: ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different maximum ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - yet ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 4: Statistic normalization: (a) reference image. (b-d): tracked images and inverse variance σ-2 rp of the residual. For pure rotation, depth noise has no ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 5: Direct keyframe alignment on sim(3): (a)-(c): two keyframes with asso- ciated depth and depth variance. (d)-(f): photometric residual, depth residual and Huber weights, ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 6: Two scenes with high scale variation. Camera frustums are displayed for each keyframe with their size corresponding to the keyframe's scale. created keyframe ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 7: Loop closure for a long and challenging outdoor trajectory (after the loop closure on the left, before on the right). Also shown are ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 8: Accumulated pointcloud of a trajectory with large scale variation, includ- ing views with an average inverse depth of less than 20 cm to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm). | embodiment, simulator version and control stack | p. 13 (4 Results), p. 12 (4 Results) |
| Task/environment | 4.2 Quantitative Evaluation We evaluate LSD-SLAM on the publicly available RGB-D dataset [25]. | reset, timeout, object/scene variation | p. 12 (4 Results), p. 12 (4 Results) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (2 Preliminaries), p. 7 (2 Preliminaries) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (2 Preliminaries), p. 6 (2 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Fig. 5: Direct keyframe alignment on sim(3): (a)-(c): two keyframes with asso- ciated depth and depth variance. (d)-(f): photometric residual, depth residual and Huber ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 1: Large-Scale Direct Monocular SLAM: LSD-SLAM generates a consistent global map, using direct image alignment and probabilistic, semi-dense depth maps instead of keypoints. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We use the very first depth map to bootstrap the system and get the correct initial scale. | definition/direction/unit from same section | p. 12 (4 Results) |
| The proposed scale-aware formulation allows to accurately estimate both fine details and large-scale geometry - this flexibility is one of the major benefits of ... | definition/direction/unit from same section | p. 13 (4 Results) |
| It can also be observed that these measures only increase the convergence radius, and have no notable effect on tracking precision. | definition/direction/unit from same section | p. 14 (4 Results) |
| Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| For comparison we show respective results from semi-dense mono-VO [9], keypoint-based mono-SLAM [15], direct RGB-D SLAM [14] and keypointbased RGB-D SLAM [7]. | comparison identity and matched condition | p. 13 (4 Results) |
| 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different number ... | comparison identity and matched condition | p. 14 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 10: Convergence radius and accuracy of sim(3) direct image alignment with and without ESM minimization (indicated by light / dark) for a different ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3.1 The Complete Method The algorithm consists of three major components: tracking, depth map estimation and map optimization as visualized in Fig. | 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (4 Results), p. 13 (4 Results), p. 13 (4 Results), p. 14 (4 Results), p. 6 (Figure/Table caption) |
| Primary metric/result | 9: Results on the TUM RGB-D benchmark [25], and two simulated sequences from [12], measured as absolute trajectory RMSE (cm). | numeric claim only at cited anchor | p. 13 (4 Results) |

- Numeric sentences retained from the body:
- **p. 13 / 4 Results - extractive PDF cue:** LSD-SLAM (#KF) [9] [15] [14] [7] fr2/desk 4.52 (116) 13.50 x 1.77 9.5 fr2/xyz 1.47 (38) 3.79 24.28 1.18 2.6 sim/desk 0.04 (39) 1.53 - ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** Tracking Depth Map Estimation Map Optimization New Image (640 x 480 at 30Hz) Track on Current KF: → estimate SE(3) transformation Current KF Refine Current ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For LSD-SLAM, we also show the number of keyframes created. 'x' denotes tracking failure, '-' no available data. | p. 13 (4 Results) |
| body limitation/failure cue | Major components of the proposed method are two key novelties: (1) a direct method to align two keyframes on sim(3), explicitly incorporating and detecting ... | p. 14 (5 Conclusion) |
| body limitation/failure cue | We experimentally showed that the approach reliably tracks and maps even challenging hand-held trajectories with a length of over 500 m, in particular including ... | p. 14 (5 Conclusion) |
| body limitation/failure cue | Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Fig. 4: Statistic normalization: (a) reference image. (b-d): tracked images and inverse variance σ-2 rp of the residual. For pure rotation, depth noise has ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The new estimate is then obtained by multiplication with the computed update ξ(n+1) = δξ(n) ◦ξ(n). | p. 5 (2 Preliminaries) |
| The iteratively solved error function then becomes E(ξ) = X i wi(ξ)r2 i (ξ), (8) and the update is computed as δξ(n) = -(JT ... | p. 5 (2 Preliminaries) |
| The left-multiplication convention used here is consistent with [23], while e.g. the default type-implementation in g2o [18] assumes rightmultiplication. | p. 6 (2 Preliminaries) |
| 3.3 Tracking new Frames: Direct se(3) Image Alignment Starting from an existing keyframe Ki = (Ii, Di, Vi), the relative 3D pose ξji ∈ ... | p. 7 (2 Preliminaries) |
| The residual's variance σ2 rp(p,ξji) is computed using covariance propagation as described in Sec. | p. 8 (2 Preliminaries) |
| Even though direct image alignment is non-convex, we found that with the steps proposed in Sec. | p. 14 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 4 Results - extractive PDF cue:** For LSD-SLAM, we also show the number of keyframes created. 'x' denotes tracking failure, '-' no available data.
- **p. 14 / 5 Conclusion - extractive PDF cue:** Major components of the proposed method are two key novelties: (1) a direct method to align two keyframes on sim(3), explicitly incorporating and detecting scale-drift ...
- **p. 14 / 5 Conclusion - extractive PDF cue:** We experimentally showed that the approach reliably tracks and maps even challenging hand-held trajectories with a length of over 500 m, in particular including large ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: In addition to accurate, semi-dense 3D reconstructions, LSD-SLAM also estimates the associated uncertainty. From left to right: Accumulated pointcloud thesholded with different maximum ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Overview over the complete LSD-SLAM algorithm. In practice, the residuals are highly correlated, such that Σξ is only a lower bound - yet ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 4: Statistic normalization: (a) reference image. (b-d): tracked images and inverse variance σ-2 rp of the residual. For pure rotation, depth noise has no ...

- **PDF anchors reviewed:** datasets p. 13 (4 Results), p. 12 (4 Results), p. 12 (4 Results), p. 13 (4 Results), metrics p. 14 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 12 (4 Results), p. 13 (4 Results), p. 14 (4 Results), baselines p. 3 (Figure/Table caption), p. 13 (4 Results), p. 14 (4 Results), results p. 12 (4 Results), p. 13 (4 Results), p. 13 (4 Results), p. 14 (4 Results), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
