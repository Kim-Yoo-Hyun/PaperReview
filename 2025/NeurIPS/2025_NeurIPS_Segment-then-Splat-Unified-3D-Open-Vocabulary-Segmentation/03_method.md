# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Segment-then-Splat-Unified-3D-Open-Vocabulary-Segmentation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- To overcome these issues and improve the robustness of object tracking, we propose three targeted post-processing strategies that dynamically detect new objects, resolve mask conflicts, and recover from ...

## 원리적 동기
- To solve this issue, most existing works [9–12] incorporate a separate language field alongside Gaussian Splatting reconstruction.
- Despite the differences in segmentation strategies, whether pixel-based or 3D-based, all existing approaches follow a “reconstruction then segmentation” (i.e., splat then segment) paradigm.
- In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.

## 핵심 방법론
- We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- To overcome these issues and improve the robustness of object tracking, we propose three targeted post-processing strategies that dynamically detect new objects, resolve mask conflicts, and recover from ...
- 3.3 Object-Specific Gaussian Initialization As our method follows a “segmentation then reconstruction” strategy, we first segment the Gaussians initialized by COLMAP into distinct sets, each representing a different ...
- To capture newly appearing objects, we introduce a detection mechanism at fixed intervals of ∆t.
- Specifically, we introduce an additional object-level loss term,
