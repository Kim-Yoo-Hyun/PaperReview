# Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, simulation, robustness
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- A prevalent limitation in many approaches is the lack of adaptation and learning once the policy is deployed on the real system .
- However, developing reliable and generalizable world models poses unique challenges due to the complexity of real-world dynamics, including nonlinearities, stochasticity, and partial observability .
- This work advances model-based reinforcement learning by addressing the challenges of long-horizon prediction, error accumulation, and sim-to-real transfer.

## Core Idea
- Building on RWM, we propose MBPO-PPO, a policy optimization framework that leverages long world model rollout fidelity.
- 9 6 Conclusion In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve optimal performance.
- The results highlight the superiority of RWM trained with autoregressive training (RWM-AR), which consistently achieves the lowest prediction errors across all environments.
- The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across diverse robotic tasks in ...

## Limitation
- Leveraging a dual-autoregressive mechanism, RWM effectively addresses key challenges such as compounding errors, partial observability, and stochastic dynamics.

## Contribution
- The proposed method employs a dual-autoregressive mechanism and self-supervised training to achieve reliable long-horizon predictions without relying on domain-specific inductive biases, ensuring adaptability across diverse robotic tasks.
- In this work, we introduce a novel framework for learning world models that accurately capture complex, partially observable, and stochastic dynamics.
- We further propose a policy optimization framework that leverages world models for efficient training in imagined environments and seamless deployment in real-world systems.

## Abstract Cue
- Learning robust and generalizable world models is crucial for enabling efficient and scalable robotic control in real-world environments.
