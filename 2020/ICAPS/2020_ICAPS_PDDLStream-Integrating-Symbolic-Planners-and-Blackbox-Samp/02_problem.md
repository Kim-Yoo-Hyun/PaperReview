# Problem - PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Many planning applications involve complex relationships defined on high-dimensional, continuous variables.
- **p. 1 / Abstract - extractive body cue:** For example, robotic manipulation requires planning with kinematic, collision, visibility, and motion constraints involving robot configurations, object poses, and robot trajectories.
- **p. 1 / Abstract - extractive body cue:** These constraints typically require specialized procedures to sample satisfying values.
- **p. 1 / Abstract - extractive body cue:** We extend PDDL to support a generic, declarative specification for these procedures that treats their implementation as black boxes.
- **p. 1 / Abstract - extractive body cue:** We provide domain-independent algorithms that reduce PDDLStream problems to a sequence of finite PDDL problems.
- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Adaptive greatly outperforms the two existing algorithms (Garrett, Lozano-P´erez, and Kaelbling 2018) on constrained and 440

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | The declarative component specifies the facts that these input and output values satisfy. | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | declarative, component, specifies, facts, input, output, values, satisfy, procedural, conditional | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | PDDLStream, planning, language, introduces, streams, interface, incorporating, sam- | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: declarative, component, specifies, facts, input, output, values, satisfy, procedural, conditional | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: PDDLStream, planning, language, introduces, streams, interface, incorporating, sam- | p. 1 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: enables, algorithm, greedily, search, space, parameter, bindings, more | p. 1 (Abstract), p. 1 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 1 (1 Introduction) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 8 (Figure/Table caption), p. 7 (9 Experiments), p. 8 (9 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Adaptive greatly outperforms the two existing algorithms (Garrett, Lozano-P´erez, and Kaelbling 2018) on constrained and 440

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 1 (Abstract)): We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ...

- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (Abstract), p. 1 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
