# 4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/NeurIPS/2025_NeurIPS_4D-VLA-Spatiotemporal-Vision-Language-Action-Pretraining-w/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing pretraining paradigms t often suffer from incomplete or under-informative input, lacking critical contextual cues required for reliable action reasoning.
- However, efficiently extracting useful information from these datasets remains a challenge for improving generalization across diverse scenarios.
- This includes symmetric trajectories—where it is difficult to infer the direction of motion—as well as cases where visually similar observations correspond to entirely different actions.

## Core Idea
- Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B , which consists of a text tokenizer T , a vision encoder ...
- To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. † Denotes no available standard deviation data.
- Note that ARM4R pretrains with 3D inputs, while our approach differs in supervision and architecture; results and a detailed discussion are provided in Appx.
- In addition, we evaluate on the ARM4R benchmark for a direct comparison with ARM4R.

## Limitation
- A limitation of our approach is its reliance on RGB-D input, which introduces hardware restriction.
- In this paper, we present 4D-VLA, which incorporates 4D information to address challenges in leveraging diverse robotic datasets for pretraining, such as coordinate system chaos and state chaos.

## Contribution
- Leveraging diverse robotic data for pretraining remains a critical challenge.
- To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos.
- This inconsistency significantly hampers pretraining efficiency.

## Abstract Cue
- Leveraging diverse robotic data for pretraining remains a critical challenge.
