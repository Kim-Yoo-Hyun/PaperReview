# Mastering Diverse Domains through World Models

- Year/Venue: 2025 / Nature
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, generalist reinforcement learning, latent imagination
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://danijar.com/project/dreamerv3/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human data has been ...
- This brittleness poses a bottleneck in applying reinforcement learning to new problems and also limits the applicability of reinforcement learning to computationally expensive models or tasks where tuning ...
- These specialized algorithms target the unique challenges posed by different application domains, such as continuous control 6 , discrete actions 7,8 , sparse rewards 9 , image inputs ...

## Core Idea
- We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily applicable to new ...
- Learning algorithm We present the third generation of the Dreamer algorithm 21,22 .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...
- Crucially, Dreamer substantially outperforms PPO across all domains. • Atari This established benchmark contains 57 Atari 2600 games with a budget of 200M frames, posing a diverse range ...
- Dreamer also outperforms the widely-used expert algorithms Rainbow 40 and IQN 41 . • ProcGen This benchmark of 16 games features randomized levels and visual distractions to test ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...
- Dreamer also substantially outperforms a high-quality implementation of the widely applicable PPO algorithm. b, Applied out of the box, Dreamer learns to obtain diamonds in the popular video ...
- Correspondence: mail@danijar.com (a) Control Suite (b) Atari (c) ProcGen (d) DMLab (e) Minecraft Figure 2: Diverse visual domains used in the experiments.

## Abstract Cue
- Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms across a wide range of benchmarks and data budgets.
