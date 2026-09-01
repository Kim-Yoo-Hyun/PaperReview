# Method - A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/TSSC.1968.300136; PDF retrieval source: https://doi.org/10.1109/TSSC.1968.300136. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM)): First, we must make some preliminary statements and definitions about graphs and search algorithms.

## Method Body Digest

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** First, we must make some preliminary statements and definitions about graphs and search algorithms.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Then, in a following section, we shall show, under a mild assumption, that this algorithm uses information from the problem represented by the graph in ...
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** Then we can define a search algorithm as follows.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** We shall suggest a specific function below, but first we shall describe how a search algorithm would use such a function.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** We shall represent this cost by h(ni, n3).
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** We shall be concerned here with graphs whose arcs have costs associated with them.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** IEEE TRANSACTIONS ON SYSTEMS SCIENCE AND CYBERNETICS, JULY 1968 optimal path, it will sometimes fail to find such a path and thus not be admissible.

## Design Rationale

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.

## Source Evidence Cues

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** First, we must make some preliminary statements and definitions about graphs and search algorithms.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Then, in a following section, we shall show, under a mild assumption, that this algorithm uses information from the problem represented by the graph in ...
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** Then we can define a search algorithm as follows.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** We shall suggest a specific function below, but first we shall describe how a search algorithm would use such a function.
- **Detected method headings:** 2) The heuristic approach typically uses special knowl (p. 1); II. AN ADMISSIBLE SEARCHING ALGORITHM (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | First, we must make some preliminary statements and definitions about graphs and search algorithms. | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | Then, in a following section, we shall show, under a mild assumption, that this algorithm uses information from the problem represented by ... | p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | Then we can define a search algorithm as follows. | p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** We shall represent this cost by h(ni, n3).
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** We shall be concerned here with graphs whose arcs have costs associated with them.
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (2) The heuristic approach typically uses special knowl).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, must, make, some, preliminary, statements, definitions, about, graphs, search, algorithms, Suppose, desire, technique | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | First, must, make, some, preliminary, statements, definitions, about, graphs, search | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | Procedures, developed, heuristic, generally, have, been, able, guarantee, minimum, cost | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | shall, represent, cost, concerned, here, graphs, whose, arcs, have, costs | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** First, we must make some preliminary statements and definitions about graphs and search algorithms.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Suppose we desire a technique for discovering a sequence of cities on the shortest route from a specified start to a specified goal city.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** IEEE TRANSACTIONS ON SYSTEMS SCIENCE AND CYBERNETICS, JULY 1968 optimal path, it will sometimes fail to find such a path and thus not be admissible.
- **p. 3 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** Suppose some evaluation function f(n) could be calculated for any node n.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | Wolfe, "A duality theorem for nonlinear programming," Q. | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | Falk, "Lagrange multipliers and nonlinear programming," J. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, must, make, some, preliminary, statements, definitions, about, graphs, search, algorithms, Then, following, section, shall, under, mild, assumption, algorithm, uses.
- **Relevant PDF headings:** 2) The heuristic approach typically uses special knowl (p. 1); II. AN ADMISSIBLE SEARCHING ALGORITHM (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | This error occurs because the estimates h(s) = 8 and h(n2) = 1 are inconsistent in view of the fact that n2 ... | p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl) |
| Search / trajectory decision | Compared with other no more informed admissible algorithms, it expands the fewest possible nodes necessary to guarantee finding an optimal path. | p. 6 (6. The value of 0(no) remains), p. 6 (6. The value of 0(no) remains) |
| Execution interface | 0 ,On (3) We assume the infimum is achieved for some fOn In actual problems one probably never has an explicit representation ... | p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains) |

## Failure and Ablation Link

- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Case 3 Termination is at a goal node without achieving minimum cost.
- **p. 7 / 6. The value of 0(no) remains - extractive body cue:** Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does not know the value of f(s), this ...
- **p. 7 / IV. DiscussION AND CONCLUSIONS - extractive body cue:** In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close as a to that node with minimum ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s.
- **p. 2 / II. AN ADMISSIBLE SEARCHING ALGORITHM - extractive body cue:** If it expands nodes which obviously cannot be on an optimal path, it is wasting effort.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Our algorithm prescribes how to use special knowledge-e.g., the knowledge that the shortest road route between any pair of cities cannot be less than the ...
- **p. 4 / 6. The value of 0(no) remains - extractive body cue:** Limitation of Subgraphs by Informationfrom the Problem In the preceding section, we proved that if h(n) is any lower bound on h(n), then A* is ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), objective p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), temporal p. 1 (Front matter), p. 1 (Front matter), p. 2 (2) The heuristic approach typically uses special knowl), p. 4 (6. The value of 0(no) remains), p. 4 (6. The value of 0(no) remains), p. 5 (6. The value of 0(no) remains).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
