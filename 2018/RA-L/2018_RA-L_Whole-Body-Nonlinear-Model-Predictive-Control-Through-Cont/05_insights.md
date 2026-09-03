# Insights — Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1712.02889; PDF retrieval source: https://arxiv.org/pdf/1712.02889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Contributions In this work, we demonstrate whole-body, contact invariant nonlinear MPC for highly dynamic motions that require explicit reasoning about the full dynamics of the ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Since our code mostly consists of matrix and vector manipulations and register sizes of AVX are doubled over SSE, we obtained an additional speedup of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** While the development of processors with faster clock speed has stalled in recent years, processing power instead foremost grows due to higher computation core counts ...
- **p. 3 / III. NMPC APPROACH - extractive body cue:** In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.
- **p. 3 / III. NMPC APPROACH - extractive body cue:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 2 (I. INTRODUCTION), p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this field, centroidal dynamics approaches [5]-[9] become increasingly popular as they capture the core dynamics of the problem.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We summarize our solver framework, which uses Auto-Differentiation and code generation to achieve high computational performance exceeding the current state of the art in robotics ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily.
- **p. 7 / VII. SUMMARY AND OUTLOOK - extractive body cue:** Furthermore, while most tasks by design stayed within the physical limitations of the platforms, GNMS would allow us to handle constraints such as torque limitations ...
- **Boundary to test:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches almost 190 Hz. While the higher update rate ... | p. 7 (Figure/Table caption), p. 5 (VI. RESULTS) |
| Failure/limitation | However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers. | p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (IV. SOFTWARE IMPLEMENTATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** While whole-body, contact invariant NMPC has been demonstrated on hardware before [15], the presented motions were rather slow or even quasi static, underlined by the fact that the authors do ... (p. 1, I. INTRODUCTION).
- **Paper-specific mechanism:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Note that running only a single solver iteration before updating the state measurement results in better overall performance than running multiple iterations and letting the solver converge. (p. 5, VI. RESULTS); the relevant task/metric cue is The performance of our algorithms is assessed on both quadrupeds. (p. 5, VI. RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Even placing planks under single feet does not deteriorate performance. (p. 5, VI. RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, model predictive control, quadruped`.
- **Reading predecessor in the generated track queue:** Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: While whole-body, contact invariant NMPC has been demonstrated on hardware before [15], the presented motions were rather slow or even quasi static, underlined by the fact that the authors do ... (p. 1, I. INTRODUCTION); preserve the objective/update rule: AN-1, B1, . . . , BN-1. - quadratize cost function (1) around X, U for multiple-shooting intervals 1 to N. policy update. (p. 3, III. NMPC APPROACH).
2. Use the paper-reported task/data/environment cue: While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as close as possible to the nominal ... (p. 6, VI. RESULTS).
3. Compare against the reported or matched baseline: HyQ can be perturbed significantly both on the base and the legs without reacting stiffly. (p. 5, VI. RESULTS).
4. Report the body metric with its denominator and aggregation: The performance of our algorithms is assessed on both quadrupeds. (p. 5, VI. RESULTS).
5. Re-run the reported ablation or stress/failure condition: The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants. (p. 4, IV. SOFTWARE IMPLEMENTATION); if none is reported, design one around: Even placing planks under single feet does not deteriorate performance. (p. 5, VI. RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 5 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 6 (VI. RESULTS), and measure the boundary at p. 5 (VI. RESULTS), p. 6 (VI. RESULTS).

## Falsifiable research question

Under the paper's stated interface (While whole-body, contact invariant NMPC has been demonstrated on hardware before [15], the presented motions were rather slow or even quasi static, ...), does the paper-specific mechanism (In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.) retain the reported evaluation outcome (The performance of our algorithms is assessed on both quadrupeds.) when tested against the paper's strongest explicit boundary (Even placing planks under single feet does not deteriorate performance.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The performance of our algorithms is assessed on both quadrupeds.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Note that running only a single solver iteration before updating the state measurement results in better overall performance than running multiple iterations and letting the solver converge. (p. 5, VI. RESULTS).
- **Strongest explicit boundary:** Even placing planks under single feet does not deteriorate performance. (p. 5, VI. RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
