# Problem — NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, humanoid, Foundation Models, NVIDIA
- Official paper: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- Code/Project: https://developer.nvidia.com/isaac/gr00t
- Source audit: official NVIDIA publication and project pages checked; full data/model details remain UNVERIFIED.

## Target Problem and Assumptions

다양한 humanoid manipulation tasks와 embodiments에 adaptation 가능한 generalist robot foundation model을 구축한다.

## Closed-Loop Position

multimodal observations와 language instruction을 humanoid manipulation action chunks로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
