# Method - Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING)): Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle and 3 as

## Method Body Digest

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** We first define the task-specific interactions based on the task mechanics in Section IV-A.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** Then, we introsuce the formal approach to construct manipulation funnels in perception state space (Section IV-B) and execution task space (Section IV-C),
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** forming an aligned comer between the inclined peg and the target hole to create contact constraints for undesired motion freedoms and progressively enter the allowed ...
- **p. 4 / A. Preliminaries - extractive body cue:** An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - 0) and a ...
- **p. 4 / B. Problem Statement - extractive body cue:** Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** For a task-specific interaction ¢}, the starting state x, and desired state x} is constrained by a common supporting vertex py defined as follows:

## Design Rationale

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.

## Source Evidence Cues

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** We first define the task-specific interactions based on the task mechanics in Section IV-A.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** Then, we introsuce the formal approach to construct manipulation funnels in perception state space (Section IV-B) and execution task space (Section IV-C),
- **Detected method headings:** A. Cartesian Impedance Controller (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as ... | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Interaction with inclined states is designed to identify and exploit its environmental contact constraints. | p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | We first define the task-specific interactions based on the task mechanics in Section IV-A. | p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** forming an aligned comer between the inclined peg and the target hole to create contact constraints for undesired motion freedoms and progressively enter the allowed ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | interaction, command, time, defined, starting, state, considered, steady, desired, Execution, Task, Space, Let, deviation | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | interaction, command, time, defined, starting, state, considered, steady, desired, Execution | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | paired, comer, hole, local, geometry, enables, downstream, iterative, insertion, process | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | forming, aligned, comer, between, inclined, target, hole, create, contact, constraints | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / A. Preliminaries - extractive body cue:** An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - 0) and a ...
- **p. 4 / B. Problem Statement - extractive body cue:** Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of ...
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** For a task-specific interaction ¢}, the starting state x, and desired state x} is constrained by a common supporting vertex py defined as follows:
- **p. 3 / A. Preliminaries - extractive body cue:** The pose of frame {)} with reference to frame {O} at time ¢ is represented as x; = [p:x] < B®, in which P CR' ...
- **p. 3 / A. Preliminaries - extractive body cue:** 3) Compliant Interactions for the Peg: As the peg is in a prism-shaped geometry as defined in Sec.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | ate b> Reset time step for execution | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | bteo © Initialize time step for perception | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 6 / B. Perception Manipulation Funnet - extractive body cue:** Proof: Since Xe is the intersection of 2; with another constraint set gev1(Tyouy) = 0 and {g4(Tyom) = 0} 4 {ae1(Tyouy) > 0} under nonidentical ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Let, represents, positive, direction, Z-axis, reference, inclined, state, angle, Interaction, states, designed, identify, exploit, environmental, contact, constraints, first, define, task-specific.
- **Relevant PDF headings:** A. Cartesian Impedance Controller (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment ... | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area) |
| Grasp / trajectory generation | Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so ... | p. 7 (2 Sample grid points G - Area), p. 11 (Figure/Table caption) |
| Contact execution / correction | Additionally, a maximum entropy-based method is introduced to improve convergence efficiency. | p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area) |

## Failure and Ablation Link

- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; (d) ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting ...
- **p. 8 / 2 Sample grid points G - Area - extractive body cue:** As long as ‘is in contact with the wall, the component of the energy gradient Foyegy that is normal to the wall is canceled out ...
- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** pose +1 automatically falls into its nearby local minimum
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING), objective p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), temporal p. 4 (B. Problem Statement), p. 4 (B. Problem Statement), p. 3 (A. Preliminaries), p. 3 (A. Preliminaries), p. 6 (B. Perception Manipulation Funnet), p. 6 (B. Perception Manipulation Funnet).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
