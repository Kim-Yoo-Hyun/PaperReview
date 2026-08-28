# Problem — SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / Science Robotics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Motion Tracking, NVIDIA
- Official paper: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Code/Project: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Source audit: official NVIDIA publication page and journal status checked; full training/evaluation details remain UNVERIFIED.

## Target Problem and Assumptions

대규모 diverse motion을 실제 humanoid가 robust하고 자연스럽게 추종하는 데 필요한 controller scaling을 다룬다.

## Closed-Loop Position

reference human motion과 humanoid proprioception을 real-time joint actions로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
