# Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, Transformer, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://qtransformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Since Transformers model discrete token sequences, we convert the Q-function estimation problem into a discrete token sequence modeling problem, and devise a suitable loss function for each token ...
- While in principle simply replacing existing architectures (e.g., ResNets or smaller convolutional neural networks ) with a Transformer is conceptually straightforward, devising a methodology that effectively makes use ...
- While prior works used simulation to create such datasets , the most representative data comes from the real world .

## Core Idea
- We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn from both narrow ...
- We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a ...
- The project’s website and videos can be found at qtransformer.github.io In our experiments, we aim to answer the following questions: (1) Can Q-Transformer learn from a combination of ...
- The offline data used in our experiments was collected with a fleet of 13 robots, and consists of a subset of the demonstration data described by Brohan et ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a ...
- : In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected ...
- Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups.

## Abstract Cue
- : In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data.
