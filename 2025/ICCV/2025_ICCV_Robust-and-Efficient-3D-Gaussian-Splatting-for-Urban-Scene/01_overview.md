# Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Robust-and-Efficient-3D-Gaussian-Splatting-for-Urban-Scene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- The source code is available at: https://yzslab.github.io/REUrbanGS. explicit representation introduces scalability challenges, as spatial complexity increases with scene size.

## Core Idea
- Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency.
- To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate that our method effectively reconstructs urban-scale scenes and outperforms previous approaches in both efficiency and quality.
- Additionally, we utilize enhancement modules, such as depth regularization, scale regularization, and antialiasing, to improve reconstruction fidelity.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results demonstrate that our method effectively reconstructs urban-scale scenes and outperforms previous approaches in both efficiency and quality.
- Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency.
- A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity.

## Abstract Cue
- We present a framework that enables fast reconstruction and real-time rendering of urban-scale scenes while maintaining robustness against appearance variations across multi-view captures.
