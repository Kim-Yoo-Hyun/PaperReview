# Method

- Year/Venue: 2024 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: 3D representation, Robotics, pretraining
- Paper link: ./2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes.
- To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through 3D point clouds.
- As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of the pre-trained image ...

## 원리적 동기
- To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through 3D point clouds.
- We underscore the importance of cluttered scenes in 3D representation learning, and automatically construct a multi-object dataset benefiting from cost-free supervision in simulation.
- We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes.

## 핵심 방법론
- As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of the pre-trained image ...
- We use Top1 classification accuracy as the main evaluation metric, and also report Top3 and Top5 for the Objaverse dataset to compare with previous work.
