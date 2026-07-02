# PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_PLANA3R-Zero-shot-Metric-Planar-3D-Reconstruction-via-Feed/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We aim to eliminate the reliance on dense plane-level annotations and accurate multi-view camera poses, addressing the limitations discussed above.
- Rather than relying on explicit planar 3D annotations, we leverage depth and normal maps3 , which are more readily available in existing two-view datasets at scale, as supervision ...
- However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models typically requires accurate plane masks and 3D plane annotations from monocular or ...

## Core Idea
- Our approach employs Vision Transformers to extract a set of sparse planar primitives, estimate relative camera poses, and supervise geometry learning via planar splatting, where gradients are propagated ...
- Using planar 3D primitives – a well-suited representation for man-made environments – we introduce P LANA 3R, a pose-free framework for metric Planar 3D Reconstruction from unposed two-view ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 4.3 Baselines and Evaluation Metrics We evaluate our P LANA 3R against state-of-the-art (SOTA) planar reconstruction methods across multiple tasks, including 3D reconstruction, pose estimation, depth estimation, and ...
- We validate P LANA 3R on multiple indoor-scene datasets with metric supervision and demonstrate strong generalization to out-of-domain indoor environments across diverse tasks under metric evaluation protocols, including ...
- Among these test sets, except for ScanNetV2, the remaining three datasets demonstrate the generalization capability of our model across different datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach employs Vision Transformers to extract a set of sparse planar primitives, estimate relative camera poses, and supervise geometry learning via planar splatting, where gradients are propagated ...
- Using planar 3D primitives – a well-suited representation for man-made environments – we introduce P LANA 3R, a pose-free framework for metric Planar 3D Reconstruction from unposed two-view ...
- Furthermore, by formulating with planar 3D representation, our method emerges with the ability for accurate plane segmentation.

## Abstract Cue
- This paper addresses metric 3D reconstruction of indoor scenes by exploiting their inherent geometric regularities with compact representations.
