# GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/.
> PDF retrieval source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / Sensors
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, tactile sensing, Force, contact, manipulation
- Official paper: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/
- Full-text retrieval: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.를 문제로 두고, In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect the contact and contact force, or force ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** Tactile sensing is an important mode for both human and robots to perceive the environment.
- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 1 / 1. Introduction - extractive body cue:** For example, a successfully commercialized sensor is the tactile sensor array from Pressure Profile Systems, which measures the normal pressure distribution over the robot fingertip, ...
- **p. 1 / 1. Introduction - extractive body cue:** The sensor has been applied to multiple commercialized robots, including the PR2 robot, and Barrett hands, and it successfully assisted common robotic tasks, such as ...
- **p. 1 / 1. Introduction - extractive body cue:** With the force measurement from the fingertip tactile sensors, a robot is much less likely to break delicate objects.
- **p. 2 / 1. Introduction - extractive body cue:** Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.
- **p. 2 / 1. Introduction - extractive body cue:** When the sensor surface is painted with small black markers, the motion of the markers provides information about both normal force and shear force.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 2 / 1. Introduction - extractive body cue:** The first GelSight prototype was developed in 2009 by Johnson and Adelson [7].
- **p. 2 / 1. Introduction - extractive body cue:** We have developed sensors that are compact, yet have resolution far exceeding that of human skin.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The reflectance function R models both the lighting environment and the surface reflectance.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is N(x, y) = ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Robots need more than force feedback, while the existing sensors do not obtain enough tactile information for the robots. | tactile image/force, vision과 proprioceptive history | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | Robots, need, more, force, feedback, while, existing, sensors, obtain, enough, tactile, information | contact geometry, force state 또는 latent dynamics | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 9 (3.4. Algorithm for Measuring Marker Motion) |
| Output/action | Sensors 2017, 17, 2762 2 of 21 cup in the hand is going to slip, and thus adjust the gripping force accordingly; we can know whether a USB connector is going to ... | grasp/contact action, force command 또는 object motion | p. 2 (1. Introduction), p. 9 (3.4. Algorithm for Measuring Marker Motion), p. 1 (1. Introduction) |
| Objective/outcome | In a simplified version, we only record the gradient at each entry space and match the gradient reading to the closest entry. | slip/contact success, force/pose error와 robustness | p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 2 / 1. Introduction - extractive body cue:** The first GelSight prototype was developed in 2009 by Johnson and Adelson [7].
- **p. 2 / 1. Introduction - extractive body cue:** We have developed sensors that are compact, yet have resolution far exceeding that of human skin.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image intensity change corresponds ...
- **p. 15 / 5. Evaluation - extractive body cue:** In this section, we take the new compact GelSight sensor mentioned in [29] as an example to evaluate the sensor's performance in estimating object shapes ...
- **p. 16 / 5.1. Evaluation of Shape Measurement - extractive body cue:** Examples of the results are shown in Figure 13a.
- **p. 16 / 5.2. Evaluation of Force Measurement - extractive body cue:** In this preliminary experiment, we train the force measurement neural network with the data of GelSight contacting objects with some basic shapes, including spheres, cylinders ...
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The results also show that the GelSight measurement of force can be robust regardless of the geometry of the contact objects.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 15 (5. Evaluation) |
| Embodiment/environment | In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods could be applied), or choose some other methods that can ... | hardware/simulator version and reset protocol | p. 18 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Dataset/benchmark | The total size of the training dataset is around 28,815. | role, split, size and leakage | p. 18 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 16 (5.2. Evaluation of Force Measurement) |
| Metric | We train the network with the mean squared error loss function for the regression problem. | definition, denominator, direction and uncertainty | p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 15 (5. Evaluation) |
| Baseline/ablation | In the figures, we compared the measured values and the ground truth, of the pitch and yaw angles of the surface normal. | fair input/data/compute/action matching | p. 16 (5.1. Evaluation of Shape Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |

## Explicit Limitations and Failure Boundary

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The change of the marker displacement field with the increase of shear force. The degree of partial slip also increases as the force ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. The contact surface is flat. When the ...
- **p. 18 / 6. Application - extractive body cue:** Additionally, it can detect slip by measuring the relative movement of the objects on the sensor.
- **p. 18 / 6. Application - extractive body cue:** As indicated in Section 3.7, the GelSight sensor can estimate the slip and incipient slip state from the stretching of the surface.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The results also show that the GelSight measurement of force can be robust regardless of the geometry of the contact objects.
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** On the one hand, the prediction from CNN highly relies on the training data, and to make robust measurement, the training data should contain the ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.를 문제로 두고, In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect the contact and contact force, or force ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape), p. 9 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing. (p. 2, 1. Introduction).
- **Actual contribution:** Tactile sensing is an important mode for both human and robots to perceive the environment. (p. 1, 1. Introduction).
- **Evaluation boundary:** The coefficient of determination (R2) and root mean square error (RMSE) for the results of three different objects are also listed in the figure. (p. 17, 5.2. Evaluation of Force Measurement).
- **Explicit failure boundary:** Sensors 2017, 17, 2762 18 of 21 truth qualitatively at all times, but the measurement at some entire contact sequences is worse than the others. (p. 18, 5.2. Evaluation of Force Measurement).
