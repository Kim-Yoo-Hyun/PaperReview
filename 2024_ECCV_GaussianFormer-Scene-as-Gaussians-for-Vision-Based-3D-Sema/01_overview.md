# GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Authors: Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, Jiwen Lu*
- Paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: "3D semantic occupancy prediction aims to obtain 3D fine-grained geometry and semantics of the surrounding scene and is an important task for the robustness ...
- Method cue: To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region ...
- Result cue: Experimental results demonstrate that GaussianFormer achieves comparable performance with state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Gaussian Splatting, semantic.
- 초록에서 확인되는 주요 cue: Most, Gaussians, Gaussian, Gaussian-to-voxel, KITTI-360, Experimental, GaussianFormer, Code.
