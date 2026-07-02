# Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Geometry-Aware-Cross-Modal-Graph-Alignment-for-Referring-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Recent advances in 3D Gaussian Splatting (3DGS) have provided a promising foundation for this problem, as the representation allows for efficient, differentiable rendering of continuous 3D scenes with ...
- Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental limitations: (1) language ...

## Core Idea
- To address this, we propose GeoCGA, a geometry-aware cross-modal graph alignment framework that bridges linguistic semantics with the 3DGS representation.
- Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental limitations: (1) language ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- GeoCGA consistently outperforms prior state-of-the-art methods, yielding relative mIoU improvements of 20.8% on Ref-LERF, 5.7% on LERF-OVS, and 1.0% on 3D-OVS.
- Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental limitations: (1) language ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental limitations: (1) language ...
- GeoCGA consistently outperforms prior state-of-the-art methods, yielding relative mIoU improvements of 20.8% on Ref-LERF, 5.7% on LERF-OVS, and 1.0% on 3D-OVS.
- To address this, we propose GeoCGA, a geometry-aware cross-modal graph alignment framework that bridges linguistic semantics with the 3DGS representation.

## Abstract Cue
- Referring 3D segmentation seeks to localize and segment target objects in a 3D scene given a natural-language query, requiring joint reasoning over geometric structures and linguistic cues.
