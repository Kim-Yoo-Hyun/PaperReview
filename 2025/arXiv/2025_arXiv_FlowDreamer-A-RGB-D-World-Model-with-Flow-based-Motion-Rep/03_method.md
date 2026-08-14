# Method

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, RGB-D, 3D scene flow, robot manipulation, 4D reasoning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- As opposed to canonical approaches that handle dynamics prediction mostly implicitly and reconcile it with visual rendering in a single model, we introduce FlowDreamer, which adopts 3D scene ...
- For the Language Table environment, we use the official simulation environment.
- For RT-1 environment, we use SimplerEnv as the simulator.

## 원리적 동기
- Existing visual world models have undergone rapid development in recent years.
- As opposed to canonical approaches that handle dynamics prediction mostly implicitly and reconcile it with visual rendering in a single model, we introduce FlowDreamer, which adopts 3D scene ...

## 핵심 방법론
- For the Language Table environment, we use the official simulation environment.
- For RT-1 environment, we use SimplerEnv as the simulator.
- As the real-world data do not contain the depth information, we collect training and inference trajectories from the simulator.
- This indicates that end-to-end training is generally a better approach, while the contribution is less than that of other components.
- Collected trajectories are split into training, validation, and test sets without overlap.
