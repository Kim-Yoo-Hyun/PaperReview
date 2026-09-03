# Evaluation - Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1177/0278364914521306; PDF retrieval source: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 22 (6.2.2 Results), p. 22 (6.2.2 Results), p. 27 (6.2.2 Results), p. 27 (6.2.2 Results), p. 28 (Figure/Table caption)): Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop.

## Evaluation Body Digest

- **p. 25 / 6.2.2 Results - extractive body cue:** The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the environment.
- **p. 22 / 6.2.2 Results - extractive body cue:** 11: Simulation B-1: Snapshots of the first movement: the robot uses only its left hand to manipulate the wheel.
- **p. 23 / 6.2.2 Results - extractive body cue:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of ...
- **p. 24 / 6.2.2 Results - extractive body cue:** 15: Simulation B-2: Snapshots of the second movement: the robot uses both hands to manipulate the wheel.
- **p. 25 / 6.2.2 Results - extractive body cue:** Finally, the last task eup is blocking the upper part of the robot (chest, arms and neck).
- **p. 27 / 6.2.2 Results - extractive body cue:** The left hand is moving backward to ensure the robot balance, and is quickly blocked by the task preventing the collision with the wall situated ...
- **p. 21 / 6.2.2 Results - extractive body cue:** The limitation of the COM causes the violation of erh: the robot then stops as close as possible to the ball.
- **p. 22 / 6.2.2 Results - extractive body cue:** The robot has to open a valve by manipulating a wheel.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 6.2.2 Results (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.2.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop. | p. 22 (6.2.2 Results) |
| 6.2.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The motion is composed of two parts: the robot first manipulates the wheel using one hand, then rotates the wheel using both hands with ... | p. 22 (6.2.2 Results) |
| 6.2.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The timing scores are summarized on Table 1. | p. 27 (6.2.2 Results) |
| 6.2.2 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on ... | p. 27 (6.2.2 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Time scores for the three movements, in milliseconds. Secondary score between parenthesis is the average number of iterations after the first one. ... | p. 28 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 25 / 6.2.2 Results - extractive body cue:** The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the environment.
- **p. 22 / 6.2.2 Results - extractive body cue:** 11: Simulation B-1: Snapshots of the first movement: the robot uses only its left hand to manipulate the wheel.
- **p. 23 / 6.2.2 Results - extractive body cue:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of ...
- **p. 24 / 6.2.2 Results - extractive body cue:** 15: Simulation B-2: Snapshots of the second movement: the robot uses both hands to manipulate the wheel.
- **p. 25 / 6.2.2 Results - extractive body cue:** Finally, the last task eup is blocking the upper part of the robot (chest, arms and neck).
- **p. 27 / 6.2.2 Results - extractive body cue:** The left hand is moving backward to ensure the robot balance, and is quickly blocked by the task preventing the collision with the wall situated ...
- **p. 21 / 6.2.2 Results - extractive body cue:** The limitation of the COM causes the violation of erh: the robot then stops as close as possible to the ball.
- **p. 22 / 6.2.2 Results - extractive body cue:** The robot has to open a valve by manipulating a wheel.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Various situations of inequality and equality con- straints. (a) reaching a distant object while keeping bal- ance. The visibility and postural tasks are ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 2: Computation time for the eHQP plotted with re- spect to the number of level p. The problems are ran- domly selected with same ...
- **p. 19 / Figure/Table caption - extractive body cue:** Fig. 3: Number of active-set iterations and computation time for the iHQP resolution using a cascade of QP. Both costs in time and in number ...
- **p. 19 / Figure/Table caption - extractive body cue:** Fig. 3. As described in Section 1.6, the number of cycle in the active-set search increases with the num- ber p of levels when using ...
- **p. 20 / Figure/Table caption - extractive body cue:** Fig. 4: Top row: snapshots of the robot motion. Bottom row: corresponding COM projection in the support polygon (view from underside, the COM position is ...
- **p. 20 / Figure/Table caption - extractive body cue:** Fig. 5: Simulation A: task sequence, listed by priority from bottom to top. The tasks are specifically marked when they become violated. The hierarchy appears ...
- **p. 20 / Figure/Table caption - extractive body cue:** Fig. 6: Simulation A: position of the COM wrt the inner and outer limits. The COM has to remain into the outer limits to ensure ...
- **p. 20 / Figure/Table caption - extractive body cue:** Fig. 7: Simulation A: position of the object projection in the image plane wrt the FOV limits. When the ball is moved outside the FOV, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the environment. | embodiment, simulator version and control stack | p. 25 (6.2.2 Results), p. 22 (6.2.2 Results) |
| Task/environment | 11: Simulation B-1: Snapshots of the first movement: the robot uses only its left hand to manipulate the wheel. | reset, timeout, object/scene variation | p. 22 (6.2.2 Results), p. 23 (6.2.2 Results) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 4 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 24 and illustrate very well the hierarchical order: the task erh has priority over the three other ones, and is always accomplished: the error ... | definition/direction/unit from same section | p. 27 (6.2.2 Results) |
| 24: Experiment C: Norm of the task errors. | definition/direction/unit from same section | p. 26 (6.2.2 Results) |
| 0 1 2 3 4 5 6 7 8 9 10 0 0.2 0.4 0.6 0.8 1 Time (s) Task error norm (m and ... | definition/direction/unit from same section | p. 26 (6.2.2 Results) |
| The timing scores are summarized on Table 1. | definition/direction/unit from same section | p. 27 (6.2.2 Results) |
| The arm comes close to collision when the robot approaches the wheel: the constraints are saturated to prevent it. | definition/direction/unit from same section | p. 23 (6.2.2 Results) |
| Table 1: Time scores for the three movements, in milliseconds. Secondary score between parenthesis is the average number of iterations after the first one. ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow and shoulder to the left obstacle. | definition/direction/unit from same section | p. 22 (6.2.2 Results) |
| As expected, the number of iterations is even lower using a proper warm start: in that case, the active search only iterates when a ... | definition/direction/unit from same section | p. 22 (6.2.2 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP ... | comparison identity and matched condition | p. 21 (6.2.2 Results) |
| In the beginning of each motion sequence (when the ball is just moved), the visibility constraint (67) might be violated without the FOV task ... | comparison identity and matched condition | p. 21 (6.2.2 Results) |
| The comparison of the computation times for both movements is given in Fig. | comparison identity and matched condition | p. 22 (6.2.2 Results) |
| 6.3 Simulation B: opening a valve The previous movement cannot be generated using the method presented in [De Lasa et al., 2010] since inequality ... | comparison identity and matched condition | p. 22 (6.2.2 Results) |
| Using a warm start of the HQP, the active search loop converges without any update in 97.5% of the 23 | comparison identity and matched condition | p. 23 (6.2.2 Results) |
| In exchange, the number of control cycles without update decreases to 96.6%. | comparison identity and matched condition | p. 25 (6.2.2 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP ... | component/input/data sensitivity | p. 21 (6.2.2 Results) |
| In the beginning of each motion sequence (when the ball is just moved), the visibility constraint (67) might be violated without the FOV task ... | component/input/data sensitivity | p. 21 (6.2.2 Results) |
| 6.3 Simulation B: opening a valve The previous movement cannot be generated using the method presented in [De Lasa et al., 2010] since inequality ... | component/input/data sensitivity | p. 22 (6.2.2 Results) |
| The maximal number of iterations is 6 (at the first iteration after the change of the ball position at T=7), the mean number is ... | component/input/data sensitivity | p. 22 (6.2.2 Results) |
| Using a warm start of the HQP, the active search loop converges without any update in 97.5% of the 23 | component/input/data sensitivity | p. 23 (6.2.2 Results) |
| The grasping task is finally removed when the last position is reached. | component/input/data sensitivity | p. 25 (6.2.2 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose an original decomposition that encompasses the hierarchy among the constraints. | Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop. | PDF body cue; verify exact table/figure and matched conditions | p. 22 (6.2.2 Results), p. 22 (6.2.2 Results), p. 27 (6.2.2 Results), p. 27 (6.2.2 Results), p. 28 (Figure/Table caption) |
| Primary metric/result | The motion is composed of two parts: the robot first manipulates the wheel using one hand, then rotates the wheel using both hands with ... | numeric claim only at cited anchor | p. 22 (6.2.2 Results) |

- Numeric sentences retained from the body:
- **p. 21 / 6.2.2 Results - extractive body cue:** At time T = 4s, the COM is at the centralband limit when several joints reach their limits (see Fig.
- **p. 21 / 6.2.2 Results - extractive body cue:** Similarly, at T = 9s, the COM is on the border of the band.
- **p. 21 / 6.2.2 Results - extractive body cue:** At T = 9.5s, some DOF of the grasp task erh collapse because of a kinematic singularity.
- **p. 21 / 6.2.2 Results - extractive body cue:** 0 1 2 3 4 5 6 7 8 9 10 0.5 1 1.5 2 2.5 3 x 10 -3 Time (s) Computation time (s) ...
- **p. 22 / 6.2.2 Results - extractive body cue:** Using the HQP and the warm start, an average of 0.56ms of computation is needed.
- **p. 22 / 6.2.2 Results - extractive body cue:** The second movement (both-arm (t=5.0s) (t=5.5s) (t=6.3s) Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De ... | p. 19 (3.6 Conclusion) |
| body limitation/failure cue | Adaptating the method for iHQP is done through the following changes: • using our eHQP solver instead of the eQP, obviously, to find the ... | p. 12 (2.6 Conclusion) |
| body limitation/failure cue | As observed in [Kanoun et al., 2011], strongly active constraints cannot be deactivated at a next level. | p. 13 (2.6 Conclusion) |
| body limitation/failure cue | However, one cannot guarantee the number of necessary iterations to reach the optimum. | p. 16 (3.6 Conclusion) |
| body limitation/failure cue | However, we cannot yet guarantee that the solver answers in a bounded number of iterations. | p. 16 (3.6 Conclusion) |
| body limitation/failure cue | The collision avoidance is enforced by the task ecoll by imposing the distance between a body of the robot and an object to be ... | p. 17 (3.6 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on ... | p. 27 (6.2.2 Results) |
| We compute a solution five time faster than [Kanoun et al., 2011] in any case and two to three time faster on the examples ... | p. 27 (6.2.2 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / 3.6 Conclusion - extractive body cue:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa ...
- **p. 12 / 2.6 Conclusion - extractive body cue:** Adaptating the method for iHQP is done through the following changes: • using our eHQP solver instead of the eQP, obviously, to find the hierarchical ...
- **p. 13 / 2.6 Conclusion - extractive body cue:** As observed in [Kanoun et al., 2011], strongly active constraints cannot be deactivated at a next level.
- **p. 16 / 3.6 Conclusion - extractive body cue:** However, one cannot guarantee the number of necessary iterations to reach the optimum.
- **p. 16 / 3.6 Conclusion - extractive body cue:** However, we cannot yet guarantee that the solver answers in a bounded number of iterations.
- **p. 17 / 3.6 Conclusion - extractive body cue:** The collision avoidance is enforced by the task ecoll by imposing the distance between a body of the robot and an object to be positive.

- **Evidence anchors reviewed:** datasets p. 25 (6.2.2 Results), p. 22 (6.2.2 Results), p. 23 (6.2.2 Results), p. 24 (6.2.2 Results), p. 25 (6.2.2 Results), p. 27 (6.2.2 Results), metrics p. 27 (6.2.2 Results), p. 26 (6.2.2 Results), p. 26 (6.2.2 Results), p. 27 (6.2.2 Results), p. 23 (6.2.2 Results), p. 28 (Figure/Table caption), baselines p. 21 (6.2.2 Results), p. 21 (6.2.2 Results), p. 22 (6.2.2 Results), p. 22 (6.2.2 Results), p. 23 (6.2.2 Results), p. 25 (6.2.2 Results), results p. 22 (6.2.2 Results), p. 22 (6.2.2 Results), p. 27 (6.2.2 Results), p. 27 (6.2.2 Results), p. 28 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (32 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on a similar computer. (p. 27, 6.2.2 Results).
- **Metric evidence:** The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow and shoulder to the left obstacle. (p. 22, 6.2.2 Results).
- **Baseline/ablation evidence:** 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start. (p. 21, 6.2.2 Results).
- **Failure/negative evidence:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. (p. 23, 6.2.2 Results).
