# Problem

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, 3D Vision, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations .
- Yet, robotic manipulation requires intricate environmental interactions, and such methods often lack a broader understanding of the robot’s action with its surroundings in terms of spatial and temporal.
- The constraints construct dynamic affordance conditions from sequential keypoints, explicitly encoding “where” and “when” the robot should interact with the environment.

## 해결하려는 문제
- Experiments in simulation and real world demonstrate that 3DS-VLA outperforms previous state-of-the-art policies and showcase its generalizable capabilities across multi-task, multi-embodiment, and diverse environmental settings.
- To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.
- Specifically, we enable the 2D vision encoder of the VLMs to encode both 2D images and 3D spatial observation by introducing a 2D-to-3D positional alignment mechanism.

## 선행 연구 / 배경 단서
- All these limitations lead us to consider: “How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?” To address the above challenges, as shown ...
- Additionally, to improve the understanding of the relationship between the environment and robot action, we introduce 3D spatial constraints, represented as sequential 3D keypoints in Cartesian coordinates.
- However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations .
