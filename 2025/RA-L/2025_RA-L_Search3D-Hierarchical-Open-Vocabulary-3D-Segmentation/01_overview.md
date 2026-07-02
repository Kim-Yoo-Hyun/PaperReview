# Search3D: Hierarchical Open-Vocabulary 3D Segmentation

- Year/Venue: 2025 / RA-L
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2025/RA-L/2025_RA-L_Search3D-Hierarchical-Open-Vocabulary-3D-Segmentation/paper.pdf
- Code/Project: http://search3d-segmentation.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions described by generic ...
- Unlike prior methods, Search3D shifts towards a more flexible open-vocabulary 3D search paradigm, moving beyond explicit object-centric queries.

## Core Idea
- However, this To evaluate our method’s ability to handle queries beyond can be problematic when performing and evaluating open- object-level descriptions, we introduce the task of scene-level vocabulary ...
- In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object parts, entire objects, ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
- For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations on ScanNet++.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object parts, entire objects, ...
- Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
- For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations on ScanNet++.

## Abstract Cue
- —Open-vocabulary 3D segmentation enables exploration of 3D spaces using free-form text descriptions.
