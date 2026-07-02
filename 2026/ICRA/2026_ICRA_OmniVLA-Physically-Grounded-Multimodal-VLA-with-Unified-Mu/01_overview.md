# OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics
- Paper link: ./2026/ICRA/2026_ICRA_OmniVLA-Physically-Grounded-Multimodal-VLA-with-Unified-Mu/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, most existing models rely solely on RGB cameras, limiting their perception and, consequently, manipulation capabilities.

## Core Idea
- We present OmniVLA, an omni-modality VLA model that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation.
- The core of our approach is the sensormasked image, a unified representation that overlays physically meaningful, spatially grounded masks onto the RGB images.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- OmniVLA achieves an average task success rate of 84%, significantly outperforms both RGB-only and rawsensor-input baseline models by 59% and 28% respectively, meanwhile showing higher learning efficiency and ...
- We evaluate OmniVLA on challenging real-world tasks that require sensor-modality perception to guide the manipulation.
- — Vision-language-action (VLA) models have shown strong generalization in robotic manipulation through largescale vision-language pretraining.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- OmniVLA achieves an average task success rate of 84%, significantly outperforms both RGB-only and rawsensor-input baseline models by 59% and 28% respectively, meanwhile showing higher learning efficiency and ...
- — Vision-language-action (VLA) models have shown strong generalization in robotic manipulation through largescale vision-language pretraining.
- They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability.

## Abstract Cue
- — Vision-language-action (VLA) models have shown strong generalization in robotic manipulation through largescale vision-language pretraining.
