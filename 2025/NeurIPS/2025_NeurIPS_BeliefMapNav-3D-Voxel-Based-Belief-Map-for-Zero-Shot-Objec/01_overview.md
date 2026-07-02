# BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BeliefMapNav-3D-Voxel-Based-Belief-Map-for-Zero-Shot-Objec/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Together, in existing works, the lack of semantic cues and spatial reasoning leads to inaccurate and imprecise target object position estimation.
- However, both LLMs and VLMs face limitations in spatial understanding and reasoning , which significantly affect target location prediction accuracy.
- Furthermore, existing methods generally rely on greedy navigation strategies , which cause frequent backand-forth movements, significantly hindering search efficiency.

## Core Idea
- To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target’s prior presence distribution within a voxelized 3D space.
- Building on this 3D voxel map, we introduce BeliefMapNav, an efficient navigation system with two key advantages: i) grounding LLM semantic reasoning within the 3D hierarchical semantics voxel ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on HM3D and HSSD benchmarks show that BeliefMapNav achieves state-of-the-art (SOTA) Success Rate (SR) and Success weighted by Path Length (SPL), with a notable 9.7 SPL improvement ...
- We conduct experiments on its validation set, consisting of 11 environments, 21 object categories, and 2,195 object-goal navigation episodes.
- 4.1 Benchmarks and Implementation details Dataset: We evaluate our method on three standard benchmarks: HM3D , MP3D and HSSD .

## Limitation
- This high-resolution 3D map can be further extended to enable robot interaction for mobile manipulation tasks, with future work focusing on real-world implementation.

## Contribution
- Experiments on HM3D and HSSD benchmarks show that BeliefMapNav achieves state-of-the-art (SOTA) Success Rate (SR) and Success weighted by Path Length (SPL), with a notable 9.7 SPL improvement ...
- To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target’s prior presence distribution within a voxelized 3D space.
- Building on this 3D voxel map, we introduce BeliefMapNav, an efficient navigation system with two key advantages: i) grounding LLM semantic reasoning within the 3D hierarchical semantics voxel ...

## Abstract Cue
- Zero-shot object navigation (ZSON) allows robots to find target objects in unfamiliar environments using natural language instructions, without relying on pre-built maps or task-specific training.
