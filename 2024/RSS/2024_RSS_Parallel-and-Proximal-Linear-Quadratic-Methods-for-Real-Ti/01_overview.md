# Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p002.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p002.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, MPC, optimal control, LQR, whole-body control, real-time
- Official paper: https://www.roboticsproceedings.org/rss20/p002.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p002.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without exploiting the parallelization capabilities of modern processing ...를 문제로 두고, We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent strides in nonlinear model predictive control (NMPC) underscore a dependence on numerical advancements to efficiently and accurately solve large-scale problems.
- **p. 1 / Abstract - extractive body cue:** Given the substantial number of variables characterizing typical wholebody optimal control (OC) problems -often numbering in the thousands- exploiting the sparse structure of the numerical ...
- **p. 1 / Abstract - extractive body cue:** Addressing the linear-quadratic regulator (LQR) problem is a fundamental building block for computing Newton or Sequential Quadratic Programming (SQP) steps in direct optimal control methods.
- **p. 1 / Abstract - extractive body cue:** This paper concentrates on equality-constrained problems featuring implicit system dynamics and dual regularization, a characteristic of advanced interiorpoint or augmented Lagrangian solvers.
- **p. 1 / Abstract - extractive body cue:** Here, we introduce a parallel algorithm for solving an LQR problem with dual regularization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Over the past decade, proposals have been given for the resolution of nonlinear equality-constrained problems.

## Core Idea

- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a general direct solver for LQ problems with implicit dynamics and additional equality constraints, leveraging parameterization to formulate a parallel ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 4 / IV. EXTENSION TO PARAMETRIC LQ PROBLEMS - extractive body cue:** In this subsection, we extend the block-sparse approach we presented in section III-C to parametric problems.
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** The coefficients of the problem are obtained from the derivatives of (48) with the following equivalences: At = φx,t Bt = φu,t Et = φy,t ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 pN ←qN + 1 µC⊤ N ¯hN; ... | proprioception, reference pose/motion, visual or language command | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM) |
| State/latent | Algorithm, Generalized, Riccati, equations, proximal, constrained, problem, Data, Cost, constraint, matrices, NCN | whole-body pose, balance/contact state와 skill/mode | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM) |
| Output/action | We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION) |
| Objective/outcome | OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 = x0 (48b) φt(xt,ut,xt+1) = 0 (48c) ... | tracking, balance, skill/task success와 recovery | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |

## Main Claims and Actual Contribution

- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a general direct solver for LQ problems with implicit dynamics and additional equality constraints, leveraging parameterization to formulate a parallel ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 4 / IV. EXTENSION TO PARAMETRIC LQ PROBLEMS - extractive body cue:** In this subsection, we extend the block-sparse approach we presented in section III-C to parametric problems.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** It is the authors' aim to improve its efficiency in the future.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Synthetic benchmark To assess the speedups our implementation of the parallel algorithm could achieve, we implemented a synthetic benchmark of problems with different horizons ranging ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** 2) Constrained NMPC on TALOS: In this subsection, we leverage our proximal solver to perform whole-body nonlinear MPC on the humanoid robot TALOS in simulation, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Embodiment/environment | 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts. | hardware/simulator version and reset protocol | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Dataset/benchmark | 2) Constrained NMPC on TALOS: In this subsection, we leverage our proximal solver to perform whole-body nonlinear MPC on the humanoid robot TALOS in simulation, similarly to what is achieved in [15] ... | role, split, size and leakage | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Metric | Each instance is run 40 times on every solver to produce a mean and standard deviation. | definition, denominator, direction and uncertainty | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Baseline/ablation | 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the CROCODDYL library [36]. | fair input/data/compute/action matching | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VII. DISCUSSION - extractive body cue:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it ...

## Why Read It

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without exploiting the parallelization capabilities of modern processing ...를 문제로 두고, We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
