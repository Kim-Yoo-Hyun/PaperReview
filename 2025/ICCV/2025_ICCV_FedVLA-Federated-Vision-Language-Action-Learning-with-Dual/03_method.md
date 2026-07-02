# Method

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/ICCV/2025_ICCV_FedVLA-Federated-Vision-Language-Action-Learning-with-Dual/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this, we propose FedVLA, the first federated VLA learning framework, enabling distributed model training that preserves data privacy without compromising performance.
- Finally, we propose an Expert-Driven Aggregation strategy at the federated server, where model aggregation is guided by activated experts, ensuring effective cross-client knowledge transfer.
- To simulate real-world variations, we introduce moderate randomness in object placement and lighting conditions to better reflect practical deployment scenarios.

## 원리적 동기
- Server Server Expert-Driven Aggregation VLA Model Vision-language-action (VLA) models have significantly advanced robotic manipulation by enabling robots to interpret language instructions for task execution.
- However, training these models often relies on large-scale user-specific data, raising concerns about privacy and security, which in turn limits their broader adoption.
- To address this, we propose FedVLA, the first federated VLA learning framework, enabling distributed model training that preserves data privacy without compromising performance.

## 핵심 방법론
- To simulate real-world variations, we introduce moderate randomness in object placement and lighting conditions to better reflect practical deployment scenarios.
- We employ the pretrained HPT as the backbone of our VLA model and train it for 1,000 communication rounds between clients and the server, with each client performing ...
- The centralized training (Centralized) aggregates all data on a single server for joint training, serving as an upper bound in performance.
- Notably, in the Close Drawer task, FedVLA surpasses centralized training by a success rate margin of about 7.0%.
