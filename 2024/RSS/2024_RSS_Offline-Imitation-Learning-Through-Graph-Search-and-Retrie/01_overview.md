# Offline Imitation Learning Through Graph Search and Retrieval

- Year/Venue: 2024 / RSS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, offline learning, graph search, retrieval
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss20/p054.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Existing works typically use offline deep reinforcement learning (RL) to solve this challenge, but in practice these algorithms are unstable and fragile due to the deadly triad issue.
- To overcome this problem, we propose GSR, a simple yet effective algorithm that learns from suboptimal demonstrations through Graph Search and Retrieval.
- As a result, a robot has to learn skills from suboptimal demonstrations and unstructured interactions, which remains a key challenge.

## Core Idea
- To overcome this problem, we propose GSR, a simple yet effective algorithm that learns from suboptimal demonstrations through Graph Search and Retrieval.
- It involves training robots to mimic human demonstrations, allowing them to acquire manipulation skills in complex environments.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- GSR can achieve a 10% to 30% higher success rate and over 30% higher proficiency compared to baselines.
- I NTRODUCTION Imitation learning is a powerful approach to learning robots that has achieved great success in robotic manipulation in recent years .
- We evaluate our method in both simulation and real-world robotic manipulation tasks with complex visual inputs, covering various precise and dexterous manipulation skills with objects of different physical ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To overcome this problem, we propose GSR, a simple yet effective algorithm that learns from suboptimal demonstrations through Graph Search and Retrieval.
- We evaluate our method in both simulation and real-world robotic manipulation tasks with complex visual inputs, covering various precise and dexterous manipulation skills with objects of different physical ...
- It involves training robots to mimic human demonstrations, allowing them to acquire manipulation skills in complex environments.

## Abstract Cue
- —Imitation learning is a powerful machine learning algorithm for a robot to acquire manipulation skills.
