# Fully Convolutional Geometric Features

- Year/Venue: 2019 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D Vision, registration, 3D geometry, representation
- Paper link: ./2019/ICCV/2019_ICCV_Fully-Convolutional-Geometric-Features/paper.pdf
- Code/Project: https://github.com/chrischoy/FCGF
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing learning-based features rely on low-level geometric characteristics as input: e.g., angular deviation , point distributions , or volumetric distance functions .
- This process is computationally expensive and features are extracted only at downsampled interest points, thus lowering the spatial resolution for subsequent registration steps.

## Core Idea
- In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- We experimentally validate our approach on both indoor and outdoor datasets.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Fullyconvolutional geometric features achieve state-of-the-art accuracy without requiring prepossessing, are compact (32 dimensions), and are 290 times faster than the most accurate prior method.
- We also present new metric learning losses that dramatically improve performance.
- State-of-the-art methods require computing low-level features as input or extracting patch-based features with limited receptive field.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Fullyconvolutional geometric features achieve state-of-the-art accuracy without requiring prepossessing, are compact (32 dimensions), and are 290 times faster than the most accurate prior method.
- In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- We experimentally validate our approach on both indoor and outdoor datasets.

## Abstract Cue
- Extracting geometric features from 3D scans or point clouds is the first step in applications such as registration, reconstruction, and tracking.
