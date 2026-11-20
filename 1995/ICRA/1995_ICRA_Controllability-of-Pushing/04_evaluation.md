# Evaluation - Controllability of Pushing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/controllability-of-pushing; PDF retrieval source: https://www.ri.cmu.edu/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (C H can be followed)): Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.

## Evaluation Body Digest

- **p. 3 / X. The Lie algebra - extractive body cue:** A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability.
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **p. 7 / C H can be followed - extractive body cue:** Our planner is adapted from Barraquand and Latombe's path planner for nonholonomicmobile robots [5].
- **p. 4 / C H can be followed - extractive body cue:** 3 Mechanics and controllability of pushing In this section we study the problem of determining the motion of a pushed object.
- **p. 4 / C H can be followed - extractive body cue:** Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.
- **p. 5 / C H can be followed - extractive body cue:** If the object is small-time locally controllable, however, it can followany path arbitrarilyclosely.
- **p. 5 / C H can be followed - extractive body cue:** 3.1.2 Solving for the motion of a pushed object Each contact point between the pusher and the slider may be sticking, breaking free, or sliding ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| C H can be followed | SYSTEM / EVALUATION SCOPE UNRESOLVED | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | p. 4 (C H can be followed) |

## Dataset / Benchmark Role

- **p. 3 / X. The Lie algebra - extractive body cue:** A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability.
- **원문 대조:** Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof).
- **p. 7 / C H can be followed - extractive body cue:** Our planner is adapted from Barraquand and Latombe's path planner for nonholonomicmobile robots [5].
- **p. 4 / C H can be followed - extractive body cue:** 3 Mechanics and controllability of pushing In this section we study the problem of determining the motion of a pushed object.
- **p. 4 / C H can be followed - extractive body cue:** Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact.
- **p. 5 / C H can be followed - extractive body cue:** If the object is small-time locally controllable, however, it can followany path arbitrarilyclosely.
- **p. 5 / C H can be followed - extractive body cue:** 3.1.2 Solving for the motion of a pushed object Each contact point between the pusher and the slider may be sticking, breaking free, or sliding ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The world frame F W and the slider frame F S.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure2: Theconvexhullofthreevelocitydirectionsin the rotation center space and on the velocity sphere. the frictional force can act in any tangential direction with any magnitude less than ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Examples of rotation center sets that yield small-time local controllability: (a) three rotation centers positively spanning a great circle of the velocity sphere; ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Limit surface mapping of a force to a velocity direction. If the support friction distribution s(x) becomes infinite at anypoint,however, the mappingis nolongerone-to-one. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: (a) The forces that the pusher can apply to the slider during sticking contact are represented by the two friction cones. (b) The ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Examples of line contact. with contact normals perpendicular to the line (Figure 6). We also assume that the coefficient of friction at all ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Procedure STABLE. 3.3.2 Controllabilityby stable pushing with line contact If the composite friction cone F from the line pushing contact contains a pure ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: The slider of Figure 7 is small-time locally controllable by stable pushing at two edges. The friction coefficient is 0.5. (zero moment about ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A car-like mobile robot can drive both forward and backward, and this symmetry, coupled with small-time accessibility, implies small-time local controllability. | embodiment, simulator version and control stack | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Theoretical scope | 원문 대조: Proposition 1의 가정 아래 회전과 병진 또는 두 회전 방향의 조합으로 목표 위치·자세에 도달할 수 있음을 설명한다. Pushing control의 비대칭성 때문에 이 controllability 논증을 small-time local controllability와 동일시하지 않는다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof) | Local controllability와 global reachability 구분; reset/timeout 근거 아님 | [PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3, Proposition 1 proof |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (C H can be followed), p. 5 (C H can be followed) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| To see this is sufficient, recall that two nonopposite velocity directions that are not both translationsare sufficient forsmall-timeaccessibility. | definition/direction/unit from same section | p. 4 (C H can be followed) |
| A slider that is controllable by pushing may have to be pushed a long distance to reach nearby configurations. | definition/direction/unit from same section | p. 5 (C H can be followed) |
| 원문 대조: 가능한 pushing contact 집합 Γ를 닫힌 piecewise-smooth curve로 둔다. Vertex가 아닌 곳에는 유일한 inward contact normal이 있고, vertex에서는 인접 normal이 정하는 범위의 방향을 허용한다. ([PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing) | Contact geometry 가정; 성능 metric 아님 | [PDF p. 5](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=5), §3.2 Controllability with point contact pushing |
| Proof: The center of friction only lies on a vertex of the convex hullif the supportfrictiondistribution s(x) integrates to zero everywhere else. | definition/direction/unit from same section | p. 7 (C H can be followed) |
| The other is a distance r2 =p from the center of friction and on the opposite side from the endpoint, where p is the ... | definition/direction/unit from same section | p. 7 (C H can be followed) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| At least one of the force directions has nonzero moment, so at least one of the velocity directions has a nonzero angular component. | component/input/data sensitivity | p. 5 (C H can be followed) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Proof: Proposition 5 in Appendix B of (Barraquand and Latombe [5]) provesthe case when V consists oftwo velocity | Using the results of the previous section, we elucidate the controllabilityproperties of objects pushed with either point contact or stable line contact. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (C H can be followed) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **원문 대조:** 가능한 velocity direction이 하나뿐인 경우(n=1) slider는 하나의 integral curve에 제한되어 accessible하지 않다. 둘 이상일 때의 조건은 같은 절의 Lie algebra와 Proposition 1에서 따로 논한다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3 Controllability of the pushing control system).
- **p. 3 / X. The Lie algebra - extractive body cue:** If n = 2, the Lie algebra L(X ) is spanned by X1, X2, and X3 = [X1 ; X2 ].
- **원문 대조:** 가능한 velocity direction이 하나뿐인 경우(n=1) slider는 하나의 integral curve에 제한되어 accessible하지 않다. 둘 이상일 때의 조건은 같은 절의 Lie algebra와 Proposition 1에서 따로 논한다. ([PDF p. 3](https://publications.ri.cmu.edu/storage/publications/pub_files/pub2/lynch_kevin_1995_1/lynch_kevin_1995_1.pdf#page=3), §2.3 Controllability of the pushing control system).
- **p. 3 / X. The Lie algebra - extractive body cue:** If n = 2, the Lie algebra L(X ) is spanned by X1, X2, and X3 = [X1 ; X2 ].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If condition (1) holds, the slider cannot rotate. | p. 3 (X. The Lie algebra) |
| body limitation/failure cue | The slider cannot be rotated (unless its limit surface contains vertices). | p. 5 (C H can be followed) |
| body limitation/failure cue | If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of ... | p. 5 (C H can be followed) |
| body limitation/failure cue | If the contact is frictionless, however, the object cannot be rotated. | p. 6 (C H can be followed) |
| body limitation/failure cue | In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be ... | p. 6 (C H can be followed) |
| body limitation/failure cue | Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / X. The Lie algebra - extractive body cue:** If condition (1) holds, the slider cannot rotate.
- **p. 5 / C H can be followed - extractive body cue:** The slider cannot be rotated (unless its limit surface contains vertices).
- **p. 5 / C H can be followed - extractive body cue:** If V k ;i \ V f ;i = ;, contact mode i cannot occur; otherwise, contact mode i is feasible and any of the ...
- **p. 6 / C H can be followed - extractive body cue:** If the contact is frictionless, however, the object cannot be rotated.
- **p. 6 / C H can be followed - extractive body cue:** In fact, with no information about the support friction distribution s(x) other than the center of friction, no velocity direction is guaranteed to be in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9: A plan found using stable pushes from only two edges. the set of stable pushing directions using STABLE. In light of Proposition 2, ...

- **Evidence anchors reviewed:** datasets p. 3 (X. The Lie algebra), p. 3 (X. The Lie algebra), p. 7 (C H can be followed), p. 4 (C H can be followed), p. 4 (C H can be followed), p. 5 (C H can be followed), metrics p. 8 (Figure/Table caption), p. 4 (C H can be followed), p. 5 (C H can be followed), p. 5 (C H can be followed), p. 7 (C H can be followed), p. 7 (C H can be followed), baselines 본문 anchor 없음, results p. 4 (C H can be followed).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
