# Method — CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

전신 제어에 전문가 혼합 정책을 적용한다.

## 학습·실행 방법

전신 제어에 전문가 혼합 정책을 적용한다. LiDAR 주행거리 추정으로 장시간 조작의 드리프트를 보정한다.

- OmniH2O [18]의 보상·도메인 랜덤화를 바탕으로 폐루프 원격조작에 맞게 변경한다. Training 및 p.8 ablation. [pr-0602 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25h/li25h.pdf#page=5)
