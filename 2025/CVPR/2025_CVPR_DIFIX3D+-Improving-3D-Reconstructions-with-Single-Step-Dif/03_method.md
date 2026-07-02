# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_DIFIX3D+-Improving-3D-Reconstructions-with-Single-Step-Dif/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we introduce D IFIX 3D+, a novel pipeline designed to enhance 3D reconstruction and novel-view synthesis through single-step diffusion models.
- At the core of our approach is D IFIX, a single-step image diffusion model trained to enhance and remove artifacts in rendered novel views caused by underconstrained regions ...
- First, it is used during the reconstruction phase to clean up pseudo-training views that */ PSNR↑ Nerfbusters Dataset SSIM↑ LPIPS↓ FID↓ PSNR↑ DL3DV Dataset SSIM↑ LPIPS↓ FID↓ Nerfbusters ...

## 원리적 동기
- Neural Radiance Fields and 3D Gaussian Splatting have revolutionized 3D reconstruction and novel-view synthesis task.
- However, achieving photorealistic rendering from extreme novel viewpoints remains challenging, as artifacts persist across representations.
- In this work, we introduce D IFIX 3D+, a novel pipeline designed to enhance 3D reconstruction and novel-view synthesis through single-step diffusion models.

## 핵심 방법론
- Our method outperforms all comparison methods by a signifi- D IFIX training.
- We use the gsplat library2 for 3DGS-based experiments and the official implementation for all other methods and baselines. cant margin across all metrics.
- We partition each scene into a set of reference views used during training and evaluate on the left-out target views.
- We also compare to Nerfbusters , which uses a 3D diffusion model to remove artifacts from NeRF1 , GANeRF , which train per-scene GAN that is used to ...
