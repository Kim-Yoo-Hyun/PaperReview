# Problem

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, simulation, robustness
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- A prevalent limitation in many approaches is the lack of adaptation and learning once the policy is deployed on the real system .
- However, developing reliable and generalizable world models poses unique challenges due to the complexity of real-world dynamics, including nonlinearities, stochasticity, and partial observability .
- This work advances model-based reinforcement learning by addressing the challenges of long-horizon prediction, error accumulation, and sim-to-real transfer.

## 해결하려는 문제
- The proposed method employs a dual-autoregressive mechanism and self-supervised training to achieve reliable long-horizon predictions without relying on domain-specific inductive biases, ensuring adaptability across diverse robotic tasks.
- In this work, we introduce a novel framework for learning world models that accurately capture complex, partially observable, and stochastic dynamics.
- We further propose a policy optimization framework that leverages world models for efficient training in imagined environments and seamless deployment in real-world systems.

## 선행 연구 / 배경 단서
- Comparative experiments with existing world model frameworks demonstrate the effectiveness of our approach. (iii) We propose an efficient policy optimization framework that leverages the learned world models for ...
- A prevalent limitation in many approaches is the lack of adaptation and learning once the policy is deployed on the real system .
- Our contributions are summarized as follows: (i) We introduce a novel network architecture and training framework that enables the learning of reliable world models capable of long autoregressive ...
