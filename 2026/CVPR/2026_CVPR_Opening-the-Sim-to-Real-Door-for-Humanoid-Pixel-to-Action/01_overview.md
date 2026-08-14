# Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

- Year/Venue: 2026 / CVPR
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, pixel-to-action, visual sim-to-real, articulated object manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Building on these advances, we develop a teacher–student–bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.

## Core Idea
- Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop consistency in sim-to-real ...
- Building on these advances, we develop a teacher–student–bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Trained entirely on synthetic simulation data, the resulting policy achieves robust zero-shot 1.
- performance across diverse articulated objects—including multiple door types—and outperforms human teleoperators by up to 31.7% in task completion time under the same whole-body control stack.
- Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop consistency in sim-to-real ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop consistency in sim-to-real ...
- Building on these advances, we develop a teacher–student–bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.
- Trained entirely on synthetic simulation data, the resulting policy achieves robust zero-shot 1.

## Abstract Cue
- performance across diverse articulated objects—including multiple door types—and outperforms human teleoperators by up to 31.7% in task completion time under the same whole-body control stack.
