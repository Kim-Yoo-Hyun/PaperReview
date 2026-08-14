# RMA: Rapid Motor Adaptation for Legged Robots

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / RSS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, locomotion, sim-to-real, online adaptation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ashish-kmr.github.io/rma-legged-robots/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in the simulator differ ...
- This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots.
- We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with ...

## Core Idea
- RMA consists of two components: a base policy and an adaptation module.
- In this paper, we report on our progress on solving this A) Training in Simulation Phase 1 Mass, COM, Friction Terrain Height (et) Motor Strength xt, at−1 Env

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments.
- These methods require considerable expertise on the part of the human designer, and in recent years there has been much interest in replicating this success using reinforcement learning ...
- Video results at https://ashish-kmr.github.io/rma-legged-robots/.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments.
- RMA consists of two components: a base policy and an adaptation module.
- In this paper, we report on our progress on solving this A) Training in Simulation Phase 1 Mass, COM, Friction Terrain Height (et) Motor Strength xt, at−1 Env

## Abstract Cue
- —Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear.
