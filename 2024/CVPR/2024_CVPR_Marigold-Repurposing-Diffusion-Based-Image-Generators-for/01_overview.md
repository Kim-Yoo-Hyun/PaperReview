# Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: Diffusion, Generation, depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Marigold-Repurposing-Diffusion-Based-Image-Generators-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can only be solved with the help of prior knowledge, ...
- Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted by the data ...

## Core Idea
- We introduce Marigold, a method for affine-invariant 1.
- The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- It delivers state-of-the-art performance across a wide range of datasets, including over 20% performance gains in specific cases.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures.
- Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted by the data ...
- We introduce Marigold, a method for affine-invariant 1.

## Abstract Cue
- monocular depth estimation that is derived from Stable Diffusion and retains its rich prior knowledge.
