# OpenScene: 3D Scene Understanding with Open Vocabularies

- Year/Venue: 2023 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, 3D semantic, CLIP
- Paper link: ./2023/CVPR/2023_CVPR_OpenScene-3D-Scene-Understanding-with-Open-Vocabularies/paper.pdf
- Code/Project: https://pengsongyou.github.io/openscene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- posed RGB images, the goal is to infer the semantics, affordances, functions, and physical properties of every 3D point.
- For example, given the house shown in Figure 1, we would like to predict which surfaces are part of a fan (semantics), made of metal (materials), within a ...
- Answers to these queries can help a robot interact intelligently with the scene or help a person understand it through interactive query and visualization.

## Core Idea
- We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in CLIP feature space.
- Our approach is effective at identifying objects, materials, affordances, activities, and room types in complex 3D scenes, all using a single model trained without any labeled 3D data.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- For example, given the house shown in Figure 1, we would like to predict which surfaces are part of a fan (semantics), made of metal (materials), within a ...
- Traditional 3D scene understanding systems are trained with supervision from benchmark datasets designed for specific tasks (e.g., 3D semantic segmentation for a closed set of 20 classes ).

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in CLIP feature space.
- Our approach is effective at identifying objects, materials, affordances, activities, and room types in complex 3D scenes, all using a single model trained without any labeled 3D data.
- This zero-shot approach enables taskagnostic training and open-vocabulary queries.

## Abstract Cue
- posed RGB images, the goal is to infer the semantics, affordances, functions, and physical properties of every 3D point.
