# SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_SplaTAM-Splat-Track-and-Map-3D-Gaussians-for-Dense-RGB-D-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This work introduces SplaTAM, an approach that, for the first time, leverages explicit volumetric representations, i.e., 3D Gaussians, to enable high-fidelity reconstruction from a single unposed RGB-D camera, ...
- For the past three decades, SLAM research has extensively centered around the question of map representation – resulting in a variety of sparse , dense , and neural ...

## Core Idea
- In contrast, our approach successfully manages to track the camera over both sequences giving an average trajectory error of only 1.2cm.
- This work introduces SplaTAM, an approach that, for the first time, leverages explicit volumetric representations, i.e., 3D Gaussians, to enable high-fidelity reconstruction from a single unposed RGB-D camera, ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments show that SplaTAM achieves up to 2× superior performance in camera pose estimation, map construction, and novel-view synthesis over existing methods, paving the way for more ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments show that SplaTAM achieves up to 2× superior performance in camera pose estimation, map construction, and novel-view synthesis over existing methods, paving the way for more ...
- This work introduces SplaTAM, an approach that, for the first time, leverages explicit volumetric representations, i.e., 3D Gaussians, to enable high-fidelity reconstruction from a single unposed RGB-D camera, ...
- SplaTAM employs a simple online tracking and mapping system tailored to the underlying Gaussian representation.

## Abstract Cue
- Dense simultaneous localization and mapping (SLAM) is crucial for robotics and augmented reality applications.
