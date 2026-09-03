# Insights — Contact-Invariant Optimization for Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html; PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...
- **p. 2 / 1 Introduction - extractive body cue:** Intuitively, CIO is a way of reshaping a highly discontinuous and local-minima-prone search space of movements and contacts, into a slightly larger but much better-behaved ...
- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 2 / 1 Introduction - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 2 / 1 Introduction - extractive body cue:** Additional innovations include a continuation scheme allowing helper forces at the potential contacts rather than the torso, as well as a feature-based model of physics ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should ...
- **p. 1 / 1 Introduction - extractive body cue:** Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, ...
- **p. 1 / 1 Introduction - extractive body cue:** With the current state-of-the-art in automated motion synthesis, any additional complex behavior would require a new movement model carefully crafted by experts from scratch.
- **p. 2 / 1 Introduction - extractive body cue:** 1.1 The key idea: Contact-Invariant Optimization (CIO) As with prior methods for automated behavior synthesis, our CIO method also comes down to exploiting domain-specific knowledge.
- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **Boundary to test:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | At the core of our framework is the contact-invariant optimization (CIO) method we introduce here. | p. 1 (Abstract), p. 1 (1 Introduction) |
| Reported outcome | Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other. | p. 6 (5 Results), p. 6 (5 Results) |
| Failure/limitation | One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density. | p. 6 (5 Results), p. 6 (5 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** This is a very large domain because almost all limb movements performed on land are made for the purpose of establishing contact with some object (including the ground) and exerting ... (p. 2, 1 Introduction).
- **Paper-specific mechanism:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. (p. 6, 5 Results); the relevant task/metric cue is The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology. (p. 6, 5 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Another simplification we make is to penalize any relative velocity at contacting end effectors (see (2)), which results in trajectories that do not have any noticeable slipping. (p. 6, 5 Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, trajectory optimization, contact invariant`.
- **Reading predecessor in the generated track queue:** GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: This is a very large domain because almost all limb movements performed on land are made for the purpose of establishing contact with some object (including the ground) and exerting ... (p. 2, 1 Introduction); preserve the objective/update rule: These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the movement trajectory. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. (p. 6, 5 Results).
3. Compare against the reported or matched baseline: For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified. (p. 6, 5 Results).
4. Report the body metric with its denominator and aggregation: The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology. (p. 6, 5 Results).
5. Re-run the reported ablation or stress/failure condition: One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density. (p. 6, 5 Results); if none is reported, design one around: Another simplification we make is to penalize any relative velocity at contacting end effectors (see (2)), which results in trajectories that do not have any noticeable slipping. (p. 6, 5 Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 6 (5 Results), p. 6 (5 Results), p. 6 (5 Results), and measure the boundary at p. 6 (5 Results), p. 7 (5 Results).

## Falsifiable research question

Under the paper's stated interface (This is a very large domain because almost all limb movements performed on land are made for the purpose of establishing contact ...), does the paper-specific mechanism (In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc) retain the reported evaluation outcome (The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology.) when tested against the paper's strongest explicit boundary (Another simplification we make is to penalize any relative velocity at contacting end effectors (see (2)), which results ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc (p. 1, 1 Introduction).
- **Paper-supported outcome:** Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. (p. 6, 5 Results).
- **Strongest explicit boundary:** Another simplification we make is to penalize any relative velocity at contacting end effectors (see (2)), which results in trajectories that do not have any noticeable slipping. (p. 6, 5 Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
