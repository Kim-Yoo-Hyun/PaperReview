# Problem

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_ReconFusion-3D-Reconstruction-with-Diffusion-Priors/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- NeRF’s dense capture requirement poses a major challenge, necessitating tens to hundreds of images for even simple objects to ensure a clean reconstruction (Fig.
- While these models excel at generating realistic images from novel view points, they do not produce a single consistent 3D shape from a sparse set of input

## 해결하려는 문제
- Our approach leverages a diffusion prior for novel view synthesis, trained on synthetic and multiview datasets, which regularizes a NeRF-based 3D reconstruction pipeline at novel camera poses beyond ...
- We present ReconFusion to reconstruct real-world scenes using only a few photos.
- Our method synthesizes realistic geometry and texture in underconstrained regions while preserving the appearance of observed regions.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
