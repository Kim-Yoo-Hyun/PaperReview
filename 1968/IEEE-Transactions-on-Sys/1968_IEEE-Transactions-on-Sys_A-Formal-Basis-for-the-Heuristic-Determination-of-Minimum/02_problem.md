# Problem - A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/TSSC.1968.300136; PDF retrieval source: https://doi.org/10.1109/TSSC.1968.300136. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

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
| Target problem | MANY PROBLEIVIS of engineering and scientific importance can be related to the general problem of finding a path through a graph. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | First, we must make some preliminary statements and definitions about graphs and search algorithms. | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | First, must, make, some, preliminary, statements, definitions, about, graphs, search | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | IEEE, TRANSACTIONS, SYSTEMS, SCIENCE, CYBERNETICS, JULY, optimal, path | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: First, must, make, some, preliminary, statements, definitions, about, graphs, search | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Procedures, developed, heuristic, generally, have, been, able, guarantee | p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: shall, represent, cost, concerned, here, graphs, whose, arcs | p. 2 (2) The heuristic approach typically uses special knowl) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (6. The value of 0(no) remains), p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** These problems have usually been approached in one of two ways, which we shall call the mathematical approach and the heuristic approach.

## What the Paper Changes

PDF contribution framing (p. 2 (2) The heuristic approach typically uses special knowl), p. 1 (A. The Problem of Finding Paths Through Graphs)): Procedures developed via the heuristic approach generally have not been able to guarantee that minimum cost solution paths will always be found.

- **p. 1 / A. The Problem of Finding Paths Through Graphs - extractive body cue:** [3] The mathematical approach is generally more concerned with the ultimate achievement of solutions than it is with the computational feasibility of the algorithms developed.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Note that, although one cannot keep a running estimate of R while the algorithm proceeds because one does ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In this case, an admissible algorithm cannot rule out the possibility that the goal might be as close ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Failure of A* to terminate could then only be caused by continued reopening of nodes within M steps ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | If it expands nodes which obviously cannot be on an optimal path, it is wasting effort. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (A. The Problem of Finding Paths Through Graphs), p. 1 (A. The Problem of Finding Paths Through Graphs), interface p. 2 (2) The heuristic approach typically uses special knowl), p. 2 (2) The heuristic approach typically uses special knowl), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), p. 3 (II. AN ADMISSIBLE SEARCHING ALGORITHM), objective p. 2 (2) The heuristic approach typically uses special knowl).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
