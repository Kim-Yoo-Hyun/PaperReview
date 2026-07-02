# SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_SDGS-Spatial-Difference-Guided-Gaussian-Splatting-for-Simu/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Crucially, it maintains robust tracking and reconstruction under extreme high-speed motion where existing RGB-based approaches fail.
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...
- This is fundamentally due to the inherent limitations of traditional imaging mechanisms of vision sensors and their dense descriptors.

## Core Idea
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...
- Our SD Gaussian descriptor with DT enhances overall convergence basin and our approach is the only method that provide sparse reconstruction using SD.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This makes it challenging for the system to achieve both efficiency and robustness in real world, making it difficult to balance reconstruction accuracy and speed.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...
- Leveraging a state-of-theart dual-channel vision sensor that generates blur-less and high-frame-rate spatial difference outputs, our method produces accurate and detailed geometric reconstructions in challenging conditions.
- It is worth noting that our method is also compatible with traditional RGB cameras, while maintaining competitive tracking accuracy.

## Abstract Cue
- 3D Gaussian Splatting (3DGS) pioneers explicit scene representation, enabling photorealistic, real-time 3D reconstruction.
