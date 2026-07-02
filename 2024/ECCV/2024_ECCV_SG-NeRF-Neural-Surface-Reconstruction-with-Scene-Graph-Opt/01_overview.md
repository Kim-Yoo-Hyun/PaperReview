# SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: NeRF, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SG-NeRF-Neural-Surface-Reconstruction-with-Scene-Graph-Opt/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To tackle this challenge, we present a novel approach that optimizes radiance fields with scene graphs to mitigate the influence of outlier poses.
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- However, NeRFs require accurate camera poses as input, and existing methods struggle to handle significantly noisy pose estimates (i.e., outliers), which are commonly encountered in real-world scenarios.

## Core Idea
- Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset (Sec.
- We evaluate the effectiveness of our method through extensive experiments on various datasets, which includes a new inward-facing dataset containing significant outlier camera poses produced by the SfM ...

## Limitation
- Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose effect is still largely alleviated with the proposed confidence scheme), ...

## Contribution
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- To tackle this challenge, we present a novel approach that optimizes radiance fields with scene graphs to mitigate the influence of outlier poses.
- Furthermore, we propose a new dataset containing typical outlier poses for a detailed evaluation.

## Abstract Cue
- 3D surface reconstruction from images is essential for numerous applications.
