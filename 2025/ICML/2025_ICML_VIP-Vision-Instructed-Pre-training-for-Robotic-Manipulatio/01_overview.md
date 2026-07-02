# VIP: Vision Instructed Pre-training for Robotic Manipulation

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning
- Paper link: ./2025/ICML/2025_ICML_VIP-Vision-Instructed-Pre-training-for-Robotic-Manipulatio/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To handle this problem, we propose to use sparse point flows to provide more detailed information.
- A primary challenge in manipulation is the tasks are diverse, and the trained policy would be confused if the task targets are not specified clearly.
- Existing works primarily rely on text instruction to describe targets.

## Core Idea
- To handle this problem, we propose to use sparse point flows to provide more detailed information.
- Therefore, we introduce utilizing vision instruction to specify targets.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The results indicate VIP improves the performance on diverse tasks significantly, and the derived policy can complete competitive tasks like “opening the lid of a tightly sealed bottle”.
- Extensive tasks are designed based on real and simulated environments to evaluate the effectiveness of our vision instructed pre-training (VIP) method.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To handle this problem, we propose to use sparse point flows to provide more detailed information.
- Extensive tasks are designed based on real and simulated environments to evaluate the effectiveness of our vision instructed pre-training (VIP) method.
- A common practice in existing manipulation pre-training paradigms is describing task targets using text instructions like “pick up the green block”.

## Abstract Cue
- Pick up the green block The effectiveness of scaling up training data in robotic manipulation is still limited.
