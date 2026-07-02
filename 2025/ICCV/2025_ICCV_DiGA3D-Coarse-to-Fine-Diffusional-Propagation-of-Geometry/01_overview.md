# DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_DiGA3D-Coarse-to-Fine-Diffusional-Propagation-of-Geometry/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, there are still challenges in performing multiple 3D inpainting tasks within a unified framework: 1) Single reference inpainting methods lack robustness when dealing with views that are ...
- To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in a coarse-tofine manner.
- Although several methods have explored unified pipelines for versatile 3D inpainting, they still face some challenges: First, some methods rely on a single reference image to guide the ...

## Core Idea
- For the coarse stage, we use PowerPaint-v1 and Stable Diffusion v1.5 with its Con- To assess our methods across various inpainting tasks, we conduct comparisons with different techniques ...
- To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in a coarse-tofine manner.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on multiple 3D inpainting tasks demonstrate the effectiveness of our method.
- Furthermore, DiGA3D introduces a Texture-Geometry Score Distillation Sampling (TG-SDS) loss to further improve the geometric consistency of inpainted 3D scenes.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in a coarse-tofine manner.
- Extensive experiments on multiple 3D inpainting tasks demonstrate the effectiveness of our method.
- Next, DiGA3D designs an Attention Feature Propagation (AFP) mechanism that propagates attention features from the selected reference views to other views via diffusion models to maintain appearance consistency.

## Abstract Cue
- Developing a unified pipeline that enables users to remove, re-texture, or replace objects in a versatile manner is crucial for text-guided 3D inpainting.
