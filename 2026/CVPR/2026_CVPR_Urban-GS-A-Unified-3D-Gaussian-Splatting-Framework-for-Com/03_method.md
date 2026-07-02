# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Urban-GS-A-Unified-3D-Gaussian-Splatting-Framework-for-Com/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from both aerial and ...
- Furthermore, we propose a Global-to-Local Optimization strategy to refine the reconstruction of under-optimized regions resulting from imbalanced view distributions.
- However, these approaches are inherently constrained by a single type view paradigm and tend to produce noticeable artifacts when rendering novel perspectives that deviate substantially from the training ...

## 원리적 동기
- However, seamless integration of both aerial and street view images to model urban scenes remains a significant challenge for 3DGS.
- This limitation highlights the necessity of jointly reconstructing scenes using aerial and street view imagery, as the complementary perspe
- In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from both aerial and ...

## 핵심 방법론
- Aerial Only Street Only Merge Aerial test set PSNR SSIM LPIPS 25.64 0.891 0.159 24.71 0.872 0.188 25.35 0.884 0.175 𝜏𝜏𝑝𝑝𝑝𝑝𝑝𝑝 Street test set PSNR SSIM LPIPS 25.21 ...
- Quantitative comparison across accumulating gradients for densification from aerial views only, street views only and merged views on Colosseum scene .
- All methods are trained with 60k iterations.
