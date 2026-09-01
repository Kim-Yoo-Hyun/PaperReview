# Evaluation - GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (B. Simulation Results), p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results), p. 6 (B. Simulation Results), p. 7 (C. Hardware Results)): According to the results, we can see an improvement

## Evaluation Body Digest

- **p. 9 / C. Hardware Results - extractive body cue:** The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the pivot point and ...
- **p. 6 / B. Simulation Results - extractive body cue:** The simulation uses the same values as the hardware for the hand joints' PD gains.
- **p. 6 / B. Simulation Results - extractive body cue:** Associated hardware experiments will be presented in IV-C.
- **p. 7 / C. Hardware Results - extractive body cue:** Dexterous Grasping: We will first introduce the underlying, problem of inaccurate force measurements in hardware by presenting a 2-finger pinch grasp of a sphere.
- **p. 9 / C. Hardware Results - extractive body cue:** 14: Cube turning hardware experiment,
- **p. 7 / B. Simulation Results - extractive body cue:** 7: Simulation environment in MuloCo for the wrench grasp and cube extrinsic manipulation, Simulated interaction forces at the ‘contact points are displayed.
- **p. 8 / C. Hardware Results - extractive body cue:** Object / Conwot / Success ate / Mean & su fore eror
- **p. 8 / C. Hardware Results - extractive body cue:** From ¢ = 27s we lift the object to show a successful grasp, at = 336 we put the object back down and keep stable ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** B. Simulation Results (p. 6); C. Hardware Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | According to the results, we can see an improvement | p. 7 (B. Simulation Results) |
| C. Hardware Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted ... | p. 8 (C. Hardware Results) |
| C. Hardware Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it ... | p. 8 (C. Hardware Results) |
| C. Hardware Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similar to the wrench example, we ‘observe a higher success rate when using the estimated force values. | p. 9 (C. Hardware Results) |
| B. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Since the thumb opposes the forces applied by the index and middle finger, thus they have to increase or decrease together, thus the equilibrium ... | p. 6 (B. Simulation Results) |

## Dataset / Benchmark Role

