# MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_MS-GS-Multi-Appearance-Sparse-View-3D-Gaussian-Splatting-i/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators that have rapidly progressed.
- High-quality scene reconstruction and novel view synthesis from images is a long-standing research problem with wide-ranging applications in AR/VR, 3D site modeling, autonomous driving, robotics, etc.
- A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.

## Core Idea
- To eliminate unreliable depth estimation in the alignment process, we propose an SfM-prompted Semantic Alignment scheme.
- Then, to introduce multi-view constraints, we propose a series of geometry-guided supervision steps at virtual views in pixel and feature levels to encourage 3D consistency and reduce overfitting.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate that MS-GS achieves photorealistic renderings under various challenging sparse-view and multi-appearance conditions, and outperforms existing approaches significantly across different datasets.
- Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone to overfitting.
- 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs–one with single appearance and two with varying appearances.

## Limitation
- We identify that one of the limitations of 3DGS-based methods in sparse-view synthesis is the sparse point cloud initialization.
- Jointly, MS-GS offers a robust solution under challenges of limited viewpoints and varying appearances that naturally arise in real-world data.

## Contribution
- We demonstrate that MS-GS achieves photorealistic renderings under various challenging sparse-view and multi-appearance conditions, and outperforms existing approaches significantly across different datasets.
- Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone to overfitting.
- To address the lack of support due to sparse initializations, our approach is built on the geometric priors elicited from monocular depth estimations.

## Abstract Cue
- In-the-wild photo collections often contain limited volumes of imagery and exhibit multiple appearances, e.g., taken at different times of day or seasons, posing significant challenges to scene reconstruction and novel view synthesis.
