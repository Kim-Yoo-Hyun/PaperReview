# GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception

- Year/Venue: 2026 / ICLR Poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Authors: Xiao Zhao, Chang Liu, Mingxu Zhu, Zheyuan Zhang, Linna Song, Qingliang Luo, Chufan Guo, Kuifeng Su
- Paper: https://openreview.net/forum?id=7jXxQ9bGoU
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: The bird’s-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive multi-task ...
- Method cue: To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based ...
- Result cue: To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based ...

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision.
- 초록에서 확인되는 주요 cue: The, BEV, However, Gaussian, This, GaussianFusion, Extensive, BEVFusion.
