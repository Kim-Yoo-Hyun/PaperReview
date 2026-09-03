# Insights — Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1609.06408; PDF retrieval source: https://arxiv.org/pdf/1609.06408. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / B. Contributions - extractive body cue:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in ...
- **p. 2 / B. Contributions - extractive body cue:** The first contribution of this paper is to formulate conditions on the derivative of a (reciprocal or zeroing) barrier function that are minimally restrictive on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, barrier functions were used in the paper [4] to develop an interior penalty method for converting constrained optimal control methods into unconstrained ones1.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is ...
- **p. 3 / C. Organization and Notation - extractive body cue:** The theory developed in the paper is illustrated on the adaptive cruise control and lane keeping problems in Sect.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the resulting controllers via ...
- **p. 2 / B. Contributions - extractive body cue:** The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed via multiple CLFs) ...
- **Contribution anchor:** p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (C. Organization and Notation), p. 1 (I. INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by the use of Lyapunov functions to certify stability properties of a set without calculating the exact solution of a system, the underlying concept ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the case of reciprocal barrier functions, existing formulations impose invariant level sets of B [5], via, ˙B ≤0, as was done in earlier work ...
- **p. 10 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** 10 1) ACC problem setup: We begin by setting up the dynamics of the problem based upon [34] and [36], which assume that the lead ...
- **p. 11 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** Simulation results of the ACC problem based on (ACC QP) (left) speed of the lead car and the controlled car with the desired speed vd ...
- **p. 14 / VII. CONCLUSIONS - extractive body cue:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a ...
- **Boundary to test:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a special focus on robotic and automotive systems.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig. | p. 2 (B. Contributions), p. 2 (B. Contributions) |
| Reported outcome | A video of the results is available on YouTube [57]. | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Failure/limitation | Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a special focus on robotic and automotive systems. | p. 14 (VII. CONCLUSIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** (43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and leading vehicle (in m/s), respectively, D is the ... (p. 10, V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS).
- **Paper-specific mechanism:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig. (p. 2, B. Contributions).
- **Evidence boundary:** the reported outcome is Comparison of two QPs Recall that Figure 2 showed simulation results obtained by applying the QP controller in (ACC QP), where the force constraints were not taken into account. (p. 13, VI. SIMULATION RESULTS); the relevant task/metric cue is Simulation results for ACC Various problem formulations are compared here. (p. 13, VI. SIMULATION RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Note that, due to limits on the wheel forces, the speed converges to vd more slowly, and begins braking earlier, as evidenced by the top plot in Fig. (p. 13, VI. SIMULATION RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, control barrier function, safety-critical control, quadratic programming`.
- **Reading predecessor in the generated track queue:** TD-MPC2: Scalable, Robust World Models for Continuous Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a special focus on robotic and automotive systems.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: (43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and leading vehicle (in m/s), respectively, D is the ... (p. 10, V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS); preserve the objective/update rule: Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: The parameters used for the simulation are given in Table I. (p. 13, VI. SIMULATION RESULTS).
3. Compare against the reported or matched baseline: Simulation results for ACC Various problem formulations are compared here. (p. 13, VI. SIMULATION RESULTS).
4. Report the body metric with its denominator and aggregation: Simulation results for ACC Various problem formulations are compared here. (p. 13, VI. SIMULATION RESULTS).
5. Re-run the reported ablation or stress/failure condition: Fig. 3. The projection of CF onto the (y, ˙y)-plane is bounded by the upper and lower curves. The subset CLK ⊂Int(CF ) is bounded by the dotted lines. Any ... (p. 13, Figure/Table caption); if none is reported, design one around: Note that, due to limits on the wheel forces, the speed converges to vd more slowly, and begins braking earlier, as evidenced by the top plot in Fig. (p. 13, VI. SIMULATION RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), match the reported outcome at p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), and measure the boundary at p. 13 (VI. SIMULATION RESULTS), p. 1 (I. INTRODUCTION).

## Falsifiable research question

Under the paper's stated interface ((43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and ...), does the paper-specific mechanism (Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, ...) retain the reported evaluation outcome (Simulation results for ACC Various problem formulations are compared here.) when tested against the paper's strongest explicit boundary (Note that, due to limits on the wheel forces, the speed converges to vd more slowly, and begins ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Simulation results for ACC Various problem formulations are compared here.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig. (p. 2, B. Contributions).
- **Paper-supported outcome:** Comparison of two QPs Recall that Figure 2 showed simulation results obtained by applying the QP controller in (ACC QP), where the force constraints were not taken into account. (p. 13, VI. SIMULATION RESULTS).
- **Strongest explicit boundary:** Note that, due to limits on the wheel forces, the speed converges to vd more slowly, and begins braking earlier, as evidenced by the top plot in Fig. (p. 13, VI. SIMULATION RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
