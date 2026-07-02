# Problem

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Paper link: ./2025/NeurIPS/2025_NeurIPS_3D-Equivariant-Visuomotor-Policy-Learning-via-Spherical-Pr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- When used with RGB data, current equivariant policies are unable to fully leverage the SO(3) structure present in the problem and underperform the point cloud version significantly .
- This paper addresses this challenge by introducing a novel diffusion policy framework that incorporates SO(3)-equivariance into eye-in-hand visuomotor learning.
- Unlike prior work that relies on segmented point clouds or calibrated multi-camera systems , our approach maintains equivariance throughout the entire policy and supports robust, sample-efficient closed-loop control ...

## 해결하려는 문제
- We perform extensive experiments in both simulation and the real world that demonstrate that our method consistently outperforms strong baselines in terms of both performance and sample efficiency.
- Equivariant models have recently been shown to improve the data efficiency of diffusion policy by a significant margin.
- This paper closes this gap by incorporating into the diffusion policy model a process that projects features from the 2D RGB camera image onto a sphere.

## 선행 연구 / 배경 단서
- More- Figure 1: We propose the first SO(3)-equivariant over, it is used in a growing number of large policy learning framework based on a single eyerobot datasets . ...
- Unlike prior work that relies on segmented point clouds or calibrated multi-camera systems , our approach maintains equivariance throughout the entire policy and supports robust, sample-efficient closed-loop control ...
- This paper addresses this challenge by introducing a novel diffusion policy framework that incorporates SO(3)-equivariance into eye-in-hand visuomotor learning.
