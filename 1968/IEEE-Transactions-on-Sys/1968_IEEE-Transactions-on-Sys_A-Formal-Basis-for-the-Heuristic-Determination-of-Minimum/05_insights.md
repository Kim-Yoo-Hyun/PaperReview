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

- **Paper-specific interface:** Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Paper-specific mechanism:** First, we must make some preliminary statements and definitions about graphs and search algorithms. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Evidence boundary:** the reported outcome is The following is a typical illustration of the sort of problem to which our results are applicable. (p. 2, 2) The heuristic approach typically uses special knowl); the relevant task/metric cue is In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less than the airline distance between city n and a preferred goal city ... (p. 4, 6. The value of 0(no) remains). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, Planning, graph search, A*`.
- **Reading predecessor in the generated track queue:** A New Approach to Linear Filtering and Prediction Problems (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Planning and Acting in Partially Observable Stochastic Domains (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this value is established as soon as the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city. (p. 2, 2) The heuristic approach typically uses special knowl); preserve the objective/update rule: Then we can define a search algorithm as follows. (p. 3, II. AN ADMISSIBLE SEARCHING ALGORITHM).
2. Use the paper-reported task/data/environment cue: The following is a typical illustration of the sort of problem to which our results are applicable. (p. 2, 2) The heuristic approach typically uses special knowl).
3. Compare against the reported or matched baseline: Case 3 Termination is at a goal node without achieving minimum cost. (p. 4, 6. The value of 0(no) remains).
4. Report the body metric with its denominator and aggregation: In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less than the airline distance between city n and a preferred goal city ... (p. 4, 6. The value of 0(no) remains).
5. Re-run the reported ablation or stress/failure condition: Case 3 Termination is at a goal node without achieving minimum cost. (p. 4, 6. The value of 0(no) remains); if none is reported, design one around: Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), match the reported outcome at p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 5 (6. The value of 0(no) remains), and measure the boundary at p. 4 (6. The value of 0(no) remains), p. 4 (6. The value of 0(no) remains).

## Falsifiable research question

Under the paper's stated interface (Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified ...), does the paper-specific mechanism (First, we must make some preliminary statements and definitions about graphs and search algorithms.) retain the reported evaluation outcome (In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less ...) when tested against the paper's strongest explicit boundary (Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (In our example with cities connected by roads, no subgraph G01 is possible for which h(n) is less ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** First, we must make some preliminary statements and definitions about graphs and search algorithms. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Paper-supported outcome:** The following is a typical illustration of the sort of problem to which our results are applicable. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Strongest explicit boundary:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
