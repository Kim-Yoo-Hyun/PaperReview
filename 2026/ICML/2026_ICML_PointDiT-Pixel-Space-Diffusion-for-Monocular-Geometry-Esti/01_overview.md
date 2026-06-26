# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

- Year/Venue: 2026 / ICML
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, depth, point cloud, 3D Vision
- Authors: Haofei Xu, Rundi Wu, Philipp Henzler, Nikolai Kalischek, Michael Oechsle, Fabian Manhardt, Marc Pollefeys, Andreas Geiger
- Paper: https://openreview.net/forum?id=hQWwTWGAyu
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions (e.g., MoGe), or necessitate compressing geometry into latent spaces (e.g., ...
- Method cue: We introduce a minimalist pixel-space Diffusion Transformer built on a plain ViT, which operates directly on raw 3D point map patches and is conditioned ...
- Result cue: State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions (e.g., MoGe), or necessitate compressing geometry into latent spaces (e.g., ...

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Diffusion, Generation, depth, point cloud, 3D Vision.
- 초록에서 확인되는 주요 cue: State-of-the-art, MoGe, GeometryCrafter, Diffusion, Transformer, ViT, DINOv3, Unlike.
