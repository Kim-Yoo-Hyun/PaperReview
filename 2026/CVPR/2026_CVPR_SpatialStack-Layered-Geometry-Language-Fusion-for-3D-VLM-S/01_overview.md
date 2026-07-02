# SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

- Year/Venue: 2026 / CVPR
- Category: 3D Large Multimodal Models
- Tags: geometry, VLM, spatial reasoning
- Paper link: ./2026/CVPR/2026_CVPR_SpatialStack-Layered-Geometry-Language-Fusion-for-3D-VLM-S/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation arises from their inability to capture fine-grained 3D geometry and spatial relationships.
- While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical signals and creating ...

## Core Idea
- To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.
- We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Building upon this framework, we develop VLM-SpatialStack, a model that achieves state-of-the-art performance on multiple 3D spatial reasoning benchmarks.
- Extensive experiments and ablations demonstrate that our multi-level fusion strategy consistently enhances 3D understanding and generalizes robustly across diverse spatial reasoning tasks, establishing SpatialStack as an effective and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Building upon this framework, we develop VLM-SpatialStack, a model that achieves state-of-the-art performance on multiple 3D spatial reasoning benchmarks.
- While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical signals and creating ...
- Extensive experiments and ablations demonstrate that our multi-level fusion strategy consistently enhances 3D understanding and generalizes robustly across diverse spatial reasoning tasks, establishing SpatialStack as an effective and ...

## Abstract Cue
- Large vision-language models (VLMs) still struggle with reliable 3D spatial reasoning, a core capability for embodied and physical AI systems.
