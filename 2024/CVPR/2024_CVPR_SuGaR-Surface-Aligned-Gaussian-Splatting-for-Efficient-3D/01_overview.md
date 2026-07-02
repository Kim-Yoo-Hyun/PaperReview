# SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_SuGaR-Surface-Aligned-Gaussian-Splatting-for-Efficient-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
- Gaussian Splatting has recently become very popular as it yields realistic rendering while being significantly faster to train than NeRFs.
- It is however challenging to extract a mesh from the millions of tiny 3D Gaussians as these Gaussians tend to be unorganized after optimization and no method has ...

## Core Idea
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
- Finally, we introduce an optional refinement strategy that binds Gaussians to the surface of the mesh, and jointly optimizes these Gaussians and the mesh through Gaussian splatting rendering.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Retrieving such an editable mesh for realistic rendering is done within minutes with our method, compared to hours with the state-of-the-art method on SDFs, while providing a better ...
- While the Gaussians allow very realistic renderings of the scene, it is still however challenging to extract the surface of the scene from them: As shown in Figure ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
- Finally, we introduce an optional refinement strategy that binds Gaussians to the surface of the mesh, and jointly optimizes these Gaussians and the mesh through Gaussian splatting rendering.
- Retrieving such an editable mesh for realistic rendering is done within minutes with our method, compared to hours with the state-of-the-art method on SDFs, while providing a better ...

## Abstract Cue
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
