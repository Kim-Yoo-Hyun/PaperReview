# Method — UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

렌더링과 실제 촉각 영상의 차이로 후보 자세의 에너지를 계산한다.

## 학습·실행 방법

렌더링과 실제 촉각 영상의 차이로 후보 자세의 에너지를 계산한다. 같은 모델로 자세 추정과 시간에 따른 추적을 수행한다.

- Song 등 [40]의 probability flow ODE를 촉각 기반 후보 자세 갱신에 사용한다. Eq. (6). [pr-0484 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=5)
