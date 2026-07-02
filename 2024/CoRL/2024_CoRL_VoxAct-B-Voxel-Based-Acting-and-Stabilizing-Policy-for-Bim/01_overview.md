# VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, 3D manipulation, bimanual, Robotics
- Paper link: ./2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/paper.pdf
- Code/Project: https://voxact-b.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This substantially reduces the overall physical dimensions of the areas used to construct a voxel grid, enabling an increase in voxel resolution without incurring computational costs.
- Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various tasks.

## Core Idea
- This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa , to use based ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In simulation, we show that VoxAct-B outperforms strong baselines on fine-grained bimanual manipulation tasks.
- For simulation experiments, we build on top of RLBench , a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct.
- We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) to improve performance.

## Limitation
- We hope that this inspires future work in asymmetric bimanual manipulation tasks.

## Contribution
- In simulation, we show that VoxAct-B outperforms strong baselines on fine-grained bimanual manipulation tasks.
- To this end, we propose VoxAct-B, a language-conditioned, voxel-based method that leverages Vision Language Models (VLMs) to prioritize key regions within the scene and reconstruct a voxel grid.
- Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various tasks.

## Abstract Cue
- : Bimanual manipulation is critical to many robotics applications.
