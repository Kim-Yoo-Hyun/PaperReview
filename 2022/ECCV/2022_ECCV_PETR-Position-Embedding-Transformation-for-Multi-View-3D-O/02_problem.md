# Problem

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_PETR-Position-Embedding-Transformation-for-Multi-View-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Previous works mainly solved this problem from the perspective of monocular object detection.
- However, such 2D-to-3D transformation in DETR3D may introduce several problems.
- Second, only the image feature at the projected point will be collected, which fails to perform the representation learning from global view.

## 해결하려는 문제
- PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.

## 선행 연구 / 배경 단서
- Previous works mainly solved this problem from the perspective of monocular object detection.
- However, such 2D-to-3D transformation in DETR3D may introduce several problems.
- Second, only the image feature at the projected point will be collected, which fails to perform the representation learning from global view.
