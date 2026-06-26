# Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath
- Paper: https://openreview.net/forum?id=nI7wKr4eop
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Learning effective multi-modal 3D representations of objects is essential for numerous applications, such as augmented reality and robotics.
- Method cue: In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and ...
- Result cue: Evaluations on two challenging real-world datasets demonstrate that Object-X produces high-fidelity novel-view synthesis comparable to standard 3D Gaussian Splatting, while significantly improving geometric accuracy.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `3D vision and embodied AI`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision and embodied AI 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision.
- 초록에서 확인되는 주요 cue: Learning, Existing, Object-X, The, Gaussian, Splatting-based, Evaluations, Splatting.
