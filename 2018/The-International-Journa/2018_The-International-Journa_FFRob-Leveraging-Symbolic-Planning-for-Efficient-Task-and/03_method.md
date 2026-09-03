# Method - FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://journals.sagepub.com/doi/10.1177/0278364917739114; PDF retrieval source: https://journals.sagepub.com/doi/10.1177/0278364917739114. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 3 (1.1 Approach)): We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.

## Method Body Digest

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** EAS is able to represent actions with complex conditions much more concisely than a traditional symbolic planning representation.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.
- **p. 2 / 1.1 Approach - extractive body cue:** We model task and motion planning as symbolic planning where the conditions of actions are complex predicates involving geometric and kinematic constraints.
- **p. 2 / 1.1 Approach - extractive body cue:** The key computational benefit of the approach is that it is able to incorporate geometric and kinematic constraints in the heuristic to strongly guide the ...
- **p. 1 / 1 Introduction - extractive body cue:** 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces.
- **p. 2 / 1.1 Approach - extractive body cue:** This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.

## Design Rationale

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** The primary contribution of this paper is FFROB, an efficient and probabilistically complete algorithm for fully integrated task and motion planning.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.

## Source Evidence Cues

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** EAS is able to represent actions with complex conditions much more concisely than a traditional symbolic planning representation.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.
- **Detected method headings:** 1.1 Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. | p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | EAS is able to represent actions with complex conditions much more concisely than a traditional symbolic planning representation. | p. 2 (1.1 Approach), p. 3 (1.1 Approach) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance. | p. 3 (1.1 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1.1 Approach - extractive body cue:** We model task and motion planning as symbolic planning where the conditions of actions are complex predicates involving geometric and kinematic constraints.
- **p. 2 / 1.1 Approach - extractive body cue:** The key computational benefit of the approach is that it is able to incorporate geometric and kinematic constraints in the heuristic to strongly guide the ...
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (1.1 Approach), p. 2 (1.1 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | have, been, tackling, problems, require, long, sequences, actions, large, discrete, state-spaces, involves, batch, sampling | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | have, been, tackling, problems, require, long, sequences, actions, large, discrete | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | introduce, Extended, Action, Specification, EAS, symbolic, planing, representation, supports, complex | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | model, task, motion, planning, symbolic, where, conditions, actions, complex, predicates | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces.
- **p. 2 / 1.1 Approach - extractive body cue:** This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions.
- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | The probability that FFROB has not identified a solution contained in the minimal length robust set of mode sequences decreases exponentially in ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | An algorithm is exponentially convergent over a class of problems if and only if the probability that the algorithm has not terminated ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | Each problem and algorithm combination was simulated over 50 trials. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, Extended, Action, Specification, EAS, symbolic, planing, representation, supports, complex, conditions, able, represent, actions, much, more, concisely, traditional, planning, Finally.
- **Relevant PDF headings:** 1.1 Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single ... | p. 30 (11 Experiments), p. 30 (11 Experiments) |
| Search / trajectory decision | The following heuristics are compared in the experiments: 1. | p. 29 (11 Experiments), p. 30 (11 Experiments) |
| Execution interface | HF F Rob, HA gave the best performance in both success rate and runtime. | p. 30 (11.4 Results), p. 30 (11.4 Results) |

## Failure and Ablation Link

- **p. 17 / Figure/Table caption - extractive body cue:** Figure 15. A star-graph CRG visualized using end-effector poses. PATH(q, q′; (V, E)) (without considering any placed or held objects). In practice, we only create ...
- **p. 30 / 11 Experiments - extractive body cue:** This allows a large number of placements to be created for constrained problems without greatly increasing the branching factor.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. The FFROB algorithm. 5.1 Extended Action Specification We model discretized PPM problems using a rep- resentation that extends Simple Action Specification (SAS+) (B¨ackstr¨om ...
- **p. 32 / Figure/Table caption - extractive body cue:** Figure 27. Best-first search extract and process procedures. A.2 Deferred Best-First Search Deferred best-first search (also called lazy greedy search) is a variant of standard ...
- **p. 30 / 11 Experiments - extractive body cue:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.
- **p. 30 / 11 Experiments - extractive body cue:** We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures.
- **p. 33 / B.1 Proof of Theorem 1 - extractive body cue:** Finally, each segment from q0 to q0 ∈B0 or from q∗to qk ∈Bk is collision-free by the problem being robustly feasible.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 3 (1.1 Approach), objective p. 2 (1.1 Approach), p. 2 (1.1 Approach), temporal p. 27 (A PPM), p. 18 (A PPM), p. 18 (A PPM), p. 24 (A PPM), p. 27 (A PPM), p. 30 (11 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. (p. 2, 1.1 Approach).
- **Objective/update evidence:** We model task and motion planning as symbolic planning where the conditions of actions are complex predicates involving geometric and kinematic constraints. (p. 2, 1.1 Approach).
- **Temporal/runtime evidence:** 11.3 Implementation We implemented FFROB in Python using the OpenRAVE robotics framework (Diankov and Kuffner 2008) for simulation. (p. 30, 11 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
