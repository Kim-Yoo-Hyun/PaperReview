# Problem

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LoopSplat-Loop-Closure-by-Registering-3D-Gaussian-Splats/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, existing 3DGS-based methods fail to address the global consistency of the scene via loop closure and/or global bundle adjustment.
- Existing methods can be split into two categories, decoupled and coupled, where decoupled methods do not leverage the dense map for the tracking task, while the coupled methods ...
- On the other hand, all coupled 3DGS SLAM methods lack strategies for achieving global consistency on the map and the poses, which leads to an accumulation of pose ...

## 해결하려는 문제
- Among the recent methods that enforce global consistency via loop closure and/or global bundle adjustment (BA), GO-SLAM requires costly retraining of the hash grid features to de- Simultaneous ...
- To this end, we propose LoopSplat, which takes RGB-D images as input and performs dense mapping with 3DGS submaps and frame-to-model tracking.
- Evaluation on the synthetic Replica and real-world TUM-RGBD, ScanNet, and ScanNet++ datasets demonstrates competitive or superior tracking, mapping, and rendering compared to existing methods for dense RGB-D SLAM.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
