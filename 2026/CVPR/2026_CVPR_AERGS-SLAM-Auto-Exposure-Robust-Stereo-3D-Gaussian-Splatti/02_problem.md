# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_AERGS-SLAM-Auto-Exposure-Robust-Stereo-3D-Gaussian-Splatti/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, existing research on 3DGS-based SLAM fails to accurately address the appearance variations induced by camera auto-exposure in prevalent real-world scenarios, resulting in reduced localization and photorealistic mapping ...
- For instance, MonoGS adjusts image brightness via two exposure parameters, yet it fails to model complex AE mechanisms.

## 해결하려는 문제
- Firstly, we propose a camera exposure network to model the camera exposure process, which we integrate with Gaussian splatting to achieve exposure-controlled novel view synthesis.
- To address this issue, we propose a stereo auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM), a framework robust to such variations and enables both reliable localization and exposure-controlled photorealistic mapping.
- Extensive experiments on public datasets and our self-collected realworld dataset demonstrate that AERGS-SLAM outperforms baselines in both localization performance and photorealistic mapping quality.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
