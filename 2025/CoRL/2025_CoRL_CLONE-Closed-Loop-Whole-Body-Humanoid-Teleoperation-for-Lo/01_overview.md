# CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2025 / CoRL
- Authors: Yixuan Li, Yutang Lin, Jieming Cui, Tengyu Liu, Wei Liang, Yixin Zhu, Siyuan Huang
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: humanoid, whole-body control, teleoperation
- Official paper: https://proceedings.mlr.press/v305/li25h.html
- Code/Project: https://humanoid-clone.github.io/

## 연구 질문과 기여

전신 원격조작에서 상·하체를 함께 제어하고 누적 위치 오차를 수정한다.

전신 제어에 전문가 혼합 정책을 적용한다. LiDAR 주행거리 추정으로 장시간 조작의 드리프트를 보정한다.

## 평가 범위

실물 Unitree G1에서 장시간 원격조작과 이동 중 위치 드리프트를 비교했다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25h/li25h.pdf#page=8)

## 선정 근거

전신 시연을 수집할 때 제어기와 실제 위치의 차이를 폐루프로 보정하는 시스템 기준이다.
