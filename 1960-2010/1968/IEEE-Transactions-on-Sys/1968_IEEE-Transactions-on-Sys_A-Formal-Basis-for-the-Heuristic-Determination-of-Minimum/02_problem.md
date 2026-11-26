# Problem - A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/TSSC.1968.300136; PDF retrieval source: https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (A. The Problem of Finding Paths Through Graphs), p. 1 (A. The Problem of Finding Paths Through Graphs)): MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Although the problem of determining the minimum cost path through a graph arises naturally in a number of interesting applications, there has been no underlying ...
- **p. 1 / Abstract - extractive body cue:** Moreover, there is no adequate conceptual framework within which the various ad hoc search strategies proposed to date can be compared.
- **p. 1 / Abstract - extractive body cue:** This paper describes how heuristic information from the problem domain can be incorporated into a formal mathematical theory of graph searching and demonstrates an optimality ...
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** These problems have usually been approached in one of two ways, which we shall call the mathematical approach and the heuristic approach.
- **p. 2 / 2) The heuristic approach typically uses special knowl - extractive body cue:** Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.
- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph. | 가중 그래프의 최소 비용 경로 탐색 | body wording is the source claim |
| Observation / input | First, we must make some preliminary statements and definitions about graphs and search algorithms. | 시작·목표 노드, 간선 비용, 휴리스틱 | exact sensor/frame/preprocessing from PDF body |
| State / latent | First, must, make, some, preliminary, statements, definitions, about, graphs, search | 노드별 누적 비용과 남은 비용의 추정치 | notation and tensor shape require body check |
| Output / action | IEEE, TRANSACTIONS, SYSTEMS, SCIENCE, CYBERNETICS, JULY, optimal, path | 선택된 경로와 확장 노드 | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | 최적 경로와 가정별 노드 확장 수 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: First, must, make, some, preliminary, statements, definitions, about, graphs, search | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Procedures, developed, heuristic, generally, have, been, able, guarantee | p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: shall, represent, cost, concerned, here, graphs, whose, arcs | p. 2 (2) The heuristic approach typically uses special knowl) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** These problems have usually been approached in one of two ways, which we shall call the mathematical approach and the heuristic approach.

## What the Paper Changes

PDF body contribution framing (p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs)): Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.

- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | If it expands nodes which obviously cannot be on an optimal path, it is wasting effort. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (A. The Problem of Finding Paths Through Graphs), p. 1 (A. The Problem of Finding Paths Through Graphs), interface p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), objective p. 2 (2) The heuristic approach typically uses special knowl).

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph. (p. 1, A. The Problem of Finding Paths Through Graphs).
- **Formulation-changing contribution:** First, we must make some preliminary statements and definitions about graphs and search algorithms. (p. 2, 2) The heuristic approach typically uses special knowl).
- **Assumption/failure evidence:** Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps of s. (p. 4, 6. The value of 0(no) remains).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
