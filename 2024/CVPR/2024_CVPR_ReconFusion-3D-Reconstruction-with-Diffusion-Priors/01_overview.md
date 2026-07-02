# ReconFusion: 3D Reconstruction with Diffusion Priors

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_ReconFusion-3D-Reconstruction-with-Diffusion-Priors/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- NeRF’s dense capture requirement poses a major challenge, necessitating tens to hundreds of images for even simple objects to ensure a clean reconstruction (Fig.
- While these models excel at generating realistic images from novel view points, they do not produce a single consistent 3D shape from a sparse set of input

## Core Idea
- We present ReconFusion to reconstruct real-world scenes using only a few photos.
- Our approach leverages a diffusion prior for novel view synthesis, trained on synthetic and multiview datasets, which regularizes a NeRF-based 3D reconstruction pipeline at novel camera poses beyond ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We perform an extensive evaluation across various real-world datasets, including forward-facing and 360-degree scenes, demonstrating significant performance improvements over previous few-view NeRF reconstruction approaches.
- However, even the most effective methods show considerable degradation at novel viewpoints compared to denser captures.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach leverages a diffusion prior for novel view synthesis, trained on synthetic and multiview datasets, which regularizes a NeRF-based 3D reconstruction pipeline at novel camera poses beyond ...
- We present ReconFusion to reconstruct real-world scenes using only a few photos.
- Our method synthesizes realistic geometry and texture in underconstrained regions while preserving the appearance of observed regions.

## Abstract Cue
- 3D reconstruction methods such as Neural Radiance Fields (NeRFs) excel at rendering photorealistic novel views of complex scenes.
