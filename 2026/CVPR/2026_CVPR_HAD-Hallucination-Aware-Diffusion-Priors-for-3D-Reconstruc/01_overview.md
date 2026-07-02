# HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_HAD-Hallucination-Aware-Diffusion-Priors-for-3D-Reconstruc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- This dependency severely limits performance in data-sparse scenarios, such as sparse-view settings and extreme novelview extrapolation tasks where the quality of rendered images degrades dramatically, as illustrated in ...
- These hallucination scores enable selective masking of unreliable pixels during the progressive 3D reconstruction procedure, preventing the introduction of nonexistent artifacts into the 3D model.

## Core Idea
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- For each scene, we first train a 3DGS model using 9 input training views, then generate 100 augmented novel views via diffusion priors at a resolution of 960×540.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across mul- 1.
- Despite their significant achievements, these methods require dense camera coverage and high-fidelity image inputs to maintain reliable performance.
- While these augmented views achieve photorealism, they often fail to maintain fidelity to the original input views.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across mul- 1.
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- Diffusion priors have recently demonstrated strong capability in enhancing the quality of sparse-view 3D reconstruction by augmenting training views at novel viewpoints, but they inevitably introduce hallucinated content ...

## Abstract Cue
- tiple benchmarks on novel view synthesis.
