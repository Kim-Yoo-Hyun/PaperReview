# Insights — FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://journals.sagepub.com/doi/10.1177/0278364917739114; PDF retrieval source: https://journals.sagepub.com/doi/10.1177/0278364917739114. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** The primary contribution of this paper is FFROB, an efficient and probabilistically complete algorithm for fully integrated task and motion planning.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.
- **p. 2 / 1.1 Approach - extractive body cue:** EAS is able to represent actions with complex conditions much more concisely than a traditional symbolic planning representation.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.
- **Contribution anchor:** p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction), p. 2 (1.1 Approach), p. 3 (1.1 Approach)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation planning remains challenging because it is notoriously difficult to work in a high-dimensional space and make a long sequence of intertwined decisions.
- **p. 2 / 1 Introduction - extractive body cue:** We cannot efficiently maintain a representation of this connectivity with a set of static assertions updated by symbolic actions; determining how the connectivity of the ...
- **p. 1 / 1 Introduction - extractive body cue:** 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.
- **p. 30 / 11 Experiments - extractive body cue:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.
- **p. 30 / 11 Experiments - extractive body cue:** We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures.
- **Boundary to test:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. | p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Reported outcome | HF F Rob, HA gave the best performance in both success rate and runtime. | p. 30 (11.4 Results), p. 30 (11.4 Results) |
| Failure/limitation | In practice, we do not increase the sampling parameter sizes upon a sampling failure. | p. 30 (11 Experiments), p. 30 (11 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions. (p. 2, 1.1 Approach).
- **Paper-specific mechanism:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. (p. 2, 1.1 Approach).
- **Evidence boundary:** the reported outcome is Experiment results over 50 trials. informative heuristic estimate. (p. 31, 11.4 Results); the relevant task/metric cue is HF F Rob, HA gave the best performance in both success rate and runtime. (p. 30, 11.4 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In practice, we do not increase the sampling parameter sizes upon a sampling failure. (p. 30, 11 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Planning, task and motion planning, manipulation`.
- **Reading predecessor in the generated track queue:** Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions. (p. 2, 1.1 Approach); preserve the objective/update rule: We model task and motion planning as symbolic planning where the conditions of actions are complex predicates involving geometric and kinematic constraints. (p. 2, 1.1 Approach).
2. Use the paper-reported task/data/environment cue: 11.3 Implementation We implemented FFROB in Python using the OpenRAVE robotics framework (Diankov and Kuffner 2008) for simulation. (p. 30, 11 Experiments).
3. Compare against the reported or matched baseline: The following heuristics are compared in the experiments: 1. (p. 29, 11 Experiments).
4. Report the body metric with its denominator and aggregation: HF F Rob, HA gave the best performance in both success rate and runtime. (p. 30, 11.4 Results).
5. Re-run the reported ablation or stress/failure condition: This allows a large number of placements to be created for constrained problems without greatly increasing the branching factor. (p. 30, 11 Experiments); if none is reported, design one around: In practice, we do not increase the sampling parameter sizes upon a sampling failure. (p. 30, 11 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1.1 Approach), p. 1 (1 Introduction), match the reported outcome at p. 31 (11.4 Results), p. 27 (11 Experiments), p. 28 (11 Experiments), and measure the boundary at p. 30 (11 Experiments), p. 24 (A PPM).

## Falsifiable research question

Under the paper's stated interface (This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions.), does the paper-specific mechanism (We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.) retain the reported evaluation outcome (HF F Rob, HA gave the best performance in both success rate and runtime.) when tested against the paper's strongest explicit boundary (In practice, we do not increase the sampling parameter sizes upon a sampling failure.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (HF F Rob, HA gave the best performance in both success rate and runtime.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. (p. 2, 1.1 Approach).
- **Paper-supported outcome:** Experiment results over 50 trials. informative heuristic estimate. (p. 31, 11.4 Results).
- **Strongest explicit boundary:** In practice, we do not increase the sampling parameter sizes upon a sampling failure. (p. 30, 11 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
