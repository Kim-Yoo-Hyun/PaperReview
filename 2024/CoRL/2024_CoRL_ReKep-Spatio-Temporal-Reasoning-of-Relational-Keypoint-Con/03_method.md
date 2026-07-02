# Method

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Planning, 3D geometry, Robotics, VLM
- Paper link: ./2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/paper.pdf
- Code/Project: https://github.com/huangwl18/ReKep
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and ...
- In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation.

## 원리적 동기
- We study ReKep in the context of the sequential manipulation problem, where each task involves multiple stages that have spatio-temporal dependencies (e.g., “grasping”, “aligning”, and “pouring” in the ...
- Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify ...
- We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and ...

## 핵심 방법론
- Herein we discuss: (1) What are Relational Keypoint Constraints (Sec.
- 3.1)? (2) How to formulate manipulation as a constrained optimization problem with ReKep (Sec.
- 3.2)? (3) What is our algorithmic instantiation that can efficiently solve the optimization in real-time (Sec.
- 3.3)? (4) How to automatically obtain ReKep from RGB-D observations and language instructions (Sec.
- 3.1 Relational Keypoint Constraints (ReKep) Herein we define a single instance of ReKep.
