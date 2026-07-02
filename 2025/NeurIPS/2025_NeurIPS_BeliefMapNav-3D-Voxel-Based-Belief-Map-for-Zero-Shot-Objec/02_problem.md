# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BeliefMapNav-3D-Voxel-Based-Belief-Map-for-Zero-Shot-Objec/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Together, in existing works, the lack of semantic cues and spatial reasoning leads to inaccurate and imprecise target object position estimation.
- However, both LLMs and VLMs face limitations in spatial understanding and reasoning , which significantly affect target location prediction accuracy.
- Furthermore, existing methods generally rely on greedy navigation strategies , which cause frequent backand-forth movements, significantly hindering search efficiency.

## 해결하려는 문제
- Experiments on HM3D and HSSD benchmarks show that BeliefMapNav achieves state-of-the-art (SOTA) Success Rate (SR) and Success weighted by Path Length (SPL), with a notable 9.7 SPL improvement ...
- To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target’s prior presence distribution within a voxelized 3D space.
- Building on this 3D voxel map, we introduce BeliefMapNav, an efficient navigation system with two key advantages: i) grounding LLM semantic reasoning within the 3D hierarchical semantics voxel ...

## 선행 연구 / 배경 단서
- Together, in existing works, the lack of semantic cues and spatial reasoning leads to inaccurate and imprecise target object position estimation.
- However, both LLMs and VLMs face limitations in spatial understanding and reasoning , which significantly affect target location prediction accuracy.
- Furthermore, existing methods generally rely on greedy navigation strategies , which cause frequent backand-forth movements, significantly hindering search efficiency.
