# SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning
- Paper link: ./2024/ECCV/2024_ECCV_SceneGraphLoc-Cross-Modal-Coarse-Visual-Localization-on-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Coarse visual localization, or place recognition, is a fundamental component in computer vision and robotics applications, defined as the task of identifying the approximate location where a query ...

## Core Idea
- We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- In image-based methods, we use all images from the database and determine the scene based on the retrieved image.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With images, SceneGraphLoc achieves performance close to that of state-of-the-art techniques depending on large image databases, while requiring three orders-of-magnitude less storage and operating orders-of-magnitude faster.
- For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet and AnyLoc .
- This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- With images, SceneGraphLoc achieves performance close to that of state-of-the-art techniques depending on large image databases, while requiring three orders-of-magnitude less storage and operating orders-of-magnitude faster.
- We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.

## Abstract Cue
- We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
