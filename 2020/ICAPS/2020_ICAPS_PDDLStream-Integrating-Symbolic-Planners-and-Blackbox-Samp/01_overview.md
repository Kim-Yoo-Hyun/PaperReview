# PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739.
> PDF retrieval source: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ICAPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, task and motion planning, symbolic planning, sampling, manipulation planning
- Official paper: https://ojs.aaai.org/index.php/ICAPS/article/view/6739
- Full-text retrieval: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593
- Code/Project: https://github.com/caelan/pddlstream
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.를 문제로 두고, We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ONR grant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Many planning applications involve complex relationships defined on high-dimensional, continuous variables.
- **p. 1 / Abstract - extractive body cue:** For example, robotic manipulation requires planning with kinematic, collision, visibility, and motion constraints involving robot configurations, object poses, and robot trajectories.
- **p. 1 / Abstract - extractive body cue:** These constraints typically require specialized procedures to sample satisfying values.
- **p. 1 / Abstract - extractive body cue:** We extend PDDL to support a generic, declarative specification for these procedures that treats their implementation as black boxes.
- **p. 1 / Abstract - extractive body cue:** We provide domain-independent algorithms that reduce PDDLStream problems to a sequence of finite PDDL problems.
- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Adaptive greatly outperforms the two existing algorithms (Garrett, Lozano-P´erez, and Kaelbling 2018) on constrained and 440

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; ...
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The declarative component specifies the facts that these input and output values satisfy. | start/goal, map, dynamics와 successor/operator description | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | declarative, component, specifies, facts, input, output, values, satisfy, procedural, conditional, generator, function | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values. | feasible action sequence 또는 minimum-cost plan | p. 1 (1 Introduction) |
| Objective/outcome | This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce low-cost solutions. | path cost, goal reachability, feasibility와 computation | p. 1 (Abstract), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; ...
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan.
- **p. 8 / 9 Experiments - extractive body cue:** Focused, Binding, and Adaptive all outperform Incremental and perform about equivalently due to the less geometrically constrained nature of the domain.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Embodiment/environment | 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. | hardware/simulator version and reset protocol | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Dataset/benchmark | 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. | role, split, size and leakage | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Metric | Figure 4: From left to right: Domain 3 success percent, Domain 3 mean runtime, and plan cost over time for Domain 2. evaluation time. An open-source Python implementation is available at https://github.com/caelan/pddlstream. ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 7 (9 Experiments), p. 8 (9 Experiments) |
| Baseline/ablation | The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). | fair input/data/compute/action matching | p. 7 (9 Experiments), p. 8 (9 Experiments), p. 8 (9 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.를 문제로 두고, We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ONR grant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 8 (9 Experiments), p. 8 (9 Experiments) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box. (p. 1, 1 Introduction).
- **Actual contribution:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ... (p. 1, 1 Introduction).
- **Evaluation boundary:** The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments).
- **Explicit failure boundary:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. (p. 8, 9 Experiments).
