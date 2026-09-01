# Evaluation - Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://hal.science/lirmm-00831097; PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS)): To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest to be grasped.

## Evaluation Body Digest

- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The acceleration ¨q can be integrated in simulation, or provided as control input to the robot servo control; or the torques can be given as ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** A tracking task is imposed to the robot head to make it oscillate.
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 10 The reference acceleration is computed from this error as a proportional-derivative (PD) control law: ¨e⋆ op = -λpeop ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** Two tasks erh and elh, defined by (47), are set on each robot gripper to control the position and orientation toward the corresponding armrest.
- **p. 13 / VII. EXPERIMENTS - extractive body cue:** The gaze task focuses sequentially on the left and right armrests and on a virtual point in front of the robot.
- **p. 14 / VII. EXPERIMENTS - extractive body cue:** Experiment C: Dynamic contact transition 1) Description: At the beginning of the motion, the robot is standing on both feet and its COM is artificially ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** The robot sits in an armchair (see Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** VII. EXPERIMENTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VII. EXPERIMENTS | EMPIRICAL / SIMULATION | To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest to be ... | p. 12 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / SIMULATION | The second gripper helps to improve the stability by decreasing the tangent forces at each contact point. | p. 14 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / SIMULATION | The second one presents a complex sequence of tasks to make the robot sit in an armchair using several successive contacts. | p. 10 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / SIMULATION | However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly ... | p. 10 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / SIMULATION | 2) Results: The experiment is summed up by Figures 3 to 6. | p. 11 (VII. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The acceleration ¨q can be integrated in simulation, or provided as control input to the robot servo control; or the torques can be given as ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** A tracking task is imposed to the robot head to make it oscillate.
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 10 The reference acceleration is computed from this error as a proportional-derivative (PD) control law: ¨e⋆ op = -λpeop ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** Two tasks erh and elh, defined by (47), are set on each robot gripper to control the position and orientation toward the corresponding armrest.
- **p. 13 / VII. EXPERIMENTS - extractive body cue:** The gaze task focuses sequentially on the left and right armrests and on a virtual point in front of the robot.
- **p. 14 / VII. EXPERIMENTS - extractive body cue:** Experiment C: Dynamic contact transition 1) Description: At the beginning of the motion, the robot is standing on both feet and its COM is artificially ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** The robot sits in an armchair (see Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Dynamic multi-contact motion with the HRP-2 model. limits), that reduce the space of possible motions. These constraints can typically be formulated as equalities ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 2. Random sampling of the reached support region. The actual support polygon is the encompassing rectangle. The point clouds display the ZMP of random ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger and ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 3. Experiment A: Top: Snapshots of the oscillatory movement 2pt- medium. Bottom: Feet and ZMP positions at the corresponding instants. The ZMP saturates on ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4. Experiment A: ZMP position along the forward (x) axis for the two motions with only the feet contacts. The support polygon is a ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 5. Experiment A: robustness criterion VI-C. For the first two motions 2pt-low and 2pt-medium, the criterion is given with respect to the support polygon ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6. Experiment A: Computation time. For the motion 2pt-medium, the saturation of the force constraints clearly induces an increase of the computation cost, whereas ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7. Experiment B: Snapshots of the motion executed on the real HRP-2 robot. The robot is standing on both feet (t = 0s). It ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics. | embodiment, simulator version and control stack | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS) |
| Task/environment | The acceleration ¨q can be integrated in simulation, or provided as control input to the robot servo control; or the torques can be given ... | reset, timeout, object/scene variation | p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (I. INTRODUCTION), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly ... | definition/direction/unit from same section | p. 10 (VII. EXPERIMENTS) |
| The task error is the position p and angle-vector orientation rθ [74] of the operational point with respect to a reference p∗, rθ∗expressed in ... | definition/direction/unit from same section | p. 10 (VII. EXPERIMENTS) |
| When reaching a fixed target, an adaptive gain is typically used: λp : //e// →(λ0 -λ∞)eβ//e// + λ∞ (49) where λ0 is the gain ... | definition/direction/unit from same section | p. 11 (VII. EXPERIMENTS) |
| Submitted to IEEE Transaction on Robotics 10 The reference acceleration is computed from this error as a proportional-derivative (PD) control law: ¨e⋆ op = ... | definition/direction/unit from same section | p. 11 (VII. EXPERIMENTS) |
| Experiment A: robustness criterion VI-C. | definition/direction/unit from same section | p. 12 (VII. EXPERIMENTS) |
| Similarly, the ZMP saturates on the back. | definition/direction/unit from same section | p. 12 (VII. EXPERIMENTS) |
| 0 5 10 15 20 25 0 5 10 15 time (s) Distance to the cone Fig. | definition/direction/unit from same section | p. 13 (VII. EXPERIMENTS) |
| The distance is computed with respect to the friction cones. | definition/direction/unit from same section | p. 13 (VII. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear ... | comparison identity and matched condition | p. 12 (VII. EXPERIMENTS) |
| From t = 0.7s, the COM is out of the support polygon with a positive velocity: it is then impossible to bring it back ... | comparison identity and matched condition | p. 14 (VII. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear ... | component/input/data sensitivity | p. 12 (VII. EXPERIMENTS) |
| From t = 0.7s, the COM is out of the support polygon with a positive velocity: it is then impossible to bring it back ... | component/input/data sensitivity | p. 14 (VII. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion. | To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest to be ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |
| Primary metric/result | The second gripper helps to improve the stability by decreasing the tangent forces at each contact point. | numeric claim only at cited anchor | p. 14 (VII. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** In theory, the control sampling time ∆T = 1ms should be used for TS.
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** The reference position is given by a time-varying sinusoid, around a central point xc = 0.02 and with amplitude of 5cm and frequency 0.3Hz (low ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 11 t=1.2s t=1.7s t=2.1s Fig.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** After t = 8s, the left arm is used to sustain the robot.
- **p. 13 / VII. EXPERIMENTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 12 t=0s t=7s t=15s t=19s Fig.
- **p. 13 / VII. EXPERIMENTS - extractive body cue:** Experiment B: Snapshots of the motion executed on the real HRP-2 robot.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q ... | p. 10 (VII. EXPERIMENTS) |
| body limitation/failure cue | To prevent a collision when grasping, an intermediate point is first reached, above the grasping position. | p. 12 (VII. EXPERIMENTS) |
| body limitation/failure cue | In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints). | p. 12 (VII. EXPERIMENTS) |
| body limitation/failure cue | Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | Experiment C: Robustness criterion VI-C. | p. 15 (VIII. CONCLUSION) |
| body limitation/failure cue | However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly ... | p. 10 (VII. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It is computed using the control framework SOT [33] and the dedicated solver [26]. | p. 10 (VII. EXPERIMENTS) |
| The dynamic simulator AMELIF [73] was used to resolve the forward dynamics from the computed torques τ ∗. | p. 10 (VII. EXPERIMENTS) |
| Then the distance of the point ψ∗(46) to this constraint set is computed. | p. 11 (VII. EXPERIMENTS) |
| First, the distance is computed to the constraint set of the solver (the 4cm-wide support polygon). | p. 11 (VII. EXPERIMENTS) |
| The distance is computed with respect to the friction cones. | p. 13 (VII. EXPERIMENTS) |
| In order to compute f, (31) should be inverted by using a particular generalized inverse X#: f = X#φ (33) The normal component f ... | p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Random forces φ are shot and the corresponding f = X#φ are computed. | p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To prevent a collision when grasping, an intermediate point is first reached, above the grasping position.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints).
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger and ...
- **p. 15 / VIII. CONCLUSION - extractive body cue:** Experiment C: Robustness criterion VI-C.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies ...

- **PDF anchors reviewed:** datasets p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS), p. 13 (VII. EXPERIMENTS), metrics p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS), baselines p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), results p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
