# Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://hal.science/lirmm-00831097.
> PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2013 / T-RO
- Authors: Layale Saab, Oscar Efrain Ramos Ponce, François Keith, Nicolas Mansard, Philippe Souères, Jean-Yves Fourquet
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, whole-body control, rigid contact, hierarchical control, inverse dynamics
- Official paper: https://hal.science/lirmm-00831097
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266
- Code/Project: not identified
- DOI: 10.1109/tro.2012.2234351 [IEEE 게재 기록](https://ieeexplore.ieee.org/document/6482266)
- 판본: 이번 요약은 IEEE 게재본 17쪽 기준이다. 9월에 작성한 발췌는 HAL 보관본 18쪽 기준이다. 게재본의 둘째 저자는 Oscar E. Ramos로 표기된다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=1)
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Saab 등은 다수 접촉과 등식·부등식 제약이 있는 휴머노이드의 전신 동역학 과제를 엄격한 우선순위로 푼다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=1)

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** The most widely-used technique to generate wholebody motions on a humanoid robot accounting for various tasks and constraints is the inverse kinematics.
- **p. 2 / Abstract - extractive body cue:** Based on the taskfunction approach, this class of methods makes possible the coordination of the robot movements to execute several tasks in parallel and account ...
- **p. 2 / Abstract - extractive body cue:** To some extent, it also enables dealing with some of the robot constraints (e.g. joint limits or visibility) and managing the quasi-static balance of the ...
- **p. 2 / Abstract - extractive body cue:** In order to fully use the whole range of possible motions, this paper proposes to extend the task-function approach to handle the full dynamics of ...
- **p. 2 / Abstract - extractive body cue:** The definition of multiple objectives is made possible by ordering them inside a strict hierarchy.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, inequality constraints cannot be taken into account explicitly.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The motion manifold cannot be sampled directly but by projection [10].

## Core Idea

- **p. 3 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Finally, the complete HQP for n contacts and k tasks is written: (39) ≺(22.1) ≺(38.1) ≺... ≺(22.n) ≺(38.n) ≺ (14.1) ≺... ≺(14.k) ≺(40), with the ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 8 of motion (22) [40].
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It also eases the use of sensory feedback, since the sensory space is often a good task-space candidate [14], [15]. | proprioception, reference pose/motion, visual or language command | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| State/latent | eases, sensory, feedback, since, space, often, good, task-space, candidate, notation, necessary, sufficient | whole-body pose, balance/contact state와 skill/mode | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION) |
| Output/action | Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of the complementary condition, i.e. no take off) ... | joint/whole-body action, motion target 또는 task trajectory | p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Objective/outcome | Elastic contact can be defined by modifying the equation 8Similarly, the constraint can be imposed on a least-square τ. | tracking, balance, skill/task success와 recovery | p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |

## Main Claims and Actual Contribution

- 강체 평면 접촉이 유지되는 조건을 이용해 역동역학 문제의 차원을 줄이고 단방향 접촉 제약을 포함한다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=4) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=6)
- 시뮬레이션의 복수 접촉 동작과 실물 HRP-2 실험을 통해 작업 순위와 접촉 조건이 있는 전신 운동을 평가한다. [PDF 11쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=11) · [PDF 13쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=6482266#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |
| Embodiment/environment | The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics. | hardware/simulator version and reset protocol | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS) |
| Dataset/benchmark | A tracking task is imposed to the robot head to make it oscillate. | role, split, size and leakage | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |
| Metric | However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies on the accuracy of the force variables. | definition, denominator, direction and uncertainty | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |
| Baseline/ablation | All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques. | fair input/data/compute/action matching | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To prevent a collision when grasping, an intermediate point is first reached, above the grasping position.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints).
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger and ...
- **p. 15 / VIII. CONCLUSION - extractive body cue:** Experiment C: Robustness criterion VI-C.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** The robustness criterion is finite when the friction cones are considered.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, inequality constraints cannot be taken into account explicitly. (p. 2, I. INTRODUCTION).
- **Actual contribution:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion. (p. 3, I. INTRODUCTION).
- **Evaluation boundary:** 2) Results: The experiment is summed up by Figures 3 to 6. (p. 11, VII. EXPERIMENTS).
- **Explicit failure boundary:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints). (p. 12, VII. EXPERIMENTS).
