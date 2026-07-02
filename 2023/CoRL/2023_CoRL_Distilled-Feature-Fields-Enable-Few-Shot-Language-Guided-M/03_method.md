# Method

- Year/Venue: 2023 / CoRL
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, NeRF, Vision-Language, manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/paper.pdf
- Code/Project: https://f3rm.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in shape, appearance, materials, ...
- We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects.
- Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ability to generalize ...

## 원리적 동기
- One challenge that makes distilled feature fields unwieldy for robotics is the long time it takes to model each scene.
- Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features.
- We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in shape, appearance, materials, ...

## 핵심 방법론
- We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in shape, appearance, materials, ...
- Undertaking such tasks in unpredictable environments — where items from a diverse set can deviate markedly from the training data, and can be hidden or jumbled amidst clutter ...
