# OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Authors: Mark He Huang, Lin Geng Foo, Christian Theobalt, Ying Sun, De Wen Soh
- Paper: https://openreview.net/forum?id=Y9AdTCCEgI
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Free-moving object reconstruction from monocular video remains challenging, particularly without reliable pose or depth cues and under arbitrary object motion.
- Method cue: We introduce OnlineSplatter, a novel online feed-forward framework generating high-quality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or ...
- Result cue: Evaluations on real-world datasets demonstrate that OnlineSplatter significantly outperforms state-of-the-art pose-free reconstruction baselines, consistently improving with more observations while maintaining constant memory and runtime.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision.
- 초록에서 확인되는 주요 cue: Free-moving, OnlineSplatter, Gaussians, RGB, Our, Gaussian, This, Evaluations.
