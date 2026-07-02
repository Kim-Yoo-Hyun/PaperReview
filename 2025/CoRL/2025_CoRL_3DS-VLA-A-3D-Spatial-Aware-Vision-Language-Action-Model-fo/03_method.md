# Method

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, 3D Vision, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1 , . . . , τN } of N expert demonstrations, each demonstration τ is paired ...
- To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.
- Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D and 3D tokens.

## 원리적 동기
- However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations .
- Yet, robotic manipulation requires intricate environmental interactions, and such methods often lack a broader understanding of the robot’s action with its surroundings in terms of spatial and temporal.
- 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1 , . . . , τN } of N expert demonstrations, each demonstration τ is paired ...

## 핵심 방법론
- 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1 , . . . , τN } of N expert demonstrations, each demonstration τ is paired ...
- Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D and 3D tokens.
- After generating 3D keypoints, instead of directly using them as task goals , we propose a text-based formulation to integrate these constraints into the VLA model as input ...
- To avoid introducing computational overhead, we introduce a non-parametric 3D tokenizer to transform the low-dimensional point cloud into high-dimensional 3D tokens.
- To model spatial constraints, we use task-specific 3D keypoints corresponding to scene entities.
