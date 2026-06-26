# Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, Diffusion, Generation, 3D Vision
- Authors: Dekai Zhu, Yixuan Hu, Youquan Liu, Dongyue Lu, Lingdong Kong, Slobodan Ilic
- Paper: https://openreview.net/forum?id=SoqzNbcBjy
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: Leveraging diffusion models, 3D LiDAR scene generation has achieved great success in both range-view and voxel-based representations.
- Method cue: To address this limitation while preserving the advantages of range-view representations, such as computational efficiency and simplified network design, we propose Spiral, a novel ...
- Result cue: Leveraging diffusion models, 3D LiDAR scene generation has achieved great success in both range-view and voxel-based representations.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: sensor fusion, LiDAR, semantic, alignment, Diffusion, Generation.
- 초록에서 확인되는 주요 cue: Leveraging, LiDAR, While, Relying, Spiral, Furthermore, Experiments, SemanticKITTI.
