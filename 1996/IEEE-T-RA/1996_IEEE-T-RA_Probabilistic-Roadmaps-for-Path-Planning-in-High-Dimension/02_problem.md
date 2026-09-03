# Problem - Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://kavrakilab.rice.edu/publications/kavraki-svestka1996probabilistic-roadmaps-for.html; PDF retrieval source: https://kavrakilab.org/publications/kavraki-svestka1996probabilistic-roadmaps-for.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction), p. 2 (I. RELATION 70 Previous Work), p. 2 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction)): However, while building the roadmap, our method heuristically identifies "difficult" regions in free C-space and generates additional configurations in those regions to increase network connectivity.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A new motion planning method for robots in static workspaces is presented.
- **p. 1 / Abstract - extractive body cue:** This method proceeds in two phases: 4 earning phase and a query phase.
- **p. 1 / Abstract - extractive body cue:** In the learning: phase, a probabilistic readmap is constructed and stored as a graph whose odes correspond to collison-free configurations and whose edges ‘correspond to ...
- **p. 1 / Abstract - extractive body cue:** These paths are computed using a simple and fast local planner.
- **p. 1 / Abstract - extractive body cue:** In ‘the query phase, any given start and goal configurations of the robot are connected to two nodes of the roadmap: the roadmap is, ‘then ...
- **p. 3 / I. RELATION 70 Previous Work - extractive body cue:** However, while building the roadmap, our method heuristically identifies "difficult" regions in free C-space and generates additional configurations in those regions to increase network connectivity.
- **p. 1 / 1. IntRopuction - extractive body cue:** ‘We have demonstrated the power of our method by applying it to a number of difficult motion planning problems involving ‘variety of robots.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, while building the roadmap, our method heuristically identifies "difficult" regions in free C-space and generates additional configurations in those regions to ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | During the query phase, paths are to be found between arbitrary input start and goal configurations, using the roadmap constructed in the ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | During, query, phase, paths, found, between, arbitrary, input, start, goal | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | Experimental, path, planning, done, fraction, second, contemporary, workstation | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: During, query, phase, paths, found, between, arbitrary, input, start, goal | p. 6 (B. The Query Phase), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: emphasizes, efficiency, primarily, developed, robots, many, dofs, move | p. 3 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction), p. 1 (1. IntRopuction) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: objective, former, obtain, reasonably, connected, graph, enough, vertices | p. 4 (A. The Learning Phase), p. 8 (IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS), p. 4 (6) N.- a set of candidate neighbors), p. 5 (6) N.- a set of candidate neighbors), p. 5 (6) N.- a set of candidate neighbors) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS), p. 2 (I. RELATION 70 Previous Work), p. 2 (I. RELATION 70 Previous Work) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 12 (VI. RESULTS WITH GENERAL IMPLEMENTATION), p. 11 (VI. RESULTS WITH GENERAL IMPLEMENTATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. IntRopuction - extractive body cue:** ‘We have demonstrated the power of our method by applying it to a number of difficult motion planning problems involving ‘variety of robots.
- **p. 2 / I. RELATION 70 Previous Work - extractive body cue:** Our roadmap planner deals efficiently with problems that are difficult for RPP, as discussed in Section V.
- **p. 2 / I. RELATION 70 Previous Work - extractive body cue:** It has been successfully experimented on difficult problems involving robots with 3 10 31 dofs, It has also bbeen used in practice with good results ...
- **p. 1 / 1. IntRopuction - extractive body cue:** Instead, they can be interwoven to adapt the size of the roadmap to difficulties encountered during the query phase, thus increasing the learning flavor of ...

## What the Paper Changes

PDF body contribution framing (p. 3 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction), p. 1 (1. IntRopuction), p. 2 (1. IntRopuction), p. 3 (I. RELATION 70 Previous Work)): Our method emphasizes efficiency and is primarily developed for robots with many dofs which move in static ‘environments.

- **p. 1 / 1. IntRopuction - extractive body cue:** ‘We have demonstrated the power of our method by applying it to a number of difficult motion planning problems involving ‘variety of robots.
- **p. 1 / 1. IntRopuction - extractive body cue:** Moreover, increased efficiency can be achieved by tailoring several components of our method, in particular the local planner, to the considered robots.
- **p. 2 / 1. IntRopuction - extractive body cue:** Next, in Sections IV-VI we apply four method to planar articulated robots.
- **p. 3 / I. RELATION 70 Previous Work - extractive body cue:** Instead, our method applies a roadmap approach 134), that is, it constructs a network of paths in free Cspace.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Unlike the ‘customized implementation, this implementation does not use any specific techniques for local path planning, collision ‘checking, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | The collision checker in [44] considers successive approximations of the objects and, its running time, on the average, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | The actual number of collision checks for connecting C;,...,Cs of Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | (1); and collision checking is done analytically, using routines from the PLAGEO library [19]. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (B. The Query Phase), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 2 (1. IntRopuction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction), p. 2 (I. RELATION 70 Previous Work), p. 2 (I. RELATION 70 Previous Work), p. 1 (1. IntRopuction), interface p. 6 (B. The Query Phase), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 2 (1. IntRopuction), objective p. 4 (A. The Learning Phase), p. 8 (IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS), p. 4 (6) N.- a set of candidate neighbors), p. 5 (6) N.- a set of candidate neighbors), p. 5 (6) N.- a set of candidate neighbors).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** ‘We have demonstrated the power of our method by applying it to a number of difficult motion planning problems involving ‘variety of robots. (p. 1, 1. IntRopuction).
- **Formulation-changing contribution:** ‘We have demonstrated the power of our method by applying it to a number of difficult motion planning problems involving ‘variety of robots. (p. 1, 1. IntRopuction).
- **Assumption/failure evidence:** We have observed that in cases when the above motion does not manage to connect configurations a and 6, it nevertheless brings the robot to a configuration b' very close ... (p. 8, IV. APPLICATION 10 PLANAR ARTICULATED ROBOTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
