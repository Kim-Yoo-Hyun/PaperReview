# Towards Learning to Complete Anything in Lidar

- Year/Venue: 2025 / ICML poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Authors: Ayça Takmaz, Cristiano Saltori, Neehar Peri, Tim Meinhardt, Riccardo de Lutio, Laura Leal-Taixé, Aljosa Osep
- Paper: https://openreview.net/forum?id=vWPzKn6usZ
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.
- Method cue: We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.
- Result cue: We show that our model can be prompted on standard benchmarks for Semantic and Panoptic Scene Completion, localize objects as (amodal) 3D bounding boxes, ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `3D vision and embodied AI`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision and embodied AI 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: sensor fusion, LiDAR, 3D Vision.
- 초록에서 확인되는 주요 cue: CAL, Complete, Anything, Lidar, Lidar-based, This, However, Different.
