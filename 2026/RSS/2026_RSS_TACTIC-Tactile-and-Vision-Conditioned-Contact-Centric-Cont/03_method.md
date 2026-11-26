# Method — TACTIC: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽의 모델·MPC 및 실험 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

RGB-D, 팔에 분산된 촉각 및 2D 근접 표현에서 다음 접촉 배치와 힘을 예측해 팔 명령을 선택한다.

## 학습·실행 방법

행동 조건부 잠재 동역학에 접촉 Jacobian을 결합한다. 표본 기반 MPC는 접촉력을 바꿀 수 있는 방향으로 행동을 샘플링하고 목표 진행과 힘 조절을 함께 평가한다.
