# Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Illustration of the Out-of-Vision (OOV) limitation in existing VLA models.
- SOMA addresses this limitation by equipping VLAs with a persistent, spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visual ...
- Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera’s field of view.

## Core Idea
- Head Camera We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
- The framework consists of three components: Spatial Memory Construction for aggregating angular-wise observations into a unified spatial–semantic representation by scanning, Dynamic Memory Refinement for maintaining global consistency over ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiment results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot ...
- Additional experiments on RoboCasa GR1 and SimplerEnv further validate the effectiveness of SOMA’s memory design under conventional fully observable settings.
- We evaluate SOMA on five self-designed challenging real-world OOV manipulation tasks, including multi-step and dualarm scenarios, where target objects are initially invisible.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiment results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot ...
- Head Camera We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
- The framework consists of three components: Spatial Memory Construction for aggregating angular-wise observations into a unified spatial–semantic representation by scanning, Dynamic Memory Refinement for maintaining global consistency over ...

## Abstract Cue
- Head Camera We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
