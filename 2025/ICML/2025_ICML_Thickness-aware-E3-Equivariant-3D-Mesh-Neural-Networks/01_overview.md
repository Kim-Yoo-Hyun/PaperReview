# Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D reconstruction, equivariant, 3D Vision
- Authors: Sungwon Kim, Namkyeong Lee, Yunyoung Doh, Seungmin Shin, Guimok Cho, Seung-Won Jeon, Sangkook Kim, Chanyoung Park
- Paper: https://openreview.net/forum?id=Ya2ksKuNMh
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Mesh-based 3D static analysis methods have recently emerged as efficient alternatives to traditional computational numerical solvers, significantly reducing computational costs and runtime for various ...
- Method cue: In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects ...
- Result cue: Evaluations on a real-world industrial dataset demonstrate the superior performance of T-EMNN in accurately predicting node-level 3D deformations, effectively capturing thickness effects while maintaining ...

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `geometry-aware equivariant modeling`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- geometry-aware equivariant modeling 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D reconstruction, equivariant, 3D Vision.
- 초록에서 확인되는 주요 cue: Mesh-based, However, This, Thickness-aware, Equivariant, Mesh, Neural, Network.
