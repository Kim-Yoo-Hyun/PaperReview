# UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

- Year/Venue: 2026 / ICLR Poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_UniSplat-Unified-Spatio-Temporal-Fusion-via-3D-Latent-Scaf/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.
- These methods typically encode inter-view correlations within the image domain via cross-attention or by constructing a multi-view stereo (MVS) cost volume, and subsequently decode the Gaussian primitives from ...

## Core Idea
- Method PixelSplat∗ (Charatan et al., 2024) MVSplat∗ (Chen et al., 2024) Omin-Scene (Wei et al., 2025) UniSplat PSNR↑ 21.51 21.61 24.27 25.37 SSIM↑ 0.616 0.658 0.736 0.765 LPIPS↓ ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Abstract Cue
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
