# QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_QuickSplat-Fast-3D-Surface-Reconstruction-via-Learned-Gaus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.
- Surface reconstruction of large, real-world scenes is a key problem in computer vision and graphics.
- We further learn to jointly estimate the densification and update of the scene parameters during each iteration; our proposed densifier network predicts new Gaussians based on the rendering ...

## Core Idea
- Both our method without post-training (“w/o opt”) and with additional SGD iterations (“w/ opt”) obtain better geometry while achieving orders of magnitude faster runtime. # Initializer Densifier (a) ...
- We introduce QuickSplat, which learns datadriven priors to generate dense initializations for 2D gaussian splatting optimization of large-scale indoor scenes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on large-scale indoor scene reconstruction demonstrate the superiority of our data-driven optimization.
- Recently, 3D Gaussian Splatting (3DGS) achieves photorealistic novel-view-synthesis from multi-view images as input.
- This provides a strong starting point for the reconstruction, which accelerates the convergence of the optimization and improves the geometry of flat wall structures.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce QuickSplat, which learns datadriven priors to generate dense initializations for 2D gaussian splatting optimization of large-scale indoor scenes.
- Recently, 3D Gaussian Splatting (3DGS) achieves photorealistic novel-view-synthesis from multi-view images as input.
- We further learn to jointly estimate the densification and update of the scene parameters during each iteration; our proposed densifier network predicts new Gaussians based on the rendering ...

## Abstract Cue
- Surface reconstruction is fundamental to computer vision and graphics, enabling applications in 3D modeling, mixed reality, robotics, and more.
