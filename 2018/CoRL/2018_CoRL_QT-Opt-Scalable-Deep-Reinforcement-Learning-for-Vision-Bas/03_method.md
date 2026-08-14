# Method

- Year/Venue: 2018 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Q-learning, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test set, while using ...
- Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- To that end, we introduce QT-Opt, a scalable self-supervised vision-based reinforcement learning framework that can leverage over 580k real-world grasp attempts to train a deep neural network Q-function ...

## 원리적 동기
- While grasping restricts the manipulation problem, it still retains many of its largest challenges: a grasping system should be able to pick up previously unseen objects with reliable ...
- To meet the generalization demands of real-world manipulation, we focus specifically on scalable learning with off-policy algorithms, and study this question in the context of the specific problem ...
- The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test set, while using ...

## 핵심 방법론
- The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test set, while using ...
- Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- The success rate of our method in both cases is very high.
- The comparison in Table 1 indicates a very large gap in performance between our method and both variants of the prior approach.
- Since the format of the data for the two methods is different due to the different action representations, we compare to two versions of this prior approach: a ...
