# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

실제 장면을 촬영한 영상에서 조작 가능한 장면을 재구성한다. 정책에 필요한 관절 제어와 카메라 시점을 시뮬레이터에서 맞추는 것이 평가의 전제다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=4)

DROID Franka의 실물 기준은 환경·정책당 20회다. 시뮬레이션에서는 평가용 장면·물체와 겹치지 않는 환경으로 정책을 1,000스텝 공동학습한 뒤 과제당 50회 실행한다. 양쪽의 과제 진행도 기준을 맞춘다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=6)

실물과 시뮬레이션에서 측정한 정책 성능의 Pearson 상관계수와 Mean Maximum Rank Violation(MMRV)을 보고한다. MMRV는 각 정책에 대해 시뮬레이션에서 순위가 뒤바뀐 상대 정책들과의 실물 점수 차이 중 최댓값을 구한 뒤 전체 정책에 걸쳐 평균한다. 순위 역전이 없으면 0이다. [지표 정의와 식 (1)](https://roboticsproceedings.org/rss22/p062.pdf#page=3) · [평가 절차](https://roboticsproceedings.org/rss22/p062.pdf#page=6)

## Proposed Evaluation — Researcher Interpretation

동일 checkpoint들을 동일 task의 실환경·재구성 환경에서 비교하고 co-training 전후 순위를 별도로 계산한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