- **p. 9 / C. Hardware Results - extractive body cue:** The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the pivot point and ...
- **p. 6 / B. Simulation Results - extractive body cue:** The simulation uses the same values as the hardware for the hand joints' PD gains.
- **p. 6 / B. Simulation Results - extractive body cue:** Associated hardware experiments will be presented in IV-C.
- **p. 7 / C. Hardware Results - extractive body cue:** Dexterous Grasping: We will first introduce the underlying, problem of inaccurate force measurements in hardware by presenting a 2-finger pinch grasp of a sphere.
- **p. 9 / C. Hardware Results - extractive body cue:** 14: Cube turning hardware experiment,
- **p. 7 / B. Simulation Results - extractive body cue:** 7: Simulation environment in MuloCo for the wrench grasp and cube extrinsic manipulation, Simulated interaction forces at the ‘contact points are displayed.
- **p. 8 / C. Hardware Results - extractive body cue:** Object / Conwot / Success ate / Mean & su fore eror
- **p. 8 / C. Hardware Results - extractive body cue:** From ¢ = 27s we lift the object to show a successful grasp, at = 336 we put the object back down and keep stable ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: FE-plane, M-Cone and Constraint convex set
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Mustration of measurement sub-space cone Assume (wo
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Block diagram of the control system.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Hardware setup including Allegro hand equipped with Touchlab fingertips, and Franka arm. The 3D-printed sphere and ‘wrench, as well as the cylindrical can ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Simulation environment in MuloCo for the wrench grasp and cube extrinsic manipulation, Simulated interaction forces at the ‘contact points are displayed.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Grasping wrench comparison using the force estimation (left) and the raw measurements (right).
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 10: Successfully grasping different objects using the proposed
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 12: 3-Finger grasp of wrench. From £ = 0s to ¢ = 27s we conirol the estimated forces to the desired values for each ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the pivot point ... | embodiment, simulator version and control stack | p. 9 (C. Hardware Results), p. 6 (B. Simulation Results) |
| Task/environment | The simulation uses the same values as the hardware for the hand joints' PD gains. | reset, timeout, object/scene variation | p. 6 (B. Simulation Results), p. 6 (B. Simulation Results) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 5 (B. Force Estimation), p. 1 (A. State of Tactile Sensors) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it ... | definition/direction/unit from same section | p. 8 (C. Hardware Results) |
| The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is ... | definition/direction/unit from same section | p. 8 (C. Hardware Results) |
| Similar to the wrench example, we ‘observe a higher success rate when using the estimated force values. | definition/direction/unit from same section | p. 9 (C. Hardware Results) |
| ‘When using the raw measurement, the system was not able to converge to the desired grasp and resulted in a force error of around ... | definition/direction/unit from same section | p. 9 (C. Hardware Results) |
| ‘Thus, through these experiments, we showed that by using the force estimation to account for measurement noise and errors, the hand can perform manipulation ... | definition/direction/unit from same section | p. 10 (C. Hardware Results) |
| This exemplifies the problem of the error in measurements, where we need the thumb to apply more force to reach to its desired value ... | definition/direction/unit from same section | p. 6 (B. Simulation Results) |
| 11, the estimated contact forces converge to the desired value with a mean error of 0.1.V. | definition/direction/unit from same section | p. 7 (C. Hardware Results) |
| Once the controller converges to the desired forces, the system starts tracking the desired cube's yaw angle with an RMS error under 1°. | definition/direction/unit from same section | p. 7 (B. Simulation Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared the controller when using the estimated force values against the raw measurements, with the results shown in Fig. | comparison identity and matched condition | p. 6 (B. Simulation Results) |
| As part of determining the benefits of our geometric framework for force planning and estimation, we compared the comutation time of our method, in ... | comparison identity and matched condition | p. 7 (B. Simulation Results) |
| The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is ... | comparison identity and matched condition | p. 8 (C. Hardware Results) |
| 1) without over-pressuring it (following constraint in eq. | comparison identity and matched condition | p. 7 (C. Hardware Results) |
| We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted ... | comparison identity and matched condition | p. 8 (C. Hardware Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 1) without over-pressuring it (following constraint in eq. | component/input/data sensitivity | p. 7 (C. Hardware Results) |
| We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted ... | component/input/data sensitivity | p. 8 (C. Hardware Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed ... | According to the results, we can see an improvement | PDF body cue; verify exact table/figure and matched conditions | p. 7 (B. Simulation Results), p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results), p. 6 (B. Simulation Results), p. 7 (C. Hardware Results) |
| Primary metric/result | We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted ... | numeric claim only at cited anchor | p. 8 (C. Hardware Results) |

- Numeric sentences retained from the body:
- **p. 8 / C. Hardware Results - extractive body cue:** We hold the grasp for 20s to show that force ‘equilibrium is achieved and the object pose remains static. ‘Then, the object is lifted successfully ...
- **p. 8 / C. Hardware Results - extractive body cue:** At 40s, we switch the controller to use the raw measurements as observation, We can see that while the system tres to control the contact ...
- **p. 8 / C. Hardware Results - extractive body cue:** From £ = 0s to ¢ = 27s we conirol the estimated forces to the desired values for each finger.
- **p. 8 / C. Hardware Results - extractive body cue:** From ¢ = 27s we lift the object to show a successful grasp, at = 336 we put the object back down and keep stable ...
- **p. 8 / C. Hardware Results - extractive body cue:** 440s we try to control the raw force values, The system is not able to contol all of the fingers to the desited force and ...
- **p. 5 / B. Force Estimation - extractive body cue:** For the experiments, we use the Allegro Hand VA which has 4 fingers, each with 4 Degrees of Freedom (DoF), and we replaced the original ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips. | p. 10 (V. Discussion) |
| body limitation/failure cue | We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, ... | p. 10 (V. Discussion) |
| body limitation/failure cue | The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is ... | p. 8 (C. Hardware Results) |
| body limitation/failure cue | For the remaining failure case, the hysteresis of multiple taxels of the index finger created the illusion of a large force being sensed making ... | p. 9 (C. Hardware Results) |
| body limitation/failure cue | Since the thumb opposes the forces applied by the index and middle finger, thus they have to increase or decrease together, thus the equilibrium ... | p. 6 (B. Simulation Results) |
| body limitation/failure cue | It can be seen that equilibrium cannot be achieved since while the thumb and middle finger have achieved forces close to desired values within ... | p. 8 (C. Hardware Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run both simulation and hardware experiments. to evaluate the performance of our proposed method. | p. 5 (B. Force Estimation) |
| Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed ... | p. 2 (B. Utilizing Tactile Readings) |
| As each extrinsic contact point contributes to one independent DoF in the sub-space cone, we first compute n. linearly independent force vectors with each ... | p. 4 (B. Force Estimation) |
| For the hardware experiments, we use a Franka FR3 arm to position and move the Allegro hand. | p. 5 (B. Force Estimation) |
| Associated hardware experiments will be presented in IV-C. | p. 6 (B. Simulation Results) |
| The simulation uses the same values as the hardware for the hand joints' PD gains. | p. 6 (B. Simulation Results) |
| Dexterous Grasping: We will first introduce the underlying, problem of inaccurate force measurements in hardware by presenting a 2-finger pinch grasp of a sphere. | p. 7 (C. Hardware Results) |
| Given the object's ‘mass, CoM, contact locations, and friction coefficients at the Contact points, we use our force planner to compute the desired force ... | p. 7 (C. Hardware Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / V. Discussion - extractive body cue:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.
- **p. 10 / V. Discussion - extractive body cue:** We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, such ...
- **p. 8 / C. Hardware Results - extractive body cue:** The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented ...
- **p. 9 / C. Hardware Results - extractive body cue:** For the remaining failure case, the hysteresis of multiple taxels of the index finger created the illusion of a large force being sensed making the ...
- **p. 6 / B. Simulation Results - extractive body cue:** Since the thumb opposes the forces applied by the index and middle finger, thus they have to increase or decrease together, thus the equilibrium cannot ...
- **p. 8 / C. Hardware Results - extractive body cue:** It can be seen that equilibrium cannot be achieved since while the thumb and middle finger have achieved forces close to desired values within an ...

- **PDF anchors reviewed:** datasets p. 9 (C. Hardware Results), p. 6 (B. Simulation Results), p. 6 (B. Simulation Results), p. 7 (C. Hardware Results), p. 9 (C. Hardware Results), p. 7 (B. Simulation Results), metrics p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results), p. 9 (C. Hardware Results), p. 10 (C. Hardware Results), p. 6 (B. Simulation Results), baselines p. 6 (B. Simulation Results), p. 7 (B. Simulation Results), p. 8 (C. Hardware Results), p. 7 (C. Hardware Results), p. 8 (C. Hardware Results), results p. 7 (B. Simulation Results), p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results), p. 6 (B. Simulation Results), p. 7 (C. Hardware Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
