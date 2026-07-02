# SAGS: Structure-Aware 3D Gaussian Splatting

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SAGS-Structure-Aware-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Novel View Synthesis (NVS) is a long-studied problem that aims to generate images of a scene from a specific point of view, using only a sparse set of ...

## Core Idea
- In this work, we propose a structure-aware Gaussian Splatting method (SAGS) that implicitly encodes the geometry of the scene, which reflects to state-of-the-art rendering performance and reduced storage ...
- Additionally, we introduce a lightweight version of SAGS, using a simple yet effective mid-point interpolation scheme, which showcases a compact representation of the scene with up to 24× ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In this work, we propose a structure-aware Gaussian Splatting method (SAGS) that implicitly encodes the geometry of the scene, which reflects to state-of-the-art rendering performance and reduced storage ...
- Extensive experiments across multiple benchmark datasets demonstrate the superiority of SAGS compared to state-of-theart 3D-GS methods under both rendering quality and model size.
- Several extensions of 3DGS have been proposed to achieve compressible and high-fidelity performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose a structure-aware Gaussian Splatting method (SAGS) that implicitly encodes the geometry of the scene, which reflects to state-of-the-art rendering performance and reduced storage ...
- Additionally, we introduce a lightweight version of SAGS, using a simple yet effective mid-point interpolation scheme, which showcases a compact representation of the scene with up to 24× ...
- Extensive experiments across multiple benchmark datasets demonstrate the superiority of SAGS compared to state-of-theart 3D-GS methods under both rendering quality and model size.

## Abstract Cue
- Following the advent of NeRFs, 3D Gaussian Splatting (3DGS) has paved the way to real-time neural rendering overcoming the computational burden of volumetric methods.
