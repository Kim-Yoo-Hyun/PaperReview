# Method - PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://cdn.aaai.org/ojs/6739/6739-40-9968-1-10-20200522.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1 Introduction), p. 1 (1 Introduction)): Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.

## Method Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine.
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 1 / 1 Introduction - extractive body cue:** The robot must find a sequence of move, pick, and place actions involving continuous variables such as robot configurations, robot trajectories, block poses, and block ...
- **p. 1 / 1 Introduction - extractive body cue:** The declarative component specifies the facts that these input and output values satisfy.
- **p. 1 / 1 Introduction - extractive body cue:** The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values.

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; ...
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...

## Source Evidence Cues

- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as ... | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine. | p. 1 (1 Introduction) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as ... | p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 1 / 1 Introduction - extractive body cue:** The robot must find a sequence of move, pick, and place actions involving continuous variables such as robot configurations, robot trajectories, block poses, and block ...
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 1 (1 Introduction).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | declarative, component, specifies, facts, input, output, values, satisfy, procedural, conditional, generator, function, possibly, infinite | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | declarative, component, specifies, facts, input, output, values, satisfy, procedural, conditional | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | PDDLStream, planning, language, introduces, streams, interface, incorporating, sam-, gratefully, acknowledge | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | enables, algorithm, greedily, search, space, parameter, bindings, more, quickly, solve | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** The declarative component specifies the facts that these input and output values satisfy.
- **p. 1 / 1 Introduction - extractive body cue:** The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | We provide domain-independent algorithms that reduce PDDLStream problems to a sequence of finite PDDL problems. | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

## Method-Specific Formal Details

- **Body-defined terms:** Streams, allow, planner, reason, about, conditions, inputs, outputs, conditional, generator, while, treating, implementation, black, algorithm, constructs, solves, sequence, finite, PDDL.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Search / trajectory decision | The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). | p. 7 (9 Experiments), p. 8 (9 Experiments) |
| Execution interface | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | p. 8 (9 Experiments), p. 8 (9 Experiments) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Left: Domain 1 (with 5 blocks). Right: A real- world robot planning to "serve a meal" on the brown tray. pling procedures in ...
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (Abstract), p. 1 (1 Introduction), temporal p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (2 Related Work), p. 2 (2 Related Work), p. 3 (2 Related Work), p. 4 (2 Related Work).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box. (p. 1, 1 Introduction).
- **Objective/update evidence:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce low-cost solutions. (p. 1, Abstract).
- **Temporal/runtime evidence:** The additional stream binding computation only marginally increases the runtime of Adaptive. (p. 8, 9 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
