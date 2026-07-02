# Problem

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language, generalization
- Paper link: ./2026/CVPR/2026_CVPR_GenSplat-Bridging-the-Generalization-Gap-in-3DGS-Language/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.
- However, they inherently lack cross-scene generalization (as they require per-scene optimization) and do not support comprehensive spatial reasoning beyond segmentation, e.g., for visual question answering (VQA) or captioning ...
- Although large-scale training enables the generalization of SceneSplat across scenes, its formulation remains restricted to a predefined vocabulary and thus fails to handle free-form language queries.

## 해결하려는 문제
- To further improve spatial alignment and computational efficiency, we introduce a Geometry-Aware Frame Selector (GAFS), which adaptively selects the most informative views based on Gaussian and textural cues.
- In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).
- Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
