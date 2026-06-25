# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

- Year/Venue: 2023 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: Gaussian Splatting, 3D reconstruction, representation
- Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- Paper: https://arxiv.org/abs/2308.04079
- PDF status: downloaded
- GitHub/Project: https://github.com/graphdeco-inria/gaussian-splatting

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos.
- Method cue: We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= ...
- Result cue: For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates.

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `core 3D geometry and scene representation learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- core 3D geometry and scene representation learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, 3D reconstruction, representation.
- 초록에서 확인되는 주요 cue: Radiance, Field, However, For, First, Gaussians, Second, Third.
