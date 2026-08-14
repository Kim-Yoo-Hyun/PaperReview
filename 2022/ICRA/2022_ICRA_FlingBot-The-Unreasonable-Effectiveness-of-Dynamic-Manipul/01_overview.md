# FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

- Year/Venue: 2022 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, cloth manipulation, dynamic manipulation, vision-based control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://flingbot.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Yet, most prior works have tackled cloth manipulation using exclusively single-arm quasi-static actions, which requires a large number of interactions for challenging initial cloth configurations and strictly limits ...

## Core Idea
- We propose to use a dual-arm pick, stretch, and fling primitive.
- Our approach learns how to unfold a piece of fabric from arbitrary initial configurations using a pick, stretch, and fling primitive for a dual-arm setup from visual observations.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The final system achieves over 80% coverage within 3 actions on novel cloths, can unfold cloths larger than the system’s reach range, and generalizes to T-shirts despite being ...
- We design a series of experiments to evaluate the advantage of dynamic actions over quasi-static actions in the task of cloth unfolding.
- In this work, we demonstrate the effectiveness of dynamic flinging actions for cloth unfolding with our proposed self-supervised learning framework, FlingBot.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach learns how to unfold a piece of fabric from arbitrary initial configurations using a pick, stretch, and fling primitive for a dual-arm setup from visual observations.
- The final system achieves over 80% coverage within 3 actions on novel cloths, can unfold cloths larger than the system’s reach range, and generalizes to T-shirts despite being ...
- In this work, we demonstrate the effectiveness of dynamic flinging actions for cloth unfolding with our proposed self-supervised learning framework, FlingBot.

## Abstract Cue
- : High-velocity dynamic actions (e.g., fling or throw) play a crucial role in our everyday interaction with deformable objects by improving our efficiency and effectively expanding our physical reach range.
