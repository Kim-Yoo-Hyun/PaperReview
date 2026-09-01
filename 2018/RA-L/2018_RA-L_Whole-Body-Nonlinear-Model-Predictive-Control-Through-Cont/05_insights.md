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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control action and Kn a linear feedback controller ...를 The optimized control input obtained from the NMPC solver is then augmented with the output of two tracking controllers. instructions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, model predictive control, quadruped`.
- **Reading predecessor in the generated track queue:** Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as close as possible to the nominal state..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to ANYmal the magnitude of the deviations is slightly larger..
4. Report the body metric and its denominator/aggregation: Even placing planks under single feet does not deteriorate performance..
5. Re-run the body-reported ablation/failure condition: The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. NMPC APPROACH), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 5 (VI. RESULTS), p. 7 (VI. RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, whole-body, Nonlinear mechanism이 Compared to ANYmal the magnitude of the deviations is slightly larger. 대비 Even placing planks under single feet does not deteriorate performance.을 개선하고, However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
