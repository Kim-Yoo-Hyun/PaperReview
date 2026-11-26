# Insights — TACTIC: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽의 모델·MPC 및 실험 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

행동 조건부 잠재 동역학에 접촉 Jacobian을 결합한다. 표본 기반 MPC는 접촉력을 바꿀 수 있는 방향으로 행동을 샘플링하고 목표 진행과 힘 조절을 함께 평가한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p060.pdf#page=8)

## Researcher interpretation

말단 센서가 놓치는 팔 링크 접촉을 제어에 사용하는 직접 비교 기준이다.

## 최소 비교 실험

같은 팔 모델과 목표를 두고 전체 촉각과 손목 센서만 제공한 경우의 과제 진행 및 최대 링크 접촉력을 비교한다.
