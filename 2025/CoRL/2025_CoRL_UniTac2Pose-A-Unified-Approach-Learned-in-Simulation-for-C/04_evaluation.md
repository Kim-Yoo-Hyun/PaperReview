# Evaluation — UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 평가 조건

시뮬레이션 학습 후 실제 촉각 영상에서 물체 종류별 자세 오차와 추적을 평가했다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=7)

## 해석할 때 확인할 조건

가린 면과 대칭 자세에서 추정기의 불확실성이 실제 오차와 함께 증가하는지 본다.

## 저자가 밝힌 한계

새 자세를 얻는 초기 추정에는 반복 디노이징이 필요해 추적보다 느리다. [원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=9)
