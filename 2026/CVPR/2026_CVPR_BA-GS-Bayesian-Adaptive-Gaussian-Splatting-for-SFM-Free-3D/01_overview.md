# BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_BA-GS-Bayesian-Adaptive-Gaussian-Splatting-for-SFM-Free-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Recent works attempt to address this limitation by leveraging pre-trained image matching models to generate Gaussian primitives but overlook the probabilistic uncertainty embedded in both the initial primitive ...
- By robustly handling initialization and optimization noise, our work paves the way for scalable 3D scene reconstruction from sparse image captures. synthesis and scene reconstruction.
- However, its reliance on Structure-from-Motion preprocessing may lead to degraded performance under sparse-view scenarios.

## Core Idea
- Hence, we propose BA-GS, a Bayesian framework that models both the global distribution and local uncertainty of Gaussian primitives.
- Among them, 3DGS offers competitive visual fidelity with a significantly faster training speed.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments across multiple benchmark datasets including Tanks and Temples, MVimgNet, and LLFF demonstrate that our method consistently outperforms existing approaches.
- This hierarchical Bayesian formulation effectively bridges probabilistic distribution modeling and uncertainty-aware optimization, resulting in improved reconstruction quality under sparse-view conditions.
- 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments across multiple benchmark datasets including Tanks and Temples, MVimgNet, and LLFF demonstrate that our method consistently outperforms existing approaches.
- Hence, we propose BA-GS, a Bayesian framework that models both the global distribution and local uncertainty of Gaussian primitives.
- 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.

## Abstract Cue
- 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.
