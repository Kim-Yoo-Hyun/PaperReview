# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_PLANA3R-Zero-shot-Metric-Planar-3D-Reconstruction-via-Feed/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We aim to eliminate the reliance on dense plane-level annotations and accurate multi-view camera poses, addressing the limitations discussed above.
- Rather than relying on explicit planar 3D annotations, we leverage depth and normal maps3 , which are more readily available in existing two-view datasets at scale, as supervision ...
- However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models typically requires accurate plane masks and 3D plane annotations from monocular or ...

## 해결하려는 문제
- Our approach employs Vision Transformers to extract a set of sparse planar primitives, estimate relative camera poses, and supervise geometry learning via planar splatting, where gradients are propagated ...
- Using planar 3D primitives – a well-suited representation for man-made environments – we introduce P LANA 3R, a pose-free framework for metric Planar 3D Reconstruction from unposed two-view ...
- Furthermore, by formulating with planar 3D representation, our method emerges with the ability for accurate plane segmentation.

## 선행 연구 / 배경 단서
- Rather than relying on explicit planar 3D annotations, we leverage depth and normal maps3 , which are more readily available in existing two-view datasets at scale, as supervision ...
- We aim to eliminate the reliance on dense plane-level annotations and accurate multi-view camera poses, addressing the limitations discussed above.
- However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models typically requires accurate plane masks and 3D plane annotations from monocular or ...
