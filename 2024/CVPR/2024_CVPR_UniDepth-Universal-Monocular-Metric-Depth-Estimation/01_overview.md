# UniDepth: Universal Monocular Metric Depth Estimation

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Authors: Luigi Piccinelli, Yung-Hsu Yang, Christos Sakaridis, Mattia Segu, Siyuan Li, Luc Van Gool
- Paper: https://arxiv.org/abs/2403.18913
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## Core Idea
핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다.

## Paper-Specific Cues
- Topic cue: Accurate monocular metric depth estimation (MMDE) is crucial to solving downstream tasks in 3D perception and modeling.
- Method cue: We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- Result cue: Thorough evaluations on ten datasets in a zero-shot regime consistently demonstrate the superior performance of UniDepth, even when compared with methods directly trained on ...

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `3D reconstruction, calibration, and geometric consistency`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Contribution
- 3D reconstruction, calibration, and geometric consistency 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: depth, 3D Vision.
- 초록에서 확인되는 주요 cue: Accurate, MMDE, However, These, UniDepth, Departing, Our, Thorough.
