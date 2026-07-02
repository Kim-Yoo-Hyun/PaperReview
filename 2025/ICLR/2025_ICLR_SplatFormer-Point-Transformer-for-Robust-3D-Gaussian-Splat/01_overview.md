# SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

- Year/Venue: 2025 / ICLR Spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- V-dimensional feature vectors vk ∈ RV : K {vk }K k=1 = fθ ({Gk }k=1 ), (4) which encapsulate key details of the 3D primitives.
- The feature decoder gθ then transforms this latent representation into splat attribute residuals K {∆Gk = (∆pk , ∆sk , ∆αk , ∆qk , ∆ak )}K k=1 = ...
- Our 3DGS splat encoder is based on the PTv3 framework (Wu et al., 2024b).

## Core Idea
- The dataset and training approach we introduce allow SplatFormer to learn rich data-driven priors from a diverse range of 3D objects and view configurations.
- This hierarchical architecture models contextual relationships among neighboring primitives.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To capture high-frequency details and improve gradient flow, skip connection MLP modules are used to map intermediate downsampling outputs to residuals, which are then added to the upsampling ...
- The metric is evaluated on OOD test views with elevation ϕood ≥ 70◦ ; colors indicate the 1st , 2nd , and 3rd best-performing model Methods Standard Regularized ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The feature decoder gθ then transforms this latent representation into splat attribute residuals K {∆Gk = (∆pk , ∆sk , ∆αk , ∆qk , ∆ak )}K k=1 = ...
- This hierarchical architecture models contextual relationships among ne
- Then another 4 stages of attention blocks and upsampling grid pooling layers are used to restore the resolution.

## Abstract Cue
- V-dimensional feature vectors vk ∈ RV : K {vk }K k=1 = fθ ({Gk }k=1 ), (4) which encapsulate key details of the 3D primitives.
