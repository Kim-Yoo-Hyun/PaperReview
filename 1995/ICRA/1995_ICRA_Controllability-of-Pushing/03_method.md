# Method - Controllability of Pushing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/controllability-of-pushing; PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed), p. 5 (C H can be followed)): For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these pushing directions to find sensorless ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** By modeling the frictional forces, however, we can find pushing plans to move the object from one configuration in the plane to another by simultaneously ...
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **원문 대조:** Limit surface에서 force f에 velocity direction v̂가 대응하면, 반대 force −f에는 반대 velocity direction −v̂가 대응한다. 기존 제어문자는 여기서 음수 부호였다. ([PDF p. 4](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=4), §3.1.1 The limit surface).
- **p. 5 / C H can be followed - extractive body cue:** For example, if a point x0 supports a finite force, the pressure at x0 is infinite, and if the coefficient of frictionis nonzero, then s(x0 ...
- **원문 대조:** 가능한 pushing contact 집합 Γ를 닫힌 piecewise-smooth curve로 둔다. Vertex가 아닌 곳에는 유일한 inward contact normal이 있고, vertex에서는 인접 normal이 정하는 범위의 방향을 허용한다. ([PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing).
- **p. 3 / X. The Lie algebra - extractive body cue:** A control system is small-time accessible from q if it satisfies the Lie Algebra Rank Condition,which states that the tangent vectors at q of vector ...
- **p. 1 / 1 Introduction - extractive body cue:** In general, the manipulator can apply control forces through any of the frictional kinematic constraints that comprise the manipulator.

## Design Rationale

- **p. 3 / C H can be followed - extractive body cue:** Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** By modeling the frictional forces, however, we can find pushing plans to move the object from one configuration in the plane to another by simultaneously ...
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **원문 대조:** Limit surface에서 force f에 velocity direction v̂가 대응하면, 반대 force −f에는 반대 velocity direction −v̂가 대응한다. 기존 제어문자는 여기서 음수 부호였다. ([PDF p. 4](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=4), §3.1.1 The limit surface).
- **p. 5 / C H can be followed - extractive body cue:** For example, if a point x0 supports a finite force, the pressure at x0 is infinite, and if the coefficient of frictionis nonzero, then s(x0 ...
- **원문 대조:** 가능한 pushing contact 집합 Γ를 닫힌 piecewise-smooth curve로 둔다. Vertex가 아닌 곳에는 유일한 inward contact normal이 있고, vertex에서는 인접 normal이 정하는 범위의 방향을 허용한다. ([PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing).
- **p. 3 / X. The Lie algebra - extractive body cue:** A control system is small-time accessible from q if it satisfies the Lie Algebra Rank Condition,which states that the tangent vectors at q of vector ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and ... | p. 1 (Abstract), p. 1 (1 Introduction) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | By modeling the frictional forces, however, we can find pushing plans to move the object from one configuration in the plane to ... | p. 1 (1 Introduction), p. 3 (X. The Lie algebra) |
| Reachability construction | 주어진 velocity direction 조합으로 목표 pose 도달 | Proposition 1의 velocity-direction 가정 | 회전·병진 또는 교대 회전의 구성적 논증 | Controllability; tactile feedback·regrasp 구현 근거 아님 | 원문 대조: Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof) | [PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** In general, the manipulator can apply control forces through any of the frictional kinematic constraints that comprise the manipulator.
- **p. 1 / 1 Introduction - extractive body cue:** Other useful sources of control forces include gravity, the frictional kinematic constraints (floor, walls, obstacles) making up the robot's environment, and dynamic forces.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 1 (1 Introduction).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, slider, rotated, desired, goal, configuration, Proposition, straightforward, generalization, result, Barraquand, Latombe, states, Lie | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Then, slider, rotated, desired, goal, configuration, Proposition, straightforward, generalization, result | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | Proof, Proposition, Appendix, Barraquand, Latombe, provesthe, case, when, consists, oftwo | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | general, manipulator, apply, control, forces, through, frictional, kinematic, constraints, comprise | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **p. 3 / X. The Lie algebra - extractive body cue:** A control system is small-time accessible from q if it satisfies the Lie Algebra Rank Condition,which states that the tangent vectors at q of vector ...
- **p. 4 / C H can be followed - extractive body cue:** This also follows from Theorem 1: Theorem 1 (Sussmann [25]) Let X be a finite set of vector fields on an open set of the ...
- **p. 5 / C H can be followed - extractive body cue:** 3.2 Controllability with point contact pushing Several researchers have constructed feedback control systems for point contact pushing.
- **p. 4 / C H can be followed - extractive body cue:** The slider's velocity direction vector ^ v is normal to the limit surface at the force f (Figure 4).
- **p. 5 / C H can be followed - extractive body cue:** Because the two force directions are not opposite, the two velocity directions are also not opposite.
- **p. 1 / 1 Introduction - extractive body cue:** In general, the manipulator can apply control forces through any of the frictional kinematic constraints that comprise the manipulator.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | 2.1 The pushing control system The pushing control system can be described abstractly by the autonomous nonlinear control system _ q = ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | To demonstrate the controllability of an object by pushing, we appeal to nonlinear control theory. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

## Method-Specific Formal Details

- **Body-defined terms:** case, line, contact, find, pushing, directions, keep, object, fixed, pusher, sensorless, plans, reposition, among, obstacles, modeling, frictional, forces, however, move.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability. | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Grasp / trajectory generation | At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular ... | p. 5 (C H can be followed) |
| Contact execution / correction | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | p. 4 (C H can be followed), p. 3 (X. The Lie algebra) |

## Failure and Ablation Link

- **p. 5 / C H can be followed - extractive body cue:** At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular component.
- **p. 3 / X. The Lie algebra - extractive body cue:** If condition (1) holds, the slider cannot rotate.
- **p. 5 / C H can be followed - extractive body cue:** The slider cannot be rotated (unless its limit surface contains vertices).
- **p. 5 / C H can be followed - extractive body cue:** If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of the ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.
- **p. 6 / C H can be followed - extractive body cue:** In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed), p. 5 (C H can be followed), objective p. 1 (1 Introduction), p. 1 (1 Introduction), temporal p. 2 (1.1 Related work), p. 1 (1.1 Related work), p. 1 (1.1 Related work), p. 2 (1.1 Related work), p. 3 (1.1 Related work).
