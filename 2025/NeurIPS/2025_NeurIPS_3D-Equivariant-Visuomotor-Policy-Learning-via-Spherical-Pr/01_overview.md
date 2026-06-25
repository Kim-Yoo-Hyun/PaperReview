# 3D Equivariant Visuomotor Policy Learning via Spherical Projection

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Authors: Boce Hu, Dian Wang, David Klee, Heng Tian, Xupeng Zhu, Haojie Huang, Robert Platt, Robin Walters
- Paper: https://openreview.net/forum?id=kXJd4JxF34
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.
- Method cue: We perform extensive experiments in both simulation and the real world that demonstrate that our method consistently outperforms strong baselines in terms of both ...
- Result cue: Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `geometry-aware equivariant modeling`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- geometry-aware equivariant modeling 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, 3D Vision, equivariant.
- 초록에서 확인되는 주요 cue: Equivariant, However, This, RGB, GoPro, Our, Image-to-Sphere, Policy.
