# Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts

- Year/Venue: 2024 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Diffusion, VLA, Planning
- Paper link: ./2024/CVPR/2024_CVPR_Generate-Subgoal-Images-before-Act-Unlocking-the-Chain-of/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Moreover, for long-horizon manipulation tasks, the deviation from general instruction tends to accumulate if lack of intermediate guidance from high-level subgoals.

## Core Idea
- Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model as a high-level ...
- Additionally, we propose bi-directional generation and frame concat mechanism to further enhance the fidelity of generated subgoal images and the accuracy of instruction following.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- CoTDiffusion achieves outstanding performance gain compared to the baselines without explicit subgoal generation, which proves that a subgoal image is worth a thousand words of instruction.
- The experiments cover various robotics manipulation scenarios including visual reasoning, visual rearrange, and visual constraints.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model as a high-level ...
- CoTDiffusion achieves outstanding performance gain compared to the baselines without explicit subgoal generation, which proves that a subgoal image is worth a thousand words of instruction.
- Additionally, we propose bi-directional generation and frame concat mechanism to further enhance the fidelity of generated subgoal images and the accuracy of instruction following.

## Abstract Cue
- Robotics agents often struggle to understand and follow the multi-modal prompts in complex manipulation scenes which are challenging to be sufficiently and accurately described by text alone.
