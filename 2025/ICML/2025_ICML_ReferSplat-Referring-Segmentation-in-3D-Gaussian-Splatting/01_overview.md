# ReferSplat: Referring Segmentation in 3D Gaussian Splatting

- Year/Venue: 2025 / ICML Oral
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_ReferSplat-Referring-Segmentation-in-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Our analysis reveals that 3D multimodal understanding and spatial relationship modeling are key challenges for R3DGS.
- To address these challenges, we propose ReferSplat, a framework that explicitly models 3D Gaussian points with natural language expressions in a spatially aware paradigm.
- This task requires the model to identify newly described objects that may be occluded or not directly visible in a novel view, posing a significant challenge for 3D ...

## Core Idea
- Training Multi-view Images We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...
- Extensive experiments demonstrate that ReferSplat achieves state-of-the-art performance on both open-vocabulary 3DGS segmentation and the newly proposed referring 3DGS segmentation tasks. ⨂ Rendered Feature Output Mask Pseudo GT ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that ReferSplat achieves state-of-the-art performance on both open-vocabulary 3DGS segmentation and the newly proposed referring 3DGS segmentation tasks. ⨂ Rendered Feature Output Mask Pseudo GT ...
- When integrating all components (index 3), referred to as ReferSplat, we achieve a substantial performance gain, reaching a new state-of-the-art.
- This raises a question: Can we design a network that models 3D Gaussians with language expressions in a spatially aware paradigm? • To tackle the challenges of R3DGS, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that ReferSplat achieves state-of-the-art performance on both open-vocabulary 3DGS segmentation and the newly proposed referring 3DGS segmentation tasks. ⨂ Rendered Feature Output Mask Pseudo GT ...
- This raises a question: Can we design a network that models 3D Gaussians with language expressions in a spatially aware paradigm? • To tackle the challenges of R3DGS, ...
- Training Multi-view Images We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...

## Abstract Cue
- Training Multi-view Images We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural language descriptions, which often contain spatial relationships or object attributes.
