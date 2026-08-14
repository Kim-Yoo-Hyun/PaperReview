# Method

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, simulation, robustness
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Building on RWM, we propose MBPO-PPO, a policy optimization framework that leverages long world model rollout fidelity.
- 9 6 Conclusion In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.
- In this work, we introduce a novel framework for learning world models that accurately capture complex, partially observable, and stochastic dynamics.

## 원리적 동기
- A prevalent limitation in many approaches is the lack of adaptation and learning once the policy is deployed on the real system .
- However, developing reliable and generalizable world models poses unique challenges due to the complexity of real-world dynamics, including nonlinearities, stochasticity, and partial observability .
- Building on RWM, we propose MBPO-PPO, a policy optimization framework that leverages long world model rollout fidelity.

## 핵심 방법론
- Building on RWM, we propose MBPO-PPO, a policy optimization framework that leverages long world model rollout fidelity.
- 9 6 Conclusion In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.
- Through extensive experiments, we demonstrate that RWM consistently outperforms state-of-the-art approaches like RSSM and transformer-based architectures in autoregressive prediction accuracy across diverse robotic environments.
- However, training from scratch remains challenging as policies can exploit model inaccuracies during exploration, leading to inefficiency and instability.
- Current training in simulation avoids potential hardware damage, but incorporating safety constraints and robust uncertainty estimates will be critical for deploying RWM and MBPO-PPO in real-world, lifelong learning ...
