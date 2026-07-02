# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BeliefMapNav-3D-Voxel-Based-Belief-Map-for-Zero-Shot-Objec/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target’s prior presence distribution within a voxelized 3D space.
- Building on this 3D voxel map, we introduce BeliefMapNav, an efficient navigation system with two key advantages: i) grounding LLM semantic reasoning within the 3D hierarchical semantics voxel ...
- The source code is publicly available at: https://github.com/ZiboKNOW/BeliefMapNav In this section, we first define the object navigation task and then present the BeliefMapNav system, which consists of three ...

## 원리적 동기
- Together, in existing works, the lack of semantic cues and spatial reasoning leads to inaccurate and imprecise target object position estimation.
- However, both LLMs and VLMs face limitations in spatial understanding and reasoning , which significantly affect target location prediction accuracy.
- To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target’s prior presence distribution within a voxelized 3D space.

## 핵심 방법론
- In this section, we first define the object navigation task and then present the BeliefMapNav system, which consists of three main modules: 3D voxel-based belief mapping, frontier observation ...
- 3.1 Task definition We define the ZSON task, where an agent is required to locate a specified target object in an unknown environment without task-specific training, pre-built maps, ...
