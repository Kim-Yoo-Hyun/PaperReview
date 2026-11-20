# Controllability of Pushing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://publications.ri.cmu.edu/controllability-of-pushing.
> PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1995 / ICRA
- Authors: Kevin M. Lynch, Matthew T. Mason
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, contact-rich manipulation, pushing, controllability
- Official paper: https://publications.ri.cmu.edu/controllability-of-pushing
- Full-text retrieval: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

문제 관련 발췌 — If the object is too large to be grasped or too heavy to be carried, however, this approach fails.

방법 관련 발췌 — Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper addresses the question "Can the object be pushed from here to there?" We characterize the set of objects that are controllable (can be ...
- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** A robotic manipulator is often required to move an object from one place to another.
- **p. 1 / 1 Introduction - extractive body cue:** An obvious solution is to equip the manipulator with a gripper and adopt the pick-and-place approach.
- **p. 1 / 1 Introduction - extractive body cue:** By designing the grasp to resist all forces that could reasonably act on the object during the motion, grasp planning and path planning can be ...
- **p. 1 / 1 Introduction - extractive body cue:** If the object is too large to be grasped or too heavy to be carried, however, this approach fails.
- **p. 1 / 1 Introduction - extractive body cue:** The "grasp" (pushingcontact configuration)and manipulator path cannot be decoupled.

## Core Idea

- **p. 3 / C H can be followed - extractive body cue:** Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity
- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** By modeling the frictional forces, however, we can find pushing plans to move the object from one configuration in the plane to another by simultaneously ...
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **원문 대조:** Limit surface에서 force f에 velocity direction v̂가 대응하면, 반대 force −f에는 반대 velocity direction −v̂가 대응한다. 기존 제어문자는 여기서 음수 부호였다. ([PDF p. 4](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=4), §3.1.1 The limit surface).
- **p. 5 / C H can be followed - extractive body cue:** For example, if a point x0 supports a finite force, the pressure at x0 is infinite, and if the coefficient of frictionis nonzero, then s(x0 ...
- **원문 대조:** 가능한 pushing contact 집합 Γ를 닫힌 piecewise-smooth curve로 둔다. Vertex가 아닌 곳에는 유일한 inward contact normal이 있고, vertex에서는 인접 normal이 정하는 범위의 방향을 허용한다. ([PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing).
- **p. 3 / X. The Lie algebra - extractive body cue:** A control system is small-time accessible from q if it satisfies the Lie Algebra Rank Condition,which states that the tangent vectors at q of vector ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Controllability assumptions | 원문 대조: Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof) | Velocity-direction 조건; RGB-D sensor 설정이 아님 | [PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof |
| State/latent | Then, slider, rotated, desired, goal, configuration, Proposition, straightforward, generalization, result, Barraquand, Latombe | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 4 (C H can be followed) |
| Output/action | A control system is small-time accessible from q if it satisfies the Lie Algebra Rank Condition,which states that the tangent vectors at q of vector fields in L(X ) must span the ... | grasp, pose, force 또는 end-effector trajectory | p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed) |
| Objective/outcome | In general, the manipulator can apply control forces through any of the frictional kinematic constraints that comprise the manipulator. | task completion, contact success, pose/force error와 generalization | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / C H can be followed - extractive body cue:** Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity
- **p. 4 / C H can be followed - extractive body cue:** Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 4 (C H can be followed) |
| Embodiment/environment | A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability. | hardware/simulator version and reset protocol | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Dataset/benchmark | Our planner is adapted from Barraquand and Latombe's path planner for nonholonomicmobile robots [5]. | role, split, size and leakage | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 7 (C H can be followed), p. 4 (C H can be followed) |
| Metric | Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, the planner uses only the extremal velocity ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 4 (C H can be followed), p. 5 (C H can be followed) |
| Baseline/ablation | At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular component. | fair input/data/compute/action matching | p. 5 (C H can be followed) |

## Explicit Limitations and Failure Boundary

- **p. 3 / X. The Lie algebra - extractive body cue:** If condition (1) holds, the slider cannot rotate.
- **p. 5 / C H can be followed - extractive body cue:** The slider cannot be rotated (unless its limit surface contains vertices).
- **p. 5 / C H can be followed - extractive body cue:** If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of the ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.
- **p. 6 / C H can be followed - extractive body cue:** In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, ...
- **원문 대조:** Pushing control system Σ는 대칭일 필요가 없으므로 small-time accessibility만으로 small-time local controllability가 따라오지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, after Proposition 1).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 1 (Abstract), p. 3 (X. The Lie algebra), p. 4 (C H can be followed)이다.
