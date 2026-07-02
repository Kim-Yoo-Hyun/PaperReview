# Generative Point Cloud Registration

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Generative-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing rich color cues ...
- Introduction Point cloud registration is a problem of finding the optimal rigid transformation, comprising a 3D rotation and a 3D translation, which aligns the source and target point ...
- Existing 3D registration methods can be roughly categorized into traditional approaches and data-driven deep methods.

## Core Idea
- We compare our method against with one representative traditional descriptor: FPFH (Rusu et al., 2009), one scene-level end-to-end registration network: RegTR (Yew & Lee, 2022), and five deep ...
- Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing rich color cues ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Recent RGB-D registration studies (Yuan et al., 2023; Mu et al., 2024) have shown images would significantly enhance the distinctiveness of point cloud descriptors, leading to improved matching ...
- However, real-world Despite the impressive performance achieved by current point cloud registration methods, their robustness remains limited in challenging scenarios that contain low overlap, repetitive patterns, or noisy ...
- These deep methods significantly enhance the quality of estimated correspondences and improve registration accuracy.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing rich color cues ...
- Recent RGB-D registration studies (Yuan et al., 2023; Mu et al., 2024) have shown images would significantly enhance the distinctiveness of point cloud descriptors, leading to improved matching ...
- However, real-world Despite the impressive performance achieved by current point cloud registration methods, their robustness remains limited in challenging scenarios that contain low overlap, repetitive patterns, or noisy ...

## Abstract Cue
- Paradigm comparison of our generative point cloud registration with conventional methods.
