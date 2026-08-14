# Problem

- Year/Venue: 2021 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, behavior cloning, continuous control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/sfujim/TD3_BC
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- The solution class for this problem revolves around the idea that the learned policy should be kept close to the data-generating process (or behavior policy), and has been ...
- In other cases, there are unmentioned hyperparameters, or secondary components, such as generative models, which make offline RL algorithms difficult to reproduce, and even more challenging to tune.
- Additionally, such mixture of details slow down the run times of the algorithms, and make causal attributions of performance gains and transfers of techniques across algorithms difficult, as ...

## 해결하려는 문제
- Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the ...
- We find that we can match the performance of state-of-the-art offline RL algorithms by simply adding a behavior cloning term to the policy update of an online RL ...
- Built on pre-existing RL algorithms, modifications to make an RL algorithm work offline comes at the cost of additional complexity.

## 선행 연구 / 배경 단서
- The solution class for this problem revolves around the idea that the learned policy should be kept close to the data-generating process (or behavior policy), and has been ...
- In other cases, there are unmentioned hyperparameters, or secondary components, such as generative models, which make offline RL algorithms difficult to reproduce, and even more challenging to tune.
- Additionally, such mixture of details slow down the run times of the algorithms, and make causal attributions of performance gains and transfers of techniques across algorithms difficult, as ...
