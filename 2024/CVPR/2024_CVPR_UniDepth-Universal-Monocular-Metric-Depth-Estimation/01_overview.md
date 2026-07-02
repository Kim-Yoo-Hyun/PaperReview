# UniDepth: Universal Monocular Metric Depth Estimation

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_UniDepth-Universal-Monocular-Metric-Depth-Estimation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Departing from the existing MMDE methods, UniDepth directly predicts metric 3D points from the input image at inference time without any additional information, striving for a universal and ...
- These methods fail to generalize to unseen domains even in the presence of moderate domain gaps, which hinders their practical applicability.

## Core Idea
- We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- In addition, we propose a geometric invariance loss that promotes the invariance of camera-prompted depth features.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Thorough evaluations on ten datasets in a zero-shot regime consistently demonstrate the superior performance of UniDepth, even when compared with methods directly trained on the testing domains.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- In addition, we propose a geometric invariance loss that promotes the invariance of camera-prompted depth features.
- We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.

## Abstract Cue
- 𝓏 𝑬 𝓏 Spherical Cartesian 𝜙 Accurate monocular metric depth estimation (MMDE) is crucial to solving downstream tasks in 3D perception and modeling.
