# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_WaterSplatting-Fast-Underwater-3D-Scene-Reconstruction-usi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Therefore, we propose a novel approach that fuses volumetric rendering with 3DGS to handle underwater data effectively.
- The same advantages are observed in simulated scenes, where our method renders better details (indicated by the red square) than the SeaThru-NeRF in both easy and hard foggy ...
- Overall, our method surpasses SeaThru-NeRF in both underwater and simulated scenes.

## 원리적 동기
- Furthermore, it does so while offering real-time rendering performance, addressing the efficiency limitations of existing methods.
- The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
- Therefore, we propose a novel approach that fuses volumetric rendering with 3DGS to handle underwater data effectively.

## 핵심 방법론
- The same advantages are observed in simulated scenes, where our method renders better details (indicated by the red square) than the SeaThru-NeRF in both easy and hard foggy ...
- Overall, our method surpasses SeaThru-NeRF in both underwater and simulated scenes.
- We conduct a quantitative analysis on different combination of loss functions, between pixel-wise component {L1 , L2 , LReg-L1 , LReg-L2 } and frame-wise {LDSSIM , LReg-DSSIM }, ...
- 3DGS prunes the Gaussians with low opacity, leaving dense and muddy cloud-like primitives to fit the medium, which causes artifacts in the novel views.
