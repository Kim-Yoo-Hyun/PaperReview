# Evaluation - D* Lite

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; legacy extraction flag: high; severe font-encoding corruption found in DOC-QA1); canonical paper source: https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf; PDF retrieval source: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.


> 정오표: 저자 페이지는 Figure 4의 line 33″에서 no-known-path 판단의 주석을 `rhs(s_start)=∞`로 명시한다. 이번 CMU PDF의 해당 줄도 rhs를 사용한다. [저자 정오표](https://idm-lab.org/bib/abstracts/Koen02e.html), PDF p. 5.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (A Performance of D* Lite), p. 7 (A B), p. 6 (Abstract), p. 6 (Abstract), p. 2 (Abstract), p. 3 (Abstract)): D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four for the vertex expansions.

## Evaluation Body Digest

- **p. 6 / Abstract - extractive body cue:** Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, we only need ...
- **p. 2 / Abstract - extractive body cue:** The goal distances are important because one can easily determine a shortest path from its current cell of the robot to the goal cell by ...
- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **원문 대조:** Robot navigation graph에서 s_start는 로봇의 현재 vertex, s_goal은 목표 vertex다. D* Lite는 이동과 edge-cost 변경 뒤에도 목표까지의 경로를 반복 계산한다. ([PDF p. 4](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=4), D* Lite, navigation formulation).
- **p. 5 / Abstract - extractive body cue:** If the robot moves again and then detects cost changes again, then the constants need to get added up.
- **p. 5 / Abstract - extractive body cue:** Then, the order of the vertices in the priority queue does not change after the robot moves and the priority queue does not need to ...
- **p. 6 / Abstract - extractive body cue:** This is not a problem since the g-value is not used to determine how the robot should move.
- **p. 7 / A Performance of D* Lite - extractive body cue:** Greedy mapping discretizes the terrain into cells with uniform resolution and then always moves the robot from its current cell to the closest cell with ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A Performance of D* Lite | EMPIRICAL / REAL-ROBOT OR HARDWARE | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four ... | p. 7 (A Performance of D* Lite) |
| A B | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results also confirm earlier experimental results that D* can outperform A* for goal-directed navigation in unknown terrain by one order of magnitude or ... | p. 7 (A B) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | In the following, we study to which degree the combination of incremental and heuristic search that D* Lite implements outperforms incremental or heuristic searches ... | p. 6 (Abstract) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | Since the actual planning times are implementation and machine dependent, they make it difficult for others to reproduce the results of our performance comparison. | p. 6 (Abstract) |
| LPA* graph notation | FORMULATION; empirical/real-robot evidence 아님 | 원문 대조: Succ(s)는 vertex s의 successor 집합이고 Pred(s)는 predecessor 집합이다. 탐색 대상은 유한 graph이며 edge cost의 증가·감소를 허용한다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation) | [PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation |

## Dataset / Benchmark Role

- **p. 6 / Abstract - extractive body cue:** Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, we only need ...
- **p. 2 / Abstract - extractive body cue:** The goal distances are important because one can easily determine a shortest path from its current cell of the robot to the goal cell by ...
- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **원문 대조:** Robot navigation graph에서 s_start는 로봇의 현재 vertex, s_goal은 목표 vertex다. D* Lite는 이동과 edge-cost 변경 뒤에도 목표까지의 경로를 반복 계산한다. ([PDF p. 4](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=4), D* Lite, navigation formulation).
- **p. 5 / Abstract - extractive body cue:** If the robot moves again and then detects cost changes again, then the constants need to get added up.
- **p. 5 / Abstract - extractive body cue:** Then, the order of the vertices in the priority queue does not change after the robot moves and the priority queue does not need to ...
- **p. 6 / Abstract - extractive body cue:** This is not a problem since the g-value is not used to determine how the robot should move.
- **p. 7 / A Performance of D* Lite - extractive body cue:** Greedy mapping discretizes the terrain into cells with uniform resolution and then always moves the robot from its current cell to the closest cell with ...

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Simple Example. along the path and discovered the first blocked cell it did not know about. Cells whose goal distances have changed are ...
- **원문 대조:** LPA*는 각 vertex의 g estimate와 one-step lookahead rhs를 유지한다. g=rhs이면 locally consistent이며, Figure 2는 이 불일치를 queue로 관리하는 알고리즘이다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2; Lifelong Planning A*: The Variables).
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: D* Lite. D* Lite So far, we have described LPA*, that repeatedly determines shortest paths between the start vertex and the goal vertex ...
- **원문 대조:** Figure 4는 optimized D* Lite이다. Queue에서 꺼낸 old key와 현재 CalculateKey를 비교하고 old key가 작으면 갱신해 다시 queue에서 처리한다. 그림 뒤의 Heap Reordering 본문과 caption이 섞인 기존 cue를 분리했다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4; Heap Reordering).
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of D* Lite and D*. fore used three measures that all correspond to common op- erations performed by the methods and thus ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Goal-Directed Navigation (Uniform). 0 100 200 300 400 500 percent of extra vertex expansions
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Goal-Directed Navigation (Adaptive). forms the other two search methods according to all three performance measures, even by more than a factor of seven ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Mapping (Uniform). schemes (Moore & Atkeson 1995; Yahja et al. 1998). We therefore used D* Lite to implement a deterministic version of the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, we only ... | embodiment, simulator version and control stack | p. 6 (Abstract), p. 2 (Abstract) |
| Task/environment | The goal distances are important because one can easily determine a shortest path from its current cell of the robot to the goal cell ... | reset, timeout, object/scene variation | p. 2 (Abstract), p. 4 (Abstract) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 3 (Abstract) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (Abstract), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Thus, D* Lite always scores zero and methods that score above zero perform worse than D* Lite. | definition/direction/unit from same section | p. 6 (Abstract) |
| Thus, D* Lite operates on the original graph and there are no restrictions on the graph except that it needs to be able to ... | definition/direction/unit from same section | p. 5 (Abstract) |
| 원문 대조: 탐색 완료 뒤 현재 vertex s의 successor 중 c(s,s′)+g(s′)를 최소화하는 s′로 이동하여 목표까지 최단 경로를 따른다. D* Lite는 goal에서 current start 쪽으로 역방향 탐색하며 g는 goal-distance estimate다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Search Direction; Theorem 8 on p. 6) | Path-extraction rule; metric 수치 아님 | [PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Search Direction; Theorem 8 on p. 6 |
| The figure also shows the corresponding 95 percent confidence intervals to demonstrate that our conclusions are statistically significant. | definition/direction/unit from same section | p. 6 (Abstract) |
| 원문 대조: Succ(s)는 vertex s의 successor 집합이고 Pred(s)는 predecessor 집합이다. 탐색 대상은 유한 graph이며 edge cost의 증가·감소를 허용한다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation) | Graph notation; metric 수치 아님 | [PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation |
| Cells whose goal distances have changed are shaded gray. | definition/direction/unit from same section | p. 2 (Abstract) |
| 원문 대조: LPA*에서 locally underconsistent vertex를 확장하면 그 vertex와 successor의 local consistency가 영향을 받을 수 있어 rhs와 queue membership을 갱신한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm) | Algorithm update case; metric 수치 아님 | [PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm |
| 원문 대조: LPA*에서 locally overconsistent vertex의 g를 rhs로 바꾸면 successor의 local consistency가 달라질 수 있다. 해당 successor들을 UpdateVertex로 처리한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm) | Algorithm update case; metric 수치 아님 | [PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four ... | comparison identity and matched condition | p. 7 (A Performance of D* Lite) |
| Keys are compared according to a lexicographic ordering. | comparison identity and matched condition | p. 3 (Abstract) |
| In the following, we study to which degree the combination of incremental and heuristic search that D* Lite implements outperforms incremental or heuristic searches ... | comparison identity and matched condition | p. 6 (Abstract) |
| These results also confirm earlier experimental results that D* can outperform A* for goal-directed navigation in unknown terrain by one order of magnitude or ... | comparison identity and matched condition | p. 7 (A B) |
| We decided not to include D* Lite without both heuristic and incremental search in the comparison because it performs so poorly that graphing its ... | comparison identity and matched condition | p. 6 (Abstract) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To maintain Invariants 13, ComputeShortestPath() therefore updates rhs-values of these vertices, checks their local consistency, and adds them to or removes them from the ... | component/input/data sensitivity | p. 3 (Abstract) |
| The priority of a vertex in the priority queue is always the same as its key (Invariant 3), which is a vector with two ... | component/input/data sensitivity | p. 3 (Abstract) |
| 원문 대조: LPA*의 invariant는 rhs(s_start)=0, 나머지 vertex에서는 rhs(s)=min_{s′∈Pred(s)}[g(s′)+c(s′,s)]이다. D* Lite는 search direction을 뒤집으므로 이 식의 start/predecessor 표기를 그대로 복사하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*: The Variables, Eq. (1)) | Invariant definition; ablation 결과 아님 | [PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*: The Variables, Eq. (1) |
| 원문 대조: U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API와 graph notation) | Queue API; ablation 수치 아님 | PDF p. 2 |
| 원문 대조: Figure 4는 optimized D* Lite이다. Queue에서 꺼낸 old key와 현재 CalculateKey를 비교하고 old key가 작으면 갱신해 다시 queue에서 처리한다. 그림 뒤의 Heap Reordering 본문과 caption이 섞인 기존 cue를 분리했다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4; Heap Reordering) | Algorithm optimization; ablation 수치 아님 | [PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4; Heap Reordering |
| 원문 대조: Old queue key가 새 CalculateKey보다 작으면 제거한 vertex를 새 priority로 재삽입한다. 이는 start가 이동해 heuristic 값이 바뀌어도 queue 전체를 매번 재정렬하지 않기 위한 처리다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering, Figure 3 lines 13′–14′) | Heap-update mechanism; ablation 수치 아님 | [PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering, Figure 3 lines 13′–14′ |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite. | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (A Performance of D* Lite), p. 7 (A B), p. 6 (Abstract), p. 6 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Primary metric/result | These results also confirm earlier experimental results that D* can outperform A* for goal-directed navigation in unknown terrain by one order of magnitude or ... | numeric claim only at cited anchor | p. 7 (A B) |

- Numeric sentences retained from the body:
- **원문 대조:** U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API).
- **원문 대조:** LPA*의 UpdateVertex는 start 이외 vertex의 rhs를 predecessor 기반 one-step lookahead로 계산한다. Queue의 기존 항목을 제거한 뒤 g≠rhs인 vertex만 새 key로 삽입한다. 손상된 의사코드 문자열을 실행 가능한 코드로 사용하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2, UpdateVertex lines 06–08).
- **원문 대조:** Optimized D* Lite의 key는 [min(g,rhs)+h(s_start,s)+k_m; min(g,rhs)]이다. Initialize는 k_m=0, g=rhs=infinity로 두고 goal의 rhs만 0으로 설정해 goal을 queue에 넣는다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4, CalculateKey and Initialize).
- **원문 대조:** Optimized D* Lite는 g≠rhs인 vertex가 queue에 있으면 key를 update하고 없으면 insert한다. g=rhs이며 queue에 있으면 remove한다. 기존 깨진 문자열은 이 세 경우의 분기를 섞고 있었다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4, UpdateVertex lines 07″–09″).
- **원문 대조:** 현재 key가 더 커졌으면 queue key를 갱신한다. 그렇지 않고 g(u)>rhs(u)이면 g(u)=rhs(u)로 바꿔 u를 제거하고 predecessor의 rhs와 queue 상태를 갱신한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4, ComputeShortestPath lines 14″–21″).
- **원문 대조:** Main loop는 c(s_start,s′)+g(s′)가 최소인 successor로 이동하고 changed edge cost를 관측한다. 변화가 있으면 k_m과 관련 rhs·queue 상태를 갱신하고 ComputeShortestPath를 다시 실행한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4, Main lines 34″–48″; Figure 3 on p. 4).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | They change to infinity when the robot discovers that they cannot be traversed. | p. 4 (Abstract) |
| body limitation/failure cue | Uniform discretizations can prevent one from finding a path if they are too coarse-grained (for example, because the resolution prevents one from noticing small ... | p. 7 (A B) |
| Queue API (실패 근거 아님) | 원문 대조: U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API와 graph notation) | PDF p. 2 |
| body limitation/failure cue | This is similar to what A* can do if it does not use backpointers. | p. 3 (Abstract) |
| body limitation/failure cue | Note that, in an actual implementation, Initialize() only needs to initialize a vertex when it encounters it during the search and thus does not ... | p. 3 (Abstract) |
| body limitation/failure cue | Theorem 6 ComputeShortestPath() does not expand any vertices whose g-values were equal to their respective start distances before ComputeShortestPath() was called. | p. 4 (Abstract) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It always computes a shortest path from its current cell to the goal cell under the assumption that cells with unknown blockage status are ... | p. 1 (Abstract) |
| It then follows this path until it reaches the goal cell, in which case it stops successfully, or it observes an untraversable cell, in ... | p. 1 (Abstract) |
| 원문 대조: U.Top()은 priority queue에서 가장 작은 priority를 가진 vertex를 반환한다. 이는 queue API 설명이며 실험 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API와 graph notation) | PDF p. 2 |
| The goal distances are important because one can easily determine a shortest path from its current cell of the robot to the goal cell ... | p. 2 (Abstract) |
| Theorem 1 already showed that ComputeShortestPath() expands each vertex at most twice. | p. 3 (Abstract) |
| Moreover, the next theorem states that the keys of the vertices expanded by ComputeShortestPath() are monotonically nondecreasing over time. | p. 3 (Abstract) |
| 원문 대조: Theorem 5는 LPA*에서 확장 가능한 locally overconsistent vertex를 goal의 [f; start-distance] key 이하인 범위로 제한한다. 이는 D* Lite의 전체 runtime 수치나 실험 ablation 결과가 아니다. ([PDF p. 4](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=4), Analytical Results, Theorem 5 (LPA*)) | [PDF p. 4](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=4), Analytical Results, Theorem 5 (LPA*) |
| The next theorem generalizes this result to all locally inconsistent vertices expanded by ComputeShortestPath(). | p. 4 (Abstract) |

