# Method

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_PETR-Position-Embedding-Transformation-for-Multi-View-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.
- 2 shows the overall architecture of the proposed PETR.
- The 3D features are further input to the transformer decoder and interact with the object queries, generated from query generator.

## 원리적 동기
- Previous works mainly solved this problem from the perspective of monocular object detection.
- However, such 2D-to-3D transformation in DETR3D may introduce several problems.
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.

## 핵심 방법론
- 2 shows the overall architecture of the proposed PETR.
- The 3D features are further input to the transformer decoder and interact with the object queries, generated from query generator.
- The 3D coordinates together with the 2D multiview features are input to the 3D position encoder, producing the 3D positionaware features F 3d = {Fi3d ∈ RC×HF ×WF ...
