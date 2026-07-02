# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BridgeVLA-Input-Output-Alignment-for-Efficient-3D-Manipula/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Another significant challenge in developing 3D VLA models lies in the misalignment between the 3D inputs used in action fine-tuning and the 2D image inputs used in original ...
- To tackle the challenges mentioned above, as inllustrated in Fig.
- This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [39, 25, 13–15] that align the observation input and action output into ...

## Core Idea
- In this paper, we introduce a new paradigm for constructing 3D VLAs.
- Even when the data are increased to 50 trajectories per task, its success rate is still much lower than BridgeVLA, which indicates only adding 3D information is not ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- BridgeVLA outperforms state-of-the-art baselines across three simulation benchmarks.
- BridgeVLA outperforms all existing state-of-the-art 3D manipulation methods on both benchmarks, addressing Q3 and Q4.
- We compare BridgeVLA with multiple baselines. (1) Image-BC (CNN) and Image-BC (ViT) are two 2D baseline methods which predict the actions directly from 2D images using CNN and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- BridgeVLA outperforms state-of-the-art baselines across three simulation benchmarks.
- In real-robot experiments, BridgeVLA outperforms a stateof-the-art baseline method by 32% on average.
- In this paper, we introduce a new paradigm for constructing 3D VLAs.

## Abstract Cue
- Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning.
