# GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, force uncertainty, dexterous manipulation, extrinsic manipulation, geometric planning
- Official paper: https://www.roboticsproceedings.org/rss21/p057.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p057.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution tactile information limit the use of these ...를 문제로 두고, Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping and extrinsic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Sense of touch that allows robots to detect contact and measure interaction forces enables them to perform ‘challenging tasks such as grasping fragile objects or ...
- **p. 1 / Abstract - extractive body cue:** Tactile sensors in theory can equip the robots with such ‘capabilities.
- **p. 1 / Abstract - extractive body cue:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise.
- **p. 1 / Abstract - extractive body cue:** This has limited the values these sensors can offer in manipulation applications that require force ‘control.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed hardware ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** We will end by describing the control architecture of our framework.
- **p. 3 / B. Force Estimation - extractive body cue:** Our projection allows changes to normal force magnitude and practically gives similar results as we will show in the experimental section,
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 5 / B. Force Estimation - extractive body cue:** We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions.
- **p. 5 / B. Force Estimation - extractive body cue:** We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J to compute direction ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The interaction between the fingertips and the objects is measured using the tactile fingertips which output normal forces at the contact location. ‘The hardware setup and experiment objects are shown in Fig. | tactile image/force, vision과 proprioceptive history | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings) |
| State/latent | interaction, between, fingertips, objects, measured, tactile, output, normal, forces, contact, location, hardware | contact geometry, force state 또는 latent dynamics | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation) |
| Output/action | the finger-object contacts with consideration of sensor error; a force estimator that uses tactile sensor reading, the robot state and the object pose to estimates all contact forces that would achieve force ... | grasp/contact action, force command 또는 object motion | p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 1 (A. State of Tactile Sensors) |
| Objective/outcome | (Force planning for extrinsic manipulation) Given 4 set of intrinsic contact points and a set of extrinsic contact points, planning a set of safe intrinsic forces can be formulated similar 10 11 ... | slip/contact success, force/pose error와 robustness | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** We will end by describing the control architecture of our framework.
- **p. 3 / B. Force Estimation - extractive body cue:** Our projection allows changes to normal force magnitude and practically gives similar results as we will show in the experimental section,
- **p. 7 / B. Simulation Results - extractive body cue:** According to the results, we can see an improvement
- **p. 8 / C. Hardware Results - extractive body cue:** We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted successfully ...
- **p. 8 / C. Hardware Results - extractive body cue:** ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it was ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (B. Simulation Results), p. 8 (C. Hardware Results) |
| Embodiment/environment | The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the pivot point and the contacts, the algorithm precomputes a trajectory ... | hardware/simulator version and reset protocol | p. 9 (C. Hardware Results), p. 6 (B. Simulation Results) |
| Dataset/benchmark | Associated hardware experiments will be presented in IV-C. | role, split, size and leakage | p. 9 (C. Hardware Results), p. 6 (B. Simulation Results), p. 6 (B. Simulation Results), p. 7 (C. Hardware Results) |
| Metric | ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it was successful and when it failed | definition, denominator, direction and uncertainty | p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results) |
| Baseline/ablation | We compared the controller when using the estimated force values against the raw measurements, with the results shown in Fig. | fair input/data/compute/action matching | p. 6 (B. Simulation Results), p. 7 (B. Simulation Results), p. 8 (C. Hardware Results) |

## Explicit Limitations and Failure Boundary

- **p. 10 / V. Discussion - extractive body cue:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.
- **p. 10 / V. Discussion - extractive body cue:** We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, such ...
- **p. 8 / C. Hardware Results - extractive body cue:** The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented ...
- **p. 9 / C. Hardware Results - extractive body cue:** For the remaining failure case, the hysteresis of multiple taxels of the index finger created the illusion of a large force being sensed making the ...
- **p. 6 / B. Simulation Results - extractive body cue:** Since the thumb opposes the forces applied by the index and middle finger, thus they have to increase or decrease together, thus the equilibrium cannot ...
- **p. 8 / C. Hardware Results - extractive body cue:** It can be seen that equilibrium cannot be achieved since while the thumb and middle finger have achieved forces close to desired values within an ...
- **p. 9 / C. Hardware Results - extractive body cue:** We also tested rotations beyond 30° but due to the friction between the ‘cube and the table, the cube would start to slip on the ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution tactile information limit the use of these ...를 문제로 두고, Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping and extrinsic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Iyrropucrion), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise. (p. 1, Abstract).
- **Actual contribution:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Evaluation boundary:** The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented in table Ill, We can ... (p. 8, C. Hardware Results).
- **Explicit failure boundary:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
