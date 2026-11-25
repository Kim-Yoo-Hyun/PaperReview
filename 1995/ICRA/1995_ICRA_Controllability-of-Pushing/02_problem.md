# Problem - Controllability of Pushing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/controllability-of-pushing; PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): If the object is too large to be grasped or too heavy to be carried, however, this approach fails.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper addresses the question "Can the object be pushed from here to there?" We characterize the set of objects that are controllable (can be ...
- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** A robotic manipulator is often required to move an object from one place to another.
- **p. 1 / 1 Introduction - extractive body cue:** An obvious solution is to equip the manipulator with a gripper and adopt the pick-and-place approach.
- **p. 1 / 1 Introduction - extractive body cue:** By designing the grasp to resist all forces that could reasonably act on the object during the motion, grasp planning and path planning can be ...
- **p. 1 / 1 Introduction - extractive body cue:** If the object is too large to be grasped or too heavy to be carried, however, this approach fails.
- **p. 1 / 1 Introduction - extractive body cue:** The "grasp" (pushingcontact configuration)and manipulator path cannot be decoupled.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | If the object is too large to be grasped or too heavy to be carried, however, this approach fails. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Controllability assumptions | 원문 대조: Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof) | Velocity-direction 조건 | 해당 증명으로 sensor/preprocessing을 추론하지 않음 |
| State / latent | Then, slider, rotated, desired, goal, configuration, Proposition, straightforward, generalization, result | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | follows, Theorem, Sussmann, Let, finite, vector, fields, open | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Then, slider, rotated, desired, goal, configuration, Proposition, straightforward, generalization, result | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 4 (C H can be followed) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: Proof, Proposition, Appendix, Barraquand, Latombe, provesthe, case, when | p. 3 (C H can be followed) |
| Objective / loss / cost | task/contact/pose objective; cue terms: general, manipulator, apply, control, forces, through, frictional, kinematic | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Success / guarantee | completion, contact success and robustness | p. 8 (Figure/Table caption), p. 4 (C H can be followed), p. 5 (C H can be followed) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** The "grasp" (pushingcontact configuration)and manipulator path cannot be decoupled.

## What the Paper Changes

PDF body contribution framing (p. 3 (C H can be followed)): Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | If condition (1) holds, the slider cannot rotate. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The slider cannot be rotated (unless its limit surface contains vertices). | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | If the contact is frictionless, however, the object cannot be rotated. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed), objective p. 1 (1 Introduction), p. 1 (1 Introduction).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
