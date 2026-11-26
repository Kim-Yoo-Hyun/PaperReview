# Method — HydroShear: Hydroelastic Shear Simulation for Tactile Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽에서 전단 모델, 센서 보정 및 표 Ⅱ 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

물체와 촉각 막 사이의 상대 자세와 변위 이력에서 촉각 전단장과 힘을 계산한다.

## 학습·실행 방법

함몰 물체 표면의 변위를 SDF로 추적하고 이력에 따라 축적된 전단과 붙었다 미끄러지는 전이를 모의한다. 이 전단 관측을 사용하는 정책을 시뮬레이션에서 강화학습한다.
