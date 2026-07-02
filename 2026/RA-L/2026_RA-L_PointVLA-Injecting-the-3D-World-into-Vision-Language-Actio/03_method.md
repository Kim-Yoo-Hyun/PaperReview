# Method

- Year/Venue: 2026 / RA-L
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, 3D Vision, Reinforcement Learning
- Paper link: ./2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.
- We compare our method against Diffusion Policy and 3D Diffusion Policy (DP3) .
- To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.

## 원리적 동기
- Retraining these models with 3D data is computationally prohibitive, while discarding existing 2D datasets wastes valuable resources.
- Therefore, it is essential to explore novel frameworks that can integrate additional 3D input into pre-existing foundation robot models, a research area that has not been underexplored in ...
- To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.

## 핵심 방법론
- We compare our method against Diffusion Policy and 3D Diffusion Policy (DP3) .
- To address this, we introduced PointVLA, a framework that enhances pre-trained VLAs with 3D point cloud inputs while preserving their 2D representations.
- By integrating a modular 3D feature injector and leveraging skip block analysis, our method incorporates spatial information efficiently without full retrain8 Task Number of Demonstrations 20 50 Block ...
- This key advantage highlights the strength of our approach, demonstrating the superiority of 3D-aware models in mitigating object hallucination.
- In contrast, our approach highlights the necessity of conditionally integrating 3D point cloud data into the model, which significantly enhances performance compared to models that rely solely on ...
