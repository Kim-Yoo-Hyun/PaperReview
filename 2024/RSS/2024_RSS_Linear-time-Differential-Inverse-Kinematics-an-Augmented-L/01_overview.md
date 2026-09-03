# Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, inverse kinematics, whole-body control, augmented Lagrangian, ADMM, real-time
- Official paper: https://www.roboticsproceedings.org/rss20/p110.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p110.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack variables.를 문제로 두고, 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Differential inverse kinematics is a core robotics problem whose state-of-the-art solutions are currently based on quadratic programming.
- **p. 1 / Abstract - extractive body cue:** In this paper, we revisit it from the perspective of augmented Lagrangian methods (AL) and the related alternating direction method of multipliers (ADMM).
- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 1 / Abstract - extractive body cue:** Combined with the ADMM strategy popularized by OSQP, we handle the same class of problems as QP-based differential IK, but scaling linearly with problem dimensions ...
- **p. 1 / Abstract - extractive body cue:** We implement our approach as C++ opensource software and evaluate it on a benchmark of robotic-arm and humanoid-locomotion tasks.
- **p. 2 / II. BACKGROUND - extractive body cue:** The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack ...
- **p. 2 / II. BACKGROUND - extractive body cue:** However, one major distinction between the current state-of-the-arts and our proposed solution is that our solver is able to efficiently exploit the specific sparsity patterns ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.
- **p. 2 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Constrained inverse kinematics ADMM formulation In the most general sense, first order constrained differential inverse kinematics can be formulated as a constrained QP problem: min ...
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** But more importantly, this mixed-coordinate formulation allows one to fully exploit the sparsity pattern induced by the robot's kinematic tree.
- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Algorithm 1 Constrained IK algorithm LOIK Require: robot model, q, vinit i s, νinit, Href i s, vref i s, Ais, bis, νlb, νub, ρv, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (14) indicates that νi is in the form of the state-feedback "control" hypothesis proposed in (9), when viewing problem (8) from the LQR perspective. | proprioception, reference pose/motion, visual or language command | p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| State/latent | indicates, form, state-feedback, control, hypothesis, when, viewing, problem, LQR, perspective, will, verified | whole-body pose, balance/contact state와 skill/mode | p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Output/action | This state-feedback "control" hypothesis (9) will be verified in Sec. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Objective/outcome | Consider the following IK problem: minimizing a quadratic tracking objective in link spatial velocities, subject to forward kinematics constraints, task space equality constraints and joint velocity box constraints: min v,ν nb X ... | tracking, balance, skill/task success와 recovery | p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 2 (II. BACKGROUND), p. 7 (B. Feasibility Detection) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.
- **p. 2 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Constrained inverse kinematics ADMM formulation In the most general sense, first order constrained differential inverse kinematics can be formulated as a constrained QP problem: min ...
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** But more importantly, this mixed-coordinate formulation allows one to fully exploit the sparsity pattern induced by the robot's kinematic tree.
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties.
- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** We observe in these results that, while LOIK is 1.5-2× faster than QP-based approaches on single-task arm scenarios, it scales more favorably when moving on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Embodiment/environment | Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of mass (as in [27], we use a fixed ... | hardware/simulator version and reset protocol | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Dataset/benchmark | Following the steps (24), (26), (27), QP matrices and vectors are uniquely defined from task targets and the current robot configuration (see e.g. the documentation of [11] for further details). | role, split, size and leakage | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Metric | They solve the same underlying problem by computing the Jacobian matrix Ji(q) of the frame at the current configuration, and setting: AQP i = Ji(q) bQP i = v∗ i (q) (26) ... | definition, denominator, direction and uncertainty | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Baseline/ablation | Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems. | fair input/data/compute/action matching | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means in particular that, for "OSQP (Drake)", (1) ...
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.

## Why Read It

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack variables.를 문제로 두고, 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (II. BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, constrainedABA only considered the equalityconstrained forward dynamics problems and therefore does not support additional terms handled in QP-based differential IK such as joint-space and task-space inequality constraints. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Explicit failure boundary:** Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
