# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_A-Lesson-in-Splats-Teacher-Guided-Diffusion-for-3D-Gaussia/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a novel framework for training 3D imageconditioned diffusion models using only 2D supervision.
- Our approach leverages suboptimal predictions from a deterministic imageto-3D model—acting as a "teacher"—to generate noisy 3D inputs, enabling effective 3D diffusion training without requiring full 3D ground truth.
- To address this, we propose leveraging sparse-view supervision as a scalable alternative.

## 원리적 동기
- First, it is an ill-posed problem because different 3D shapes can produce identical 2D projections.
- A key challenge in training 3D diffusion models with 2D supervi- sion is that the standard training paradigm requires both the denoising process and supervision to be in ...
- We present a novel framework for training 3D imageconditioned diffusion models using only 2D supervision.

## 핵심 방법론
- 1-view Chairs PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ SRN CodeNeRF FE-NVS ViewsetDiff w/o D ViewsetDiff w D 22.25 23.80 22.83 23.21 23.29 ...
