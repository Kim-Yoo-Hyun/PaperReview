# Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

- Year/Venue: 2025 / 3DV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, point cloud, 3D Vision
- Authors: Lisa Weijler, Pedro Hermosilla
- Paper: https://3dvconf.github.io/2025/accepted-papers/
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative ...
- Method cue: Our experiments show that our approach achieves competitive or superior performance across a range of datasets and tasks, including object classification and semantic segmentation, ...
- Result cue: Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `geometry-aware equivariant modeling`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- geometry-aware equivariant modeling 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: equivariant, point cloud, 3D Vision.
- 초록에서 확인되는 주요 cue: Extending, Further, However, While, This, Our.
