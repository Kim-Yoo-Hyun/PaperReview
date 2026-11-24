# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

절단과 봉합으로 부착 관계가 변하는 실험은 시뮬레이션에서 수행했다. 동물 조직 실험은 스테레오 내시경 영상에서 봉합으로 고정된 부위를 추정하는 과제였다. [PDF 2쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=2) · [PDF 10쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=10) · [PDF 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=12)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## Dataset / Benchmark Role

실제 조직에서 관찰한 영상과 시뮬레이션에서 생성한 부착 상태의 정답을 구분해 평가했다. [PDF 2쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=2) · [PDF 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=12)

## Metrics and Success Definition

영상 기반 부착 부위의 검출을 평가했다. 추정한 부착 강도는 XPBD 시뮬레이터에 정의된 값이며 물리 단위로 보정된 힘이 아니다. [PDF 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=12)

## Proposed Evaluation — Researcher Interpretation

정보 이득 probe와 단순 displacement probe를 task outcome으로 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html).
