# 3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_3D-Gaussian-Splatting-with-Self-Constrained-Priors-for-Hig/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Rendering 3D surfaces has been revolutionized within the modeling of radiance fields through either 3DGS or NeRF.
- Although 3DGS has shown advantages over NeRF in terms of rendering quality or speed, there is still room for improvement in recovering high fidelity surfaces through 3DGS.
- To resolve this issue, we propose a self-constrained prior to constrain the learning of 3D Gaussians, aiming for more accurate depth rendering.

## Core Idea
- To resolve this issue, we propose a self-constrained prior to constrain the learning of 3D Gaussians, aiming for more accurate depth rendering.
- Error map comparison of rendering on NeRF-Synthetic. our method extracts stable implicit priors from depth maps for more stable geometry inference.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We justify our idea and report our superiority over the state-of-the-art methods in evaluations on widely used benchmarks.
- Although 3DGS has shown advantages over NeRF in terms of rendering quality or speed, there is still room for improvement in recovering high fidelity surfaces through 3DGS.
- Compared with ray tracing based neural rendering methods , 3DGS shows faster rendering speed and better visual fidelity.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To resolve this issue, we propose a self-constrained prior to constrain the learning of 3D Gaussians, aiming for more accurate depth rendering.
- However, it is still limited in recovering accurate geometry. h312h@wayne.edu Recent works on improving accuracy of depth rendering adopts different strategies, such as reformulating rendering equations for unbiased ...
- We justify our idea and report our superiority over the state-of-the-art methods in evaluations on widely used benchmarks.

## Abstract Cue
- Rendering 3D surfaces has been revolutionized within the modeling of radiance fields through either 3DGS or NeRF.
