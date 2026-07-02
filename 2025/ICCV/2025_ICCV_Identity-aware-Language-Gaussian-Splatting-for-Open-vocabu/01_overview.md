# Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2025/ICCV/2025_ICCV_Identity-aware-Language-Gaussian-Splatting-for-Open-vocabu/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation still makes the practical use of open-vocabulary 3D semantic segmentation challenging.
- To do this, most previous methods have utilized high-quality 3D point clouds , however, it is quite difficult to acquire data, which reflects various realworld environments, with language ...

## Core Idea
- To address this issue, we propose a simple yet powerful method that aligns language embeddings via the identity information.
- Furthermore, we propose a progressive mask expanding scheme that enables more accurate extraction of semantic mask boundaries.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance in open-vocabulary 3D semantic segmentation. https://github.com/DCVL-3D/ILGS release view2 Cosine similarity Others Sheep view2 view1 Gaussian field ...
- Even though many methods have shown the notable improvement in this task, they still have difficulties to make language embeddings be consistent across different views.
- This inconsistency highly results in mis-labeling where different language embeddings are assigned to the same part of an object.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance in open-vocabulary 3D semantic segmentation. https://github.com/DCVL-3D/ILGS release view2 Cosine similarity Others Sheep view2 view1 Gaussian field ...
- Even though many methods have shown the notable improvement in this task, they still have difficulties to make language embeddings be consistent across different views.
- To address this issue, we propose a simple yet powerful method that aligns language embeddings via the identity information.

## Abstract Cue
- view1 Text query : Sheep Open-vocabulary 3D semantic segmentation has been actively studied by incorporating language features into 3D scene representations.
