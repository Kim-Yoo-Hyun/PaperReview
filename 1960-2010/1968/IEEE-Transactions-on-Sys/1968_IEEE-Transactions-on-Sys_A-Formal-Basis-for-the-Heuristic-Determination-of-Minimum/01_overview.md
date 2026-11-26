# A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/TSSC.1968.300136.
> PDF retrieval source: https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Authors: Peter Hart, Nils Nilsson, Bertram Raphael
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, graph search, A*
- Official paper: https://api.crossref.org/works/10.1109/TSSC.1968.300136
- Full-text retrieval: https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf) 기준이다.

## Why This Paper Is Here

Hart·Nilsson·Raphael은 시작점까지의 비용과 남은 비용의 휴리스틱 추정값을 결합하는 A* 그래프 탐색을 정식화했다. [PDF 1쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=1)

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

A*는 시작·목표 노드, 간선 비용과 휴리스틱을 사용해 그래프의 최소 비용 경로를 탐색한다. 허용성 논증과 조건부 노드 확장 비교에는 센서나 피드백 제어 루프가 없다. [PDF 2쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=2) · [PDF 3쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=3)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, we must make some preliminary statements and definitions about graphs and search algorithms. | 시작·목표 노드, 간선 비용, 휴리스틱 | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| State/latent | First, must, make, some, preliminary, statements, definitions, about, graphs, search, algorithms, Suppose | 노드별 누적 비용과 남은 비용의 추정치 | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Output/action | Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city. | 선택된 경로와 확장 노드 | p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Objective/outcome | We shall represent this cost by h(ni, n3). | 최적 경로와 가정별 노드 확장 수 | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |

## Main Claims and Actual Contribution

- 남은 최적 비용을 과대평가하지 않는 휴리스틱에 대해 논문이 정의한 그래프 조건에서 최소 비용 경로를 찾음을 증명한다. [PDF 2쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=2) · [PDF 3쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=3) · [PDF 4쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=4)
- 서로 다른 탐색법이 사용하는 휴리스틱 정보와 노드 확장 수를 비교하며 일관성 가정의 역할을 분석한다. [PDF 5쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=5) · [PDF 6쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=6) · [PDF 7쪽](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/astar.pdf#page=7)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (A. The Problem of Finding Paths Through Graphs), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph. (p. 1, A. The Problem of Finding Paths Through Graphs).
- **Actual contribution:** First, we must make some preliminary statements and definitions about graphs and search algorithms. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Evaluation boundary:** The following is a typical illustration of the sort of problem to which our results are applicable. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Explicit failure boundary:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
