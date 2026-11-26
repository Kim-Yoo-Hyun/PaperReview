# TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–9쪽의 지도·학습·하드웨어 평가 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RSS
- Authors: Samuel Triest, Amirreza Shaban, David Fan, Wenshan Wang, Sebastian Scherer
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Navigation, traversability, inverse reinforcement learning, uncertainty estimation, BEV
- Official paper: https://roboticsproceedings.org/rss22/p070.html
- Code/Project: not identified

## 연구 질문과 기여

고속 오프로드 주행에서는 가려진 지형의 상태와 통과 위험이 함께 달라진다.

차량 센서의 기하·시각 특징으로 복셀 지도를 구성한다. 조감도에서 기하, 의미, 속도 및 비용을 함께 추정하고 역강화학습과 가림 복원으로 학습한다. 계획 중 예측 불확실성을 비용에 반영한다.

## 평가 범위

오프라인 계획 품질과 실물 ATV 주행을 분리해 평가했다. 표 Ⅵ은 안전 운전자 개입과 충돌, 주행 속도를 따로 기록한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p070.pdf#page=8)

## 선정 근거

시각적 불확실성이 실제 이동 경로와 안전에 미치는 영향을 검증하는 내비게이션 기준선이다.
