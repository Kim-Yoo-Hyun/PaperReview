# Insights — Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p002.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a general direct solver for LQ problems with implicit dynamics and additional equality constraints, leveraging parameterization to formulate a parallel ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 4 / IV. EXTENSION TO PARAMETRIC LQ PROBLEMS - extractive body cue:** In this subsection, we extend the block-sparse approach we presented in section III-C to parametric problems.
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** The coefficients of the problem are obtained from the derivatives of (48) with the following equivalences: At = φx,t Bt = φu,t Et = φy,t ...
- **Contribution anchor:** p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 4 (IV. EXTENSION TO PARAMETRIC LQ PROBLEMS), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** While solving the LQR is often a bottleneck in recent efficient optimal control solvers [21, 36, 22], most of them rely on sequential implementation without ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Over the past decade, proposals have been given for the resolution of nonlinear equality-constrained problems.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This paper follows up from our prior work on augmented Lagrangian methods for numerical optimal control with implicit dynamics and constraints [29, 28].
- **p. 2 / I. INTRODUCTION - extractive body cue:** This formulation is extended in Section IV to parametric LQ problems, which we finally use in Section V to build a parallel algorithm and discuss ...
- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 ...
- **p. 9 / VII. DISCUSSION - extractive body cue:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it ...
- **Boundary to test:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section. | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION) |
| Reported outcome | It is the authors' aim to improve its efficiency in the future. | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Failure/limitation | In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ... | p. 9 (VII. DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp. (p. 3, III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM).
- **Paper-specific mechanism:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16]. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is The timing results of this experiment are shown in fig. (p. 10, VIII. EXPERIMENTS); the relevant task/metric cue is Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC. (p. 10, VIII. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage ... (p. 9, VII. DISCUSSION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, MPC, optimal control, LQR, whole-body control, real-time`.
- **Reading predecessor in the generated track queue:** Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Differentiable Robust Model Predictive Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp. (p. 3, III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM); preserve the objective/update rule: OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 = x0 (48b) φt(xt,ut,xt+1) = ... (p. 8, VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY).
2. Use the paper-reported task/data/environment cue: 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts. (p. 9, VIII. EXPERIMENTS).
3. Compare against the reported or matched baseline: 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the CROCODDYL library [36]. (p. 9, VIII. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC. (p. 10, VIII. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: It is the authors' aim to improve its efficiency in the future. (p. 9, VIII. EXPERIMENTS); if none is reported, design one around: In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage ... (p. 9, VII. DISCUSSION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 10 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), and measure the boundary at p. 9 (VII. DISCUSSION), p. 11 (VIII. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.), does the paper-specific mechanism (In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].) retain the reported evaluation outcome (Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC.) when tested against the paper's strongest explicit boundary (In our setting, the linear subproblem (47) does not have that same structure (such that our construction from ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16]. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** The timing results of this experiment are shown in fig. (p. 10, VIII. EXPERIMENTS).
- **Strongest explicit boundary:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage ... (p. 9, VII. DISCUSSION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
