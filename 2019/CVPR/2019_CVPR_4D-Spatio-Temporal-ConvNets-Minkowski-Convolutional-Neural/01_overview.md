# 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

- Year/Venue: 2019 / CVPR
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision
- Authors: Christopher Choy, JunYoung Gwak, Silvio Savarese
- Paper: https://arxiv.org/abs/1904.08755
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: In many robotics and VR/AR applications, 3D-videos are readily-available sources of input (a continuous sequence of depth images, or LIDAR scans).
- Method cue: In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- Result cue: Experimentally, we show that convolutional neural networks with only generalized 3D sparse convolutions can outperform 2D or 2D-3D hybrid methods by a large margin.

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `core 3D geometry and scene representation learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- core 3D geometry and scene representation learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision.
- 초록에서 확인되는 주요 cue: LIDAR, However, For, Experimentally, Also.
