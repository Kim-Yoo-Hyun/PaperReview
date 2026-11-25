# Method - D* Lite

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; legacy extraction flag: high; severe font-encoding corruption found in DOC-QA1); canonical paper source: https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf; PDF retrieval source: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.


> 정오표: 저자 페이지는 Figure 4의 line 33″에서 no-known-path 판단의 주석을 `rhs(s_start)=∞`로 명시한다. 이번 CMU PDF의 해당 줄도 rhs를 사용한다. [저자 정오표](https://idm-lab.org/bib/abstracts/Koen02e.html), PDF p. 5.

## Method in One Sentence

- **원문 대조:** LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2).

## Method Body Digest

- **원문 대조:** LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2).
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 2 / Abstract - extractive body cue:** It applies to finite graph search problems on known graphs whose edge costs increase or decrease over time (which can also be used to model ...
- **p. 3 / Abstract - extractive body cue:** Similarity to A* When we described LPA*, we already pointed out strong algorithmic similarities between LPA* and A*.
- **p. 4 / Abstract - extractive body cue:** The terrain is modeled as an eight-connected graph.
- **원문 대조:** 로봇 이동에 따른 heuristic 보정량은 queue의 모든 vertex에 공통이므로 그만큼 일괄 차감하지 않아도 순서는 유지된다. 누적 보정량 k_m을 새 key 계산에 더하는 방식으로 전체 heap 재정렬을 피한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering).
- **원문 대조:** LPA*의 UpdateVertex는 start 이외 vertex의 rhs를 predecessor 기반 one-step lookahead로 계산한다. Queue의 기존 항목을 제거한 뒤 g≠rhs인 vertex만 새 key로 삽입한다. 손상된 의사코드 문자열을 실행 가능한 코드로 사용하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2, UpdateVertex lines 06–08).

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- **p. 1 / Abstract - extractive body cue:** Building on LPA*, we therefore present D* Lite, a novel replanning method that implements the same navigation strategy as D* but is algorithmically different.
- **p. 4 / Abstract - extractive body cue:** We now use LPA* to develop D* Lite, that repeatedly determines shortest paths between the current vertex of the robot and the goal vertex as ...

## Source Evidence Cues

- **원문 대조:** LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2).
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 2 / Abstract - extractive body cue:** It applies to finite graph search problems on known graphs whose edge costs increase or decrease over time (which can also be used to model ...
- **p. 3 / Abstract - extractive body cue:** Similarity to A* When we described LPA*, we already pointed out strong algorithmic similarities between LPA* and A*.
- **p. 4 / Abstract - extractive body cue:** The terrain is modeled as an eight-connected graph.
- **원문 대조:** 로봇 이동에 따른 heuristic 보정량은 queue의 모든 vertex에 공통이므로 그만큼 일괄 차감하지 않아도 순서는 유지된다. 누적 보정량 k_m을 새 key 계산에 더하는 방식으로 전체 heap 재정렬을 피한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Incremental graph search | 이전 탐색의 g/rhs를 재사용 | Graph와 변경된 edge cost | UpdateVertex 후 ComputeShortestPath | Shortest-path estimates; sensor mapping 구현 아님 | 원문 대조: LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2) | [PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2 |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The resulting D* Lite algorithm is easy to understand and analyze. | p. 1 (Abstract), p. 1 (Abstract) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different. | p. 1 (Abstract), p. 2 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** LPA*의 UpdateVertex는 start 이외 vertex의 rhs를 predecessor 기반 one-step lookahead로 계산한다. Queue의 기존 항목을 제거한 뒤 g≠rhs인 vertex만 새 key로 삽입한다. 손상된 의사코드 문자열을 실행 가능한 코드로 사용하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2, UpdateVertex lines 06–08).
- **원문 대조:** Edge cost 또는 g의 변경으로 영향을 받는 vertex의 rhs를 재계산하고 local consistency에 맞춰 queue를 수정한다. 이 문단은 invariant 유지 절차이며 논문이 보고한 ablation 또는 failure 실험은 아니다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm).
- **원문 대조:** Main loop는 c(s_start,s′)+g(s′)가 최소인 successor로 이동하고 changed edge cost를 관측한다. 변화가 있으면 k_m과 관련 rhs·queue 상태를 갱신하고 ComputeShortestPath를 다시 실행한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4, Main lines 34″–48″; Figure 3 on p. 4).
- **원문 대조:** 탐색 완료 뒤 현재 vertex s의 successor 중 c(s,s′)+g(s′)를 최소화하는 s′로 이동하여 목표까지 최단 경로를 따른다. D* Lite는 goal에서 current start 쪽으로 역방향 탐색하며 g는 goal-distance estimate다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Search Direction; Theorem 8 on p. 6).
- **p. 1 / Abstract - extractive body cue:** Motivation Consider a goal-directed robot-navigation task in unknown terrain, where the robot always observes which of its eight adjacent cells are traversable and then moves ...
- **원문 대조:** c(s,s′)는 s에서 successor s′로 이동하는 양의 edge cost이며 infinity를 허용한다. LPA*는 현재 graph topology와 edge cost를 알고 start–goal shortest path를 계산하는 설정이다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation).
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Lite, substantially, shorter, uses, only, tie-breaking, criterion, when, comparing, priorities, simplifies, maintenance, does, need | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Lite, substantially, shorter, uses, only, tie-breaking, criterion, when, comparing, priorities | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | gain, insight, behavior, present, various, theoretical, properties, LPA, apply, Lite | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | 원문 대조: 최단 경로는 edge cost의 합을 최소화한다. 깨진 queue 함수명 목록은 objective나 risk 항의 근거가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API와 graph notation) | Graph-search cost; queue API와 구분 | PDF p. 2 |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** D* Lite is substantially shorter than D*, uses only one tie-breaking criterion when comparing priorities, which simplifies the maintenance of the priorities, and does not ...
- **p. 3 / Abstract - extractive body cue:** Moreover, the next theorem states that the keys of the vertices expanded by ComputeShortestPath() are monotonically nondecreasing over time.
- **원문 대조:** 로봇 이동에 따른 heuristic 보정량은 queue의 모든 vertex에 공통이므로 그만큼 일괄 차감하지 않아도 순서는 유지된다. 누적 보정량 k_m을 새 key 계산에 더하는 방식으로 전체 heap 재정렬을 피한다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering).
- **p. 1 / Abstract - extractive body cue:** The robot starts at the start cell and has to move to the goal cell.
- **p. 2 / Abstract - extractive body cue:** Cells whose goal distances have changed are shaded gray.
- **원문 대조:** LPA*의 h(s,s_goal)은 goal distance를 근사하며 nonnegative이고 consistent해야 한다. 본문은 goal에서 0인 조건과 edge를 따른 triangle inequality를 명시한다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, heuristic assumptions).
- **p. 4 / Abstract - extractive body cue:** D* Lite searches from the goal vertex to the start vertex and thus its g-values are estimates
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The rhs-values are one-step lookahead values based on the g-values and thus potentially better informed than the g-values. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | not recovered | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

