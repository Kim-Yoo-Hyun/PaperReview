# Problem

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_UniDepth-Universal-Monocular-Metric-Depth-Estimation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Departing from the existing MMDE methods, UniDepth directly predicts metric 3D points from the input image at inference time without any additional information, striving for a universal and ...
- These methods fail to generalize to unseen domains even in the presence of moderate domain gaps, which hinders their practical applicability.

## 해결하려는 문제
- We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- In addition, we propose a geometric invariance loss that promotes the invariance of camera-prompted depth features.
- We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
