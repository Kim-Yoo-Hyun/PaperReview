# Method — TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–9쪽의 지도·학습·하드웨어 평가 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

차량 관측에서 지역 지도를 만들고 예상 통과 비용과 속도 지도를 주행 계획기에 넘긴다.

## 학습·실행 방법

차량 센서의 기하·시각 특징으로 복셀 지도를 구성한다. 조감도에서 기하, 의미, 속도 및 비용을 함께 추정하고 역강화학습과 가림 복원으로 학습한다. 계획 중 예측 불확실성을 비용에 반영한다.
