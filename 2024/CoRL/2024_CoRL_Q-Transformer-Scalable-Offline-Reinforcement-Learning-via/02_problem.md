# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, Transformer, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://qtransformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Since Transformers model discrete token sequences, we convert the Q-function estimation problem into a discrete token sequence modeling problem, and devise a suitable loss function for each token ...
- While in principle simply replacing existing architectures (e.g., ResNets or smaller convolutional neural networks ) with a Transformer is conceptually straightforward, devising a methodology that effectively makes use ...
- While prior works used simulation to create such datasets , the most representative data comes from the real world .

## 해결하려는 문제
- We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a ...
- : In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected ...
- Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups.

## 선행 연구 / 배경 단서
- Since Transformers model discrete token sequences, we convert the Q-function estimation problem into a discrete token sequence modeling problem, and devise a suitable loss function for each token ...
- While in principle simply replacing existing architectures (e.g., ResNets or smaller convolutional neural networks ) with a Transformer is conceptually straightforward, devising a methodology that effectively makes use ...
- Autonomous data Human demonstrations Mixed quality data Autoregressive Q-learning Conservative regularization Monte-Carlo returns … Q-Transformer environment step … action dimension Q-values per action dimension Figure 1: Q-Transformer enables ...
