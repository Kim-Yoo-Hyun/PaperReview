# SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, 3D geometry, Transformer
- Authors: not extracted
- Paper: https://arxiv.org/abs/2006.10503
- PDF status: downloaded
- GitHub/Project: https://github.com/FabianFuchsML/se3-transformer-public

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 attention 기반 sequence modeling을 통해 장거리 의존성과 modality alignment를 scale-up 가능한 방식으로 학습하는 것이다.

## Paper-Specific Cues
- Topic cue: 초록 cue를 자동 추출하지 못함.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `sequence/representation learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- sequence/representation learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: equivariant, 3D geometry, Transformer.
