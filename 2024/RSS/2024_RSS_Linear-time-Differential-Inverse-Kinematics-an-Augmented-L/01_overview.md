# Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Bruce Wingo, Ajay Suresha Sathya, Stéphane Caron, Seth Hutchinson, Justin Carpentier
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, inverse kinematics, whole-body control, augmented Lagrangian, ADMM, real-time
- Official paper: https://www.roboticsproceedings.org/rss20/p110.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p110.html
- Code/Project: https://github.com/Simple-Robotics/Loik
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

증강 라그랑주 방법을 이용해 로봇의 미분 역기구학 문제에서 관절 수에 선형으로 증가하는 구조적 계산을 제시했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p110.pdf#page=1)

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

- 강체 계통의 재귀로 등식 제약 부분문제를 풀고 ADMM을 결합해 부등식이 있는 미분 역기구학도 다룬다. [PDF 2쪽](https://www.roboticsproceedings.org/rss20/p110.pdf#page=2) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p110.pdf#page=5)
- 로봇팔과 휴머노이드 보행의 역기구학 벤치마크에서 C++ 구현의 계산 시간을 기존 QP 풀이기와 비교했다. [PDF 8쪽](https://www.roboticsproceedings.org/rss20/p110.pdf#page=8) · [PDF 10쪽](https://www.roboticsproceedings.org/rss20/p110.pdf#page=10)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (II. BACKGROUND), p. 1 (I. INTRODUCTION), p. 1 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, constrainedABA only considered the equalityconstrained forward dynamics problems and therefore does not support additional terms handled in QP-based differential IK such as joint-space and task-space inequality constraints. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Explicit failure boundary:** Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).

## 원문과 공개 자료

- 코드 — 재귀식 미분 역기구학 풀이기 · include/loik/loik-loid-optimized.hxx [배포 파일](https://raw.githubusercontent.com/Simple-Robotics/Loik/12892d5d700b7eb5a3b135a0bc062cf01cbb9f12/include/loik/loik-loid-optimized.hxx)
