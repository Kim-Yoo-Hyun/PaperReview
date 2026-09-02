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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 pN ←qN + 1 µC⊤ N ¯hN; ...를 We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, MPC, optimal control, LQR, whole-body control, real-time`.
- **Reading predecessor in the generated track queue:** Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Differentiable Robust Model Predictive Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts..
3. Compare against the body-reported baseline or a matched simpler baseline: 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the CROCODDYL library [36]..
4. Report the body metric and its denominator/aggregation: Each instance is run 40 times on every solver to produce a mean and standard deviation..
5. Re-run the body-reported ablation/failure condition: In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it is still possible to leverage or design ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY); the primary result is directionally consistent at p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, secondary, contribution mechanism이 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the ... 대비 Each instance is run 40 times on every solver to produce a mean and standard deviation.을 개선하고, In our setting, the linear subproblem (47) does not have that same structure (such that our ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
