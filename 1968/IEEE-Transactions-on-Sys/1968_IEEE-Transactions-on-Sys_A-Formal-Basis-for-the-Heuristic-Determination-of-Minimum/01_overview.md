# A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/TSSC.1968.300136.
> PDF retrieval source: https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, Planning, graph search, A*
- Official paper: https://doi.org/10.1109/TSSC.1968.300136
- Full-text retrieval: https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.를 문제로 두고, Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Although the problem of determining the minimum cost path through a graph arises naturally in a number of interesting applications, there has been no underlying ...
- **p. 1 / Abstract - extractive body cue:** Moreover, there is no adequate conceptual framework within which the various ad hoc search strategies proposed to date can be compared.
- **p. 1 / Abstract - extractive body cue:** This paper describes how heuristic information from the problem domain can be incorporated into a formal mathematical theory of graph searching and demonstrates an optimality ...
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** These problems have usually been approached in one of two ways, which we shall call the mathematical approach and the heuristic approach.

## Core Idea

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** First, we must make some preliminary statements and definitions about graphs and search algorithms.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Then, in a following section, we shall show, under a mild assumption, that this algorithm uses information from the problem represented by the graph in ...
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** Then we can define a search algorithm as follows.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** We shall suggest a specific function below, but first we shall describe how a search algorithm would use such a function.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, we must make some preliminary statements and definitions about graphs and search algorithms. | start/goal, map, dynamics와 successor/operator description | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| State/latent | First, must, make, some, preliminary, statements, definitions, about, graphs, search, algorithms, Suppose | path, trajectory, symbolic state 또는 task-motion decision | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Output/action | Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city. | feasible action sequence 또는 minimum-cost plan | p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Objective/outcome | We shall represent this cost by h(ni, n3). | path cost, goal reachability, feasibility와 computation | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |

## Main Claims and Actual Contribution

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation for {Gn,0 but ...
- **p. 5 / 6. The value of 0(no) remains - extractive body cue:** It means that any estimate h(n) calculated from data available in the "physical" situation represented by node n alone would not be improved by using ...
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Application of r to the source nodes, to their successors, and so forth as long as new nodes can be generated results in an explicit ...
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** The following is a typical illustration of the sort of problem to which our results are applicable.
- **p. 3 / 1) Mark s "open" and calculatef(s) - extractive body cue:** Starting with s, we obtain successors ni and n2.
- **p. 3 / 1) Mark s "open" and calculatef(s) - extractive body cue:** Suppose A * expands ni next with successors n2 and n3.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains) |
| Embodiment/environment | not stated or recoverable in the selected PDF body | hardware/simulator version and reset protocol | 본문 anchor 없음 |
| Dataset/benchmark | not stated or recoverable in the selected PDF body | role, split, size and leakage | 본문 anchor 없음 |
| Metric | This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of the fact that n2 is only six units away from s. | definition, denominator, direction and uncertainty | p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| Baseline/ablation | Compared with other no more informed admissible algorithms, it expands the fewest possible nodes necessary to guarantee finding an optimal path. | fair input/data/compute/action matching | p. 6 (6. The value of 0(no) remains), p. 6 (6. The value of 0(no) remains), p. 4 (6. The value of 0(no) remains) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6. The value of 0(no) remains - extractive body cue:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this ...
- **p. 7 / IV. DiscussION AND CONCLUSIONS - extractive body cue:** In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close as a to that node with minimum ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s.
- **p. 2 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** If it expands nodes which obviously cannot be on an optimal path, it is wasting effort.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Our algorithm prescribes how to use special knowledge-e.g., the knowledge that the shortest road route between any pair of cities cannot be less than the ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Limitation of Subgraphs by Informationfrom the Problem In the preceding section, we proved that if h(n) is any lower bound on h(n), then A* is ...
- **p. 5 / 6. The value of 0(no) remains - extractive body cue:** The information that there cannot exist a path from s to a goal with total cost less than eight was somehow available for the computation ...

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.를 문제로 두고, Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (A. The Problem of Finding Paths Through Graphs), p. 1 (A. The Problem of Finding Paths Through Graphs), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph. (p. 1, A. The Problem of Finding Paths Through Graphs).
- **Actual contribution:** First, we must make some preliminary statements and definitions about graphs and search algorithms. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Evaluation boundary:** The following is a typical illustration of the sort of problem to which our results are applicable. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Explicit failure boundary:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
