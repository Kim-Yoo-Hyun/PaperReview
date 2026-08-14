# Method

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, conservative learning, Q-learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/aviralkumar2907/CQL
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of a policy under ...
- The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by also incorporating a ...

## 원리적 동기
- However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning , RL is ...
- If we can instead learn a conservative estimate of the value function, which provides a lower bound on the true values, this overestimation problem could be addressed.
- We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.

## 핵심 방법론
- We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by also incorporating a ...
- Our primary contribution is an algorithmic framework, which we call conservative Q-learning (CQL), for learning conservative, lower-bound estimates of the value function, by regularizing the Q-values during training.
- However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning , RL is ...
