# D* Lite

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf.
> PDF retrieval source: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2002 / AAAI
- Authors: Sven Koenig, Maxim Likhachev
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, path planning, incremental search, Navigation
- Official paper: https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf
- Full-text retrieval: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.


> 정오표: 저자 페이지는 Figure 4의 line 33″에서 no-known-path 판단의 주석을 `rhs(s_start)=∞`로 명시한다. 이번 CMU PDF의 해당 줄도 rhs를 사용한다. [저자 정오표](https://idm-lab.org/bib/abstracts/Koen02e.html), PDF p. 5.

## Why This Paper Is Here

문제 관련 발췌 — The challenge is to identify these cells efficiently.

방법 관련 발췌 — To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Incremental heuristic search methods use heuristics to focus their search and reuse information from previous searches to find solutions to series of similar search tasks ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we apply Lifelong Planning A* to robot navigation in unknown terrain, including goal-directed navigation in unknown terrain and mapping of unknown terrain.
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 1 / Abstract - extractive body cue:** We prove properties about D* Lite and demonstrate experimentally the advantages of combining incremental and heuristic search for the applications studied.
- **p. 2 / Abstract - extractive body cue:** The challenge is to identify these cells efficiently.
- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- **p. 1 / Abstract - extractive body cue:** Building on LPA*, we therefore present D* Lite, a novel replanning method that implements the same navigation strategy as D* but is algorithmically different.
- **p. 4 / Abstract - extractive body cue:** We now use LPA* to develop D* Lite, that repeatedly determines shortest paths between the current vertex of the robot and the goal vertex as ...
- **원문 대조:** LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2).
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 2 / Abstract - extractive body cue:** It applies to finite graph search problems on known graphs whose edge costs increase or decrease over time (which can also be used to model ...
- **p. 3 / Abstract - extractive body cue:** Similarity to A* When we described LPA*, we already pointed out strong algorithmic similarities between LPA* and A*.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | D* Lite is substantially shorter than D*, uses only one tie-breaking criterion when comparing priorities, which simplifies the maintenance of the priorities, and does not need nested if-statements with complex conditions that ... | camera/depth stream, pose, map와 language goal | p. 1 (Abstract), p. 3 (Abstract) |
| State/latent | Lite, substantially, shorter, uses, only, tie-breaking, criterion, when, comparing, priorities, simplifies, maintenance | robot pose, free-space/semantic map와 local goal | p. 1 (Abstract), p. 3 (Abstract), p. 5 (Abstract) |
| Output/action | Moreover, the next theorem states that the keys of the vertices expanded by ComputeShortestPath() are monotonically nondecreasing over time. | collision-free trajectory 또는 velocity command | p. 3 (Abstract), p. 5 (Abstract), p. 1 (Abstract) |
| Algorithm invariant maintenance | 원문 대조: LPA*의 UpdateVertex는 start 이외 vertex의 rhs를 predecessor 기반 one-step lookahead로 계산한다. Queue의 기존 항목을 제거한 뒤 g≠rhs인 vertex만 새 key로 삽입한다. 손상된 의사코드 문자열을 실행 가능한 코드로 사용하지 않는다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2, UpdateVertex lines 06–08) | LPA* queue update; 안전·localization·latency metric 아님 | [PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2, UpdateVertex lines 06–08 |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- **p. 1 / Abstract - extractive body cue:** Building on LPA*, we therefore present D* Lite, a novel replanning method that implements the same navigation strategy as D* but is algorithmically different.
- **p. 4 / Abstract - extractive body cue:** We now use LPA* to develop D* Lite, that repeatedly determines shortest paths between the current vertex of the robot and the goal vertex as ...
- **p. 7 / A Performance of D* Lite - extractive body cue:** D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four for ...
- **p. 7 / A B - extractive body cue:** These results also confirm earlier experimental results that D* can outperform A* for goal-directed navigation in unknown terrain by one order of magnitude or more ...
- **p. 6 / Abstract - extractive body cue:** In the following, we study to which degree the combination of incremental and heuristic search that D* Lite implements outperforms incremental or heuristic searches individually.
- **p. 6 / Abstract - extractive body cue:** Since the actual planning times are implementation and machine dependent, they make it difficult for others to reproduce the results of our performance comparison.
- **원문 대조:** Succ(s)는 vertex s의 successor 집합이고 Pred(s)는 predecessor 집합이다. 탐색 대상은 유한 graph이며 edge cost의 증가·감소를 허용한다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Lifelong Planning A*, graph notation).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A Performance of D* Lite), p. 7 (A B) |
| Embodiment/environment | Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, we only need to perform a simulation study. | hardware/simulator version and reset protocol | p. 6 (Abstract), p. 2 (Abstract) |
| Dataset/benchmark | They change to infinity when the robot discovers that they cannot be traversed. | role, split, size and leakage | p. 6 (Abstract), p. 2 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |
| Metric | Thus, D* Lite always scores zero and methods that score above zero perform worse than D* Lite. | definition, denominator, direction and uncertainty | p. 6 (Abstract), p. 5 (Abstract), p. 5 (Abstract) |
| Baseline/ablation | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four for the vertex expansions. | fair input/data/compute/action matching | p. 7 (A Performance of D* Lite), p. 3 (Abstract), p. 6 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **p. 7 / A B - extractive body cue:** Uniform discretizations can prevent one from finding a path if they are too coarse-grained (for example, because the resolution prevents one from noticing small gaps ...
- **원문 대조:** U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API).
- **p. 3 / Abstract - extractive body cue:** This is similar to what A* can do if it does not use backpointers.
- **p. 3 / Abstract - extractive body cue:** Note that, in an actual implementation, Initialize() only needs to initialize a vertex when it encounters it during the search and thus does not need ...
- **p. 4 / Abstract - extractive body cue:** Theorem 6 ComputeShortestPath() does not expand any vertices whose g-values were equal to their respective start distances before ComputeShortestPath() was called.
- **p. 5 / Abstract - extractive body cue:** Then, the order of the vertices in the priority queue does not change after the robot moves and the priority queue does not need to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 3 (Abstract)이다.
