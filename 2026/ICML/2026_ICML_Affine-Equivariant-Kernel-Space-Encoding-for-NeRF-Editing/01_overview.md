# Affine-Equivariant Kernel Space Encoding for NeRF Editing

- Year/Venue: 2026 / ICML
- Category: 3D Equivariance, Calibration, and Registration
- Tags: NeRF, equivariant, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Affine-Equivariant-Kernel-Space-Encoding-for-NeRF-Editing/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making localized editing and physically ...

## Core Idea
- In this paper, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a spatial encoding for neural radiance fields that provides localized, deformation-aware feature representations.
- This enables intuitive, localized scene editing directly via Gaussian kernels without retraining, while maintaining high-quality rendering.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making localized editing and physically ...
- While several works introduce explicit control structures or point-based latent representations to improve editability, these approaches often suffer from limited locality, sensitivity to deformations, or visual artifacts.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This enables intuitive, localized scene editing directly via Gaussian kernels without retraining, while maintaining high-quality rendering.
- In this paper, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a spatial encoding for neural radiance fields that provides localized, deformation-aware feature representations.
- To preserve detail without sacrificing editability, we further propose a training-time feature distillation mechanism that transfers information from multi-resolution hash grid encodings into the kernel field, yielding a ...

## Abstract Cue
- This kernel-based formulation enables stable feature interpolation under spatial transformations while preserving continuity and high reconstruction quality.
