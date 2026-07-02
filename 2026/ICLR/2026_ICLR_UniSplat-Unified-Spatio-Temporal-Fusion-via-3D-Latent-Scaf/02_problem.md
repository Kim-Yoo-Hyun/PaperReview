# Problem

- Year/Venue: 2026 / ICLR Poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_UniSplat-Unified-Spatio-Temporal-Fusion-via-3D-Latent-Scaf/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.
- These methods typically encode inter-view correlations within the image domain via cross-attention or by constructing a multi-view stereo (MVS) cost volume, and subsequently decode the Gaussian primitives from ...

## 해결하려는 문제
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## 선행 연구 / 배경 단서
- These methods typically encode inter-view correlations within the image domain via cross-attention or by constructing a multi-view stereo (MVS) cost volume, and subsequently decode the Gaussian primitives from ...
- EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.
- Recent advances in 3D Gaussian Splatting (Yan et al., 2024; Jiawei et al., 2025; Kerbl et al., 2023) have demonstrated impressive rendering efficiency and fidelity.
