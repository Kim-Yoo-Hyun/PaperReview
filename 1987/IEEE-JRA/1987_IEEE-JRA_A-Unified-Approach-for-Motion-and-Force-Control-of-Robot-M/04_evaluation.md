# Evaluation - A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://cs.stanford.edu/group/manips/publications.html; PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 6 (V. Constnainep Motion Operarions), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 9 (VI. Sixcutar Coxmiourarions)): The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces acting on it.

## Evaluation Body Digest

- **p. 4 / X 1 column matrix x of independent configuration parame - extractive body cue:** 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL.
- **p. 5 / X 1 column matrix x of independent configuration parame - extractive body cue:** KHATIB: MOTION AND FORCE CONTROL OF ROBOT MANIPULATORS
- **p. 3 / I. Inrropucrion - extractive body cue:** For control systems implemented for tasks specified with respect to the end-effector coordinate frame, these matrices will be specified with respect to that, coordinate frame ...
- **p. 3 / I. Inrropucrion - extractive body cue:** ‘and fact on vectors described in the reference frame Oly ‘A position command vector, for instance, intially expressed in Go is transformed by the rotation ...
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** For tasks where the desired motion of the end-effector is specified, a linear dynamic behavior can be obtained by selecting
- **p. 9 / IX. Susmary ano Discussion - extractive body cue:** The use of the generalized task specification matrix has provided a more
- **p. 9 / IX. Susmary ano Discussion - extractive body cue:** ‘A methodology for the description of end-effector constrained motion tasks based on the construction of generalized task specification matrices has been proposed.
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| I. Inrropucrion | SYSTEM / EVALUATION SCOPE UNRESOLVED | The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces ... | p. 3 (I. Inrropucrion) |
| IV. Exp-Errecror Morton Controt | SYSTEM / EVALUATION SCOPE UNRESOLVED | By isolating these coefficients, end-effector dynamic decoupling and control can be achieved in a two-level control system architecture [15]. | p. 6 (IV. Exp-Errecror Morton Controt) |
| V. Constnainep Motion Operarions | SYSTEM / EVALUATION SCOPE UNRESOLVED | For end-effector motions specified in terms of Cartesian coordinates and instantaneous angular rotations, the dynamic decoupling and motion control of the end-effector can be ... | p. 6 (V. Constnainep Motion Operarions) |
| VII. Contnot. oF REDUNDANT MANIPULATORS | SYSTEM / EVALUATION SCOPE UNRESOLVED | Asymptotic stabilization of the system can be achieved by the addition of dissipative joint forces [13]. | p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS) |
| VII. Contnot. oF REDUNDANT MANIPULATORS | SYSTEM / EVALUATION SCOPE UNRESOLVED | As in the case of nonredundant manipulators, the dynamic decoupling and control of the end-effector can be achieved by selecting an operational command vector ... | p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS) |

## Dataset / Benchmark Role

