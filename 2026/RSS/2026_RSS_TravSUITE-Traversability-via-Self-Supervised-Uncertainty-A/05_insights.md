# Insights — TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–9쪽의 지도·학습·하드웨어 평가 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

차량 센서의 기하·시각 특징으로 복셀 지도를 구성한다. 조감도에서 기하, 의미, 속도 및 비용을 함께 추정하고 역강화학습과 가림 복원으로 학습한다. 계획 중 예측 불확실성을 비용에 반영한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p070.pdf#page=8)

## Researcher interpretation

시각적 불확실성이 실제 이동 경로와 안전에 미치는 영향을 검증하는 내비게이션 기준선이다.

## 최소 비교 실험

같은 주행 구간에서 복원 기능과 불확실성 비용을 각각 끄고 계획 속도와 개입 횟수를 비교한다.
