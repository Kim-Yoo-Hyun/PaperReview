# Method — ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 IEEE 서지와 학회 원문 PDF 3–8쪽의 능동 수집·실물 실험 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

물체와 로봇 상태, 밀기 행동에서 다음 물체 상태를 예측해 kinodynamic planner의 후보를 평가한다.

## 학습·실행 방법

공칭 물리 모델의 예측 오차를 잔차로 학습하고, 예측 불확실성을 기준으로 새 상호작용을 고른다. 보정 동역학과 불확실성을 이용해 접촉을 포함한 경로를 계획한다.
