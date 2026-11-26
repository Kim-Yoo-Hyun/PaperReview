# Insights — HydroShear: Hydroelastic Shear Simulation for Tactile Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽에서 전단 모델, 센서 보정 및 표 Ⅱ 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

함몰 물체 표면의 변위를 SDF로 추적하고 이력에 따라 축적된 전단과 붙었다 미끄러지는 전이를 모의한다. 이 전단 관측을 사용하는 정책을 시뮬레이션에서 강화학습한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p155.pdf#page=9)

## Researcher interpretation

서랍 같은 미끄럼 과제에서 촉각 모델의 물리적 차이가 실물 정책에 전달되는지 비교할 수 있다.

## 최소 비교 실험

동일한 학습·제어 조건에서 전단 관측의 이력만 제거하고 서랍 손잡이 미끄럼과 성공률을 비교한다.
