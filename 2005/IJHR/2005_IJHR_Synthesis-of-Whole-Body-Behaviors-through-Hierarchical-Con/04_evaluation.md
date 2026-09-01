# Evaluation - Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~lsentis/files/publications.html; PDF retrieval source: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2005_IJHR.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4.3. Movement feasibility), p. 12 (X Direction), p. 13 (6. Summary and discussion)): But first, to evaluate the performance and determine the optimal ordering we examine a scenario where the center of gravity control shares control priority with the hand position control,

## Evaluation Body Digest

- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 4. Multi-level hierarchy - extractive PDF cue:** A humanoid robot must accomplish a collection of operational tasks while satisfying several constraints acting on the robot's body.
- **p. 6 / 4. Multi-level hierarchy - extractive PDF cue:** Let us suppose there are N behavioral primitives (constraints, operational tasks, and postures) controlling the robot's behavior at a given time.
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** (16) The dynamic behavior in task space can be obtained by projecting the robot's joint dynamics into the associated task space, i.e.
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** The following torque equation embodies a multi-level control hierarchy integrating both constraints and tasks into a single torque control reference: Γ =Γconstraints + N T ...
- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** In the case that an active task becomes ill-conditioned we say that the robot's movement is infeasible.
- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** This complex behavior is complemented with additional tasks to control the robot's center of gravity and to maintain a body symmetry posture.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Movement feasibility | SYSTEM / EVALUATION SCOPE UNRESOLVED | But first, to evaluate the performance and determine the optimal ordering we examine a scenario where the center of gravity control shares control priority ... | p. 10 (4.3. Movement feasibility) |
| X Direction | SYSTEM / EVALUATION SCOPE UNRESOLVED | The results of this control are shown in Figure 4. | p. 12 (X Direction) |
| 6. Summary and discussion | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our major contribution is in presenting a novel and unified framework that is based on robust theoretical results. | p. 13 (6. Summary and discussion) |

## Dataset / Benchmark Role

- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 4. Multi-level hierarchy - extractive PDF cue:** A humanoid robot must accomplish a collection of operational tasks while satisfying several constraints acting on the robot's body.
- **p. 6 / 4. Multi-level hierarchy - extractive PDF cue:** Let us suppose there are N behavioral primitives (constraints, operational tasks, and postures) controlling the robot's behavior at a given time.
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** (16) The dynamic behavior in task space can be obtained by projecting the robot's joint dynamics into the associated task space, i.e.
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** The following torque equation embodies a multi-level control hierarchy integrating both constraints and tasks into a single torque control reference: Γ =Γconstraints + N T ...
- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** In the case that an active task becomes ill-conditioned we say that the robot's movement is infeasible.
- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** This complex behavior is complemented with additional tasks to control the robot's center of gravity and to maintain a body symmetry posture.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 1. Task and posture decomposition: In this sequence, we control the robot's hands to grab a box while maintaining body self-balance (based on the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2. Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 3. Hand position control under joint limit constraints: In this sequence, the robot is commanded to reach a target position with its right hand ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 4. Data recorded when the center of gravity and the hand position tasks share priority: When the knees flexion and right elbow joint-limits are ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 5. Data recorded when the center of gravity task precedes the hand position task: The center of gravity error stays small (a) when the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near ... | embodiment, simulator version and control stack | p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints) |
| Task/environment | Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, ... | reset, timeout, object/scene variation | p. 5 (3. Integration of constraints), p. 6 (4. Multi-level hierarchy) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 5 (3. Integration of constraints), p. 8 (4.3. Movement feasibility) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 11 0 1 2 3 -2 0 2 time [s] error [cm] Balancing Error | definition/direction/unit from same section | p. 11 (4.3. Movement feasibility) |
| While in motion, the error in the center of gravity horizontal position is initially zero while the hand moves down at steady speed. | definition/direction/unit from same section | p. 12 (X Direction) |
| Data recorded when the center of gravity task precedes the hand position task: The center of gravity error stays small (a) when the knee ... | definition/direction/unit from same section | p. 12 (X Direction) |
| As a result, an error appears in both tasks according to their control gains. | definition/direction/unit from same section | p. 13 (X Direction) |
| The steady-state errors for the center of gravity task are 1 cm in the X direction and 3 cm in the Y direction, while ... | definition/direction/unit from same section | p. 13 (X Direction) |
| Fig. 2. Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Therefore, in the case of a motion conflict, the task would be unable to operate within this projection. | definition/direction/unit from same section | p. 6 (3. Integration of constraints) |
| We create this hierarchy to integrate constraints and organize additional tasks according to desired priorities, while optimizing the execution of the global task. | definition/direction/unit from same section | p. 6 (4. Multi-level hierarchy) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We can then modify the task trajectory or remove its control while the control of other higher priority tasks such as balancing or control ... | component/input/data sensitivity | p. 9 (4.3. Movement feasibility) |
| Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, ... | component/input/data sensitivity | p. 5 (3. Integration of constraints) |
| This projection ensures that the operational task does not introduce acceleration components into the constrained directions. | component/input/data sensitivity | p. 6 (3. Integration of constraints) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the ... | But first, to evaluate the performance and determine the optimal ordering we examine a scenario where the center of gravity control shares control priority ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4.3. Movement feasibility), p. 12 (X Direction), p. 13 (6. Summary and discussion) |
| Primary metric/result | The results of this control are shown in Figure 4. | numeric claim only at cited anchor | p. 12 (X Direction) |

