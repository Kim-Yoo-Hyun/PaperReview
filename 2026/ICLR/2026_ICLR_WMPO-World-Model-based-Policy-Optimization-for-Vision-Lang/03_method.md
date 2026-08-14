# Method

- Year/Venue: 2026 / ICLR Poster
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, model predictive control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://wm-po.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.

## 원리적 동기
- The first leverages human intervention to guide learning [7–9], which reduces exploration cost but is labor-intensive and hard to scale.
- Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections.
- We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.

## 핵심 방법론
- Coffee StackThree ThreePieceAssembly Square Mean (%) – Base policy 43.8 46.9 19.5 24.2 33.6 128 GRPO DPO Ours 38.3 43.8 52.3 53.9 17.2 23.4 25.0 28.1 33.2 37.3 ...
