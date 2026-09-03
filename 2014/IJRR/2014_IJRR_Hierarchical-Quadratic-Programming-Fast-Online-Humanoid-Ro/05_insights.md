# Insights — Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1177/0278364914521306; PDF retrieval source: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 6 / 1 Introduction - extractive body cue:** We propose an original decomposition that encompasses the hierarchy among the constraints.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Equality hierarchical quadratic program We propose in this section a method to solve a hierarchy of linear equality in the least-square sense.
- **p. 5 / 1 Introduction - extractive body cue:** However, this expressivity reduction enables to obtain very impressive result for walking, jumping or, as shown in [Mordatch et al., 2012], for planning contacts and ...
- **p. 3 / 1 Introduction - extractive body cue:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) ...
- **p. 2 / 1 Introduction - extractive body cue:** A dedicated simplex solver was designed in [Isermann, 1982] for linear problem only.
- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We prove here that each outer loop of Algorithm 3 terminates.
- **Contribution anchor:** p. 6 (1 Introduction), p. 6 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 28 (B.2 Algorithm 3 termination)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, it is difficult to relax a DOF that was clamped.
- **p. 4 / 1 Introduction - extractive body cue:** The form (2) can be extended to inequalities by introducing an additional variable w, named the slack variable, in the parameter vector: min x,w ∥w ...
- **p. 5 / 1 Introduction - extractive body cue:** However, both methods [Kanoun et al., 2011] and [De Lasa et al., 2010] have the same intrinsic problem due to the nature of the underlying ...
- **p. 3 / 1 Introduction - extractive body cue:** A simplified version was proposed in [De Lasa et al., 2010], that improves the computation cost but prevents the inclusion of inequality except at the ...
- **p. 19 / 3.6 Conclusion - extractive body cue:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa ...
- **p. 12 / 2.6 Conclusion - extractive body cue:** Adaptating the method for iHQP is done through the following changes: • using our eHQP solver instead of the eQP, obviously, to find the hierarchical ...
- **Boundary to test:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa et al., 2010] for this setup because ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose an original decomposition that encompasses the hierarchy among the constraints. | p. 6 (1 Introduction), p. 6 (1 Introduction) |
| Reported outcome | Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop. | p. 22 (6.2.2 Results), p. 22 (6.2.2 Results) |
| Failure/limitation | The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa et al., 2010] for this setup because ... | p. 19 (3.6 Conclusion), p. 12 (2.6 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q. (p. 3, 1 Introduction).
- **Paper-specific mechanism:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) in the next sections. (p. 3, 1 Introduction).
- **Evidence boundary:** the reported outcome is For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on a similar computer. (p. 27, 6.2.2 Results); the relevant task/metric cue is The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow and shoulder to the left obstacle. (p. 22, 6.2.2 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. (p. 23, 6.2.2 Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, hierarchical QP, task hierarchy`.
- **Reading predecessor in the generated track queue:** Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa et al., 2010] for this setup because ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q. (p. 3, 1 Introduction); preserve the objective/update rule: We note m the total number of constraints, and w = (∥w1∥, · · · , ∥wp∥). (p. 28, B.2 Algorithm 3 termination).
2. Use the paper-reported task/data/environment cue: 11: Simulation B-1: Snapshots of the first movement: the robot uses only its left hand to manipulate the wheel. (p. 22, 6.2.2 Results).
3. Compare against the reported or matched baseline: 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start. (p. 21, 6.2.2 Results).
4. Report the body metric with its denominator and aggregation: The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow and shoulder to the left obstacle. (p. 22, 6.2.2 Results).
5. Re-run the reported ablation or stress/failure condition: 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start. (p. 21, 6.2.2 Results); if none is reported, design one around: Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. (p. 23, 6.2.2 Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 Introduction), p. 5 (1 Introduction), match the reported outcome at p. 27 (6.2.2 Results), p. 26 (6.2.2 Results), p. 27 (6.2.2 Results), and measure the boundary at p. 23 (6.2.2 Results), p. 19 (3.6 Conclusion).

## Falsifiable research question

Under the paper's stated interface (Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q.), does the paper-specific mechanism (Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with ...) retain the reported evaluation outcome (The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow ...) when tested against the paper's strongest explicit boundary (Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The constraints are the joint limits, the support polygon, the FOV and the distance of the left elbow ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (32 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) in the next sections. (p. 3, 1 Introduction).
- **Paper-supported outcome:** For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on a similar computer. (p. 27, 6.2.2 Results).
- **Strongest explicit boundary:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. (p. 23, 6.2.2 Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
