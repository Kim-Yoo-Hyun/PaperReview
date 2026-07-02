# GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GeoGaussian-Geometry-aware-Gaussian-Splatting-for-Scene-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Due to the impressive rendering quality of Neural Radiance Fields (NeRF) , the area of photo-realistic novel view synthesis (NVS) has become a popular research topic in the ...
- While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( ) shows better performance in terms of training speed and rendering quality.
- 3D Gaussian Splatting is explicitly represented by a set of Gaussian points parameterized by its position, orientation, and spherical harmonics parameters.

## Core Idea
- To mitigate this issue, we propose a novel approach called GeoGaussian.
- Benefiting from the proposed architecture, the generative ability of 3D Gaussians is enhanced, especially in structured regions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- Throughout all experiments, we maintain a consistent learning rate of 0.0002 for Gaussian optimization and γ is set to 0.0002.
- The proposed GeoGaussian approach is trained and evaluated on a desktop PC equipped with an Intel Core i9 12900K 3.50GHz processor and a single GeForce RTX 3090 GPU.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To mitigate this issue, we propose a novel approach called GeoGaussian.
- Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- Benefiting from the proposed architecture, the generative ability of 3D Gaussians is enhanced, especially in structured regions.

## Abstract Cue
- During the Gaussian Splatting optimization process, the scene geometry can gradually deteriorate if its structure is not deliberately preserved, especially in non-textured regions such as walls, ceilings, and furniture surfaces.
