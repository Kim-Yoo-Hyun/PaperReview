# Hindsight Experience Replay

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1707.01495.
> PDF retrieval source: https://arxiv.org/pdf/1707.01495. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / NeurIPS
- Authors: Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, OpenAI Pieter Abbeel, Wojciech Zaremba
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards
- Official paper: https://arxiv.org/abs/1707.01495
- Full-text retrieval: https://arxiv.org/pdf/1707.01495
- Code/Project: https://github.com/openai/baselines
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

HER는 원래 목표에 실패한 에피소드도 실제로 도달한 상태를 새 목표로 지정해 학습에 재사용한다. [PDF 1쪽](https://arxiv.org/pdf/1707.01495#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Dealing with sparse rewards is one of the biggest challenges in Reinforcement Learning (RL).
- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 1 / Abstract - extractive body cue:** It can be combined with an arbitrary off-policy RL algorithm and may be seen as a form of implicit curriculum.
- **p. 1 / Abstract - extractive body cue:** We demonstrate our approach on the task of manipulating objects with a robotic arm.
- **p. 1 / Abstract - extractive body cue:** In particular, we run experiments on three different tasks: pushing, sliding, and pick-and-place, in each case using only binary rewards indicating whether or not the ...
- **p. 5 / 2 Background - extractive body cue:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly ...
- **p. 1 / 1 Introduction - extractive body cue:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can ...
- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 4 / 2 Background - extractive body cue:** In order to solve this problem we introduce the technique of Hindsight Experience Replay which is the crux of our approach.
- **p. 2 / 2 Background - extractive body cue:** In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments.
- **p. 3 / 2 Background - extractive body cue:** Instead of shaping the reward we propose a different solution which does not require any domain knowledge.
- **p. 4 / 2 Background - extractive body cue:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary ...
- **p. 3 / 2 Background - extractive body cue:** 2.3 Deep Deterministic Policy Gradients (DDPG) Deep Deterministic Policy Gradients (DDPG) (Lillicrap et al., 2015) is a model-free RL algorithm for continuous action spaces.
- **p. 3 / 2 Background - extractive body cue:** In DDPG we maintain two neural networks: a target policy (also called an actor) π : S →A and an action-value function approximator (called the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A deterministic policy is a mapping from states to actions: π : S →A. | state 또는 observation, action, reward와 transition history | p. 2 (2 Background), p. 3 (2 Background) |
| State/latent | deterministic, policy, mapping, states, actions, setup, possible, train, approximator, Q-function, direct, bootstrapping | policy/value state와 action-selection variable | p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction) |
| Output/action | (2015a) show that in this setup it is possible to train an approximator to the Q-function using direct bootstrapping from the Bellman equation (just like in case of DQN) and that a ... | action policy와 induced trajectory | p. 3 (2 Background), p. 2 (1 Introduction), p. 3 (2 Background) |
| Objective/outcome | The network is trained using mini-batch gradient descent on the loss L which encourages the approximated Q-function to satisfy the Bellman equation: L = E (Q(st, at) -yt)2, where yt = rt ... | expected return, task success, stability와 sample efficiency | p. 2 (2 Background), p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- 경험 재생 시 대체 목표에 맞춰 보상을 다시 계산해 오프폴리시 목표 조건부 강화학습과 결합한다. [PDF 3쪽](https://arxiv.org/pdf/1707.01495#page=3) · [PDF 4쪽](https://arxiv.org/pdf/1707.01495#page=4)
- 밀기·미끄러뜨리기·집어 놓기에서 이진 보상만 사용할 때의 학습을 비교하고 시뮬레이션 정책의 실물 전이를 시연했다. [PDF 7쪽](https://arxiv.org/pdf/1707.01495#page=7) · [PDF 8쪽](https://arxiv.org/pdf/1707.01495#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible to the real world. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | In this task a box is placed on a table in front of the robot and the task is to move it to the target location on the table. | role, split, size and leakage | p. 5 (4 Experiments), p. 10 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Metric | 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 timesteps) 0% ... | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | 4.2 we compare the performance of DDPG with and without HER. | fair input/data/compute/action matching | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Experiments - extractive body cue:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it ...
- **p. 10 / 5 Related work - extractive body cue:** It does not have to be robust to noisy observations because it is not used during the deployment on the physical robot.
- **p. 8 / 4 Experiments - extractive body cue:** Our results suggest that domain-agnostic reward shaping does not work well (at least in the simple forms we have tried).
- **p. 8 / 4 Experiments - extractive body cue:** Surprisingly neither DDPG, nor DDPG+HER was able to successfully solve any of the tasks with any of these reward functions8.Our results are consistent with the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Learning curves for the shaped reward r(s, a, g) = -/g -s′ object/2 (it performed best among the shaped rewards we have tried). ...
- **p. 10 / 4 Experiments - extractive body cue:** After retraining the policy with gaussian noise (std=1cm) added to observations10 the success rate increased to 5/5.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 5 (2 Background), p. 1 (1 Introduction), p. 3 (2 Background), p. 4 (2 Background)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped (Ng et ... (p. 1, 1 Introduction).
- **Actual contribution:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy ... (p. 2, 1 Introduction).
- **Evaluation boundary:** 4.6 we show the results of the experiments on the physical robot. (p. 5, 4 Experiments).
- **Explicit failure boundary:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
