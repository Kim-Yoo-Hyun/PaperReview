# Method

- Year/Venue: 2026 / ICML spotlight
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, depth, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.

## 원리적 동기
- Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive.
- By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.
- To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.

## 핵심 방법론
- LC 00 01 02 03 04 05 06 07 08 09 10 Avg.
- Avg.* Detail seq. frames 4541 1101 4661 801 271 2761 1101 1101 4071 1591 1201 2109 2210 seq. length (m) - 2453.20 5067.23 3724.19 560.89 393.65 2205.58 1232.88 ...
- ORB-SLAM2 × 40.65 502.20 47.82 0.94 1.30 29.95 40.82 16.04 43.09 38.77 5.42 69.73 26.48 ORB-SLAM2 ✓ 6.03 508.34 14.76 1.02 1.57 4.04 11.16 2.19 38.85 8.39 6.63 ...
- MASt3R-SLAM ✓ TL TL TL TL TL TL TL TL TL TL TL CUT3R × OOM OOM OOM 148.1 22.31 OOM OOM OOM OOM OOM OOM Fast3R × ...
- Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on Waymo Open dataset.
