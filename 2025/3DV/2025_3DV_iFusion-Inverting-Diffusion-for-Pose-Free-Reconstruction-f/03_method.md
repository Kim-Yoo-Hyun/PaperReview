# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, geometry, Diffusion, Generation, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_iFusion-Inverting-Diffusion-for-Pose-Free-Reconstruction-f/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
- To address this, we harness a pre-trained novel view synthesis diffusion model, which embeds implicit knowledge about the geometry and appearance of diverse objects.
- Our strategy unfolds in three steps: (1) We invert the diffusion model for camera pose estimation instead of synthesizing novel views. (2) The diffusion model is finetuned using ...

## 원리적 동기
- However, assuming the availability of pose may be unrealistic, and existing pose estimators fail in sparseview scenarios.
- Introduction Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various ∗ Part of this work was done as a research intern at ...
- We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.

## 핵심 방법론
- Specifically, One2-3-45 represents image-based methods, which directly regresses SDFs from the generated multi-view images; on the other hand, Zero123-SDS , Magic123 , and DreamGaussian are SDS-based approahces.
