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

- **Paper-specific interface:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear complexity algorithm. (p. 3, III. LOW-COMPLEXITY DIFFERENTIAL INVERSE).
- **Paper-specific mechanism:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS); the relevant task/metric cue is We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, inverse kinematics, whole-body control, augmented Lagrangian, ADMM, real-time`.
- **Reading predecessor in the generated track queue:** Differentiable Robust Model Predictive Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. Bottom: value of the ADMM parameter µ ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear complexity algorithm. (p. 3, III. LOW-COMPLEXITY DIFFERENTIAL INVERSE); preserve the objective/update rule: Embracing optimization further enabled the integration of configuration and joint-velocity limits as inequality constraints. (p. 1, I. INTRODUCTION).
2. Use the paper-reported task/data/environment cue: Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of mass (as in [27], we use ... (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
3. Compare against the reported or matched baseline: Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems. (p. 9, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
4. Report the body metric with its denominator and aggregation: We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
5. Re-run the reported ablation or stress/failure condition: A tasks consists of two components: a target, as detailed in the latter two sections for the scenarios in this benchmark, and dynamics. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS); if none is reported, design one around: Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), and measure the boundary at p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS).

## Falsifiable research question

Under the paper's stated interface (The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an ...), does the paper-specific mechanism (Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.) retain the reported evaluation outcome (We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan ...) when tested against the paper's strongest explicit boundary (Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Strongest explicit boundary:** Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
