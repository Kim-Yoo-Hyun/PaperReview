# LangSplat: 3D Language Gaussian Splatting

- Year/Venue: 2024 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, Vision-Language, grounding
- Paper link: ./2024/CVPR/2024_CVPR_LangSplat-3D-Language-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...
- By employing a tile-based splatting technique for rendering language features, we circumvent the costly rendering process inherent in NeRF.

## Core Idea
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- Instead of directly learning CLIP embeddings, LangSplat first trains a scene-wise language autoencoder and then learns language features on the scene-specific latent space, bed bench room sofa lawn ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Humans live in a 3D world and commonly use natural language to interact with a 3D scene.
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- This paper introduces LangSplat, which constructs a 3D language field that enables precise and efficient open-vocabulary querying within 3D spaces.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- Instead of directly learning CLIP embeddings, LangSplat first trains a scene-wise language autoencoder and then learns language features on the scene-specific latent space,

## Abstract Cue
- Humans live in a 3D world and commonly use natural language to interact with a 3D scene.
