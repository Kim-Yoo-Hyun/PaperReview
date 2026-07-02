# Method

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: RL and Imitation Learning
- Tags: Reinforcement Learning, Transformer, policy
- Paper link: ./2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/paper.pdf
- Code/Project: https://github.com/kzl/decision-transformer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- 3 Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- In this work, we use the GPT architecture , which modifies the transformer architecture with a causal selfattention mask to enable autoregressive generation, replacing the summation/softmax over the ...
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.

## 원리적 동기
- We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
- In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.
- 3 Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).

## 핵심 방법론
- 3 Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- In this work, we use the GPT architecture , which modifies the transformer architecture with a causal selfattention mask to enable autoregressive generation, replacing the summation/softmax over the ...
- 3 Method In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm 1.
- Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- We consider the following shift in paradigm: instead of training a policy through conventional RL algorithms like temporal difference (TD) learning , we will train transformer models on ...
