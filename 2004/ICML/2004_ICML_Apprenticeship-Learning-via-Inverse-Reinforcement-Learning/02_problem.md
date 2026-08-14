# Problem

- Year/Venue: 2004 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Imitation Learning, inverse reinforcement learning, apprenticeship learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ai.stanford.edu/~pabbeel/irl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Introduction Given a sequential decision making problem posed in the Markov decision process (MDP) formalism, a number of standard algorithms exist for finding an optimal or near-optimal policy.
- The MDP formalism is useful for many problems because it is often easier to specify the reward function than to directly specify the value function (and/or optimal policy).
- However, we believe that even the reward function is frequently difficult to specify manually.

## 해결하려는 문제
- We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an algorithm for learning ...
- We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert’s reward function, the policy output by ...
- Introduction Given a sequential decision making problem posed in the Markov decision process (MDP) formalism, a number of standard algorithms exist for finding an optimal or near-optimal policy.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
