# Evaluation — HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 평가 조건

다단 선반의 실제 파지와 훈련 범위 밖 높이에 대한 시뮬레이션 결과를 구분한다. [원문 및 평가 절](https://arxiv.org/pdf/2611.01659#page=8)

## 해석할 때 확인할 조건

같은 높이·물체에서 시점 탐색 효과와 전신 동역학 필터의 효과를 따로 비교한다.

## 저자가 밝힌 한계

실제 배포에서는 양발 지지를 유지해 발을 떼지 않는다. 팔과 몸통 기울임으로 닿지 않는 목표는 위치 재조정이 필요하다. [원문](https://arxiv.org/pdf/2611.01659#page=11)
