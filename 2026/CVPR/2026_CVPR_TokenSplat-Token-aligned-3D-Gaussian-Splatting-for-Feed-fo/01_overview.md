# TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_TokenSplat-Token-aligned-3D-Gaussian-Splatting-for-Feed-fo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Furthermore, most existing pose-free methods rely on pixel-aligned 3DGS heads that generate Gaussians at pixellevel gra
- Pose estimation via structurefrom-motion (SfM) is computationally expensive and prone to failure in challenging environments, significantly impacting reconstruction stability.
- However, these approaches typically entangle scene content and viewpoint cues in the same feature embeddings, making it difficult to disentangle camera parameters from scene content and causing pose ...

## Core Idea
- We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
- This maintains clean factorization within a feed-forward architecture, enabling coherent reconstruction and stable pose estimation without iterative refinement.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that TokenSplat achieves higher reconstruction fidelity and novel-view synthesis quality in pose-free settings, and significantly improves pose estimation accuracy compared to prior pose-free methods.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that TokenSplat achieves higher reconstruction fidelity and novel-view synthesis quality in pose-free settings, and significantly improves pose estimation accuracy compared to prior pose-free methods.
- We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
- Furthermore, most existing pose-free methods rely on pixel-aligned 3DGS heads that generate Gaussians at pixellevel gra

## Abstract Cue
- We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
