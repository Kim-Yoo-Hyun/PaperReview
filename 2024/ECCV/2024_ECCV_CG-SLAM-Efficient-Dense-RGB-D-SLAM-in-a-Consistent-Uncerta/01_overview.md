# CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_CG-SLAM-Efficient-Dense-RGB-D-SLAM-in-a-Consistent-Uncerta/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene mapping simultaneously with ...
- Despite their notable successes in surface modeling and novel view synthesis, existing NeRF-based methods are hindered by their computationally intensive and time-consuming volume rendering pipeline.

## Core Idea
- Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping.
- We incorporated an uncertainty model that utilizes the geometry prior to attach the uncertainty property on rendered images and Gaussian primitives.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on various datasets demonstrate that CG-SLAM achieves superior tracking and mapping performance with a notable tracking speed of around 15 Hz.
- In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec.

## Limitation
- We believe it is a very interesting direction for future work.
- Considerable memory usage is one limitation of the Gaussianbased system.

## Contribution
- Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping.
- Experiments on various datasets demonstrate that CG-SLAM achieves superior tracking and mapping performance with a notable tracking speed of around 15 Hz.
- This paper presents an efficient dense RGB-D SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and geometric stability.

## Abstract Cue
- Recently neural radiance fields (NeRF) have been widely exploited as 3D representations for dense simultaneous localization and mapping (SLAM).
