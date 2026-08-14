# Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2016 / JMLR
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, guided policy search, policy learning, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Policy search methods can allow robots to learn control policies for a wide range of tasks, but practical applications of policy search often require hand-engineered components for perception, ...
- In this paper, we aim to answer the following question: does training the perception and control systems jointly end-toend provide better performance than training each component separately?
- To this end, we develop a method that can be used to learn policies that map raw image observations directly to torques at the robot’s motors.

## Core Idea
- To this end, we develop a method that can be used to learn policies that map raw image observations directly to torques at the robot’s motors.
- In this paper, we aim to answer the following question: does training the perception and control systems jointly end-toend provide better performance than training each component separately?

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our method on a range of real-world manipulation tasks that require close coordination between vision and control, such as screwing a cap onto a bottle, and ...

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We evaluate our method on a range of real-world manipulation tasks that require close coordination between vision and control, such as screwing a cap onto a bottle, and ...
- To this end, we develop a method that can be used to learn policies that map raw image observations directly to torques at the robot’s motors.
- In this paper, we aim to answer the following question: does training the perception and control systems jointly end-toend provide better performance than training each component separately?

## Abstract Cue
- Policy search methods can allow robots to learn control policies for a wide range of tasks, but practical applications of policy search often require hand-engineered components for perception, state estimation, and low-level control.
