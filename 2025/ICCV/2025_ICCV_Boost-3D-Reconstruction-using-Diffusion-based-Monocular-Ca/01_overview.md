# Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_Boost-3D-Reconstruction-using-Diffusion-based-Monocular-Ca/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To overcome these limitations, recent studies have recast monocular camera calibration as a learning-based regression problem, leveraging a single image to directly infer its intrinsic parameters.
- Monocular camera calibration is inherently an ill-posed problem, requiring additional information to address it.
- Traditional approaches have attempted to incorporate handcrafted knowledge to solve the problem, such as the gravity direction , Manhattan World constraints , and human face priors .

## Core Idea
- 1, we present two portrait In this paper, we present DM-Calib, a diffusion-based approach for estimating pinhole camera intrinsic parameters from a single input image.
- Though our method is trained for metric depth, we transform the predicted depth into affine-invariant depth for broader comparisons.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- While learning-based methods benefit from data-driven knowledge, outperforming traditional approaches, they are constrained by the limited availability of public datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- 1, we present two portrait In this paper, we present DM-Calib, a diffusion-based approach for estimating pinhole camera intrinsic parameters from a single input image.
- However, most existing methods depend on handcrafted assumptions or are constrained by limited training data, resulting in poor generalization across dive
- As a result, these methods tend to overfit on training data and exhibit poor generalization to unseen scenarios.

## Abstract Cue
- pose estimation , 3D reconstruction , and zero-shot metric depth estimation .
