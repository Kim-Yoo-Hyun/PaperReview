# Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Repurposing-2D-Diffusion-Models-with-Gaussian-Atlas-for-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this challenge, we propose repurposing pre-trained 2D diffusion models for 3D object generation.
- However, such models have significant limitations especially when trained solely on 3D data, as high-quality 3D data is relatively scarce compared to 2D images.
- Previous Work Recent advances in text-to-image diffusion models have been driven by the increasing availability of paired 2D data.

## Core Idea
- We introduce Gaussian Atlas, a novel representation that utilizes dense 2D grids, enabling the fine-tuning of 2D diffusion models to generate 3D Gaussians.
- To fully harness the capabilities of these 2D diffusion models, we introduce Gaussian Atlas, a nove DreamGaussian LGM TriplaneGaussian GaussianCube “A carved GaussianAtlas stone” (Ours) CLIP score ⇒ ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experimental results show that text-to-image diffusion models can be effectively adapted for 3D content generation, bridging the gap between 2D and 3D modeling. or Text Prompts 2D ...
- In this work, we achieve 3D object generation by directly fine-tuning 2D generation models.
- To achieve higher rendering fidelity in 3D generation, it is desirable to leverage the learned prior knowledge from well-pretrained 2D diffusion models .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce Gaussian Atlas, a novel representation that utilizes dense 2D grids, enabling the fine-tuning of 2D diffusion models to generate 3D Gaussians.
- To fully harness the capabilities of these 2D diffusion models, we introduce Gaussian Atlas, a nove
- Our approach demonstrates successful transfer learning from a pre-trained 2D diffusion model to a 2D manifold flattened from 3D structures.

## Abstract Cue
- Previous Work Recent advances in text-to-image diffusion models have been driven by the increasing availability of paired 2D data.
