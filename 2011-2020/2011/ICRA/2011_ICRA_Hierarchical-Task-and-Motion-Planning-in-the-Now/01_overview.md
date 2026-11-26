# Hierarchical Task and Motion Planning in the Now

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ICRA.2011.5980391.
> PDF retrieval source: https://doi.org/10.1109/ICRA.2011.5980391. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / ICRA
- Authors: Leslie Pack Kaelbling, Tomas Lozano-Perez
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://api.crossref.org/works/10.1109/ICRA.2011.5980391
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391) 기준이다.

## Why This Paper Is Here

Kaelbling과 Lozano-Pérez는 긴 조작 과제에서 기호적 결정과 연속 기하 경로를 계층적으로 계획하며 필요한 단계부터 실행한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper we outline an approach to the integration of task planning and motion planning that has the following key properties: It is aggressively ...
- **p. 1 / Abstract - extractive body cue:** It operates on detailed, continuous geometric representations and does not require a-priori discretization of the state or action spaces.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As robots become more physically robust and capable of sophisticated sensing, navigation, and manipulation, we want them to carry out increasingly complex tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A robot that helps in a household must plan over the scale of hours or days, considering abstract features such as the desires of the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of such tasks derives from very long time horizons and large numbers of objects to be considered and manipulated.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## Core Idea

- **p. 7 / V. ALGORITHMS - extractive body cue:** The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- **p. 7 / V. ALGORITHMS - extractive body cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...

## Observation, State, and Output Interface

HPN은 술어 목표를 회귀 탐색하고 파지·경로 계획을 호출하며 필요한 부분을 실행 중 구체화한다. 세척·보관과 장애물 재배치 예제로 심볼릭 계획과 기하학적 가능성을 분석한다. 실물 로봇 시험을 근거로 삼지 않는다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=5) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=7)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p if prim(oi): currentState = world.execute(oi) else HPN(currentState, ... | 초기 상태·목표 술어·기하 모델·연산자 | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| State/latent | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else, PLAN, prim | 추상 수준별 부분 계획과 물체의 점유 공간 | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION) |
| Output/action | The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; goal is a conjunction of fluents describing ... | 실행할 파지·이동·놓기 동작 | p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | A motion planner lazily builds a 4-dof visibility-graph; x, y translation constraints are represented as C-space polygons for discrete ranges of z and θ. | 계획의 타당성 및 실행 중 필요한 탐색 | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |

## Main Claims and Actual Contribution

- 물체 재배치와 충돌 회피를 연속 기하 조건으로 표현하고 추상적인 행동을 필요한 수준까지 세분화한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=5)
- 통합 계획 및 실행 알고리즘을 기술하고 조작 장면에서 계획에 들이는 계산량과 행동 선택을 조사했다. [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5980391#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (B C), p. 6 (C C) |
| Embodiment/environment | The first requires that a swept volume of the robot moving to object a and picking it up be free. | hardware/simulator version and reset protocol | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE) |
| Dataset/benchmark | Washing domain, in which the robot must move object A to the washing area, wash it, and put it in the storage area. tree we have constructed. | role, split, size and leakage | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE), p. 3 (B C), p. 3 (IV. REPRESENTATION) |
| Metric | To operate in infinite domains, we augment the standard operator descriptions with the following features: Suggesters, which are procedures that map current start and goal states, and bindings of other variables, to ... | definition, denominator, direction and uncertainty | p. 5 (C C), p. 2 (III. EXAMPLE), p. 5 (C C) |
| Baseline/ablation | First, it may not be possible to make pn true without undoing p1, . . . , pn-1. | fair input/data/compute/action matching | p. 6 (C C), p. 5 (C C), p. 2 (III. EXAMPLE) |

## Explicit Limitations and Failure Boundary

- **p. 6 / C C - extractive body cue:** Because these variables both have infinite domains in our setting, we cannot enumerate them.
- **p. 6 / C C - extractive body cue:** If at attempt at serializing operations at an abstract level fails, then the planning problem is
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there is no collision with taboo regions, and ...
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of the regions in Taboos.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 7 (V. ALGORITHMS), p. 3 (B C), p. 6 (C C)이다.
