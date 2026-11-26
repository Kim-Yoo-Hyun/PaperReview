# Planning Optimal Grasps

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.1992.219918.
> PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1992 / ICRA
- Authors: C. Ferrari, J. Canny
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Grasp Planning, manipulation, contact, analytic grasp metric
- Official paper: https://api.crossref.org/works/10.1109/ROBOT.1992.219918
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918) 기준이다.

## Why This Paper Is Here

Ferrari와 Canny는 접촉이 가할 수 있는 힘과 토크를 이용해 외란에 견디는 파지의 품질을 정량화한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper we will address the problem of planning optimal grasps.
- **p. 1 / Abstract - extractive body cue:** Two general optimality criteria, that consider the total finger force and the maximum finger force will be introduced and discussed.
- **p. 1 / Abstract - extractive body cue:** Moreover their formalization, using various metrics on a space of generalized forces, will be detailed.
- **p. 1 / Abstract - extractive body cue:** The geometric interpretation of the two criteria will lead to an efficient planning algorithm.
- **p. 1 / Abstract - extractive body cue:** An example of its use in a robotic environment equipped with two-jaw and three-jaw grippers will also be shown.
- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan.
- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** In section four, we introduce and discuss the quality criteria we are proposing.
- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 1 / 2 Working hypotheses - extractive body cue:** In this model, fingers can exert any force pointing into the friction cone at the point of contact.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Hence we have an immediate representation of each point contact force exerted by the fingers.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Then a precise definition for magnitude of the applied forces will be given in the next.

## Observation, State, and Output Interface

마찰 접촉의 힘·토크 공간에서 볼록껍질로 파지 품질을 계산한다. 두 턱·세 턱 그리퍼의 평면 파지를 기하학적으로 선택한다. 접촉력은 계산 변수이며 힘 센서 측정이나 전신 제어 실험이 아니다. [PDF 2쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=2) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=6)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object to the point contact where the force ... | 물체 형상·접촉점·마찰·허용 손가락 힘 | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces) |
| State/latent | reaction, torque, given, where, vector, pointing, center, mass, object, point, contact, force | 접촉 힘과 토크가 만드는 렌치 집합 | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Output/action | Of course, there can still be some directions where the reaction wrench can be greater, but we want to be assured we get a lower bound over all directions. | 품질 기준에 따라 고른 그리퍼 파지 | p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses) |
| Objective/outcome | The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at any point contact. | 힘 예산별 외력 저항과 파지 품질 | p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp), p. 2 (4 The Quality of Grasp) |

## Main Claims and Actual Contribution

- 손가락 힘의 합과 각 손가락의 최대 힘을 각각 제한할 때 가능한 일반화 힘의 집합을 기하학적으로 구성한다. [PDF 2쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=2) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=4)
- 품질 기준의 기하적 해석을 파지 계획에 적용해 두 턱 및 세 턱 그리퍼의 평면 물체 사례를 제시했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=219918#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (4.1 Representing Anger forces) |
| Embodiment/environment | Avoiding large forces minimizes the deformation of both the object and the jaws. | hardware/simulator version and reset protocol | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses) |
| Dataset/benchmark | Given a grasp configuration (i.e. a set of point contacts on the object), Q is defined as follows: Q = minLQw W We take the minimum because we usually have no control ... | role, split, size and leakage | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses), p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces) |
| Metric | Without loss of generality, we choose llwll so that 11g11 = 1. | definition, denominator, direction and uncertainty | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Baseline/ablation | Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. | fair input/data/compute/action matching | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Because of their intricate design, they are difficult to control and plan.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (6 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Because of their intricate design, they are difficult to control and plan. (p. 1, 1 Introduction).
- **Actual contribution:** In section four, we introduce and discuss the quality criteria we are proposing. (p. 1, 1 Introduction).
- **Evaluation boundary:** Figure 1: Graphic Evaluation of the Quality Criteria 5 An Example of Using the Quality Criteria In the next subsections, we will present an algo- rithm that can evaluate the ... (p. 5, Figure/Table caption).
- **Explicit failure boundary:** In a force closure grasp, finger locations do not change to counter external forces. (p. 1, 2 Working hypotheses).
