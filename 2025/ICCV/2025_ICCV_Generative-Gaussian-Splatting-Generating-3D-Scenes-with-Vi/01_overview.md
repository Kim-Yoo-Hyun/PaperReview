# Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Generative-Gaussian-Splatting-Generating-3D-Scenes-with-Vi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Synthesizing consistent and photorealistic 3D scenes is an open problem in computer vision.
- Video diffusion models generate impressive videos but cannot directly synthesize 3D representations, i.e., lack 3D consistency in the generated sequences.
- In addition, directly training generative 3D models is challenging due to a lack of 3D training data at scale.

## Core Idea
- In this work, we present Generative Gaussian Splatting (GGS) – a novel approach that integrates a 3D representation with a pre-trained latent video diffusion model.
- However, these works cannot leverage pre-trained video diffusion models, because of their custom network architectures for incorporating the 3D representation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our approach on two common benchmark datasets for scene synthesis, RealEstate10K and ScanNet++, and find that our proposed GGS model significantly improves both the 3D consistency ...
- In this work, we investigate how 3D representations can be directly integrated with powerful video diffusion priors to improve the consistency of the generated images and thereby the ...
- One challenge is that state-of-the-art diffusion models

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we present Generative Gaussian Splatting (GGS) – a novel approach that integrates a 3D representation with a pre-trained latent video diffusion model.
- We evaluate our approach on two common benchmark datasets for scene synthesis, RealEstate10K and ScanNet++, and find that our proposed GGS model significantly improves both the 3D consistency ...
- One challenge is that state-of-the-art diffusion models

## Abstract Cue
- Introduction Synthesizing consistent and photorealistic 3D scenes is an open problem in computer vision.
