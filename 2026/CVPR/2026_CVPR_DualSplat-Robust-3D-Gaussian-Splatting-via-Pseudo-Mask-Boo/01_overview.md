# DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_DualSplat-Robust-3D-Gaussian-Splatting-via-Pseudo-Mask-Boo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We address this challenge with DualSplat, a Failure-toPrior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage.
- Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks.
- Existing approaches to transient-robust reconstruction mainly follow two directions.

## Core Idea
- In the lower example, our method reduces erroneous background occlusion more effectively and reconstructs a cleaner static layout around the object and wall boundary.
- We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.
- While 3D Gaussian Splatting (3DGS) achieves realtime photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency.
- Recent 3DGS-based methods improve efficiency by incorporating pretrained features, learned masks, or explicit static/transient decomposition.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- While 3D Gaussian Splatting (3DGS) achieves realtime photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency.
- Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.
- We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training.

## Abstract Cue
- https://lans1ot.github.io/DualSplat/.
