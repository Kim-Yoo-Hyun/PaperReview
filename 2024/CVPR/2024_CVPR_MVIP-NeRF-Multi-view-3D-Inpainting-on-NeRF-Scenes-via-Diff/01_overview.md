# MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: NeRF, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_MVIP-NeRF-Multi-view-3D-Inpainting-on-NeRF-Scenes-via-Diff/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To overcome these limitations, we propose a novel approach called MVIP-NeRF that harnesses the potential of diffusion priors for NeRF inpainting, addressing both appearance and geometry aspects.
- Inpainting on NeRF scenes presents two intricate challenges: (i) how to ensure that the same region observed in multiple views is completed in a consistent way, espe- cially ...
- Several NeRF inpainting techniques have been developed to address speciﬁc aspects of these challenges .

## Core Idea
- To overcome these limitations, we propose a novel approach called MVIP-NeRF that harnesses the potential of diffusion priors for NeRF inpainting, addressing both appearance and geometry aspects.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experimental results show better appearance and geometry recovery than previous NeRF inpainting methods.
- MVIP-NeRF performs joint inpainting across multiple views to reach a consistent solution, which is achieved via an iterative optimization process based on Score Distillation Sampling (SDS).
- This is due to two key reasons: (i) independently inpainting constituent images results in view-inconsistent imagery, and (ii) 2D inpainters struggle to ensure high-quality geometry completion and alignment ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To overcome these limitations, we propose a novel approach called MVIP-NeRF that harnesses the potential of diffusion priors for NeRF inpainting, addressing both appearance and geometry aspects.
- Our experimental results show better appearance and geometry recovery than previous NeRF inpainting methods.
- MVIP-NeRF performs joint inpainting across multiple views to reach a consistent solution, which is achieved via an iterative optimization process based on Score Distillation Sampling (SDS).

## Abstract Cue
- Despite the emergence of successful NeRF inpainting methods built upon explicit RGB and depth 2D inpainting supervisions, these methods are inherently constrained by the capabilities of their underlying 2D inpainters.
