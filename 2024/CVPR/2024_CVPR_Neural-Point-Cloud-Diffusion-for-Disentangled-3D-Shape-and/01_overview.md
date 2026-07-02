# Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Neural-Point-Cloud-Diffusion-for-Disentangled-3D-Shape-and/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The general challenge for 3D diffusion models lies in selecting the right 3D representation.
- However, none of the existing models enable disentangled generation to control the shape and appearance separately.
- However, manually creating such assets is a labor-intensive and costly task that requires expert skills.

## Core Idea
- For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach.
- Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other nondisentanglement-capable ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Recently, diffusion models have shown remarkable results in generation quality of 3D objects.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach.
- Recently, diffusion models have shown remarkable results in generation quality of 3D objects.
- We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder.

## Abstract Cue
- Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR.
