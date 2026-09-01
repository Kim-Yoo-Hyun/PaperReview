# Method - GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 6 (A. Force Measurement via Tactile Array), p. 4 (B. Force Estimation)): In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how to obtain force estimation «and ...

## Method Body Digest

- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 5 / B. Force Estimation - extractive body cue:** We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions.
- **p. 5 / B. Force Estimation - extractive body cue:** We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J to compute direction ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 6 / A. Force Measurement via Tactile Array - extractive body cue:** We use these characteristics in simulating our tactile responses in MuJoCo to have an accurate representation of the error and noise of our tactile fingertips ...
- **p. 4 / B. Force Estimation - extractive body cue:** As each extrinsic contact point contributes to one independent DoF in the sub-space cone, we first compute n. linearly independent force vectors with each one ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** In this paper, we propose GeoDEx, a unified framework that fully utilizes imperfect tactile sensor readings and can be used for force planning and control ...
- **p. 5 / B. Force Estimation - extractive body cue:** (Force planning for extrinsic manipulation) Given 4 set of intrinsic contact points and a set of extrinsic contact points, planning a set of safe intrinsic ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...

## Source Evidence Cues

- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 5 / B. Force Estimation - extractive body cue:** We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions.
- **p. 5 / B. Force Estimation - extractive body cue:** We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J to compute direction ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 6 / A. Force Measurement via Tactile Array - extractive body cue:** We use these characteristics in simulating our tactile responses in MuJoCo to have an accurate representation of the error and noise of our tactile fingertips ...
- **p. 4 / B. Force Estimation - extractive body cue:** As each extrinsic contact point contributes to one independent DoF in the sub-space cone, we first compute n. linearly independent force vectors with each one ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** In this paper, we propose GeoDEx, a unified framework that fully utilizes imperfect tactile sensor readings and can be used for force planning and control ...
- **Detected method headings:** method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the ... | p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions. | p. 5 (B. Force Estimation), p. 5 (B. Force Estimation) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J ... | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Force Estimation - extractive body cue:** (Force planning for extrinsic manipulation) Given 4 set of intrinsic contact points and a set of extrinsic contact points, planning a set of safe intrinsic ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Forces on FE-plane satisfy linear force equilibrium constraints:
- **p. 3 / B. Utilizing Tactile Readings - extractive body cue:** Definition 3 (Constraint convex set).
- **p. 3 / B. Utilizing Tactile Readings - extractive body cue:** 2: FE-plane, M-Cone and Constraint convex set
- **p. 4 / B. Force Estimation - extractive body cue:** thus we rewrite constraints of af. as constraints on ¢, for each linear constraint of from constraint matrix Ce
- **p. 4 / B. Force Estimation - extractive body cue:** Cyclilr ze > di <2) It can be rewritten as Cyclile + -Cyeli]™M! - Cpe] Sb 13) We can then write constraints on the ellipsoid ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 4 (B. Force Estimation), p. 4 (B. Force Estimation), p. 5 (B. Force Estimation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | interaction, between, fingertips, objects, measured, tactile, output, normal, forces, contact, location, hardware, setup, experiment | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | interaction, between, fingertips, objects, measured, tactile, output, normal, forces, contact | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | Through, various, experimental, while, relying, direct, inaccurate, noisy, force, readings | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | Force, planning, extrinsic, manipulation, Given, intrinsic, contact, points, safe, forces | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / B. Force Estimation - extractive body cue:** The interaction between the fingertips and the objects is measured using the tactile fingertips which output normal forces at the contact location. ‘The hardware setup ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** the finger-object contacts with consideration of sensor error; a force estimator that uses tactile sensor reading, the robot state and the object pose to estimates ...
- **p. 5 / B. Force Estimation - extractive body cue:** Due to the sensor's measurement error we use the proposed force estimator in IL-B to get an improved force observation that we use to close ...
- **p. 1 / A. State of Tactile Sensors - extractive body cue:** As one of the state-of-the-art tactile sensor arrays, Xela sensors [10] is compact, deformable, and can provide 3D force direction and magnitude readings with contact ...
- **p. 6 / A. Force Measurement via Tactile Array - extractive body cue:** forces and their dense coverage of the fingertip surface, including sides and the top, allows a reliable tactile-based dexterous ‘manipulation, However, despite their higher performance ...
- **p. 1 / B. Utilizing Tactile Readings - extractive body cue:** For camera-based tactile sensors, [17] has built depth maps from raw images and regressive analytical models to extract, force data from depth maps.
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Additionally, compared to directly running ‘optimization using SOCP (Second Order Cone Programming), planning and force estimation using our framework achieves a Lx ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, will, first, define, necessary, concepts, theoretical, framework, then, address, problems, obtain, force, estimation, perform, planning, observation, uncertainty, MwoCo, simulate.
- **Relevant PDF headings:** method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the ... | p. 9 (C. Hardware Results), p. 6 (B. Simulation Results) |
| Contact / dynamics inference | We compared the controller when using the estimated force values against the raw measurements, with the results shown in Fig. | p. 6 (B. Simulation Results), p. 7 (B. Simulation Results) |
| Force-aware action correction | According to the results, we can see an improvement | p. 7 (B. Simulation Results), p. 8 (C. Hardware Results) |

## Failure and Ablation Link

- **p. 7 / C. Hardware Results - extractive body cue:** 1) without over-pressuring it (following constraint in eq.
- **p. 8 / C. Hardware Results - extractive body cue:** We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted successfully ...
- **p. 10 / V. Discussion - extractive body cue:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.
- **p. 10 / V. Discussion - extractive body cue:** We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, such ...
- **p. 8 / C. Hardware Results - extractive body cue:** The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented ...
- **p. 9 / C. Hardware Results - extractive body cue:** For the remaining failure case, the hysteresis of multiple taxels of the index finger created the illusion of a large force being sensed making the ...
- **p. 6 / B. Simulation Results - extractive body cue:** Since the thumb opposes the forces applied by the index and middle finger, thus they have to increase or decrease together, thus the equilibrium cannot ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 6 (A. Force Measurement via Tactile Array), p. 4 (B. Force Estimation), objective p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 4 (B. Force Estimation), p. 4 (B. Force Estimation), temporal p. 1 (Front matter), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 7 (B. Simulation Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
