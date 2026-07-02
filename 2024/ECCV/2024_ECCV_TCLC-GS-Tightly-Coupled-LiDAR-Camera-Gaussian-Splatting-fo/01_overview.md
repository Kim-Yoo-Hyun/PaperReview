# TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_TCLC-GS-Tightly-Coupled-LiDAR-Camera-Gaussian-Splatting-fo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Urban-level reconstruction and rendering present significant challenges due to the vast scale of the unbounded environments and the sparse nature of the captured data.

## Core Idea
- Comprehensive evaluations conducted on the Waymo Open Dataset and nuScenes Dataset validate our method’s stateof-the-art (SOTA) performance.
- During the information as supervision, which enhances the training process by learning of a robust geometry.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Utilizing a single NVIDIA RTX 3090 Ti, our method demonstrates fast training and achieves real-time RGB and depth rendering at 90 FPS in resolution of 1920×1280 (Waymo), and ...
- For our experiments, we selected six challenging recording sequences from this dataset, utilizing surrounding views captured by three cameras and corresponding data

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Utilizing a single NVIDIA RTX 3090 Ti, our method demonstrates fast training and achieves real-time RGB and depth rendering at 90 FPS in resolution of 1920×1280 (Waymo), and ...
- Comprehensive evaluations conducted on the Waymo Open Dataset and nuScenes Dataset validate our method’s stateof-the-art (SOTA) performance.
- During the information as supervision, which enhances the training process by learning of a robust geometry.

## Abstract Cue
- Most 3D Gaussian Splatting (3D-GS) based methods for urban scenes initialize 3D Gaussians directly with 3D LiDAR points, which not only underutilizes LiDAR data capabilities but also overlooks the potential advantages of fusing LiDAR with camera data.