## Limitations and Verification Questions

- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **p. 7 / A B - extractive body cue:** Uniform discretizations can prevent one from finding a path if they are too coarse-grained (for example, because the resolution prevents one from noticing small gaps ...
- **원문 대조:** U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API).
- **p. 3 / Abstract - extractive body cue:** This is similar to what A* can do if it does not use backpointers.
- **p. 3 / Abstract - extractive body cue:** Note that, in an actual implementation, Initialize() only needs to initialize a vertex when it encounters it during the search and thus does not need ...
- **p. 4 / Abstract - extractive body cue:** Theorem 6 ComputeShortestPath() does not expand any vertices whose g-values were equal to their respective start distances before ComputeShortestPath() was called.

- **Evidence anchors reviewed:** datasets p. 6 (Abstract), p. 2 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 5 (Abstract), p. 5 (Abstract), metrics p. 6 (Abstract), p. 5 (Abstract), p. 5 (Abstract), p. 6 (Abstract), p. 2 (Abstract), p. 2 (Abstract), baselines p. 7 (A Performance of D* Lite), p. 3 (Abstract), p. 6 (Abstract), p. 7 (A B), p. 6 (Abstract), results p. 7 (A Performance of D* Lite), p. 7 (A B), p. 6 (Abstract), p. 6 (Abstract), p. 2 (Abstract), p. 3 (Abstract).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
