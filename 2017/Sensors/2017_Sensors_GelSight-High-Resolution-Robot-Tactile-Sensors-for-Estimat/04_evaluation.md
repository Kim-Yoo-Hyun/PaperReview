# Evaluation - GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/; PDF retrieval source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement), p. 16 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement)): Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change corresponds to the surface normal of ...

## Evaluation Body Digest

- **p. 18 / 5.2. Evaluation of Force Measurement - extractive body cue:** In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be applied), ...
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** On the other hand, for the given training set and test set, the measurement is still influenced by the contact geometry.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The total size of the training dataset is around 28,815.
- **p. 16 / 5.2. Evaluation of Force Measurement - extractive body cue:** In this preliminary experiment, we train the force measurement neural network with the data of GelSight contacting objects with some basic shapes, including spheres, cylinders ...
- **p. 15 / 5. Evaluation - extractive body cue:** In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object shapes ...
- **p. 16 / 5.1. Evaluation of Shape Measurement - extractive body cue:** The ground truth of the geometry is hard to get, but the reconstructed 3D structures capture both the overall shape and local textures of the ...
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** We train the network with the mean squared error loss function for the regression problem.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The coefficient of determination (R2) and root mean square error (RMSE) for the results of three different objects are also listed in the figure.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 5. Evaluation (p. 15); 5.1. Evaluation of Shape Measurement (p. 16); 5.2. Evaluation of Force Measurement (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change ... | p. 9 (Figure/Table caption) |
| 5. Evaluation | EMPIRICAL / SIMULATION | In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object ... | p. 15 (5. Evaluation) |
| 5.1. Evaluation of Shape Measurement | EMPIRICAL / SIMULATION | Examples of the results are shown in Figure 13a. | p. 16 (5.1. Evaluation of Shape Measurement) |
| 5.2. Evaluation of Force Measurement | EMPIRICAL / SIMULATION | In this preliminary experiment, we train the force measurement neural network with the data of GelSight contacting objects with some basic shapes, including spheres, ... | p. 16 (5.2. Evaluation of Force Measurement) |
| 5.2. Evaluation of Force Measurement | EMPIRICAL / SIMULATION | The results also show that the GelSight measurement of force can be robust regardless of the geometry of the contact objects. | p. 17 (5.2. Evaluation of Force Measurement) |

## Dataset / Benchmark Role

- **p. 18 / 5.2. Evaluation of Force Measurement - extractive body cue:** In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be applied), ...
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** On the other hand, for the given training set and test set, the measurement is still influenced by the contact geometry.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The total size of the training dataset is around 28,815.
- **p. 16 / 5.2. Evaluation of Force Measurement - extractive body cue:** In this preliminary experiment, we train the force measurement neural network with the data of GelSight contacting objects with some basic shapes, including spheres, cylinders ...
- **p. 15 / 5. Evaluation - extractive body cue:** In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object shapes ...
- **p. 16 / 5.1. Evaluation of Shape Measurement - extractive body cue:** The ground truth of the geometry is hard to get, but the reconstructed 3D structures capture both the overall shape and local textures of the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. (a) a cookie is pressed against the skin of an elastomer block; (b) the skin is distorted, as shown in this view from ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. (a) basic principle of the Gelsight and the desktop design introduced in [7]. There are four main components for the GelSight sensor: an ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. (a) an example pattern of printed markers on the GelSight. In the figure, the elastomer is for the fingertip GelSight sensor [30] (Got ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. The minimum distinguishable force of the fingertip GelSight (Setup shown in Figure 14a, using the shape measurement and marker measurement respectively. The sensor ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Three kinds of elastomer coatings: semi-specular coating painted by bronze flake and aluminum flake paint, and matte coating by aluminum powder. In the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5. The procedure of segmenting and locating the markers in the GelSight images. (a) the initial GelSight frame Frm0 when noting is in touch; ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change corresponds ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be ... | embodiment, simulator version and control stack | p. 18 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Task/environment | On the other hand, for the given training set and test set, the measurement is still influenced by the contact geometry. | reset, timeout, object/scene variation | p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 9 (3.4. Algorithm for Measuring Marker Motion), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We train the network with the mean squared error loss function for the regression problem. | definition/direction/unit from same section | p. 17 (5.2. Evaluation of Force Measurement) |
| The coefficient of determination (R2) and root mean square error (RMSE) for the results of three different objects are also listed in the figure. | definition/direction/unit from same section | p. 17 (5.2. Evaluation of Force Measurement) |
| In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object ... | definition/direction/unit from same section | p. 15 (5. Evaluation) |
| For evaluating GelSight's geometry measurement, we firstly evaluate the sensor's precision in measuring the surface normal. | definition/direction/unit from same section | p. 16 (5.1. Evaluation of Shape Measurement) |
| The figures also indicate that there is some spatial variance of the sensor's measurement, but can be accepted for an approximate measurement. | definition/direction/unit from same section | p. 16 (5.1. Evaluation of Shape Measurement) |
| Figure 1. (a) a cookie is pressed against the skin of an elastomer block; (b) the skin is distorted, as shown in this view ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 2. (a) basic principle of the Gelsight and the desktop design introduced in [7]. There are four main components for the GelSight sensor: ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 1. The minimum distinguishable force of the fingertip GelSight (Setup shown in Figure 14a, using the shape measurement and marker measurement respectively. The ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the figures, we compared the measured values and the ground truth, of the pitch and yaw angles of the surface normal. | comparison identity and matched condition | p. 16 (5.1. Evaluation of Shape Measurement) |
| The comparison between the output of the neural network and ground truth from the force/torque sensor is summarized in Figure 14b-e. | comparison identity and matched condition | p. 17 (5.2. Evaluation of Force Measurement) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We replace the network's last fully-connected layer with an output layer of four neurons, corresponding to the forces and torques in four axes (Fx, ... | component/input/data sensitivity | p. 17 (5.2. Evaluation of Force Measurement) |
| Figure 2. (a) basic principle of the Gelsight and the desktop design introduced in [7]. There are four main components for the GelSight sensor: ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 14. Evaluation on the force measurement of fingertip GelSight with simple but unseen objects. (a) experiment setup, where the GelSight is fixed on ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to ... | Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement), p. 16 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Primary metric/result | In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object ... | numeric claim only at cited anchor | p. 15 (5. Evaluation) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Figure 8. The change of the marker displacement field with the increase of shear force. The degree of partial slip also increases as the ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. The contact surface is flat. When ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Additionally, it can detect slip by measuring the relative movement of the objects on the sensor. | p. 18 (6. Application) |
| body limitation/failure cue | As indicated in Section 3.7, the GelSight sensor can estimate the slip and incipient slip state from the stretching of the surface. | p. 18 (6. Application) |
| body limitation/failure cue | The results also show that the GelSight measurement of force can be robust regardless of the geometry of the contact objects. | p. 17 (5.2. Evaluation of Force Measurement) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The CNN model for measuring force and torque is adjusted from VGG-16 net [34], pre-trained on the computer vision dataset ImageNet [35]. | p. 17 (5.2. Evaluation of Force Measurement) |
| In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be ... | p. 18 (5.2. Evaluation of Force Measurement) |
| (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on ... | p. 8 (3.3. Algorithm for Measuring Shape) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The change of the marker displacement field with the increase of shear force. The degree of partial slip also increases as the force ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. The contact surface is flat. When the ...
- **p. 18 / 6. Application - extractive body cue:** Additionally, it can detect slip by measuring the relative movement of the objects on the sensor.
- **p. 18 / 6. Application - extractive body cue:** As indicated in Section 3.7, the GelSight sensor can estimate the slip and incipient slip state from the stretching of the surface.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The results also show that the GelSight measurement of force can be robust regardless of the geometry of the contact objects.

- **Evidence anchors reviewed:** datasets p. 18 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 16 (5.2. Evaluation of Force Measurement), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement), metrics p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement), p. 16 (5.1. Evaluation of Shape Measurement), p. 4 (Figure/Table caption), baselines p. 16 (5.1. Evaluation of Shape Measurement), p. 17 (5.2. Evaluation of Force Measurement), results p. 9 (Figure/Table caption), p. 15 (5. Evaluation), p. 16 (5.1. Evaluation of Shape Measurement), p. 16 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The coefficient of determination (R2) and root mean square error (RMSE) for the results of three different objects are also listed in the figure. (p. 17, 5.2. Evaluation of Force Measurement).
- **Metric evidence:** In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object shapes and contact force. (p. 15, 5. Evaluation).
- **Baseline/ablation evidence:** In the figures, we compared the measured values and the ground truth, of the pitch and yaw angles of the surface normal. (p. 16, 5.1. Evaluation of Shape Measurement).
- **Failure/negative evidence:** Sensors 2017, 17, 2762 18 of 21 truth qualitatively at all times, but the measurement at some entire contact sequences is worse than the others. (p. 18, 5.2. Evaluation of Force Measurement).
