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

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces.를 This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In practice, we do not increase the sampling parameter sizes upon a sampling failure.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Planning, task and motion planning, manipulation`.
- **Reading predecessor in the generated track queue:** Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single top grasp..
3. Compare against the body-reported baseline or a matched simpler baseline: The following heuristics are compared in the experiments: 1..
4. Report the body metric and its denominator/aggregation: HF F Rob, HA gave the best performance in both success rate and runtime..
5. Re-run the body-reported ablation/failure condition: Figure 15. A star-graph CRG visualized using end-effector poses. PATH(q, q′; (V, E)) (without considering any placed or held objects). In practice, we only create MOVE actions between start and goal configurations ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 3 (1.1 Approach); the primary result is directionally consistent at p. 30 (11.4 Results), p. 30 (11.4 Results), p. 31 (11.4 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Extended, Action mechanism이 The following heuristics are compared in the experiments: 1. 대비 HF F Rob, HA gave the best performance in both success rate and runtime.을 개선하고, In practice, we do not increase the sampling parameter sizes upon a sampling failure. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
