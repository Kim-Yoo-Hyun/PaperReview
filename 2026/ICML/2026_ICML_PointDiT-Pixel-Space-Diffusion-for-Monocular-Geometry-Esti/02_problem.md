# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, depth, point cloud, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_PointDiT-Pixel-Space-Diffusion-for-Monocular-Geometry-Esti/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing approaches to this challenge can be broadly categorized into two distinct groups.
- However, remains an ill-posed problem due to the fundamental scale and depth ambiguities of perspective projection.
- Unlike existing latent diffusion-based approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers.

## 해결하려는 문제
- State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions (e.g., MoGe), or necessitate compressing geometry into latent spaces (e.g., GeometryCrafter) to leverage pre-trained ...
- We introduce a minimalist pixel-space Diffusion Transformer built on a plain ViT, which operates directly on raw 3D point map patches and is conditioned on image tokens from ...
- We show that this streamlined approach yields results superior to complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
