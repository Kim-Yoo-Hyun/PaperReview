# Method

- Year/Venue: 2017 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, meta-learning, visual manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://arxiv.org/abs/1703.07326
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Our proposed architecture consists of three modules: the demonstration network, the context network, and the manipulation network.
- In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.

## 원리적 동기
- To accomplish this, we must solve two broad problems.
- For example, when it is conditioned on a single demonstration for task F, it should behave like a good policy for task F. (c) We can phrase this ...
- Our proposed architecture consists of three modules: the demonstration network, the context network, and the manipulation network.

## 핵심 방법론
- Our proposed architecture consists of three modules: the demonstration network, the context network, and the manipulation network.
- While, in principle, a generic neural network could learn the mapping from demonstration and current observation to appropriate action, we found it important to use an appropriate architecture.
- Our architecture for learning block stacking is one of the main contributions of this paper, and we believe it is representative of what architectures for one-shot imitation learning ...
- Hence, we randomly discard a subset of time steps during training, an operation we call temporal dropout, analogous to .
- An illustration of the architecture is shown in Fig.
