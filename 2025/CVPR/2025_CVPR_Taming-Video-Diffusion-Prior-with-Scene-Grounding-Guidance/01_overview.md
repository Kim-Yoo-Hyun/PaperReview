# Taming Video Diffusion Prior with Scene-Grounding Guidance for 3D Gaussian Splatting from Sparse Inputs

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_Taming-Video-Diffusion-Prior-with-Scene-Grounding-Guidance/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite recent successes in novel view synthesis using 3D Gaussian Splatting (3DGS), modeling scenes with sparse inputs remains a challenge.
- Despite recent advances in scene representations based on 3DGS, modeling scenes with sparse inputs remains a significant challenge.
- To address the challenge of inconsistencies, we introduce a novel scene-grounding guidance based on rendered sequences from an optimized 3DGS, which tames the diffusion model to generate consistent ...

## Core Idea
- We propose using video diffusion models that provide plausible interpretations for regions that are outside the field of view and occluded.
- To tackle these issues, we propose to use a reconstruction by generation pipeline that leverages learned priors from video diffusion models to provide plausible interpretations for regions outside ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments demonstrate that our method significantly improves upon the baseline and achieves state-ofthe-art performance on challenging benchmarks.
- 3DGS achieves comparable performance to NeRF while requiring significantly less training time and offering higher inference speeds.
- While there have been promising improvements , the commonly used faceforwarding and object-oriented ‘outside-in’ viewing settings oversimplify real-world sparse-input modeling, causi

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments demonstrate that our method significantly improves upon the baseline and achieves state-ofthe-art performance on challenging benchmarks.
- To address the challenge of inconsistencies, we introduce a novel scene-grounding guidance based on rendered sequences from an optimized 3DGS, which tames the diffusion model to generate consistent ...
- To tackle these issues, we propose to use a reconstruction by generation pipeline that leverages learned priors from video diffusion models to provide plausible interpretations for regions outside ...

## Abstract Cue
- holistic scene modeling, we also propose a trajectory initialization method.
