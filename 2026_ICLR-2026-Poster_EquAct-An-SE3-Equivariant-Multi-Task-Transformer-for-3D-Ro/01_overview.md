# EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation

- Year/Venue: 2026 / ICLR 2026 Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Authors: Xupeng Zhu, Yu Qi, Yizhe Zhu, Robin Walters, Robert Platt
- Paper: https://openreview.net/forum?id=d1wuA8oIH0
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Multi-task manipulation policy often builds on transformer's ability to jointly process language instructions and 3D observations in a shared embedding space.
- Method cue: To address this issue, we propose EquAct, which is theoretically guaranteed to generalize to novel 3D scene transformations by leveraging SE(3) equivariance shared across ...
- Result cue: Finally, EquAct demonstrates strong spatial generalization ability and achieves state-of-the-art across $18$ RLBench tasks with both SE(3) and SE(2) scene perturbations, different amounts of ...

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
- 초록에서 확인되는 주요 cue: Multi-task, However, Policies, EquAct, U-net, Fourier, Feature-wise, Linear.
