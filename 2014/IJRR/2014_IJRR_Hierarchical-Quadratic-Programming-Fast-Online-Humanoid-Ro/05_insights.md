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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q.를 The evolution in the image space (or task space) with respect to the robot input is given by ˙e = J ˙q, with J = ∂e ∂q the task Jacobian.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa et al., 2010] for this setup because ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose an original decomposition that encompasses the hierarchy among the constraints.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, hierarchical QP, task hierarchy`.
- **Reading predecessor in the generated track queue:** Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa et al., 2010] for this setup because ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the environment..
3. Compare against the body-reported baseline or a matched simpler baseline: 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start..
4. Report the body metric and its denominator/aggregation: 24 and illustrate very well the hierarchical order: the task erh has priority over the three other ones, and is always accomplished: the error exponentially converges as imposed..
5. Re-run the body-reported ablation/failure condition: 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 28 (B.2 Algorithm 3 termination); the primary result is directionally consistent at p. 22 (6.2.2 Results), p. 22 (6.2.2 Results), p. 27 (6.2.2 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 original, decomposition, encompasses mechanism이 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP ... 대비 24 and illustrate very well the hierarchical order: the task erh has priority over the three other ones, ...을 개선하고, The ball is then placed back in front of the robot: the COM comes back to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
