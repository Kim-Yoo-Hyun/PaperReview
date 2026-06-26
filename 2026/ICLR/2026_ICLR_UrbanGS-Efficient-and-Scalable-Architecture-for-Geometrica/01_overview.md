# UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan
- Paper: https://openreview.net/forum?id=L3utaw6SD9
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## Core Idea
핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다.

## Paper-Specific Cues
- Topic cue: While 3D Gaussian Splatting (3DGS) delivers high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments introduces critical challenges in geometric consistency, ...
- Method cue: We present UrbanGS, a scalable reconstruction framework that effectively addresses these challenges for city-scale applications.
- Result cue: To improve scalability, we introduce a Spatially Adaptive Gaussian Pruning (SAGP) strategy, which dynamically adjusts Gaussian density based on local geometric complexity and visibility ...

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `3D reconstruction, calibration, and geometric consistency`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Contribution
- 3D reconstruction, calibration, and geometric consistency 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D reconstruction, 3D Vision.
- 초록에서 확인되는 주요 cue: While, Gaussian, Splatting, UrbanGS, Depth-Consistent, D-Normal, Regularization, This.
