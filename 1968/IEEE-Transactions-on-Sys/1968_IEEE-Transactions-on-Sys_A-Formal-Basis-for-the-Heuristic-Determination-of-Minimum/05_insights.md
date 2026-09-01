# Insights — A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/TSSC.1968.300136; PDF retrieval source: https://doi.org/10.1109/TSSC.1968.300136. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** First, we must make some preliminary statements and definitions about graphs and search algorithms.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Then, in a following section, we shall show, under a mild assumption, that this algorithm uses information from the problem represented by the graph in ...
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** Then we can define a search algorithm as follows.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** We shall suggest a specific function below, but first we shall describe how a search algorithm would use such a function.
- **Contribution anchor:** p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM)

### Strongest assumption and failure boundary

- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** These problems have usually been approached in one of two ways, which we shall call the mathematical approach and the heuristic approach.
- **p. 7 / 6. The value of 0(no) remains - extractive body cue:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this ...
- **p. 7 / IV. DiscussION AND CONCLUSIONS - extractive body cue:** In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close as a to that node with minimum ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s.
- **p. 2 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** If it expands nodes which obviously cannot be on an optimal path, it is wasting effort.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Our algorithm prescribes how to use special knowledge-e.g., the knowledge that the shortest road route between any pair of cities cannot be less than the ...
- **Boundary to test:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this value is established as soon as the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found. | p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs) |
| Reported outcome | 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 but instead one selects a pro103 Authorized licensed ... | p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains) |
| Failure/limitation | Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this value is established as soon as the ... | p. 7 (6. The value of 0(no) remains), p. 7 (IV. DiscussION AND CONCLUSIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 First, we must make some preliminary statements and definitions about graphs and search algorithms.를 Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this value is established as soon as the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, Planning, graph search, A*`.
- **Reading predecessor in the generated track queue:** A New Approach to Linear Filtering and Prediction Problems (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Planning and Acting in Partially Observable Stochastic Domains (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this value is established as soon as the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: dataset/benchmark role not recovered.
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with other no more informed admissible algorithms, it expands the fewest possible nodes necessary to guarantee finding an optimal path..
4. Report the body metric and its denominator/aggregation: This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of the fact that n2 is only six units away from s..
5. Re-run the body-reported ablation/failure condition: Case 3 Termination is at a goal node without achieving minimum cost..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM); the primary result is directionally consistent at p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Procedures, developed, heuristic mechanism이 Compared with other no more informed admissible algorithms, it expands the fewest possible nodes necessary to ... 대비 This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of ...을 개선하고, Note that, although one cannot keep a running estimate of R while the algorithm proceeds because ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
