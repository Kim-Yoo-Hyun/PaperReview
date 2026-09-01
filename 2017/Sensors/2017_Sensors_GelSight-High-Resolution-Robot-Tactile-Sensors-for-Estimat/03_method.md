# Method - GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/; PDF retrieval source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape)): The reflectance function R models both the lighting environment and the surface reflectance.

## Method Body Digest

- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The reflectance function R models both the lighting environment and the surface reflectance.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is N(x, y) = ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** In a simplified version, we only record the gradient at each entry space and match the gradient reading to the closest entry.
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The lookup table is three-dimensional, and each entry contains a gradient and a first-order approximation of the reflectance functions in the neighborhood near the gradient.
- **p. 2 / 1. Introduction - extractive body cue:** Robots need more than force feedback, while the existing sensors do not obtain enough tactile information for the robots.
- **p. 2 / 1. Introduction - extractive body cue:** Sensors 2017, 17, 2762 2 of 21 cup in the hand is going to slip, and thus adjust the gripping force accordingly; we can know ...
- **p. 9 / 3.4. Algorithm for Measuring Marker Motion - extractive body cue:** (a) the initial GelSight frame Frm0 when noting is in touch; (b) the low-pass Gaussian filtered image I0 from Frm0, where only the color background ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 2 / 1. Introduction - extractive body cue:** The first GelSight prototype was developed in 2009 by Johnson and Adelson [7].
- **p. 2 / 1. Introduction - extractive body cue:** We have developed sensors that are compact, yet have resolution far exceeding that of human skin.

## Source Evidence Cues

- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The reflectance function R models both the lighting environment and the surface reflectance.
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is N(x, y) = ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...
- **Detected method headings:** 3.3. Algorithm for Measuring Shape (p. 7); 3.4. Algorithm for Measuring Marker Motion (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | The reflectance function R models both the lighting environment and the surface reflectance. | p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is ... | p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast ... | p. 8 (3.3. Algorithm for Measuring Shape) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** In a simplified version, we only record the gradient at each entry space and match the gradient reading to the closest entry.
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** The lookup table is three-dimensional, and each entry contains a gradient and a first-order approximation of the reflectance functions in the neighborhood near the gradient.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Robots, need, more, force, feedback, while, existing, sensors, obtain, enough, tactile, information, hand, going | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Robots, need, more, force, feedback, while, existing, sensors, obtain, enough | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | past, decades, researchers, have, developed, many, different, tactile, sensors, robots | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | simplified, version, only, record, gradient, entry, space, match, reading, closest | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Robots need more than force feedback, while the existing sensors do not obtain enough tactile information for the robots.
- **p. 2 / 1. Introduction - extractive body cue:** Sensors 2017, 17, 2762 2 of 21 cup in the hand is going to slip, and thus adjust the gripping force accordingly; we can know ...
- **p. 9 / 3.4. Algorithm for Measuring Marker Motion - extractive body cue:** (a) the initial GelSight frame Frm0 when noting is in touch; (b) the low-pass Gaussian filtered image I0 from Frm0, where only the color background ...
- **p. 1 / 1. Introduction - extractive body cue:** With the force measurement from the fingertip tactile sensors, a robot is much less likely to break delicate objects.
- **p. 1 / 1. Introduction - extractive body cue:** The sensor has been applied to multiple commercialized robots, including the PR2 robot, and Barrett hands, and it successfully assisted common robotic tasks, such as ...
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** Sensors 2017, 17, 2762 8 of 21 sources from multiple directions, which can be inferred as the different channels in the red-green-blue (RGB) image I ...
- **p. 7 / 3.3. Algorithm for Measuring Shape - extractive body cue:** We model the surface of the sensor with a height function z = f (x, y), so that the surface normal is N(x, y) = ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | However, the relationship between the markers' motion and the contact force or shape is nonlinear when the contact geometry is unknown. | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Sensors 2017, 17, 2762 18 of 21 truth qualitatively at all times, but the measurement at some entire contact sequences is worse ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...
- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** The CNN model for measuring force and torque is adjusted from VGG-16 net [34], pre-trained on the computer vision dataset ImageNet [35].
- **p. 8 / 3.3. Algorithm for Measuring Shape - extractive body cue:** (4) We solve the Poission Equation (3) using fast Poisson solver with discrete sine transform (DST), thus we can get a fast computation on the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** reflectance, function, models, lighting, environment, surface, model, sensor, height, normal, form, because, zero, level, scalar, field, normally, equal, solve, Poission.
- **Relevant PDF headings:** 3.3. Algorithm for Measuring Shape (p. 7); 3.4. Algorithm for Measuring Marker Motion (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | In the long run, for making a good force measurement with GelSight, we should either collect a more comprehensive dataset (simulation methods ... | p. 18 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Contact / dynamics inference | In the figures, we compared the measured values and the ground truth, of the pitch and yaw angles of the surface normal. | p. 16 (5.1. Evaluation of Shape Measurement), p. 17 (5.2. Evaluation of Force Measurement) |
| Force-aware action correction | Figure 6. Calibration images (part) with different GelSight sensors. During calibration, a ball/ball array is pressed on the sensor, and the image ... | p. 9 (Figure/Table caption), p. 15 (5. Evaluation) |

## Failure and Ablation Link

- **p. 17 / 5.2. Evaluation of Force Measurement - extractive body cue:** We replace the network's last fully-connected layer with an output layer of four neurons, corresponding to the forces and torques in four axes (Fx, Fy, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. (a) basic principle of the Gelsight and the desktop design introduced in [7]. There are four main components for the GelSight sensor: an ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 14. Evaluation on the force measurement of fingertip GelSight with simple but unseen objects. (a) experiment setup, where the GelSight is fixed on a ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in linear relationship with the indenting depth, but ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The change of the marker displacement field with the increase of shear force. The degree of partial slip also increases as the force ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. The contact surface is flat. When the ...
- **p. 18 / 6. Application - extractive body cue:** Additionally, it can detect slip by measuring the relative movement of the objects on the sensor.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3.3. Algorithm for Measuring Shape), p. 7 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape), objective p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape), temporal p. 16 (5.2. Evaluation of Force Measurement), p. 18 (5.2. Evaluation of Force Measurement), p. 18 (5.2. Evaluation of Force Measurement), p. 2 (1. Introduction), p. 3 (2. Related Work), p. 4 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
