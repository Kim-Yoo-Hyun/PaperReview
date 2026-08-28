# Problem — HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/he2025hover/
- Code/Project: https://hover-versatile-humanoid.github.io/
- Source audit: official NVIDIA publication and project pages checked; full robot protocol remains UNVERIFIED.

## Target Problem and Assumptions

locomotion, pose/keypoint tracking 등 여러 whole-body commands를 하나의 real humanoid controller가 안정적으로 수행한다.

## Closed-Loop Position

humanoid proprioception과 velocity/pose/keypoint commands를 whole-body joint actions로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
