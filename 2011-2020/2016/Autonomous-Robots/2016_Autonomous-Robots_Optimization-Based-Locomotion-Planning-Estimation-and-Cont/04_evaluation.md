# Evaluation - Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/; PDF retrieval source: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 7, 11. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation)): To characterize the state estimator we evaluate its performance in a variety of experiments.

## Evaluation Body Digest

- **p. 19 / 6 Experiments - extractive body cue:** We describe several experiments performed on the robot and in simulation.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** Because the robot's BDI estimator requires information from their walking controller, we were unable to use our walking controller in these tests.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** Orientation estimation performance is comparable between different estimators.Notethattheprecisionofthegroundtruthorientation determined using VICON measurements is on the order of 1◦, so we were unable to differentiate yaw ...
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** This drift rate generally increases when the walking dynamically or on non-flat terrain.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** To characterize the state estimator we evaluate its performance in a variety of experiments.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 6 Experiments (p. 19); 6.1 State estimation evaluation (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.1 State estimation evaluation | EMPIRICAL / SIMULATION | To characterize the state estimator we evaluate its performance in a variety of experiments. | p. 19 (6.1 State estimation evaluation) |
| 6.1 State estimation evaluation | EMPIRICAL / SIMULATION | In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions. | p. 19 (6.1 State estimation evaluation) |

## Dataset / Benchmark Role

- **p. 19 / 6 Experiments - extractive body cue:** We describe several experiments performed on the robot and in simulation.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** Because the robot's BDI estimator requires information from their walking controller, we were unable to use our walking controller in these tests.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We describe several experiments performed on the robot and in simulation. | embodiment, simulator version and control stack | p. 19 (6 Experiments), p. 19 (6.1 State estimation evaluation) |
| Task/environment | Because the robot's BDI estimator requires information from their walking controller, we were unable to use our walking controller in these tests. | reset, timeout, object/scene variation | p. 19 (6.1 State estimation evaluation) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 14 (5.1 Requirements and approach), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Orientation estimation performance is comparable between different estimators.Notethattheprecisionofthegroundtruthorientation determined using VICON measurements is on the order of 1◦, so we were unable to differentiate ... | definition/direction/unit from same section | p. 19 (6.1 State estimation evaluation) |
| This drift rate generally increases when the walking dynamically or on non-flat terrain. | definition/direction/unit from same section | p. 19 (6.1 State estimation evaluation) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe ... | To characterize the state estimator we evaluate its performance in a variety of experiments. | PDF body cue; verify exact table/figure and matched conditions | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |
| Primary metric/result | In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions. | numeric claim only at cited anchor | p. 19 (6.1 State estimation evaluation) |

- Numeric sentences retained from the body:
- **PDF p. 7, §3.1 footstep constraints (DOC-QA2 원문 대조):** Safe terrain region 선택 Y_r,j는 A_r p_j≤b_r를 함의한다. Piecewise-linear sin/cos, approximate reachability 및 extra-step constraints를 결합하는 footstep planning formulation이다. Publisher header와 깨진 implication glyph를 제거했다.
- **p. 7 / 3.1.3 Determining the number of footsteps - extractive body cue:** For a footstep plan of N = 12 steps, in which each step must be assigned to one of R = 10 safe regions, L ...
- **p. 10 / 4.2 COM and COP stabilization - extractive body cue:** If we assume that the centroidal angular momentum of the robot, ˙k = 0, k = 0, and the normal moment, τ n = 0, ...
- **PDF p. 11, §4.2 Eq. (23) (DOC-QA2 원문 대조):** COM/COP stabilization은 fixed COM height의 linear dynamics와 output relation 하에서 COP tracking error 및 control의 quadratic integral cost를 최소화한다. 이는 controller objective이며 trial success나 empirical error metric 자체가 아니다.
- **p. 13 / 4.5 Efficient QP solver - extractive body cue:** SolvingtheQPforAtlasduringtypicalwalkingtakesapproximately 0.2ms (1ms including QP setup time) (Kuindersma et al.
- **p. 13 / 4.5 Efficient QP solver - extractive body cue:** Including all additional controller software components, such as those that evaluate the footstep trajectories, determine whether a body is in contact, handle messages to and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The robot's trailing foot eventually collided with the front of the step resulting in a fall. | p. 20 (6.3 Closed-loop walking with LIDAR feedback) |
| body limitation/failure cue | This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall. | p. 20 (6.3 Closed-loop walking with LIDAR feedback) |
| body limitation/failure cue | 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the robot's head cameras to be no ... | p. 22 (6.4.1 Running) |
| body limitation/failure cue | In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions. | p. 19 (6.1 State estimation evaluation) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 9 the value of fusing LIDAR-based corrections becomes evident after just a few steps. | p. 19 (6.1 State estimation evaluation) |
| Code for our planning and control algorithms, along with a variety of simulation examples, is available for download in the Drake (2014a) toolbox. | p. 19 (6 Experiments) |
| Implementation on hardware demands that sufficiently high control rates be achieved. | p. 13 (4.5 Efficient QP solver) |
| We first analyze the environment and compute a set of convex regions where contacts are allowed. | p. 3 (3 Motion planning) |
| We retain some elements from both categories, performing a simultaneous optimization of the discrete assignment of footsteps to convex regions and the continuous position ... | p. 3 (3.1 Footstep planning as a mixed-integer convex) |
| We use binary variables of this form to indicate the assignment of footsteps to regions. | p. 4 (3.1 Footstep planning as a mixed-integer convex) |
| We create a matrix Y ∈{0, 1}R×N to represent the assignment of footsteps to safe regions. | p. 4 (3.1 Footstep planning as a mixed-integer convex) |
| That seed point forms the center of a very small obstacle-free ellipsoid. | p. 5 (3.1.1 Convex decomposition) |

## Limitations and Verification Questions

- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall.
- **p. 22 / 6.4.1 Running - extractive body cue:** 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the robot's head cameras to be no more ...
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions.

- **Evidence anchors reviewed:** datasets p. 19 (6 Experiments), p. 19 (6.1 State estimation evaluation), metrics p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation), baselines 본문 anchor 없음, results p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation).

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)
