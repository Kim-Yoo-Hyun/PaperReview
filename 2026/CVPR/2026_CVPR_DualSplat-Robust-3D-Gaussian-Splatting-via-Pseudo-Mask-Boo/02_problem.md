# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_DualSplat-Robust-3D-Gaussian-Splatting-via-Pseudo-Mask-Boo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We address this challenge with DualSplat, a Failure-toPrior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage.
- Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks.
- Existing approaches to transient-robust reconstruction mainly follow two directions.

## 해결하려는 문제
- While 3D Gaussian Splatting (3DGS) achieves realtime photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency.
- Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.
- We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
