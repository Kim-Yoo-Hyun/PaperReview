# Problem - Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Because of their intricate design, they are difficult to control and plan.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper we will address the problem of planning optimal grasps.
- **p. 1 / Abstract - extractive body cue:** Two general optimality criteria, that consider the total finger force and the maximum finger force will be introduced and discussed.
- **p. 1 / Abstract - extractive body cue:** Moreover their formalization, using various metrics on a space of generalized forces, will be detailed.
- **p. 1 / Abstract - extractive body cue:** The geometric interpretation of the two criteria will lead to an efficient planning algorithm.
- **p. 1 / Abstract - extractive body cue:** An example of its use in a robotic environment equipped with two-jaw and three-jaw grippers will also be shown.
- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan.
- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Because of their intricate design, they are difficult to control and plan.
| Observation / input | The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass ... | 물체 형상·접촉점·마찰·허용 손가락 힘 | exact sensor/frame/preprocessing from PDF body |
| State / latent | reaction, torque, given, where, vector, pointing, center, mass, object, point | 접촉 힘과 토크가 만드는 렌치 집합 | notation and tensor shape require body check |
| Output / action | case, state, hypothesis, magnitude, forces, contact, points, upper-bounded | 품질 기준에 따라 고른 그리퍼 파지 | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | 힘 예산별 외력 저항과 파지 품질 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | 물체 형상·접촉점·마찰·허용 손가락 힘; body terms: reaction, torque, given, where, vector, pointing, center, mass, object, point | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Decision / output variable | 품질 기준에 따라 고른 그리퍼 파지; body terms: section, four, introduce, discuss, quality, criteria, proposing, give | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | 힘 예산별 외력 저항과 파지 품질; cue terms: first, concerned, finding, grasp, configurations, maximize, wrench, given | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Success / guarantee | completion, contact success and robustness | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): In section four, we introduce and discuss the quality criteria we are proposing.

- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine ... | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

물체 형상·접촉점·마찰·허용 손가락 힘 → 접촉 힘과 토크가 만드는 렌치 집합 → 품질 기준에 따라 고른 그리퍼 파지. [원문 근거](./01_overview.md#observation-state-and-output-interface)

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses), objective p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces).

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Because of their intricate design, they are difficult to control and plan. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** In section four, we introduce and discuss the quality criteria we are proposing. (p. 1, 1 Introduction).
- **Assumption/failure evidence:** In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
