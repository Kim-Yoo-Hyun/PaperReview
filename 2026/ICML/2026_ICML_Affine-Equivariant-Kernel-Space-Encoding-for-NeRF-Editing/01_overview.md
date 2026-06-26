# Affine-Equivariant Kernel Space Encoding for NeRF Editing

- Year/Venue: 2026 / ICML
- Category: 3D Equivariance, Calibration, and Registration
- Tags: NeRF, equivariant, 3D Vision
- Authors: Mikołaj Zieliński, Krzysztof Byrski, Tomasz Szczepanik, Dominik Belter, Przemysław Spurek
- Paper: https://openreview.net/forum?id=fAj3MJghc0
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making ...
- Method cue: In this paper, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a spatial encoding for neural radiance fields that provides localized, deformation-aware feature representations.
- Result cue: Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making ...

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `geometry-aware equivariant modeling`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- geometry-aware equivariant modeling 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: NeRF, equivariant, 3D Vision.
- 초록에서 확인되는 주요 cue: Neural, While, Affine-Equivariant, Kernel, Space, Encoding, EKS, Instead.
