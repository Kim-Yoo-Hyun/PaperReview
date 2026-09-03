# Problem - D* Lite

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://idm-lab.org/bib/abstracts/Koen02e.html; PDF retrieval source: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract)): The challenge is to identify these cells efficiently.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Incremental heuristic search methods use heuristics to focus their search and reuse information from previous searches to find solutions to series of similar search tasks ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we apply Lifelong Planning A* to robot navigation in unknown terrain, including goal-directed navigation in unknown terrain and mapping of unknown terrain.
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 1 / Abstract - extractive body cue:** We prove properties about D* Lite and demonstrate experimentally the advantages of combining incremental and heuristic search for the applications studied.
- **p. 2 / Abstract - extractive body cue:** The challenge is to identify these cells efficiently.
- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The challenge is to identify these cells efficiently. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | D* Lite is substantially shorter than D*, uses only one tie-breaking criterion when comparing priorities, which simplifies the maintenance of the priorities, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Lite, substantially, shorter, uses, only, tie-breaking, criterion, when, comparing, priorities | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | However, since, same, vertices, priority, queue, order, does | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Lite, substantially, shorter, uses, only, tie-breaking, criterion, when, comparing, priorities | p. 1 (Abstract), p. 3 (Abstract), p. 5 (Abstract) |
| Decision / output variable | path/waypoint/velocity; body terms: gain, insight, behavior, present, various, theoretical, properties, LPA | p. 1 (Abstract), p. 1 (Abstract), p. 4 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: BRT, RT/, tHUpS, Remove, RT/7S, qZgBh3, Insert, CalculateKey | p. 3 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (Abstract), p. 1 (Abstract), p. 2 (Abstract) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (Abstract), p. 5 (Abstract), p. 5 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **p. 2 / Abstract - extractive body cue:** (It does nothing if the current priority of vertex ] already equals ` .) Finally, U.Remove RT]AS removes vertex ] from priority queue U . ...
- **p. 1 / Abstract - extractive body cue:** It is currently also being integrated into Mars Rover prototypes and tactical mobile robot prototypes for urban reconnaissance (Matthies et al.
- **p. 1 / Abstract - extractive body cue:** Introduction Incremental search methods, such as DynamicSWSF-FP (Ramalingam & Reps 1996), are currently not much used in artificial intelligence.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 1 (Abstract), p. 4 (Abstract)): To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.

- **p. 1 / Abstract - extractive body cue:** Building on LPA*, we therefore present D* Lite, a novel replanning method that implements the same navigation strategy as D* but is algorithmically different.
- **p. 4 / Abstract - extractive body cue:** We now use LPA* to develop D* Lite, that repeatedly determines shortest paths between the current vertex of the robot and the goal vertex as ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | They change to infinity when the robot discovers that they cannot be traversed. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Uniform discretizations can prevent one from finding a path if they are too coarse-grained (for example, because the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | (It does nothing if the current priority of vertex ] already equals ` .) Finally, U.Remove RT]AS removes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | This is similar to what A* can do if it does not use backpointers. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 3 (Abstract), p. 5 (Abstract), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), interface p. 1 (Abstract), p. 3 (Abstract), p. 5 (Abstract), p. 1 (Abstract), objective p. 3 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
