# CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences

- Year/Venue: 2025 / 3DV
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Authors: Huajian Zeng, Maolin Gao, Daniel Cremers
- Paper: https://3dvconf.github.io/2025/accepted-papers/
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: The interest in matching non-rigidly deformed shapes represented as raw point clouds is rising due to the proliferation of low-cost 3D sensors.
- Method cue: We propose to tackle these challenges by learning a new shape representation -- a per-point high dimensional embedding, in an embedding space where semantically ...
- Result cue: Extensive experiments demonstrate new state-of-the-art results and robustness in numerous challenging non-rigid shape matching benchmarks and show its great potential in other shape analysis ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `3D vision and embodied AI`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision and embodied AI 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: point cloud, 3D Vision.
- 초록에서 확인되는 주요 cue: The, Yet, Consequently, Extensive.
