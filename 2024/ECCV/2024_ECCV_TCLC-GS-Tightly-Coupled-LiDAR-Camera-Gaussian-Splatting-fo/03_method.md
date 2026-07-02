# Method

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_TCLC-GS-Tightly-Coupled-LiDAR-Camera-Gaussian-Splatting-fo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Comprehensive evaluations conducted on the Waymo Open Dataset and nuScenes Dataset validate our method’s stateof-the-art (SOTA) performance.
- During the information as supervision, which enhances the training process by learning of a robust geometry.
- In this paper, we design a novel tightly coupled LiDAR-Camera Gaussian Splatting (TCLC-GS) to fully leverage the combined strengths of both LiDAR and camera sensors, enabling rapid, high-quality ...

## 원리적 동기
- Urban-level reconstruction and rendering present significant challenges due to the vast scale of the unbounded environments and the sparse nature of the captured data.
- Comprehensive evaluations conducted on the Waymo Open Dataset and nuScenes Dataset validate our method’s stateof-the-art (SOTA) performance.

## 핵심 방법론
- NeRF NeRF-W Instant-NGP Point-NeRF NPLF Mip-NeRF Mip-NeRF 360 DNMP 3D-GS TCLC-GS PSNR↑ SSIM↑ LPIPS↓ 26.24 0.87 0.47 26.92 0.89 0.42 26.77 0.88 0.40 26.26 0.87 0.45 25.62 0.88 ...
- Method TCLC-GS w/o 3D mesh TCLC-GS w/o colorized 3D mesh TCLC-GS w/o octree implicit feature TCLC-GS w/o dense depth supervision TCLC-GS full PSNR↑ 26.36 27.61 27.81 27.96 28.11 ...
