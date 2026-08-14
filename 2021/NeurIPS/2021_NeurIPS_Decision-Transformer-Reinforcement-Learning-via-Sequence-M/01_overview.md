# Decision Transformer: Reinforcement Learning via Sequence Modeling

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Reinforcement Learning, Transformer, policy
- Paper link: ./2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/paper.pdf
- Code/Project: https://github.com/kzl/decision-transformer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.

## Core Idea
- 3 Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- In this work, we use the GPT architecture , which modifies the transformer architecture with a causal selfattention mask to enable autoregressive generation, replacing the summation/softmax over the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- By conditioning an autoregressive model on the desired return (reward), past states, and actions, our Decision Transformer model can generate future actions that achieve the desired return.
- Despite its simplicity, Decision Transformer matches or exceeds the performance of state-of-the-art model-free offline RL baselines on Atari, OpenAI Gym, and Key-to-Door tasks. a a linear decoder ... ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.
- Despite its simplicity, Decision Transformer matches or exceeds the performance of state-of-the-art model-free offline RL baselines on Atari, OpenAI Gym, and Key-to-Door tasks. a a linear decoder ... ...
- Tokens are fed into a GPT architecture which predicts actions autoregressively using a causal self-attention mask.

## Abstract Cue
- We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