## Method-Specific Formal Details

- **Body-defined terms:** Lifelong, Planning, Algorithm, main, function, LPA, first, calls, Initialize, search, problem, resulting, Lite, easy, understand, analyze, implements, same, behavior, Stentz.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, ... | p. 6 (Abstract), p. 2 (Abstract) |
| Global / local decision | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor ... | p. 7 (A Performance of D* Lite), p. 3 (Abstract) |
| Motion execution / recovery | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor ... | p. 7 (A Performance of D* Lite), p. 7 (A B) |

## Failure and Ablation Link

- **p. 3 / Abstract - extractive body cue:** To maintain Invariants 13, ComputeShortestPath() therefore updates rhs-values of these vertices, checks their local consistency, and adds them to or removes them from the priority ...
- **p. 3 / Abstract - extractive body cue:** The priority of a vertex in the priority queue is always the same as its key (Invariant 3), which is a vector with two components: ...
- **원문 대조:** LPA*의 invariant는 rhs(s_start)=0, 나머지 vertex에서는 rhs(s)=min_{s′∈Pred(s)}[g(s′)+c(s′,s)]이다. D* Lite는 search direction을 뒤집으므로 이 식의 start/predecessor 표기를 그대로 복사하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*: The Variables, Eq. (1)).
- **원문 대조:** U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API).
- **원문 대조:** Figure 4는 optimized D* Lite이다. Queue에서 꺼낸 old key와 현재 CalculateKey를 비교하고 old key가 작으면 갱신해 다시 queue에서 처리한다. 그림 뒤의 Heap Reordering 본문과 caption이 섞인 기존 cue를 분리했다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Figure 4; Heap Reordering).
- **원문 대조:** Old queue key가 새 CalculateKey보다 작으면 제거한 vertex를 새 priority로 재삽입한다. 이는 start가 이동해 heuristic 값이 바뀌어도 queue 전체를 매번 재정렬하지 않기 위한 처리다. ([PDF p. 5](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=5), Heap Reordering, Figure 3 lines 13′–14′).
- **p. 6 / Abstract - extractive body cue:** We decided not to include D* Lite without both heuristic and incremental search in the comparison because it performs so poorly that graphing its performance ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), objective p. 2 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 5 (Abstract), p. 1 (Abstract), p. 2 (Abstract), temporal p. 2 (Abstract).
