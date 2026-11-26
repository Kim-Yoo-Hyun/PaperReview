# Insights — Sampling-based Algorithms for Optimal Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (76 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1105.1186; PDF retrieval source: https://arxiv.org/pdf/1105.1186. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 1 Introduction - extractive body cue:** As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the ...
- **p. 11 / 1 Introduction - extractive body cue:** In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among n randomly-sampled points in Xfree, ...
- **p. 13 / 1 Introduction - extractive body cue:** Algorithm 3: RRT 1 V ←{xinit}; E ←∅; 2 for i = 1, . . . , n do 3 xrand ←SampleFreei; 4 xnearest ←Nearest(G ...
- **p. 2 / 1 Introduction - extractive body cue:** Important contributions towards broader applicability of these methods include navigation functions (Rimon and Koditschek, 1992) and randomization (Barraquand and Latombe, 1993).
- **p. 4 / 1 Introduction - extractive body cue:** A summary of the contributions can be found below, and is shown in Table 1.
- **p. 4 / 1 Introduction - extractive body cue:** 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties ...
- **p. 2 / 1 Introduction - extractive body cue:** Instead of using an explicit representation of the environment, samplingbased algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and ...
- **Contribution anchor:** p. 4 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and ...
- **p. 6 / 1 Introduction - extractive body cue:** The feasibility problem of path planning is to find a feasible path, if one exists, and report failure otherwise: Problem 2 (Feasible path planning) Given ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, the rate of decay of the probability of failure is exponential, under the assumption that the environment has good "visibility" properties (Barraquand et al., ...
- **p. 2 / 1 Introduction - extractive body cue:** Even though these algorithms are not complete, they provide probabilistic completeness guarantees in the sense that the probability that the planner fails to return a ...
- **p. 3 / 1 Introduction - extractive body cue:** The RRT algorithm has been shown to be probabilistically complete (Kuffner and LaValle, 2000), with an exponential rate of decay for the probability of failure ...
- **p. 35 / 6 Conclusion - extractive body cue:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...
- **Boundary to test:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the focus of the paper is on path ... | p. 4 (1 Introduction), p. 11 (1 Introduction) |
| Reported outcome | An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves O(cd,ε log n) query time using O(d n) space (Arya et al., 1999), where cd,ε ≤ d⌈1+6d/ε⌉d. | p. 31 (V RRT∗), p. 33 (V RRT∗) |
| Failure/limitation | In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in ... | p. 35 (6 Conclusion), p. 17 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set of goal states, the motion planning problem is to find ...를 For convenience, inputs and outputs of the algorithms are not shown explicitly, but are as follows.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the focus of the paper is on path ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, motion planning, RRT*, asymptotic optimality`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., in O(log n) time, especially for anytime ....
3. Compare against the body-reported baseline or a matched simpler baseline: Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number of simple operations, such as comparisons, additions, multiplications..
4. Report the body metric and its denominator/aggregation: Figure 25: The set eBn,m of non-intersection balls is illustrated. Finally, the following lemma states that the cost of the minimum cost path in the graph returned by the PRM∗algorithm converges to ....
5. Re-run the body-reported ablation/failure condition: Figure 11: Cost of the best path in the PRM∗algorithm is shown in up to 2, 3, 4, and 5 dimensional configuration spaces, in Figures (a), (b), (c), and (d), respectively. The ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (1 Introduction), p. 2 (1 Introduction), p. 7 (1 Introduction); the primary result is directionally consistent at p. 31 (V RRT∗), p. 33 (V RRT∗), p. 33 (V RRT∗); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 early, seminal, papers mechanism이 Using these results, a thorough analysis of the computational complexity of the all the algorithms is ... 대비 Figure 25: The set eBn,m of non-intersection balls is illustrated. Finally, the following lemma states that the cost ...을 개선하고, In order to address these limitations of existing algorithms, a number of new algorithms are introduced, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
