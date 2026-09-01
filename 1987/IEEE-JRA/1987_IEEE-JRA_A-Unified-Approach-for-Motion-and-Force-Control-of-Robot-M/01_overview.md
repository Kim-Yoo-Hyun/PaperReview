# A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://cs.stanford.edu/group/manips/publications.html.
> PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 1987 / IEEE JRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, operational space control, force control, manipulation
- Official paper: https://cs.stanford.edu/group/manips/publications.html
- Full-text retrieval: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.를 문제로 두고, These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 1 / Abstract - extractive body cue:** Fist, issues related to the description of end-effector tasks that involve constrained motion and active force contro are discussed. ‘The fundamentals of the operational space ...
- **p. 1 / Abstract - extractive body cue:** The extension of this formulation to redundant manipulator systems is also presented, constructing the end-effector equations of ‘motion and describing their behavior with respect to ...
- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** configuration, the manipulator is treated as ame ‘redundant with respect tothe motion ofthe end-effector in the subspace ‘of operational space orthogonal to the singular direction.
- **p. 1 / I. Inrropucrion - extractive body cue:** The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.
- **p. 1 / I. Inrropucrion - extractive body cue:** Obviously, these characteristics cannot be found in the manipulator joint space dynamic model, which only provides a description of the interaction between joint motions.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism ...
- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of the end-effector.
- **p. 3 / I. Inrropucrion - extractive body cue:** However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model describing ...
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** ‘The Jacobian matrix J(q) associated with a given representation of the end-effector orientation x, can then be expressed in the form [13]

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector. | joint/task state, reference와 sensor feedback | p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion) |
| State/latent | However, task, specification, motion, contact, forces, dynamics, force, sensing, feedback, closely, linked | state estimate, task-space error와 control decision | p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion) |
| Output/action | The description of the dynamic interaction between end-effector motions and the effects of these motions on the end-effector's behavior in the direction of force control are basic requirements for the analysis and ... | torque, force, velocity 또는 position command | p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 5 (IV. Exp-Errecror Morton Controt) |
| Objective/outcome | The number of degrees of freedom of the constrained end-effector is given by the difference between mo and the number of independent ‘equations specifying the geometric constraints, assumed to be holonomic. | tracking, stability, constraint satisfaction과 contact behavior | p. 2 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.
- **p. 3 / I. Inrropucrion - extractive body cue:** The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces acting ...
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** By isolating these coefficients, end-effector dynamic decoupling and control can be achieved in a two-level control system architecture [15].
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** For end-effector motions specified in terms of Cartesian coordinates and instantaneous angular rotations, the dynamic decoupling and motion control of the end-effector can be achieved ...
- **p. 8 / VII. Contnot. oF REDUNDANT MANIPULATORS - extractive body cue:** Asymptotic stabilization of the system can be achieved by the addition of dissipative joint forces [13].
- **p. 8 / VII. Contnot. oF REDUNDANT MANIPULATORS - extractive body cue:** As in the case of nonredundant manipulators, the dynamic decoupling and control of the end-effector can be achieved by selecting an operational command vector of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt) |
| Embodiment/environment | 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL. | hardware/simulator version and reset protocol | p. 4 (X 1 column matrix x of independent configuration parame), p. 5 (X 1 column matrix x of independent configuration parame) |
| Dataset/benchmark | For control systems implemented for tasks specified with respect to the end-effector coordinate frame, these matrices will be specified with respect to that, coordinate frame as well. | role, split, size and leakage | p. 4 (X 1 column matrix x of independent configuration parame), p. 5 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion), p. 3 (I. Inrropucrion) |
| Metric | In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks. | definition, denominator, direction and uncertainty | p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (V. Constnainep Motion Operarions), p. 6 (V. Constnainep Motion Operarions) |
| Baseline/ablation | These forces can be selected to actin the null space of the Jacobian matrix [16] This precludes any effect of the additional forces on the endeffector and maintains its dynamic decoupling. | fair input/data/compute/action matching | p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 5 (X 1 column matrix x of independent configuration parame), p. 3 (X 1 column matrix x of independent configuration parame) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the endeffector position and orientation.
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘manipulator, and the dynamic behavior of the entire redundant system cannot be represented by a dynamic model in coordinates only of the end-effector configuration.
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** Within this framework of control and at the level ‘f the uncoupled system linear, nonlinear, robust [32], and adaptive [3] control structures can be implemented.

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.를 문제로 두고, These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
