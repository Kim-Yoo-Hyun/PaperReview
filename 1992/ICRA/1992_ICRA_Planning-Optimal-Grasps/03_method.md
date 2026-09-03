# Method - Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (4 The Quality of Grasp)): The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at any point contact.

## Method Body Digest

- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 1 / 2 Working hypotheses - extractive body cue:** In this model, fingers can exert any force pointing into the friction cone at the point of contact.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Hence we have an immediate representation of each point contact force exerted by the fingers.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Then a precise definition for magnitude of the applied forces will be given in the next.
- **p. 1 / 2 Working hypotheses - extractive body cue:** Gripper jaws can exert forces and torques on the grasped objects through the contact points.
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Moreover, it minimizes the power for actuating the gripper.

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** In section four, we introduce and discuss the quality criteria we are proposing.
- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.

## Source Evidence Cues

- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 1 / 2 Working hypotheses - extractive body cue:** In this model, fingers can exert any force pointing into the friction cone at the point of contact.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Hence we have an immediate representation of each point contact force exerted by the fingers.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Then a precise definition for magnitude of the applied forces will be given in the next.
- **p. 1 / 2 Working hypotheses - extractive body cue:** Gripper jaws can exert forces and torques on the grasped objects through the contact points.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case ... | p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | In this model, fingers can exert any force pointing into the friction cone at the point of contact. | p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Hence we have an immediate representation of each point contact force exerted by the fingers. | p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Moreover, it minimizes the power for actuating the gripper.
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Avoiding large forces minimizes the deformation of both the object and the jaws.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Without loss of generality, we choose llwll so that 11g11 = 1.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** We have that the total force is: Minimizing the total Anger force n f =CA i= 1 Every fi is in the friction cone and ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reaction, torque, given, where, vector, pointing, center, mass, object, point, contact, force, applied, course | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | reaction, torque, given, where, vector, pointing, center, mass, object, point | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | section, four, introduce, discuss, quality, criteria, proposing, give, geometric, interpretation | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | first, concerned, finding, grasp, configurations, maximize, wrench, given, independent, force | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Of course, there can still be some directions where the reaction wrench can be greater, but we want to be assured we get a lower ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 2 / 2 Working hypotheses - extractive body cue:** Any force and torque on the object can be represented by a point in the wrench space.
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** In section 2, we mentioned how forces and torques can be represented by points in the wrench space.
- **p. 1 / 2 Working hypotheses - extractive body cue:** Gripper jaws can exert forces and torques on the grasped objects through the contact points.
- **p. 1 / 2 Working hypotheses - extractive body cue:** A grasp is said to be force closure if it is possible to apply forces and torques at the contact points such that any external ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The solution proposed in this paper is more general, and unifies in a general framework the formalization of the optimality criteria. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | This algorithm has to be repeated for each side of the polygon comparing at the end of each step the new minimum ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, concerned, finding, grasp, configurations, maximize, wrench, given, independent, force, limits, minimize, worst-case, applied, point, contact, model, fingers, exert, pointing.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Avoiding large forces minimizes the deformation of both the object and the jaws. | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses) |
| Grasp / trajectory generation | Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large ... | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces) |
| Contact execution / correction | We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this ... | p. 3 (4.1 Representing Anger forces), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Without loss of generality, we choose llwll so that 11g11 = 1.
- **p. 2 / 4.1 Representing Anger forces - extractive body cue:** In general f i is given by a convex combination of forces along the extrema of the friction cone, whose normal component is ft.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (4 The Quality of Grasp), objective p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp), p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), temporal p. 2 (3 Related work), p. 5 (5.1 Two-jaw gripper grasping a polygonal object).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Hence we have an immediate representation of each point contact force exerted by the fingers. (p. 2, 2 Working hypotheses).
- **Objective/update evidence:** Without loss of generality, we choose llwll so that 11g11 = 1. (p. 3, 4.1 Representing Anger forces).
- **Temporal/runtime evidence:** This algorithm has to be repeated for each side of the polygon comparing at the end of each step the new minimum with the previous one and keeping track of ... (p. 5, 5.1 Two-jaw gripper grasping a polygonal object).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
