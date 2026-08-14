# World Action Models are Zero-shot Policies

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, zero-shot policy, action representation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Introduction Recent robotic foundation models, termed Vision-Language Action models (VLAs), extend pretrained VisionLanguage Models (VLMs) to predict motor actions (Bjorck et al., 2025; Black et al., 2024; Brohan ...
- Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, ...
- However, they fail at a task like “untie the shoelace” if that specific skill was not present in the robot training data.

## Core Idea
- We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- We explore few-shot embodiment adaptation by post-training on 30 minutes of new embodiment play data and evaluating on pick-and-place variants requiring strong language following.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in realrobot experiments.
- Finally, we demonstrate two forms of cross-embodiment transfer: video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just ...
- State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in realrobot experiments.
- We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- Finally, we demonstrate two forms of cross-embodiment transfer: video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just ...

## Abstract Cue
- State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments.
