# Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, legged locomotion, Navigation, robust perception
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://bit.ly/45NBTuh
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- In a quantitative comparison with existing heuristic-based locally reactive planners, our policy increases the success rate over 30 % when facing perception failures.
- Unlike previous works relying on heuristics and anomaly detection to update navigational information, we train our navigation policy to reconstruct the environment information in the latent space from ...

## Core Idea
- We validate our approach in simulation and on the real quadruped robot ANYmal running in real-time (<10 ms CPU inference).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- For legged robots that can robustly traverse various terrains , such local planners have become a routine and demonstrated remarkable performance in different tasks , .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We validate our approach in simulation and on the real quadruped robot ANYmal running in real-time (<10 ms CPU inference).
- Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- In a quantitative comparison with existing heuristic-based locally reactive planners, our policy increases the success rate over 30 % when facing perception failures.

## Abstract Cue
- — Autonomous robots must navigate reliably in unknown environments even under compromised exteroceptive perception, or perception failures.
