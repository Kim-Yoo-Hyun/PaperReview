# Method

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_UniDepth-Universal-Monocular-Metric-Depth-Estimation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- In addition, we propose a geometric invariance loss that promotes the invariance of camera-prompted depth features.
- We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.

## 원리적 동기
- Departing from the existing MMDE methods, UniDepth directly predicts metric 3D points from the input image at inference time without any additional information, striving for a universal and ...
- These methods fail to generalize to unseen domains even in the presence of moderate domain gaps, which hinders their practical applicability.
- We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.

## 핵심 방법론
- The last four methods are tested in a zero-shot setting.
- The required training time amounts to roughly
