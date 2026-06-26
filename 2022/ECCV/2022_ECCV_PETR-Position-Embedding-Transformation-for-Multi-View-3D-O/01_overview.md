# PETR: Position Embedding Transformation for Multi-View 3D Object Detection

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision
- Authors: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
- Paper: https://arxiv.org/abs/2203.05625
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.
- Method cue: In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.
- Result cue: PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.

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
- 초록에서 확인되는 주요 cue: PETR, Object, NDS, Code.
