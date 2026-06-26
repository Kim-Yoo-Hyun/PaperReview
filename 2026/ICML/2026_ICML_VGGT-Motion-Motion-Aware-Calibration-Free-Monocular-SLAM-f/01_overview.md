# VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

- Year/Venue: 2026 / ICML spotlight
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, depth, 3D Vision
- Authors: Zhuang Xiong, Chen Zhang, Qingshan Xu, Wenbing Tao
- Paper: https://openreview.net/forum?id=GyRMbsYFiG
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## Core Idea
핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다.

## Paper-Specific Cues
- Topic cue: Despite recent progress in calibration-free monocular SLAM via 3D vision foundation models, scale drift remains severe on long sequences.
- Method cue: To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.
- Result cue: By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `3D reconstruction, calibration, and geometric consistency`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Contribution
- 3D reconstruction, calibration, and geometric consistency 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: geometry, depth, 3D Vision.
- 초록에서 확인되는 주요 cue: Despite, SLAM, Motion-agnostic, VGGT-Motion, Specifically, Sim, Finally, Experiments.
