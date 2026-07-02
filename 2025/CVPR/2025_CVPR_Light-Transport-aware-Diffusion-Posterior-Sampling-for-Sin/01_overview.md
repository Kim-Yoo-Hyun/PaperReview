# Light Transport-aware Diffusion Posterior Sampling for Single-View Reconstruction of 3D Volumes

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_Light-Transport-aware-Diffusion-Posterior-Sampling-for-Sin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, this problem is ill-posed and, in general, requires additional views to constrain the object parameters and infer plausible reconstructions of unseen parts.
- In such scenarios, the problem becomes so ill-posed that it requires dozens, if not hundreds, of different views to adequately constrain the object parameters .
- The challenge increases significantly when these parameters describe complex distributions of volumetric materials, such as clouds, smoke, or fire.

## Core Idea
- We introduce a single-view reconstruction technique of volumetric fields in which multiple light scattering effects are omnipresent, such as in clouds.
- The neural diffusion model is trained on the latent codes of a novel, diffusion-friendly, monoplanar representation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through various experiments, we demonstrate single-view reconstruction of volumetric clouds at a previously unattainable quality.
- We model the unknown distribution of volumetric fields using an unconditional diffusion model trained on a novel benchmark dataset comprising 1,000 synthetically simulated volumetric density fields.

## Limitation
- Test View A notable limitation is the ambiguity between what is represented by θ and ϕ.
- Further limitations arise from the use of a pre-trained diffusion model which, even for clouds alone, requires days to compute the latent encoding.

## Contribution
- We model the unknown distribution of volumetric fields using an unconditional diffusion model trained on a novel benchmark dataset comprising 1,000 synthetically simulated volumetric density fields.
- Through various experiments, we demonstrate single-view reconstruction of volumetric clouds at a previously unattainable quality.
- We introduce a single-view reconstruction technique of volumetric fields in which multiple light scattering effects are omnipresent, such as in clouds.

## Abstract Cue
- We introduce a single-view reconstruction technique of volumetric fields in which multiple light scattering effects are omnipresent, such as in clouds.
