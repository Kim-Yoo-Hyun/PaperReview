# Method — SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / Science Robotics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Motion Tracking, NVIDIA
- Official paper: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Code/Project: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Source audit: official NVIDIA publication page and journal status checked; full training/evaluation details remain UNVERIFIED.

## Pipeline

large motion corpus와 scalable physics learning을 이용해 general motion-tracking whole-body policy를 학습한다.

## Interface

reference human motion과 humanoid proprioception을 real-time joint actions로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
