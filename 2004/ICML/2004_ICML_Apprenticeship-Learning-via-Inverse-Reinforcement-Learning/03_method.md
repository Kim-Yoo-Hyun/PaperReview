# Method

- Year/Venue: 2004 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Imitation Learning, inverse reinforcement learning, apprenticeship learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ai.stanford.edu/~pabbeel/irl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert demonstrating the task ...
- This setting is useful in applications (such as the task of driving) where it may be difficult to write down an explicit reward function specifying exactly how different ...
- We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an algorithm for learning ...

## 원리적 동기
- Introduction Given a sequential decision making problem posed in the Markov decision process (MDP) formalism, a number of standard algorithms exist for finding an optimal or near-optimal policy.
- The MDP formalism is useful for many problems because it is often easier to specify the reward function than to directly specify the value function (and/or optimal policy).
- We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert demonstrating the task ...

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
