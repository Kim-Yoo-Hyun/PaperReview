# SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_SR3R-Rethinking-Super-Resolution-3D-Reconstruction-With-Fe/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited from pretrained 2D ...
- We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific high-frequency geometry and ...

## Core Idea
- We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific high-frequency geometry and ...
- Training Objective The predicted HR 3DGS G HR is rendered into novel-view images and supervised using the corresponding ground-

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 3D super-resolution (3DSR) aims to reconstruct highresolution (HR) 3D scenes from low-resolution (LR) multiview images.
- Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited from pretrained 2D ...
- This severely limits reconstruction fidelity, cross-scene generalization, and real-time usability.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific high-frequency geometry and ...
- Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited from pretrained 2D ...

## Abstract Cue
- 3D super-resolution (3DSR) aims to reconstruct highresolution (HR) 3D scenes from low-resolution (LR) multiview images.
