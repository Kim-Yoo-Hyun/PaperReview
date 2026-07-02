# Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Rh-3DGS-Robust-Open-Vocabulary-Scene-Understanding-via-Rie/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Problem: Boundary ambiguity & view inconsistency Open-vocabulary 3D scene understanding answers free-form text queries over reconstructed scenes.
- Existing 3DGS-based methods often average normalized embeddings in Euclidean space.
- Visibility-Calibrated Distillation (VCD) computes per-pixel reliability weights from rasterization statistics and down-weights ambiguous pixels.

## Core Idea
- We propose Rh-3DGS, a robust semantic 3DGS framework that uses reliability-aware distillation and manifold-consistent aggregation.
- Rh-3DGS applies VCD for pixel reliability, VFM for hyperspherical aggregation, and LIC for local 3D consistency, yielding sharper and view-stable masks (g–h). ple is 3D Gaussian Splatting (3DGS) ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on three benchmarks show that Rh3DGS is best on open-vocabulary segmentation, boundary quality, and view-consistent rendering. (b) Baseline mask (View-1) (a) RGB(View-1) + zoom-in box (c) Baseline ...
- Lightweight Consistency Contrast (LIC) regularizes the 3D semantic field with neighborhood-based multi-positive contrast to improve local consistency and sharper boundaries.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on three benchmarks show that Rh3DGS is best on open-vocabulary segmentation, boundary quality, and view-consistent rendering. (b) Baseline mask (View-1) (a) RGB(View-1) + zoom-in box (c) Baseline ...
- We propose Rh-3DGS, a robust semantic 3DGS framework that uses reliability-aware distillation and manifold-consistent aggregation.
- However, lifting dense 2D foundationmodel embeddings into 3D Gaussian Splatting (3DGS) is still challenging.

## Abstract Cue
- Problem: Boundary ambiguity & view inconsistency Open-vocabulary 3D scene understanding answers free-form text queries over reconstructed scenes.
