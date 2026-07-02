# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_AERGS-SLAM-Auto-Exposure-Robust-Stereo-3D-Gaussian-Splatti/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this issue, we propose a stereo auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM), a framework robust to such variations and enables both reliable localization and exposure-controlled photorealistic mapping.
- Firstly, we propose a camera exposure network to model the camera exposure process, which we integrate with Gaussian splatting to achieve exposure-controlled novel view synthesis.
- We run AERGS-SLAM and all baseline methods using their official implementations on a desktop computer equipped with an RTX 4090 24GB GPU, an Intel Core i7-13900K CPU, and ...

## 원리적 동기
- However, existing research on 3DGS-based SLAM fails to accurately address the appearance variations induced by camera auto-exposure in prevalent real-world scenarios, resulting in reduced localization and photorealistic mapping ...
- For instance, MonoGS adjusts image brightness via two exposure parameters, yet it fails to model complex AE mechanisms.
- To address this issue, we propose a stereo auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM), a framework robust to such variations and enables both reliable localization and exposure-controlled photorealistic mapping.

## 핵심 방법론
- We run AERGS-SLAM and all baseline methods using their official implementations on a desktop computer equipped with an RTX 4090 24GB GPU, an Intel Core i7-13900K CPU, and ...
