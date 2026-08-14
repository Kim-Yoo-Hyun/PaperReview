# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2018 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, continuous control, maximum entropy
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/haarnoja/sac
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning.
- Both of these challenges severely limit the applicability of such methods to complex, real-world domains.
- Correspondence to: Tuomas Haarnoja <haarnoja@berkeley.edu>. of these methods in real-world domains has been hampered by two major challenges.

## Core Idea
- In this paper, we propose soft actor-critic, an offpolicy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy ...
- Second, these methods are often brittle with respect to their hyperparameters: learning rates, exploration constants, and other settings must be set carefully for different problem settings to achieve ...
- Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy ...
- Second, these methods are often brittle with respect to their hyperparameters: learning rates, exploration constants, and other settings must be set carefully for different problem settings to achieve ...
- Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds.

## Abstract Cue
- Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks.
