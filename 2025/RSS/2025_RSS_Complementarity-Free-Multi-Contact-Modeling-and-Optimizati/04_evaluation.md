# Evaluation - Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 12 (Figure/Table caption), p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results)): (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success

## Evaluation Body Digest

- **p. 9 / B. MPC Setting and Results - extractive body cue:** ABLE Il: The model setting for all objects and tasks.
- **p. 9 / B. MPC Setting and Results - extractive body cue:** The MPC path and final cost functions for all objects and tasks are defined as
- **p. 10 / B. MPC Setting and Results - extractive body cue:** to the very low success rate of Implicit MPC for this task type,
- **p. 10 / B. MPC Setting and Results - extractive body cue:** 9 shows some random examples of in-air manipulation with different objects
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate across ...
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Tach objec' rewlls are bated on 20 random als, or impli MPC, final position or quatesion errors are computed using all due to fewer successful ...
- **p. 9 / B. MPC Setting and Results - extractive body cue:** the manipulation accuracy is evaluated using
- **p. 9 / B. MPC Setting and Results - extractive body cue:** final postion eror final heading angle error: /¥arge 60 both calculated using the last 20 steps of a MPC rollout Fg

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** B. MPC Setting and Results (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. MPC Setting and Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | p. 10 (B. MPC Setting and Results) |
| B. MPC Setting and Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | to the very low success rate of Implicit MPC for this task type, | p. 10 (B. MPC Setting and Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate ... | p. 12 (Figure/Table caption) |
| B. MPC Setting and Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | For each object, we conduct 20 trials with different random inital and target poses. ‘The results are in Table IV, where we quantify the ... | p. 9 (B. MPC Setting and Results) |
| B. MPC Setting and Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | the manipulation accuracy is evaluated using | p. 9 (B. MPC Setting and Results) |

## Dataset / Benchmark Role

- **p. 9 / B. MPC Setting and Results - extractive body cue:** ABLE Il: The model setting for all objects and tasks.
- **p. 9 / B. MPC Setting and Results - extractive body cue:** The MPC path and final cost functions for all objects and tasks are defined as
- **p. 10 / B. MPC Setting and Results - extractive body cue:** to the very low success rate of Implicit MPC for this task type,
- **p. 10 / B. MPC Setting and Results - extractive body cue:** 9 shows some random examples of in-air manipulation with different objects

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols. I~ and Allegro hand on-palm ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Left: a sphere is accelerated between two frictional planes under an external force (green arrow), Right: the tangential velocity of the sphere versus ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Left: an unactuated box sliding with initial horizontal velocity Middle and right: the horizontal velocity and vertical position uajectories, respectively. QP-based model (7) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, our ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Three-fingertip fingertips (red, green, blue) are actuated. The tests include 4 objects: (a) Stanford bunny, (b) cube, (c) foam brick, and (d) stick. ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: On-ground manipulation examples. (a) On-ground rotation of Stanford bunny. (b) On-ground flipping of cube. (¢) On-ground flipping of foambrick. (2}(e) On-ground flipping of ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 9: Inair manipulation examples. (a) Two random trials of bunny in-air manipulation. (b) Two random trials of cube in-air manipulation. (c) ‘Two random tials ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 11: (a) TriFinger in-hand manipulation. (b) 4-Fingered Allegro hand on-palm reorientation. Both simulation environments are built using MuroCo [59].

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ABLE Il: The model setting for all objects and tasks. | embodiment, simulator version and control stack | p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results) |
| Task/environment | The MPC path and final cost functions for all objects and tasks are defined as | reset, timeout, object/scene variation | p. 9 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| to the very low success rate of Implicit MPC for this task type, | definition/direction/unit from same section | p. 10 (B. MPC Setting and Results) |
| Tach objec' rewlls are bated on 20 random als, or impli MPC, final position or quatesion errors are computed using all due to fewer ... | definition/direction/unit from same section | p. 10 (B. MPC Setting and Results) |
| the manipulation accuracy is evaluated using | definition/direction/unit from same section | p. 9 (B. MPC Setting and Results) |
| final postion eror final heading angle error: /¥arge 60 both calculated using the last 20 steps of a MPC rollout Fg | definition/direction/unit from same section | p. 9 (B. MPC Setting and Results) |
| Fig. 13: An example of the TriFinger in-hand manipulation of an aiplane object. The first five panels are screenshots of a MPC rollout at ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Fig. 4: Left: a sphere is accelerated between two frictional planes under an external force (green arrow), Right: the tangential velocity of the sphere ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | comparison identity and matched condition | p. 10 (B. MPC Setting and Results) |
| Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 5: Left: an unactuated box sliding with initial horizontal velocity Middle and right: the horizontal velocity and vertical position uajectories, respectively. QP-based model ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Without ground support, the three fingertips | comparison identity and matched condition | p. 10 (B. MPC Setting and Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without ground support, the three fingertips | component/input/data sensitivity | p. 10 (B. MPC Setting and Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | PDF body cue; verify exact table/figure and matched conditions | p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 12 (Figure/Table caption), p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results) |
| Primary metric/result | to the very low success rate of Implicit MPC for this task type, | numeric claim only at cited anchor | p. 10 (B. MPC Setting and Results) |

- Numeric sentences retained from the body:
- **p. 9 / B. MPC Setting and Results - extractive body cue:** to 5 x 10~ for its best performance, while keeping all other
- **p. 9 / B. MPC Setting and Results - extractive body cue:** Bag ~ Ul Papa =0 GS) For each object, we conduct 20 trials with different random
- **p. 9 / B. MPC Setting and Results - extractive body cue:** final postion eror final heading angle error: /¥arge 60 both calculated using the last 20 steps of a MPC rollout Fg
- **p. 9 / B. MPC Setting and Results - extractive body cue:** For each object, we conduct 20 trials with different random inital and target poses. ‘The results are in Table IV, where we quantify the manipulation ...
- **p. 9 / B. MPC Setting and Results - extractive body cue:** both calculated using the last 20 steps of a MPC rollout.
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Final errors are computed using the last 20 rollout steps in succesful ils,

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length ... | p. 9 (B. MPC Setting and Results) |
| body limitation/failure cue | Fig. 17: An failure case for stick reorientation, | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | The fingertips must coordinate to prevent the object from falling while moving it to the target. | p. 9 (A. Environment and Task Setup) |
| body limitation/failure cue | Fil postion Vial quaeiion MPC soe Succes ust prevent the object from falling while moving it to 8% Shor 8) ere 8) ng time ... | p. 10 (B. MPC Setting and Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Final errors are computed using the last 20 rollout steps in succesful ils, | p. 10 (B. MPC Setting and Results) |
| In contrast, existing models (56, 12, 62, 33] treat the contact, normal and enforce Coulomb's friction separately, which typically leads to additional hyperparameters and ... | p. 2 (A. Rigid Body Multi-contact Models) |
| This implementation creates « closed-loop control effect on the real system, ie., feedback from system state qf to control input 1 (qi | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model) |
| as) Equation (18) shows that the proposed model (16) can be interpreted as a force-spring system, where hiv represents the position displacement in the ... | p. 5 (C. Physical Interpretation of the New Model) |
| both calculated using the last 20 steps of a MPC rollout. | p. 9 (B. MPC Setting and Results) |
| 8 visualizes some random trials of on-ground flip manipulation. | p. 9 (B. MPC Setting and Results) |
| For the proposed method, the exors are computed using sucessful Wal | p. 10 (B. MPC Setting and Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. MPC Setting and Results - extractive body cue:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 17: An failure case for stick reorientation,
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, our ...
- **p. 9 / A. Environment and Task Setup - extractive body cue:** The fingertips must coordinate to prevent the object from falling while moving it to the target.
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Fil postion Vial quaeiion MPC soe Succes ust prevent the object from falling while moving it to 8% Shor 8) ere 8) ng time te ...

- **PDF anchors reviewed:** datasets p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), metrics p. 12 (Figure/Table caption), p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results), p. 13 (Figure/Table caption), baselines p. 10 (B. MPC Setting and Results), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (B. MPC Setting and Results), results p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 12 (Figure/Table caption), p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
