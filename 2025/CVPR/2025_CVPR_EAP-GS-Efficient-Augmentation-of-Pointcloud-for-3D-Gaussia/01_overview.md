# EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction

- Year/Venue: 2025 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_EAP-GS-Efficient-Augmentation-of-Pointcloud-for-3D-Gaussia/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In practice, a sufficient number of images are often difficult to obtain due to various limitations.
- Furthermore, our APA can be framed as a modular augmentation to existing methods with minimal overhead.
- We implemented APA by extending Structure-From-Motion (SFM) to focus on pointcloud generation in regions with complex structure but sparse pointcloud distribution, which significantly increases the number of valuable ...

## Core Idea
- Specifically, we introduce an Attentional Pointcloud Augmentation (APA) technique, which retains two-view tracks as an option for pointcloud generation.
- To address this, we propose EAP-GS, a method to enhance initialization for fast, accurate, and stable few-shot scene reconstruction.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results from various indoor and outdoor scenes demonstrate that the proposed EAP-GS achieves outstanding scene reconstruction performance and surpasses state-of-the-art methods.
- However, due to the slow training and inference speed of NeRF-based methods, 3DGS stands out for its rapid reconstruction speed and real-time rendering capabilities, while still delivering high-quality ...
- 3D Gaussian splatting (3DGS) has shown impressive performance in 3D scene reconstruction.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results from various indoor and outdoor scenes demonstrate that the proposed EAP-GS achieves outstanding scene reconstruction performance and surpasses state-of-the-art methods.
- Specifically, we introduce an Attentional Pointcloud Augmentation (APA) technique, which retains two-view tracks as an option for pointcloud generation.
- However, due to the slow training and inference speed of NeRF-based methods, 3DGS stands out for its rapid reconstruction speed and real-time rendering capabilities, while still delivering high-quality ...

## Abstract Cue
- 3D Gaussian splatting (3DGS) has shown impressive performance in 3D scene reconstruction.
