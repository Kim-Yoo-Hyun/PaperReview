# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, geometry, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_VideoRFSplat-Direct-Scene-Level-Text-to-3D-Gaussian-Splatt/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose an architecture and a sampling strategy to jointly model multi-view images and camera poses when fine-tuning a video genera- tion model.
- We propose VideoRFSplat, a direct text-to-3D model leveraging a video generation model to generate realistic 3D Gaussian Splatting (3DGS) for unbounded real-world scenes.
- Additionally, we propose an asynchronous sampling strategy that denoises camera poses faster than multi-view images, allowing rapidly denoised poses to condition multi-view generation, reducing mutual ambiguity and enhancing ...

## 원리적 동기
- Trained on multiple large-scale real-world datasets (RealEstate10K, MVImgNet, DL3DV-10K, ACID), VideoRFSplat outperforms existing text-to-3D direct generation methods that heavily depend on post-hoc refinement via score distillation sampling, achieving ...
- In this work, we propose an architecture and a sampling strategy to jointly model multi-view images and camera poses when fine-tuning a video genera- tion model.

## 핵심 방법론
- Quality Metrics BRISQUE↓ NIQE↓ CLIPScore↑ DreamFusion Magic3D LatentNeRF SJC Fantasia3D ProlificDreamer 90.2 92.8 88.6 82.0 69.6 61.5 10.48 11.20 9.19 10.15 7.65 7.07 - Director3D Director3D (w/ SDS++) ...
- VideoRFSplat outperforms all baselines without SDS++ refinement.
- Method MVImgNet 30.48 31.00 31.43 32.30 88.44 95.88 79.91 85.31 30.04 31.68 30.06 31.90 VideoRFSplat 30.33 33.0 73.69 32.5 34.9 35.3 5.32 5.64 33.3 33.3 32.8 32.8 δ ...
- FID-10K↓ CLIPScore↑ FID-2.4K↓ CLIPScore↑ 39.55 41.80 34.85 35.46 Vanilla sampling Vanilla sampling (w/o Eq.
- Ablation study on asynchronous sampling.
