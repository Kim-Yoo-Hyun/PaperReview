# 3D Equivariant Visuomotor Policy Learning via Spherical Projection

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Paper link: ./2025/NeurIPS/2025_NeurIPS_3D-Equivariant-Visuomotor-Policy-Learning-via-Spherical-Pr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- When used with RGB data, current equivariant policies are unable to fully leverage the SO(3) structure present in the problem and underperform the point cloud version significantly .
- This paper addresses this challenge by introducing a novel diffusion policy framework that incorporates SO(3)-equivariance into eye-in-hand visuomotor learning.
- Unlike prior work that relies on segmented point clouds or calibrated multi-camera systems , our approach maintains equivariance throughout the entire policy and supports robust, sample-efficient closed-loop control ...

## Core Idea
- The observation x ∈ X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈ R7 , including the end-effector’s ...
- In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We perform extensive experiments in both simulation and the real world that demonstrate that our method consistently outperforms strong baselines in terms of both performance and sample efficiency.
- We compare against three strong baselines: (1) Diffusion Policy : A diffusion-based policy without any equivariance, serving as the primary reference. (2) EquiDiff (modified) : Designed for fixed-camera ...
- Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.

## Limitation
- Limitations Our method has several limitations for future investigation.
- Extending the equivariance correction to handle camera translations is a promising direction for future work.
- Second, our approach models rotational equivariance but does not address translational equivariance.

## Contribution
- We perform extensive experiments in both simulation and the real world that demonstrate that our method consistently outperforms strong baselines in terms of both performance and sample efficiency.
- Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.
- This paper closes this gap by incorporating into the diffusion policy model a process that projects features from the 2D RGB camera image onto a sphere.

## Abstract Cue
- Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.
