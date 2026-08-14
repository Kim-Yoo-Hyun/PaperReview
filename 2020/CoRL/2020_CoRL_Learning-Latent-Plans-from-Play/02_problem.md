# Problem

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, learning from play, latent plans
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://learning-from-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Expert demonstrations, on the other hand, can be arbitrarily complex but are expensive to collect, and still typically form narrow training distributions over visited states, leading to an ...
- This remains a challenging open problem in robotics.
- Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised collection () that ...

## 해결하려는 문제
- We find that this combination generalizes well empirically—after self-supervising on unlabeled play, our method substantially outperforms individual expert-trained policies on 18 difficult user-specified visual manipulation tasks in a ...
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...
- In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.

## 선행 연구 / 배경 단서
- Expert demonstrations, on the other hand, can be arbitrarily complex but are expensive to collect, and still typically form narrow training distributions over visited states, leading to an ...
- This remains a challenging open problem in robotics.
- Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised collection () that ...
