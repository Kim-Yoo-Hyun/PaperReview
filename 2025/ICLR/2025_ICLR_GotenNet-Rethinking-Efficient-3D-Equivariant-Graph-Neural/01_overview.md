# GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks

- Year/Venue: 2025 / ICLR Poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, 3D Vision
- Authors: Sarp Aykent, Tian Xia
- Paper: https://openreview.net/forum?id=5wxCQDtbMo
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Understanding complex three-dimensional (3D) structures of graphs is essential for accurately modeling various properties, yet many existing approaches struggle with fully capturing the intricate ...
- Method cue: To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict ...
- Result cue: We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and high-degree property ...

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
- 초록에서 확인되는 주요 cue: Understanding, These, Geometric, Tensor, Network, GotenNet, Euclidean, Our.
