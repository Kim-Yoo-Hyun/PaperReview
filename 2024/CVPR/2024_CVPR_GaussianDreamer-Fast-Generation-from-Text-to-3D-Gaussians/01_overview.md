# GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_GaussianDreamer-Fast-Generation-from-Text-to-3D-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- 3D diffusion models have good 3D consistency, but their quality and generalization are limited as trainable 3D data is expensive and hard to obtain.
- Introduction 3D asset generation has been an expensive and professional work in conventional pipelines.
- The former one is direct to implement and holds strong 3D consistency, but struggles to extend into a large generation domain as 3D data is usually hard and ...

## Core Idea
- Conclusion We propose a fast text-to-3D method GaussianDreamer by bridging the abilities of 3D and 2D diffusion models via the Gaussian splatting representation.
- Visualization Results In this section, we present the results of initializing the 3D Gaussians with two different 3D diffusion models: text-to3D and text-to-motion diffusion models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In recent times, the generation of 3D assets from text prompts has shown impressive results.
- Recently, diffusion models have achieved great success in creating high-quality and realistic 2D images.
- This results in the generated 3D assets falling short in dealing with complex text prompts and producing complex/fine geometry and appearance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Here come two main streams for achieving this goal: (i) training a new diffusion model with 3D data (namely the 3D diffusion model) and (ii) lifting the 2D ...
- This paper attempts to bridge the power from the two types of diffusion models via the recent explicit and efficient 3D Gaussian splatting representation.
- A fast 3D object generation framework, named as GaussianDreamer, is proposed, where the 3D diffusion model provides priors for initialization and the 2D diffusion model enriches the geometry ...

## Abstract Cue
- In recent times, the generation of 3D assets from text prompts has shown impressive results.
