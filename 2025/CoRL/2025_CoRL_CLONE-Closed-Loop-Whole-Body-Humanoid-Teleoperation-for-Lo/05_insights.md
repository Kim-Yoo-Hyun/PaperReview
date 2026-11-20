# Insights — CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

전신 제어에 전문가 혼합 정책을 적용한다. LiDAR 주행거리 추정으로 장시간 조작의 드리프트를 보정한다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25h/li25h.pdf#page=8)

## Researcher interpretation

전신 시연을 수집할 때 제어기와 실제 위치의 차이를 폐루프로 보정하는 시스템 기준이다.

- OmniH2O [18]의 보상·도메인 랜덤화를 바탕으로 폐루프 원격조작에 맞게 변경한다. Training 및 p.8 ablation. [pr-0602 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25h/li25h.pdf#page=5)

## 최소 비교 실험

같은 경로·조작자에서 전역 위치 보정 유무에 따른 최종 위치 오차를 비교한다.