- Numeric sentences retained from the body:
- **p. 8 / 4.1. Recursive null-spaces - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 8 This mathematical constraint leads to the following unique solution Nprec(k) = I - k-1 X i=1 Ji/prec(i)Ji/prec(i), ...
- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** For this simulated experiment, we use a humanoid robot model consisting of 24 degrees of freedom: 2×6 for the legs, 2×4 for the arms, 2 ...
- **p. 12 / X Direction - extractive PDF cue:** When the hip, elbow, and knee flexion joint limits are reached at t = 0.9 s, 1 s, and 1.2 s respectively, the center of ...
- **p. 4 / 3. Integration of constraints - extractive PDF cue:** The control of robots under constraints has been investigated since the mid 1970s.
- **p. 8 / 4.1. Recursive null-spaces - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 8 This mathematical constraint leads to the following unique solution Nprec(k) = I - k-1 X i=1 Ji/prec(i)Ji/prec(i), ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our research has addressed a wide set of constraints, such as joint-limits, collision avoidance, and self-collision avoidance, based on reactive techniques at the whole-body ... | p. 13 (6. Summary and discussion) |
| body limitation/failure cue | Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near ... | p. 5 (3. Integration of constraints) |
| body limitation/failure cue | However, the center of gravity horizontal position cannot be maintained (a), because its control is directly affected by the hand control. i.e. Γ = ... | p. 11 (X Direction) |
| body limitation/failure cue | Because the hierarchy assigns higher priority to the center of gravity task, it maintains its desired goal position (above the robot's feet) at all ... | p. 12 (X Direction) |
| body limitation/failure cue | December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 13 conflict in their control (cannot be simultaneously accomplished). | p. 13 (X Direction) |
| body limitation/failure cue | This projection ensures that the operational task does not introduce acceleration components into the constrained directions. | p. 6 (3. Integration of constraints) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| While today the interactive control of humanoids is limited to the online selection of a few preplanned motions, with this new controller, we construct ... | p. 13 (6. Summary and discussion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 6. Summary and discussion - extractive PDF cue:** Our research has addressed a wide set of constraints, such as joint-limits, collision avoidance, and self-collision avoidance, based on reactive techniques at the whole-body level.
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the ...
- **p. 11 / X Direction - extractive PDF cue:** However, the center of gravity horizontal position cannot be maintained (a), because its control is directly affected by the hand control. i.e. Γ = ΓJLC ...
- **p. 12 / X Direction - extractive PDF cue:** Because the hierarchy assigns higher priority to the center of gravity task, it maintains its desired goal position (above the robot's feet) at all times, ...
- **p. 13 / X Direction - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 13 conflict in their control (cannot be simultaneously accomplished).
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** This projection ensures that the operational task does not introduce acceleration components into the constrained directions.

- **PDF anchors reviewed:** datasets p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints), p. 6 (4. Multi-level hierarchy), p. 6 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), metrics p. 11 (4.3. Movement feasibility), p. 12 (X Direction), p. 12 (X Direction), p. 13 (X Direction), p. 13 (X Direction), p. 5 (Figure/Table caption), baselines 본문 anchor 없음, results p. 10 (4.3. Movement feasibility), p. 12 (X Direction), p. 13 (6. Summary and discussion).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
