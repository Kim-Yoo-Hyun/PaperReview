# Insights — D* Lite

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; legacy extraction flag: high; severe font-encoding corruption found in DOC-QA1); canonical paper source: https://idm-lab.org/bib/abstracts/Koen02e.html; PDF retrieval source: https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.


> 정오표: 저자 페이지는 Figure 4의 line 33″에서 no-known-path 판단의 주석을 `rhs(s_start)=∞`로 명시한다. 이번 CMU PDF의 해당 줄도 rhs를 사용한다. [저자 정오표](https://idm-lab.org/bib/abstracts/Koen02e.html), PDF p. 5.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- **p. 1 / Abstract - extractive body cue:** Building on LPA*, we therefore present D* Lite, a novel replanning method that implements the same navigation strategy as D* but is algorithmically different.
- **p. 4 / Abstract - extractive body cue:** We now use LPA* to develop D* Lite, that repeatedly determines shortest paths between the current vertex of the robot and the goal vertex as ...
- **원문 대조:** LPA*는 g를 infinity로 초기화하고 start의 rhs를 0으로 두어 priority queue에서 탐색을 시작한다. Edge cost가 바뀌면 영향을 받는 vertex의 rhs와 queue membership을 UpdateVertex로 갱신한 뒤 ComputeShortestPath를 호출한다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm; Figure 2 on p. 2).
- **p. 1 / Abstract - extractive body cue:** The resulting D* Lite algorithm is easy to understand and analyze.
- **p. 1 / Abstract - extractive body cue:** It implements the same behavior as Stentz' Focussed Dynamic A* but is algorithmically different.
- **p. 2 / Abstract - extractive body cue:** It applies to finite graph search problems on known graphs whose edge costs increase or decrease over time (which can also be used to model ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (Abstract), p. 4 (Abstract), p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / Abstract - extractive body cue:** The challenge is to identify these cells efficiently.
- **p. 4 / Abstract - extractive body cue:** They change to infinity when the robot discovers that they cannot be traversed.
- **원문 대조:** U.Update(s,k)는 queue 안 vertex s의 priority를 k로 바꾸며 같으면 아무 작업도 하지 않는다. U.Remove(s)는 s를 queue에서 제거한다. 이는 queue API 정의이며 failure나 ablation 결과가 아니다. ([PDF p. 2](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=2), Figure 2 위 priority-queue API).
- **p. 1 / Abstract - extractive body cue:** It is currently also being integrated into Mars Rover prototypes and tactical mobile robot prototypes for urban reconnaissance (Matthies et al.
- **p. 1 / Abstract - extractive body cue:** Introduction Incremental search methods, such as DynamicSWSF-FP (Ramalingam & Reps 1996), are currently not much used in artificial intelligence.
- **p. 7 / A B - extractive body cue:** Uniform discretizations can prevent one from finding a path if they are too coarse-grained (for example, because the resolution prevents one from noticing small gaps ...
- **p. 3 / Abstract - extractive body cue:** This is similar to what A* can do if it does not use backpointers.
- **Boundary to test:** They change to infinity when the robot discovers that they cannot be traversed.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite. | p. 1 (Abstract), p. 1 (Abstract) |
| Reported outcome | D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four for the vertex expansions. | p. 7 (A Performance of D* Lite), p. 7 (A B) |
| Failure/limitation | They change to infinity when the robot discovers that they cannot be traversed. | p. 4 (Abstract), p. 7 (A B) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 D* Lite is substantially shorter than D*, uses only one tie-breaking criterion when comparing priorities, which simplifies the maintenance of the priorities, and does not need nested if-statements with complex conditions that ...를 Moreover, the next theorem states that the keys of the vertices expanded by ComputeShortestPath() are monotonically nondecreasing over time.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 They change to infinity when the robot discovers that they cannot be traversed.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, path planning, incremental search, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** They change to infinity when the robot discovers that they cannot be traversed.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Since all methods move the robot in the same way and D* has already been demonstrated with great success on real robots, we only need to perform a simulation study..
3. Compare against the body-reported baseline or a matched simpler baseline: D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance measures, even more than a factor of four for the vertex expansions..
4. Report the body metric and its denominator/aggregation: Thus, D* Lite always scores zero and methods that score above zero perform worse than D* Lite..
5. **재현 계획의 원문 근거:** Edge cost 또는 g의 변경으로 영향을 받는 vertex의 rhs를 재계산하고 local consistency에 맞춰 queue를 수정한다. 이 문단은 invariant 유지 절차이며 논문이 보고한 ablation 또는 failure 실험은 아니다. ([PDF p. 3](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf#page=3), Lifelong Planning A*: The Algorithm). 실제 재현은 이 문헌 대조에서 수행하지 않았다.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract); the primary result is directionally consistent at p. 7 (A Performance of D* Lite), p. 7 (A B), p. 6 (Abstract); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 gain, insight, behavior mechanism이 D* Lite outperforms D* Lite without incremental search (that is, A*) according to all three performance ... 대비 Thus, D* Lite always scores zero and methods that score above zero perform worse than D* Lite.을 개선하고, They change to infinity when the robot discovers that they cannot be traversed. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
