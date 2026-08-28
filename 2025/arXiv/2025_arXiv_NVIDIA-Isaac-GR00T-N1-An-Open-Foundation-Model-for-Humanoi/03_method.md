# Method — NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, humanoid, Foundation Models, NVIDIA
- Official paper: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- Code/Project: https://developer.nvidia.com/isaac/gr00t
- Source audit: official NVIDIA publication and project pages checked; full data/model details remain UNVERIFIED.

## Pipeline

VLM backbone과 diffusion/action model을 결합한 dual-system architecture 및 heterogeneous robot data training을 제시한다.

## Interface

multimodal observations와 language instruction을 humanoid manipulation action chunks로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
