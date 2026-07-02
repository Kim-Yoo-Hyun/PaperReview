# Problem

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: RL and Imitation Learning
- Tags: Reinforcement Learning, Transformer, policy
- Paper link: ./2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/paper.pdf
- Code/Project: https://github.com/kzl/decision-transformer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.

## 해결하려는 문제
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.
- Despite its simplicity, Decision Transformer matches or exceeds the performance of state-of-the-art model-free offline RL baselines on Atari, OpenAI Gym, and Key-to-Door tasks. a a linear decoder ... ...
- Tokens are fed into a GPT architecture which predicts actions autoregressively using a causal self-attention mask.

## 선행 연구 / 배경 단서
- 4 2.2 Transformers . . . . . . . . . . . . . . . . . . . . . . . . . ...
