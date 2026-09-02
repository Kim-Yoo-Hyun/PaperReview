# Insights — Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.
- **p. 2 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Constrained inverse kinematics ADMM formulation In the most general sense, first order constrained differential inverse kinematics can be formulated as a constrained QP problem: min ...
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** But more importantly, this mixed-coordinate formulation allows one to fully exploit the sparsity pattern induced by the robot's kinematic tree.
- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 2 (II. BACKGROUND), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / II. BACKGROUND - extractive body cue:** The weighted approach addresses these conflicts by defining slack variables on equality constraints, and relaxing the problem into a weighted quadratic penalization over these slack ...
- **p. 2 / II. BACKGROUND - extractive body cue:** However, one major distinction between the current state-of-the-arts and our proposed solution is that our solver is able to efficiently exploit the specific sparsity patterns ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, constrainedABA only considered the equalityconstrained forward dynamics problems and therefore does not support additional terms handled in QP-based differential IK such as joint-space and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This approach relies on a class of convex optimization problems that has received more analysis and software development.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means in particular that, for "OSQP (Drake)", (1) ...
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.
- **Boundary to test:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. Bottom: value of the ADMM parameter µ ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties. | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Failure/limitation | Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. Bottom: value of the ADMM parameter µ ... | p. 10 (Figure/Table caption), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 (14) indicates that νi is in the form of the state-feedback "control" hypothesis proposed in (9), when viewing problem (8) from the LQR perspective.를 This state-feedback "control" hypothesis (9) will be verified in Sec.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. Bottom: value of the ADMM parameter µ ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, inverse kinematics, whole-body control, augmented Lagrangian, ADMM, real-time`.
- **Reading predecessor in the generated track queue:** Differentiable Robust Model Predictive Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. Bottom: value of the ADMM parameter µ ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of mass (as in [27], we use a fixed ....
3. Compare against the body-reported baseline or a matched simpler baseline: Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems..
4. Report the body metric and its denominator/aggregation: They solve the same underlying problem by computing the Jacobian matrix Ji(q) of the frame at the current configuration, and setting: AQP i = Ji(q) bQP i = v∗ i (q) (26) ....
5. Re-run the body-reported ablation/failure condition: A tasks consists of two components: a target, as detailed in the latter two sections for the scenarios in this benchmark, and dynamics..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND); the primary result is directionally consistent at p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Inequality, constraints, ADMM-based mechanism이 Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK ... 대비 They solve the same underlying problem by computing the Jacobian matrix Ji(q) of the frame at the current ...을 개선하고, Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
