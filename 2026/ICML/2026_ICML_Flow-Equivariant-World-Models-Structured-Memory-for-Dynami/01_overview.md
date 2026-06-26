# Flow Equivariant World Models: Structured Memory for Dynamic Environments

- Year/Venue: 2026 / ICML
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, 3D Vision
- Authors: Hansen Lillemark, Benhao Huang, Fangneng Zhan, Yilun Du, T. Anderson Keller
- Paper: https://openreview.net/forum?id=jgqFnXEDGG
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Embodied systems experience the world as 'a symphony of flows': a combination of many continuous streams of sensory input coupled to self-motion, interwoven with ...
- Method cue: In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics ...
- Result cue: We demonstrate the advantage of this framework over state-of-the-art diffusion, memory-augmented, and recurrent world model architectures on 2D and 3D partially observed video world ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `geometry-aware equivariant modeling`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- geometry-aware equivariant modeling 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: equivariant, 3D Vision.
- 초록에서 확인되는 주요 cue: Embodied, These, Without, Flow, Equivariant, World, Modeling, The.
