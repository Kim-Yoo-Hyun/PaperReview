# Maximum Entropy Inverse Reinforcement Learning

- Year/Venue: 2008 / AAAI
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, inverse reinforcement learning, maximum entropy, demonstrations
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Capturing purposeful, sequential decision-making behavior can be quite difficult for general-purpose statistical machine learning algorithms; in such problems, algorithms must often reason about consequences of actions far into ...
- In problems of imitation learning the goal is to learn to predict the behavior and decisions an agent would choose– e.g., the motions a person would take to ...
- A powerful recent idea for approaching problems of imitation learning is to structure the space of learned policies to be solutions of search, planning, or, more generally, Markov ...

## Core Idea
- We develop our technique in the context of modeling realworld navigation and driving behaviors where collected data is inherently noisy and imperfect.
- In this work, we develop a probabilistic approach based on the principle of maximum entropy.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A key concern is that demonstrated behavior is prone to noise and imperfect behavior.
- This approach reduces learning to the problem of recovering a utility function that makes the behavior induced by a near-optimal policy closely mimic demonstrated behavior.
- Recent research has shown the benefit of framing problems of imitation learning as solutions to Markov Decision Problems.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach provides a well-defined, globally normalized distribution over decision sequences, while providing the same performance guarantees as existing methods.
- In this work, we develop a probabilistic approach based on the principle of maximum entropy.
- We develop our technique in the context of modeling realworld navigation and driving behaviors where collected data is inherently noisy and imperfect.

## Abstract Cue
- employ the principle of maximum entropy to resolve the ambiguity in choosing a distribution over decisions.
