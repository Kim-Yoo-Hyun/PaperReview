# Method — HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/he2025hover/
- Code/Project: https://hover-versatile-humanoid.github.io/
- Source audit: official NVIDIA publication and project pages checked; full robot protocol remains UNVERIFIED.

## Pipeline

multi-mode command conditioning과 large-scale physics training을 결합한 unified neural controller를 학습한다.

## Interface

humanoid proprioception과 velocity/pose/keypoint commands를 whole-body joint actions로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
