# Method

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, 3D manipulation, bimanual, Robotics
- Paper link: ./2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/paper.pdf
- Code/Project: https://voxact-b.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa , to use based ...
- To this end, we propose VoxAct-B, a language-conditioned, voxel-based method that leverages Vision Language Models (VLMs) to prioritize key regions within the scene and reconstruct a voxel grid.

## 원리적 동기
- This substantially reduces the overall physical dimensions of the areas used to construct a voxel grid, enabling an increase in voxel resolution without incurring computational costs.
- Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various tasks.
- This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.

## 핵심 방법론
- This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa , to use based ...
- In the following, we use similar notation as but index components as belonging to an arm using the superscript: arm ∈ {acting, stabilizing}.
