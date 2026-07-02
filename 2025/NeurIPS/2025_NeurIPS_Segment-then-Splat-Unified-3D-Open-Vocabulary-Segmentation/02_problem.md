# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Segment-then-Splat-Unified-3D-Open-Vocabulary-Segmentation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To solve this issue, most existing works [9–12] incorporate a separate language field alongside Gaussian Splatting reconstruction.
- Despite the differences in segmentation strategies, whether pixel-based or 3D-based, all existing approaches follow a “reconstruction then segmentation” (i.e., splat then segment) paradigm.
- 2) Failure to capture true 3D object information, complicating 3D object extraction and limiting downstream tasks like robot navigation and 3D manipulation.

## 해결하려는 문제
- In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- Extensive experiments on various datasets demonstrate the effectiveness of our proposed method in both static and dynamic scenarios.
- Segment then Splat reverses the long-established approach of “segmentation after reconstruction” by dividing Gaussians into distinct object sets before reconstruction.

## 선행 연구 / 배경 단서
- Unlike existing methods that adopt a “splat then segment” approach, our method reverses the process by first initializing each object with a specific set of Gaussians, as shown ...
- To solve this issue, most existing works [9–12] incorporate a separate language field alongside Gaussian Splatting reconstruction.
- Despite the differences in segmentation strategies, whether pixel-based or 3D-based, all existing approaches follow a “reconstruction then segmentation” (i.e., splat then segment) paradigm.
