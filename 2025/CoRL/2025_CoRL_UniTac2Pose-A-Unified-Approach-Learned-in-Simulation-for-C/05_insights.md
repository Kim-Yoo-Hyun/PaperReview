# Insights — UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

렌더링과 실제 촉각 영상의 차이로 후보 자세의 에너지를 계산한다. 같은 모델로 자세 추정과 시간에 따른 추적을 수행한다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=7)

## Researcher interpretation

새 물체의 손안 자세·추적·불확실성을 같은 촉각 추정기에서 평가하는 비교 기준이다.

- Song 등 [40]의 probability flow ODE를 촉각 기반 후보 자세 갱신에 사용한다. Eq. (6). [pr-0484 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=5)

## 최소 비교 실험

가린 면과 대칭 자세에서 추정기의 불확실성이 실제 오차와 함께 증가하는지 본다.
