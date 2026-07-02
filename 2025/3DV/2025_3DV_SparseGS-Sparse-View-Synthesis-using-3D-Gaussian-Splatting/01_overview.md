# SparseGS: Sparse View Synthesis using 3D Gaussian Splatting

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_SparseGS-Sparse-View-Synthesis-using-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views.
- SparseGS incorporates depth priors, novel depth rendering techniques, and a pruning heuristic to mitigate floater artifacts, alongside an Unseen Viewpoint Regularization module to alleviate background collapses.

## Core Idea
- In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views.
- However, this technique requires dense training views to accurately reconstruct 3D geometry.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our extensive evaluations on the Mip-NeRF360, LLFF, and DTU datasets demonstrate that SparseGS achieves highquality reconstruction in both unbounded and forwardfacing scenarios, with as few as 12 and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views.
- Our extensive evaluations on the Mip-NeRF360, LLFF, and DTU datasets demonstrate that SparseGS achieves highquality reconstruction in both unbounded and forwardfacing scenarios, with as few as 12 and ...
- However, this technique requires dense training views to accurately reconstruct 3D geometry.

## Abstract Cue
- 3D Gaussian Splatting (3DGS) has recently enabled real-time rendering of unbounded 3D scenes for novel view synthesis.
