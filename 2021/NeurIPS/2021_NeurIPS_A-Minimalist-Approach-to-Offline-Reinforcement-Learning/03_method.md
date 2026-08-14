# Method

- Year/Venue: 2021 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, behavior cloning, continuous control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/sfujim/TD3_BC
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the ...

## 원리적 동기
- The solution class for this problem revolves around the idea that the learned policy should be kept close to the data-generating process (or behavior policy), and has been ...
- In other cases, there are unmentioned hyperparameters, or secondary components, such as generative models, which make offline RL algorithms difficult to reproduce, and even more challenging to tune.
- Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the ...

## 핵심 방법론
- Traditionally, reinforcement learning (RL) is thought of as a paradigm for online learning, where the interaction between the RL agent and its environment is of fundamental concern for ...
- In offline RL (historically known as batch RL), the agent learns from a fixed-sized dataset, collected by some arbitrary and possibly unknown process [Lange et al., 2012].
- Eliminating the need to interact with the environment is noteworthy as data collection can often be expensive, risky, or otherwise challenging, particularly in real-world applications.
- Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained ...
- Unfortunately, the main benefit of offline RL, the lack of environment interaction, is also what makes it a challenging task.
