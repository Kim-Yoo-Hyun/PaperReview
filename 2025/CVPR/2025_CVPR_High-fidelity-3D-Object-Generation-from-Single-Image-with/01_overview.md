# High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_High-fidelity-3D-Object-Generation-from-Single-Image-with/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, the persisting challenge arises due to the inherent geometric ambiguity and limited information provided in single-view images.
- Despite the current progress, these methods still suffer from the inconsistency jointly caused by the geometric ambiguity in the 2D images, and the lack of structure of 3D ...

## Core Idea
- To this end, we propose a novel hybrid Voxel-Gaussian representation, where a 3D voxel representation contains explicit 3D geometric information, eliminating the geometric ambiguity from 2D images.
- In this paper, we propose to fix these issues by GS-RGBN, a new RGBN-volume Gaussian Reconstruction Model designed to generate high-fidelity 3D objects from single-view images.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate the superiority of our methods over prior works in terms of high-quality reconstruction results, robust generalization, and good efficiency.
- They learn 3D Gaussians from 2D RGB images generated from pre-trained multi-view diffusion (MVD) models, and have shown a promising avenue for 3D generation through a single image.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate the superiority of our methods over prior works in terms of high-quality reconstruction results, robust generalization, and good efficiency.
- They learn 3D Gaussians from 2D RGB images generated from pre-trained multi-view diffusion (MVD) models, and have shown a promising avenue for 3D generation through a single image.
- In this paper, we propose to fix these issues by GS-RGBN, a new RGBN-volume Gaussian Reconstruction Model designed to generate high-fidelity 3D objects from single-view images.

## Abstract Cue
- Recently single-view 3D generation via Gaussian splatting has emerged and developed quickly.
