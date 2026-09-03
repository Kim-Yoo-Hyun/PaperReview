# Problem - Sampling-based Algorithms for Optimal Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (76 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1105.1186; PDF retrieval source: https://arxiv.org/pdf/1105.1186. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and failure otherwise.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in ...
- **p. 1 / Abstract - extractive body cue:** However, little effort has been devoted to the formal analysis of the quality of the solution returned by such algorithms, e.g., as a function of ...
- **p. 1 / Abstract - extractive body cue:** The purpose of this paper is to fill this gap, by rigorously analyzing the asymptotic behavior of the cost of the solution returned by stochastic ...
- **p. 1 / Abstract - extractive body cue:** A number of negative results are provided, characterizing existing algorithms, e.g., showing that, under mild technical conditions, the cost of the solution returned by broadly ...
- **p. 1 / Abstract - extractive body cue:** The main contribution of the paper is the introduction of new algorithms, namely, PRM∗and RRT∗, which are provably asymptotically optimal, i.e., such that the cost ...
- **p. 1 / 1 Introduction - extractive body cue:** An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and ...
- **p. 6 / 1 Introduction - extractive body cue:** The feasibility problem of path planning is to find a feasible path, if one exists, and report failure otherwise: Problem 2 (Feasible path planning) Given ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | Informally, speaking, given, robot, description, dynamics, environment, initial, state, goal | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | Input, output, data, same, algorithms, introduced, Section, Informally | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: Informally, speaking, given, robot, description, dynamics, environment, initial, state, goal | p. 1 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: early, seminal, papers, incremental, samplingbased, motion, planning, algorithms | p. 4 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: example, interested, solution, paths, minimum, cost, respect, given | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 61 (Figure/Table caption), p. 17 (Figure/Table caption), p. 33 (V RRT∗) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 6 / 1 Introduction - extractive body cue:** The feasibility problem of path planning is to find a feasible path, if one exists, and report failure otherwise: Problem 2 (Feasible path planning) Given ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, the rate of decay of the probability of failure is exponential, under the assumption that the environment has good "visibility" properties (Barraquand et al., ...
- **p. 2 / 1 Introduction - extractive body cue:** Even though these algorithms are not complete, they provide probabilistic completeness guarantees in the sense that the probability that the planner fails to return a ...
- **p. 3 / 1 Introduction - extractive body cue:** The RRT algorithm has been shown to be probabilistically complete (Kuffner and LaValle, 2000), with an exponential rate of decay for the probability of failure ...

## What the Paper Changes

PDF body contribution framing (p. 4 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the focus of the paper is ...

- **p. 11 / 1 Introduction - extractive body cue:** In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among n randomly-sampled points in Xfree, ...
- **p. 13 / 1 Introduction - extractive body cue:** Algorithm 3: RRT 1 V ←{xinit}; E ←∅; 2 for i = 1, . . . , n do 3 xrand ←SampleFreei; 4 xnearest ←Nearest(G ...
- **p. 2 / 1 Introduction - extractive body cue:** Important contributions towards broader applicability of these methods include navigation functions (Rimon and Koditschek, 1992) and randomization (Barraquand and Latombe, 1993).
- **p. 4 / 1 Introduction - extractive body cue:** A summary of the contributions can be found below, and is shown in Table 1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 35 | In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | First, each algorithm is analyzed in terms of the number of calls to the CollisionFree procedure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | Number of calls to the CollisionFree procedure Let MALG n denote the total number of calls to the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 1 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction), p. 2 (1 Introduction), objective p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
