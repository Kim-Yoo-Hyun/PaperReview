# Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, 3D Vision
- Authors: Haoyu Wu, Diankun Wu, Tianyu He, Junliang Guo, Yang Ye, Yueqi Duan, Jiang Bian
- Paper: https://openreview.net/forum?id=ULXYZCms41
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: Videos inherently represent 2D projections of a dynamic 3D world.
- Method cue: To bridge this gap between video diffusion models and the underlying 3D nature of the physical world, we propose Geometry Forcing, a simple yet ...
- Result cue: Experimental results demonstrate that our method substantially improves visual quality and 3D consistency over the baseline methods.

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Diffusion, Generation, 3D Vision.
- 초록에서 확인되는 주요 cue: Videos, However, Geometry, Forcing, Our, Angular, Alignment, Scale.
