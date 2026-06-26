# GeoCalib: Learning Single-image Calibration with Geometric Optimization

- Year/Venue: 2024 / ECCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, 3D Vision
- Authors: Alexander Veicht*, Paul-Edouard Sarlin*, Philipp Lindenberger, Marc Pollefeys
- Paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5636_ECCV_2024_paper.php
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## Core Idea
핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다.

## Paper-Specific Cues
- Topic cue: 초록 cue를 자동 추출하지 못함.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map.

## Main Claims
- 논문은 `3D reconstruction, calibration, and geometric consistency`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Contribution
- 3D reconstruction, calibration, and geometric consistency 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: geometry, 3D Vision.
