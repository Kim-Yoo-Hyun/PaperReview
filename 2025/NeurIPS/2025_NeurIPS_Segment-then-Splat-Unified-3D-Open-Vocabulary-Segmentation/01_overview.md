# Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

- Year/Venue: 2025 / NeurIPS Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Segment-then-Splat-Unified-3D-Open-Vocabulary-Segmentation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To solve this issue, most existing works [9–12] incorporate a separate language field alongside Gaussian Splatting reconstruction.
- Despite the differences in segmentation strategies, whether pixel-based or 3D-based, all existing approaches follow a “reconstruction then segmentation” (i.e., splat then segment) paradigm.
- 2) Failure to capture true 3D object information, complicating 3D object extraction and limiting downstream tasks like robot navigation and 3D manipulation.

## Core Idea
- In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on various datasets demonstrate the effectiveness of our proposed method in both static and dynamic scenarios.
- Notably, 2D pixel-based methods LERF_OVS 3DOVS tend to produce relatively ambiguous boundMethod mIoU↑ Time↓ mIoU↑ Time↓ aries, whereas our approach, leveraging the SegLangSplat 46.37 62.00 82.49 68.90 ment ...
- Our method outperforms all baseline ap- static (a) and dynamic (b) scenes. proaches.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- Extensive experiments on various datasets demonstrate the effectiveness of our proposed method in both static and dynamic scenarios.
- Segment then Splat reverses the long-established approach of “segmentation after reconstruction” by dividing Gaussians into distinct object sets before reconstruction.

## Abstract Cue
- Open-vocabulary querying in 3D space is crucial for enabling more intelligent perception in applications such as robotics, autonomous systems, and augmented reality.
