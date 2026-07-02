# iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views

- Year/Venue: 2025 / 3DV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, geometry, Diffusion, Generation, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_iFusion-Inverting-Diffusion-for-Pose-Free-Reconstruction-f/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, assuming the availability of pose may be unrealistic, and existing pose estimators fail in sparseview scenarios.
- Introduction Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various ∗ Part of this work was done as a research intern at ...
- On the other hand, sparse-view methods assume the availability of an accurate camera pose for each view .

## Core Idea
- We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
- To address this, we harness a pre-trained novel view synthesis diffusion model, which embeds implicit knowledge about the geometry and appearance of diverse objects.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments demonstrate strong performance in both pose estimation and novel view synthesis.
- Additional views improve reconstruction fidelity but necessitate known camera poses.
- While single-view reconstruction yields visually appealing results, it can deviate significantly from the actual object, especially on unseen sides.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
- Experiments demonstrate strong performance in both pose estimation and novel view synthesis.
- To address this, we harness a pre-trained novel view synthesis diffusion model, which embeds implicit knowledge about the geometry and appearance of diverse objects.

## Abstract Cue
- We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
