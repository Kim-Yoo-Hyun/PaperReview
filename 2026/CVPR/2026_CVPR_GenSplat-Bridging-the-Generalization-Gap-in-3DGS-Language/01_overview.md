# GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language, generalization
- Paper link: ./2026/CVPR/2026_CVPR_GenSplat-Bridging-the-Generalization-Gap-in-3DGS-Language/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.
- However, they inherently lack cross-scene generalization (as they require per-scene optimization) and do not support comprehensive spatial reasoning beyond segmentation, e.g., for visual question answering (VQA) or captioning ...
- Although large-scale training enables the generalization of SceneSplat across scenes, its formulation remains restricted to a predefined vocabulary and thus fails to handle free-form language queries.

## Core Idea
- In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).
- Following , we use diverse datasets for training, including ScanRefer , Nr3D , Sr3D , Multi3DRefer , ScanQA , SQA3D , Scan2Cap and Nr3DCaptioning .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive cross-task evaluations (including 3D referring segmentation, 3D visual question answering, and 3D open-vocabulary understanding) demonstrate state-of-the-art performances and strong generalization capability of GenSplat.
- ing this gap to achieve fine-grained language-guided understanding across 3DGS representations is highly desirable.
- Unlike previous methods that either achieve cross-scene generalization by being bounded to a predefined vocabulary or handle free-form language by overfitting to individual scenes, GenSplat is robust to ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To further improve spatial alignment and computational efficiency, we introduce a Geometry-Aware Frame Selector (GAFS), which adaptively selects the most informative views based on Gaussian and textural cues.
- In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).
- Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.

## Abstract Cue
- ing this gap to achieve fine-grained language-guided understanding across 3DGS representations is highly desirable.
