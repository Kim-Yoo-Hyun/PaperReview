# Method

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, model-based RL, distribution shift
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/tianheyu927/mopo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- Hence, the central question that this work is trying to answer is: can we develop an offline RL algorithm that generalizes beyond the state and action support of ...
- Based on our analysis, we develop a practical method that estimates model error using the predicted variance of a learned model, uses this uncertainty estimate as a reward ...

## 원리적 동기
- Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving and healthcare , because they rely on costly online trial-and-error.
- First, modelbased RL algorithms effectively receive more supervision, since the model is trained on every transition, even in sparse-reward settings.
- Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.

## 핵심 방법론
- Hence, the central question that this work is trying to answer is: can we develop an offline RL algorithm that generalizes beyond the state and action support of ...
- Based on our analysis, we develop a practical method that estimates model error using the predicted variance of a learned model, uses this uncertainty estimate as a reward ...
- Offline RL methods propose to mitigate bootstrapped error by constraining the learned policy to the behavior policy induced by the dataset .
- Hence, designing RL algorithms that can learn from those diverse, static datasets would both enable more practical RL training in the real world and lead to more effective ...
