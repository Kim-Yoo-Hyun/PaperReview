# Insights — Controllability of Pushing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/controllability-of-pushing; PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / C H can be followed - extractive body cue:** Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity
- **p. 1 / Abstract - extractive body cue:** For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these ...
- **p. 1 / 1 Introduction - extractive body cue:** By modeling the frictional forces, however, we can find pushing plans to move the object from one configuration in the plane to another by simultaneously ...
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **원문 대조:** Limit surface에서 force f에 velocity direction v̂가 대응하면, 반대 force −f에는 반대 velocity direction −v̂가 대응한다. 기존 제어문자는 여기서 음수 부호였다. ([PDF p. 4](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=4), §3.1.1 The limit surface).
- **p. 5 / C H can be followed - extractive body cue:** For example, if a point x0 supports a finite force, the pressure at x0 is infinite, and if the coefficient of frictionis nonzero, then s(x0 ...
- **원문 대조:** 가능한 pushing contact 집합 Γ를 닫힌 piecewise-smooth curve로 둔다. Vertex가 아닌 곳에는 유일한 inward contact normal이 있고, vertex에서는 인접 normal이 정하는 범위의 방향을 허용한다. ([PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing).
- **Contribution anchor:** p. 3 (C H can be followed), p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (X. The Lie algebra), p. 4 (C H can be followed), p. 5 (C H can be followed)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** If the object is too large to be grasped or too heavy to be carried, however, this approach fails.
- **p. 1 / 1 Introduction - extractive body cue:** The "grasp" (pushingcontact configuration)and manipulator path cannot be decoupled.
- **p. 3 / X. The Lie algebra - extractive body cue:** If condition (1) holds, the slider cannot rotate.
- **p. 5 / C H can be followed - extractive body cue:** The slider cannot be rotated (unless its limit surface contains vertices).
- **p. 5 / C H can be followed - extractive body cue:** If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of the ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.
- **p. 6 / C H can be followed - extractive body cue:** In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be in ...
- **Boundary to test:** If condition (1) holds, the slider cannot rotate.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity | p. 3 (C H can be followed), p. 1 (Abstract) |
| Reported outcome | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | p. 4 (C H can be followed) |
| Failure/limitation | If condition (1) holds, the slider cannot rotate. | p. 3 (X. The Lie algebra), p. 5 (C H can be followed) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- The paper-specific mechanism to preserve in a reproduction is: Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- 현재 등급·주 트랙·태그는 [논문 개요](./01_overview.md)에서 확인한다.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** If condition (1) holds, the slider cannot rotate.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability..
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, the planner uses only the extremal velocity ....
5. Re-run the body-reported ablation/failure condition: At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular component..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (X. The Lie algebra); the primary result is directionally consistent at p. 4 (C H can be followed); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Proof, Proposition, Appendix mechanism이 a matched simpler baseline 대비 Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions ...을 개선하고, If condition (1) holds, the slider cannot rotate. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
