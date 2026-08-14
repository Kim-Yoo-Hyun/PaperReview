# AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, atomic skills, skill composition, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- These challenges present significant barriers for existing VLA models, which use monolithic action decoders trained on aggregated data, resulting in poor scalability.
- To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.
- However, real-world robotic tasks often involve longhorizon, multi-step problem-solving and require generalization for continual skill acquisition, extending beyond single actions or skills.

## Core Idea
- To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.
- Furthermore, we introduce a flexible routing encoder that automatically assigns dedicated atomic experts to new skills, enabling continual learning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- By unifying task planning and action execution within this framework, it achieves strong performance on long-horizon and continual learning tasks in both simulation and real-world settings. world deployments ...
- In simulation, AtomicVLA outperforms π0 by 2.4% on LIBERO, 10% on LIBERO-LONG, and outperforms π0 and π0.5 by 0.22 and 0.25 in average task length on CALVIN.
- We validate our approach through extensive experiments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Furthermore, we introduce a flexible routing encoder that automatically assigns dedicated atomic experts to new skills, enabling continual learning.
- We validate our approach through extensive experiments.
- To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.

## Abstract Cue
- (1) Previous VLA (2) Our AtomicVLA 100 Text SG-MoE Recent advances in Visual-Language-Action (VLA) models have shown promising potential for robotic manipulation tasks.
