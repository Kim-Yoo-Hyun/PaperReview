# Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

- Year/Venue: 2025 / NeurIPS 2025 Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Huan Wang, Yu Yin
- Paper: https://openreview.net/forum?id=ycPVp0577R
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Open-vocabulary querying in 3D space is crucial for enabling more intelligent perception in applications such as robotics, autonomous systems, and augmented reality.
- Method cue: In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- Result cue: Extensive experiments on various datasets demonstrate the effectiveness of our proposed method in both static and dynamic scenarios.

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
- 초록에서 확인되는 주요 cue: Open-vocabulary, However, Moreover, Segment, Splat, Gaussian, Splatting, Gaussians.
