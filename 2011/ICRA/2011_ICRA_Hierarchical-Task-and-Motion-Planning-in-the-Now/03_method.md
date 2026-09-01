# Method - Hierarchical Task and Motion Planning in the Now

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980391; PDF retrieval source: https://doi.org/10.1109/ICRA.2011.5980391. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS)): The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.

## Method Body Digest

- **p. 7 / V. ALGORITHMS - extractive PDF cue:** The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** A motion planner lazily builds a 4-dof visibility-graph; x, y translation constraints are represented as C-space polygons for discrete ranges of z and θ.
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** In the examples in this paper, it was constrained to do translation only and to return a single path.
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p if prim(oi): currentState ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** It makes choices and commits to them, limiting the length of plans and exponentially decreasing the amount of search required. • It operates in the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## Source Evidence Cues

- **p. 7 / V. ALGORITHMS - extractive PDF cue:** The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...
- **Detected method headings:** V. ALGORITHMS (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, ... | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current ... | p. 7 (V. ALGORITHMS) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, ... | p. 7 (V. ALGORITHMS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / V. ALGORITHMS - extractive PDF cue:** A motion planner lazily builds a 4-dof visibility-graph; x, y translation constraints are represented as C-space polygons for discrete ranges of z and θ.
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** In the examples in this paper, it was constrained to do translation only and to return a single path.
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 7 (V. ALGORITHMS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else, PLAN, prim, execute, NEXTLEVEL | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | motion, planner, lazily, builds, visibility-graph, translation, constraints, represented, C-space, polygons | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / V. ALGORITHMS - extractive PDF cue:** HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p if prim(oi): currentState ...
- **p. 7 / V. ALGORITHMS - extractive PDF cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** It makes choices and commits to them, limiting the length of plans and exponentially decreasing the amount of search required. • It operates in the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | So, we simply execute the first abstract step, observe the resulting world state, and then plan in detail for the next one. | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | The complexity of such tasks derives from very long time horizons and large numbers of objects to be considered and manipulated. | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architecture, thought, doing, depth-first, traversal, planning, tree, implemented, recursive, algorithm, below, execution, system, invoked, calling, HPN, currentState, goal, operators, absLevel.
- **Relevant PDF headings:** V. ALGORITHMS (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | The first requires that a swept volume of the robot moving to object a and picking it up be free. | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE) |
| Dynamics / constraint solve | First, it may not be possible to make pn true without undoing p1, . . . , pn-1. | p. 6 (C C), p. 5 (C C) |
| Feedback / actuation | Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the ... | p. 3 (B C), p. 6 (C C) |

## Failure and Ablation Link

- **p. 5 / C C - extractive PDF cue:** In goal regression, when applying an operation to a goal g, the goal fluent and any side effect fluents are always removed from g; in ...
- **p. 2 / III. EXAMPLE - extractive PDF cue:** Because our cost model is still somewhat weak, it chooses to remove b first.
- **p. 2 / III. EXAMPLE - extractive PDF cue:** To remove b from the swept volume, a parking place, shown as PB in figure 3.1, is suggested.
- **p. 6 / C C - extractive PDF cue:** First, it may not be possible to make pn true without undoing p1, . . . , pn-1.
- **p. 3 / B C - extractive PDF cue:** Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it was ...
- **p. 5 / C C - extractive PDF cue:** There is one additional primitive that has no geometric component: Wash() simply causes the washing machine to be run, and any objects that are in ...
- **p. 6 / C C - extractive PDF cue:** Because these variables both have infinite domains in our setting, we cannot enumerate them.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), objective p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), temporal p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 2 (III. EXAMPLE), p. 3 (B C), p. 3 (B C).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
