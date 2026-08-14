# Method

- Year/Venue: 2026 / CVPR
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, perceptive locomotion, LiDAR, 3D navigation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://gallantloco.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce Gallant, a voxel-grid–based perceptive learning framework for humanoid locomotion and local navigation in 3D constrained environments.
- This requires a perception architecture that enables anticipatory collision checking, clearance-aware motion generation, and planning of contact-rich maneuvers.
- The training environment is divided into 8\,\mathrm {m} \times 8\,\mathrm {m} blocks.

## 원리적 동기
- However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture the full 3D ...
- While recent systems have progressed from lab prototypes to real-world deployment , ensuring operational safety remains a key challenge.
- We introduce Gallant, a voxel-grid–based perceptive learning framework for humanoid locomotion and local navigation in 3D constrained environments.

## 핵심 방법론
- We introduce Gallant, a voxel-grid–based perceptive learning framework for humanoid locomotion and local navigation in 3D constrained environments.
- The training environment is divided into 8\,\mathrm {m} \times 8\,\mathrm {m} blocks.
- Recent work explores end-to-end training by adding obstacle-avoidance rewards to velocity tracking , but this creates conflicting objectives.
- Recent LiDAR simulation advances enable realistic sensing during training.
- Moreover, the 2D structure enables efficient parallel training and supports real-time inference on onboard compute.
