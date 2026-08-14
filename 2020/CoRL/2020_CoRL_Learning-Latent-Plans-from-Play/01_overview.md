# Learning Latent Plans from Play

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, learning from play, latent plans
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://learning-from-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Expert demonstrations, on the other hand, can be arbitrarily complex but are expensive to collect, and still typically form narrow training distributions over visited states, leading to an ...
- This remains a challenging open problem in robotics.
- Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised collection () that ...

## Core Idea
- In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The motivation of the state experiments is to understand the how all methods compare on the control problem independent of visual representation learning, which could potentially be improved ...
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...
- We find that this combination generalizes well empirically—after self-supervising on unlabeled play, our method substantially outperforms individual expert-trained policies on 18 difficult user-specified visual manipulation tasks in a ...

## Limitation
- Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring the effects of imbalance in play data distributions as discussed ...

## Contribution
- We find that this combination generalizes well empirically—after self-supervising on unlabeled play, our method substantially outperforms individual expert-trained policies on 18 difficult user-specified visual manipulation tasks in a ...
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...
- In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.

## Abstract Cue
- : Acquiring a diverse repertoire of general-purpose skills remains an open challenge for robotics.
