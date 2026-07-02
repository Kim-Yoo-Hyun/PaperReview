# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_MS-GS-Multi-Appearance-Sparse-View-3D-Gaussian-Splatting-i/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators that have rapidly progressed.
- High-quality scene reconstruction and novel view synthesis from images is a long-standing research problem with wide-ranging applications in AR/VR, 3D site modeling, autonomous driving, robotics, etc.
- A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.

## 해결하려는 문제
- We demonstrate that MS-GS achieves photorealistic renderings under various challenging sparse-view and multi-appearance conditions, and outperforms existing approaches significantly across different datasets.
- Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone to overfitting.
- To address the lack of support due to sparse initializations, our approach is built on the geometric priors elicited from monocular depth estimations.

## 선행 연구 / 배경 단서
- To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators that have rapidly progressed.
- High-quality scene reconstruction and novel view synthesis from images is a long-standing research problem with wide-ranging applications in AR/VR, 3D site modeling, autonomous driving, robotics, etc.
- A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.
