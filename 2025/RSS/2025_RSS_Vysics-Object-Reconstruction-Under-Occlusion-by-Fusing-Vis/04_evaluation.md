# Evaluation - Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption)): Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** While PLL is capable of identifying friction coefficients essentially by observing acceleration during periods of sliding, sliding motions in our dataset largely occur during sustained ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated geometry ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 10: ‘The dynamics prediction accuracy evaluated by the duration of the simulated trajectory under small pose error.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose stays within 10em of position error and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** The object masks for a video were semi-automatically generated from manual masks
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A 2D depiction of the physical meaning of a DSF (3) and its implication on the SDF (1). Shades of green points have ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 6); VI. RESULTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 10: ‘The dynamics prediction accuracy evaluated by the duration of the simulated trajectory under small pose error. | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 11: The dynamics prediction accuracy evaluated by the temporal overlap of robot-object contact happening lation and in the real world. The real world ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** While PLL is capable of identifying friction coefficients essentially by observing acceleration during periods of sliding, sliding motions in our dataset largely occur during sustained ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A 2D depiction of the physical meaning of a DSF (3) and its implication on the SDF (1). Shades of green points have ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Detailed Vysies diagram, Blue arrows denote the vision-based information flow through BundleSDF (66), and green arrows for PLL {9, 53]. Purple arrows indicate ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Visualization of the loss functions as the incorporation of vision and contact dynamics. Blue represents the geometry learned from vision, and green represents ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: The 7 objects and their names in our dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: A qualitative example of generative single-view recon- struction on an occluded RGB image of the egg object.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Task/environment | While PLL is capable of identifying friction coefficients essentially by observing acceleration during periods of sliding, sliding motions in our dataset largely occur during ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL SETUP) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (IV. APPROACH), p. 2 (A. Vision-Based Geometry Reconstruction and Completion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 10: ‘The dynamics prediction accuracy evaluated by the duration of the simulated trajectory under small pose error. | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose stays within 10em of position error ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The object masks for a video were semi-automatically generated from manual masks | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL SETUP) |
| These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL SETUP) |
| Fig. 2: A 2D depiction of the physical meaning of a DSF (3) and its implication on the SDF (1). Shades of green points ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 4: Visualization of the loss functions as the incorporation of vision and contact dynamics. Blue represents the geometry learned from vision, and green ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector ... | Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Primary metric/result | Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** We used a RealSense D455 collecting (640x480 pixel RGBD images at 30Hz.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** 5: The 7 objects and their names in our dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the ... | p. 9 (B. Dynamics Predictions) |
| body limitation/failure cue | Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind ... | p. 8 (A. Geometry Reconstruction) |
| body limitation/failure cue | Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry. | p. 6 (V. EXPERIMENTAL SETUP) |
| body limitation/failure cue | In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. | p. 6 (V. EXPERIMENTAL SETUP) |
| body limitation/failure cue | 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. | p. 7 (B. Metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Computer vision has made strides in ge~ ‘ometry reconstruction from image inputs. | p. 2 (A. Vision-Based Geometry Reconstruction and Completion) |
| Recent computer vision works combine the pose and shape estimation problems [75, 31, 66, 58]. | p. 2 (C. Simultaneous Tracking and Shape Reconstruction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Dynamics Predictions - extractive body cue:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind Vysics ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory.
- **p. 7 / B. Metrics - extractive body cue:** 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline.

- **Evidence anchors reviewed:** datasets p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), metrics p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), baselines p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as ... (p. 6, V. EXPERIMENTAL SETUP).
- **Metric evidence:** Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose stays within 10em of position error and within 45 degrees of rotational ... (p. 9, Figure/Table caption).
- **Baseline/ablation evidence:** Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, the mesh projection is shown in ... (p. 7, Figure/Table caption).
- **Failure/negative evidence:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. (p. 6, V. EXPERIMENTAL SETUP).
