# MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_MGSR-2D-3D-Mutual-boosted-Gaussian-Splatting-for-High-fide/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Nevertheless, achieving high-fidelity surface reconstruction (SR) and improving the realism of novel view synthesis (NVS) under various light conditions are two main challenges in 3DGS.
- Despite recent progress, these tasks are often addressed independently, with GS-based rendering methods struggling under diverse light conditions and failing to produce accurate surfaces, while GS-based reconstruction methods ...
- Prior to this, each branch completes an independent warm-up phase, with an early stopping strategy implemented to reduce computational costs.

## Core Idea
- To address this, we propose MGSR, a 2D/3D Mutual-boosted Gaussian Splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy.
- Similar to previous baselines , we utilized the same 15 scans from the DTU dataset to validate our approach.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Using the transmitted component as supervision, the 2DGS branch also achieves high-fidelity surface reconstruction.
- We evaluate MGSR on a diverse set of synthetic and real-world datasets, at both object and scene levels, demonstrating strong performance in rendering and surface reconstruction.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this, we propose MGSR, a 2D/3D Mutual-boosted Gaussian Splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy.
- 3DGS effectively resolves the issues of low training efficiency and insufficient geometric accuracy in previous NeRF methods.
- Novel view synthesis (NVS) and surface reconstruction (SR) are essential tasks in 3D Gaussian Splatting (3DGS).

## Abstract Cue
- Novel view synthesis (NVS) and surface reconstruction (SR) are essential tasks in 3D Gaussian Splatting (3DGS).
