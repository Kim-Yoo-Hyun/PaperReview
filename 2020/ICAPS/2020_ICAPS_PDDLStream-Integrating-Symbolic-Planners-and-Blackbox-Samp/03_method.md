# Method - PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

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

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
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
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

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
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | We provide domain-independent algorithms that reduce PDDLStream problems to a sequence of finite PDDL problems. | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | The procedural component is a conditional generator, a function from input values to a possibly infinite sequence of output values. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Streams, allow, planner, reason, about, conditions, inputs, outputs, conditional, generator, while, treating, implementation, black, algorithm, constructs, solves, sequence, finite, PDDL.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Search / trajectory decision | The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). | p. 7 (9 Experiments), p. 8 (9 Experiments) |
| Execution interface | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | p. 8 (9 Experiments), p. 8 (9 Experiments) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Left: Domain 1 (with 5 blocks). Right: A real- world robot planning to "serve a meal" on the brown tray. pling procedures in ...
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (Abstract), p. 1 (1 Introduction), temporal p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (2 Related Work), p. 2 (2 Related Work), p. 3 (2 Related Work), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
