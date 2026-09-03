# Problem - Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p002.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM)): While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without exploiting the parallelization capabilities of ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent strides in nonlinear model predictive control (NMPC) underscore a dependence on numerical advancements to efficiently and accurately solve large-scale problems.
- **p. 1 / Abstract - extractive body cue:** Given the substantial number of variables characterizing typical wholebody optimal control (OC) problems -often numbering in the thousands- exploiting the sparse structure of the numerical ...
- **p. 1 / Abstract - extractive body cue:** Addressing the linear-quadratic regulator (LQR) problem is a fundamental building block for computing Newton or Sequential Quadratic Programming (SQP) steps in direct optimal control methods.
- **p. 1 / Abstract - extractive body cue:** This paper concentrates on equality-constrained problems featuring implicit system dynamics and dual regularization, a characteristic of advanced interiorpoint or augmented Lagrangian solvers.
- **p. 1 / Abstract - extractive body cue:** Here, we introduce a parallel algorithm for solving an LQR problem with dual regularization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Over the past decade, proposals have been given for the resolution of nonlinear equality-constrained problems.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Algorithm, Generalized, Riccati, equations, proximal, constrained, problem, Data, Cost, constraint | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | control, constraint, multiplier, co-state, next, state, parametric, solution | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Algorithm, Generalized, Riccati, equations, proximal, constrained, problem, Data, Cost, constraint | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM) |
| Decision / output variable | joint/whole-body action; body terms: present, secondary, contribution, have, implemented, evaluated, experimental, section | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: OPTIMIZER, consider, nonlinear, discrete-time, trajectory, optimization, problem, implicit | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| Success / guarantee | motion/task success and recovery | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Over the past decade, proposals have been given for the resolution of nonlinear equality-constrained problems.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This paper follows up from our prior work on augmented Lagrangian methods for numerical optimal control with implicit dynamics and constraints [29, 28].
- **p. 2 / I. INTRODUCTION - extractive body cue:** This formulation is extended in Section IV to parametric LQ problems, which we finally use in Section V to build a parallel algorithm and discuss ...
- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 ...

## What the Paper Changes

PDF body contribution framing (p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 4 (IV. EXTENSION TO PARAMETRIC LQ PROBLEMS)): We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a general direct solver for LQ problems with implicit dynamics and additional equality constraints, leveraging parameterization to formulate a parallel ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 4 / IV. EXTENSION TO PARAMETRIC LQ PROBLEMS - extractive body cue:** In this subsection, we extend the block-sparse approach we presented in section III-C to parametric problems.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | In our setting, the linear subproblem (47) does not have that same structure (such that our construction from ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), interface p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION), objective p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage ... (p. 9, VII. DISCUSSION).
- **Formulation-changing contribution:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16]. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage ... (p. 9, VII. DISCUSSION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
