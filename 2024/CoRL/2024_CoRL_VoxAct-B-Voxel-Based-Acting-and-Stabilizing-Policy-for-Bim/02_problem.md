# Problem

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, 3D manipulation, bimanual, Robotics
- Paper link: ./2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/paper.pdf
- Code/Project: https://voxact-b.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This substantially reduces the overall physical dimensions of the areas used to construct a voxel grid, enabling an increase in voxel resolution without incurring computational costs.
- Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various tasks.

## 해결하려는 문제
- In simulation, we show that VoxAct-B outperforms strong baselines on fine-grained bimanual manipulation tasks.
- To this end, we propose VoxAct-B, a language-conditioned, voxel-based method that leverages Vision Language Models (VLMs) to prioritize key regions within the scene and reconstruct a voxel grid.
- Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various tasks.

## 선행 연구 / 배경 단서
- This substantially reduces the overall physical dimensions of the areas used to construct a voxel grid, enabling an increase in voxel resolution without incurring computational costs.
- To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.
- To address this, we propose utilizing VLMs to focus on the most pertinent regions within the scene by cropping out less relevant regions.
