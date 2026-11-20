# UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2025 / CoRL
- Authors: Mingdong Wu, Long Yang, Jin Liu, Weiyao Huang, Lehong Wu, Zelin Chen, Daolin Ma, Hao Dong
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 6D pose estimation, tactile sensing, pose tracking
- Official paper: https://proceedings.mlr.press/v305/wu25d.html
- Code/Project: https://unitac2pose-web.vercel.app/

## 연구 질문과 기여

시뮬레이션에서 학습한 시각식 촉각 모델로 손안 물체의 자세와 불확실성을 추정한다.

렌더링과 실제 촉각 영상의 차이로 후보 자세의 에너지를 계산한다. 같은 모델로 자세 추정과 시간에 따른 추적을 수행한다.

## 평가 범위

시뮬레이션 학습 후 실제 촉각 영상에서 물체 종류별 자세 오차와 추적을 평가했다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=7)

## 선정 근거

새 물체의 손안 자세·추적·불확실성을 같은 촉각 추정기에서 평가하는 비교 기준이다.
