# Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2017 / IROS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, sim-to-real, domain randomization, perception
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- INTRODUCTION Performing robotic learning in a physics simulator could accelerate the impact of machine learning on robotics by allowing faster, more scalable, and lower-cost data collection than is ...

## Core Idea
- To our knowledge, this is the first successful transfer of a deep neural network trained only on simulated RGB images (without pre-training on real images) to the real ...
- Ideally, we could learn policies that encode complex behaviors entirely in simulation and successfully run those policies on physical robots with minimal additional training.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Learning in simulation is especially promising for building on recent results using deep reinforcement learning to achieve human-level performance on tasks like Atari and robotic control , .
- CONCLUSION We demonstrated that an object detector trained only in simulation can achieve high enough accuracy in the real world to perform grasping in clutter.
- — Bridging the ‘reality gap’ that separates simulated robotics from experiments on hardware could accelerate robotic research through improved data availability.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- Learning in simulation is especially promising for building on recent results using deep reinforcement learning to achieve human-level performance on tasks like Atari and robotic control , .
- — Bridging the ‘reality gap’ that separates simulated robotics from experiments on hardware could accelerate robotic research through improved data availability.
- To demonstrate the capabilities of our detectors, we show they can be used to perform grasping in a cluttered environment.

## Abstract Cue
- — Bridging the ‘reality gap’ that separates simulated robotics from experiments on hardware could accelerate robotic research through improved data availability.
