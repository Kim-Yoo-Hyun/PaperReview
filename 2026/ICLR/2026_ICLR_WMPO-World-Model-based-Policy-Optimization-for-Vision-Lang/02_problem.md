# Problem

- Year/Venue: 2026 / ICLR Poster
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, model predictive control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://wm-po.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- The first leverages human intervention to guide learning [7–9], which reduces exploration cost but is labor-intensive and hard to scale.
- Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections.

## 해결하려는 문제
- Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, ...
- We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections.

## 선행 연구 / 배경 단서
- This self-improvement process can lead to policies that are more robust and capable of recovering from failure.
- The first leverages human intervention to guide learning [7–9], which reduces exploration cost but is labor-intensive and hard to scale.
- The dominant approach for training these models is imitation learning (IL) from large-scale human demonstrations .