- **p. 4 / X 1 column matrix x of independent configuration parame - extractive body cue:** 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL.
- **p. 5 / X 1 column matrix x of independent configuration parame - extractive body cue:** KHATIB: MOTION AND FORCE CONTROL OF ROBOT MANIPULATORS
- **p. 3 / I. Inrropucrion - extractive body cue:** For control systems implemented for tasks specified with respect to the end-effector coordinate frame, these matrices will be specified with respect to that, coordinate frame ...
- **p. 3 / I. Inrropucrion - extractive body cue:** ‘and fact on vectors described in the reference frame Oly ‘A position command vector, for instance, intially expressed in Go is transformed by the rotation ...
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** For tasks where the desired motion of the end-effector is specified, a linear dynamic behavior can be obtained by selecting
- **p. 9 / IX. Susmary ano Discussion - extractive body cue:** The use of the generalized task specification matrix has provided a more
- **p. 9 / IX. Susmary ano Discussion - extractive body cue:** ‘A methodology for the description of end-effector constrained motion tasks based on the construction of generalized task specification matrices has been proposed.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. One-degree-of freedom moti,

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL. | embodiment, simulator version and control stack | p. 4 (X 1 column matrix x of independent configuration parame), p. 5 (X 1 column matrix x of independent configuration parame) |
| Task/environment | KHATIB: MOTION AND FORCE CONTROL OF ROBOT MANIPULATORS | reset, timeout, object/scene variation | p. 5 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 2 (I. Inrropucrion), p. 5 (IV. Exp-Errecror Morton Controt) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. | definition/direction/unit from same section | p. 5 (IV. Exp-Errecror Morton Controt) |
| 3, where ky represents the force error gain and k,y denotes the velocity gain in Fz An effective strategy for the control of the ... | definition/direction/unit from same section | p. 7 (V. Constnainep Motion Operarions) |
| Instantaneous angular rotations have been used for the description of orientation error of the end-effector. | definition/direction/unit from same section | p. 6 (V. Constnainep Motion Operarions) |
| An angular rotation error vector 56 that corresponds to the error between the actual orientation of the end-effector and its desired orientation can be ... | definition/direction/unit from same section | p. 6 (V. Constnainep Motion Operarions) |
| A position error term on s(q) is used in the control vector for tasks that involve a motion toward goal positions located at oF ... | definition/direction/unit from same section | p. 9 (VI. Sixcutar Coxmiourarions) |
| However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model ... | definition/direction/unit from same section | p. 3 (I. Inrropucrion) |
| This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15] | definition/direction/unit from same section | p. 5 (IV. Exp-Errecror Morton Controt) |
| Force rate feedback has also been used in F. ‘A more detailed description of the components involved in this control system, real-time implementation issues, ... | definition/direction/unit from same section | p. 7 (V. Constnainep Motion Operarions) |

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
| These forces can be selected to actin the null space of the Jacobian matrix [16] This precludes any effect of the additional forces on ... | component/input/data sensitivity | p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS) |
| In the foregoing relations, the components involved in the endeffector equations of motion (14), i.e., A, 4, p, are expressed in terms of joint ... | component/input/data sensitivity | p. 5 (X 1 column matrix x of independent configuration parame) |
| In the reference frame (o, the system of my equations expressing the components of x as functions of joint coordinates, i.e., the geometric model, ... | component/input/data sensitivity | p. 3 (X 1 column matrix x of independent configuration parame) |
| Using the expression of A(x) in (18), the components of u(x, 48) in (19) can be written as, | component/input/data sensitivity | p. 4 (X 1 column matrix x of independent configuration parame) |
| ‘The components of the my X Mig matrices T(r) are the Christoffel symbols x, given as a function of the partial derivatives of A(x) ... | component/input/data sensitivity | p. 4 (X 1 column matrix x of independent configuration parame) |
| where Ag(q) and 6,(g, 4) are defined similarly to A(q) and (q, 4) with J(g) being replaced by Jo(q). | component/input/data sensitivity | p. 6 (V. Constnainep Motion Operarions) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn | The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 6 (V. Constnainep Motion Operarions), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 9 (VI. Sixcutar Coxmiourarions) |
| Primary metric/result | By isolating these coefficients, end-effector dynamic decoupling and control can be achieved in a two-level control system architecture [15]. | numeric claim only at cited anchor | p. 6 (IV. Exp-Errecror Morton Controt) |

- Numeric sentences retained from the body:
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** [94] and [4°] are the symbolic notations for the n(n - 1)/2 x Tand.m x 1 column matrices
- **p. 2 / I. Inrropucrion - extractive body cue:** where J designates the 3 x 3 identity matrix.
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** [94] and [4°] are the symbolic notations for the n(n - 1)/2 x Tand.m x 1 column matrices

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15] | p. 5 (IV. Exp-Errecror Morton Controt) |
| body limitation/failure cue | ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the endeffector position and orientation. | p. 7 (VI. ReDunpaNT MANIPULATORS) |
| body limitation/failure cue | ‘manipulator, and the dynamic behavior of the entire redundant system cannot be represented by a dynamic model in coordinates only of the end-effector configuration. | p. 7 (VI. ReDunpaNT MANIPULATORS) |
| body limitation/failure cue | Within this framework of control and at the level ‘f the uncoupled system linear, nonlinear, robust [32], and adaptive [3] control structures can be ... | p. 5 (IV. Exp-Errecror Morton Controt) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| "The authors withthe Artificial Intelligence Laboratory, Computer Science Department, Cedar Hall, Stanford Universiy, Stanford, CA 94305, | p. 1 (I. Inrropucrion) |
| This allows a more efficient implementation of the control system for real-time operations. | p. 3 (I. Inrropucrion) |
| Force rate feedback has also been used in F. ‘A more detailed description of the components involved in this control system, real-time implementation issues, ... | p. 7 (V. Constnainep Motion Operarions) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the endeffector position and orientation.
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘manipulator, and the dynamic behavior of the entire redundant system cannot be represented by a dynamic model in coordinates only of the end-effector configuration.
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** Within this framework of control and at the level ‘f the uncoupled system linear, nonlinear, robust [32], and adaptive [3] control structures can be implemented.

- **Evidence anchors reviewed:** datasets p. 4 (X 1 column matrix x of independent configuration parame), p. 5 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion), p. 3 (I. Inrropucrion), p. 5 (IV. Exp-Errecror Morton Controt), p. 9 (IX. Susmary ano Discussion), metrics p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (V. Constnainep Motion Operarions), p. 6 (V. Constnainep Motion Operarions), p. 6 (V. Constnainep Motion Operarions), p. 9 (VI. Sixcutar Coxmiourarions), p. 3 (I. Inrropucrion), baselines 본문 anchor 없음, results p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 6 (V. Constnainep Motion Operarions), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 9 (VI. Sixcutar Coxmiourarions).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt).
- **Metric evidence:** In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. (p. 5, IV. Exp-Errecror Morton Controt).
- **Baseline/ablation evidence:** In the reference frame (o, the system of my equations expressing the components of x as functions of joint coordinates, i.e., the geometric model, is given by (p. 3, X 1 column matrix x of independent configuration parame).
- **Failure/negative evidence:** This performance has been obtained despite the limitations in controlling the manipulator joint torques [27]. ‘Accurate identification of the PUMA. (p. 10, IX. Susmary ano Discussion).
