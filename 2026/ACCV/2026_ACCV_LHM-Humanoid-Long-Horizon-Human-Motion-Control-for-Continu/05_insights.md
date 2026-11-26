# Insights — LHM-Humanoid: Long-Horizon Human Motion Control for Continuous Object Transport in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1–3.3, §4.2–4.3, Tables 1 and 3; ACCV 2026 programme 검토. [방법·평가 원문](https://arxiv.org/html/2508.16943)

## Paper-supported conclusion

첫 물체를 놓고 물러나는 교사와 그 상태에서 다음 과업을 시작하는 교사를 RL로 학습해 하나의 정책으로 증류한다. 이 정책의 스텝별 행동을 다시 1인칭 RGB·언어 학생에게 DAgger로 가르친다. [원문 및 평가 절](https://arxiv.org/html/2508.16943)

## Researcher interpretation

HumanVLA의 단일 재배치에서 다음 운반을 시작할 수 있는 자세까지 연구 단위를 넓힌 비교점이다. 실물 전신 제어나 자율적인 언어 하위 목표 생성을 입증하는 자료로 확대하지 않는다.

## 최소 비교 실험

같은 두 물체 배치에서 손을 뗀 직후의 자세를 맞추고, 다음 물체 접근과 두 작업 전체 성공을 따로 비교한다.

## 검증 질문

두 번째 사이클 실패가 첫 물체에서 늦게 손을 뗀 탓인지 다음 목표를 시각적으로 놓친 탓인지 분리하는 지표가 필요하다.
