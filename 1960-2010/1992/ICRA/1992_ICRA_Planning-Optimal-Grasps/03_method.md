# Method - Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

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

물체 형상·접촉점·마찰·허용 손가락 힘 → 접촉 힘과 토크가 만드는 렌치 집합 → 품질 기준에 따라 고른 그리퍼 파지. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Moreover, it minimizes the power for actuating the gripper.
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Avoiding large forces minimizes the deformation of both the object and the jaws.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Without loss of generality, we choose llwll so that 11g11 = 1.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** We have that the total force is: Minimizing the total Anger force n f =CA i= 1 Every fi is in the friction cone and ...
- **Formal bridge:** 물체 형상·접촉점·마찰·허용 손가락 힘 → 접촉 힘과 토크가 만드는 렌치 집합 → 품질 기준에 따라 고른 그리퍼 파지.
- **Equation/algorithm anchors:** p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reaction, torque, given, where, vector, pointing, center, mass, object, point, contact, force, applied, course | 물체 형상·접촉점·마찰·허용 손가락 힘 | body cue; exact tensor/frame verify |
| State/latent | reaction, torque, given, where, vector, pointing, center, mass, object, point | 접촉 힘과 토크가 만드는 렌치 집합 | body cue; notation verify |
| Action/output | section, four, introduce, discuss, quality, criteria, proposing, give, geometric, interpretation | 품질 기준에 따라 고른 그리퍼 파지 | body cue; unit/decoder verify |
| Objective/constraint | first, concerned, finding, grasp, configurations, maximize, wrench, given, independent, force | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Of course, there can still be some directions where the reaction wrench can be greater, but we want to be assured we get a lower ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 2 / 2 Working hypotheses - extractive body cue:** Any force and torque on the object can be represented by a point in the wrench space.
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** In section 2, we mentioned how forces and torques can be represented by points in the wrench space.
- **p. 1 / 2 Working hypotheses - extractive body cue:** Gripper jaws can exert forces and torques on the grasped objects through the contact points.
- **p. 1 / 2 Working hypotheses - extractive body cue:** A grasp is said to be force closure if it is possible to apply forces and torques at the contact points such that any external ...
- **Normalized interface:** observation=물체 형상·접촉점·마찰·허용 손가락 힘; state=접촉 힘과 토크가 만드는 렌치 집합; output/action=품질 기준에 따라 고른 그리퍼 파지.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | The solution proposed in this paper is more general, and unifies in a general framework the formalization of the optimality criteria. | episode/sequence/action-chunk boundary |
| Rate / latency | This algorithm has to be repeated for each side of the polygon comparing at the end of each step the new minimum ... | Hz/fps, inference time and control rate |
| Memory | not stated or recoverable in the selected PDF body | window and reset |
| Compute | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

## Method-Specific Formal Details

- **Body-defined terms:** first, concerned, finding, grasp, configurations, maximize, wrench, given, independent, force, limits, minimize, worst-case, applied, point, contact, model, fingers, exert, pointing.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | Avoiding large forces minimizes the deformation of both the object and the jaws. | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses) |
| 원문 대조 | Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large ... | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces) |
| 원문 대조 | We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this ... | p. 3 (4.1 Representing Anger forces), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Without loss of generality, we choose llwll so that 11g11 = 1.
- **p. 2 / 4.1 Representing Anger forces - extractive body cue:** In general f i is given by a convex combination of forces along the extrema of the friction cone, whose normal component is ft.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (4 The Quality of Grasp), objective p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp), p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), temporal p. 2 (3 Related work), p. 5 (5.1 Two-jaw gripper grasping a polygonal object).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Hence we have an immediate representation of each point contact force exerted by the fingers. (p. 2, 2 Working hypotheses).
- **Objective/update evidence:** Without loss of generality, we choose llwll so that 11g11 = 1. (p. 3, 4.1 Representing Anger forces).
- **Temporal/runtime evidence:** This algorithm has to be repeated for each side of the polygon comparing at the end of each step the new minimum with the previous one and keeping track of ... (p. 5, 5.1 Two-jaw gripper grasping a polygonal object).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
