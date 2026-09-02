# Problem - Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack variables.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Differential inverse kinematics is a core robotics problem whose state-of-the-art solutions are currently based on quadratic programming.
- **p. 1 / Abstract - extractive body cue:** In this paper, we revisit it from the perspective of augmented Lagrangian methods (AL) and the related alternating direction method of multipliers (ADMM).
- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 1 / Abstract - extractive body cue:** Combined with the ADMM strategy popularized by OSQP, we handle the same class of problems as QP-based differential IK, but scaling linearly with problem dimensions ...
- **p. 1 / Abstract - extractive body cue:** We implement our approach as C++ opensource software and evaluate it on a benchmark of robotic-arm and humanoid-locomotion tasks.
- **p. 2 / II. BACKGROUND - extractive body cue:** The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack ...
- **p. 2 / II. BACKGROUND - extractive body cue:** However, one major distinction between the current state-of-the-arts and our proposed solution is that our solver is able to efficiently exploit the specific sparsity patterns ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | (14) indicates that νi is in the form of the state-feedback "control" hypothesis proposed in (9), when viewing problem (8) from the ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | indicates, form, state-feedback, control, hypothesis, when, viewing, problem, LQR, perspective | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | causal, relationship, defined, index-shifted, dynamics, equation, implies, state-feedback | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: indicates, form, state-feedback, control, hypothesis, when, viewing, problem, LQR, perspective | p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Decision / output variable | joint/whole-body action; body terms: Inequality, constraints, ADMM-based, strategy, dealing, where, ADMM, iteration | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Consider, following, problem, minimizing, quadratic, tracking, objective, link | p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (B. Feasibility Detection), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Success / guarantee | motion/task success and recovery | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / II. BACKGROUND - extractive body cue:** However, one major distinction between the current state-of-the-arts and our proposed solution is that our solver is able to efficiently exploit the specific sparsity patterns ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, constrainedABA only considered the equalityconstrained forward dynamics problems and therefore does not support additional terms handled in QP-based differential IK such as joint-space and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This approach relies on a class of convex optimization problems that has received more analysis and software development.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 2 (II. BACKGROUND), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE)): 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.

- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.
- **p. 2 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Constrained inverse kinematics ADMM formulation In the most general sense, first order constrained differential inverse kinematics can be formulated as a constrained QP problem: min ...
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** But more importantly, this mixed-coordinate formulation allows one to fully exploit the sparsity pattern induced by the robot's kinematic tree.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), objective p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
