# VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VLA-Cache-Efficient-Vision-Language-Action-Manipulation-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To mitigate the extensive cost of VLA models, existing works often adopt generic acceleration techniques, such as model lightweighting , quantization , and early-exit .
- Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem , with traditional reinforcement learning approaches often suffering from poor ...
- While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics of VLA tasks.

## Core Idea
- To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens ...
- When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency architectures and delivering additive ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15% ...
- Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM and FastV on OpenVLA as compared methods in the LIBERO benchmark.
- In simulation, we evaluate VLA-Cache on three open-source VLA models: OpenVLA , OpenVLA-OFT and CogAct , using the LIBERO benchmark and SIMPLER environment , respectively.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens ...
- Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15% ...
- This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.

## Abstract Cue
- Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner.
