# Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fast-in-Slow-A-Dual-System-VLA-Model-Unifying-Fast-Manipul/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation.
- However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2.

## Core Idea
- In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing ...
- To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2’s contextual understanding to ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in realworld tasks in terms of average success rate, while achieving a 117.7 Hz control ...
- As shown in Table 1, FiS-VLA achieves an average success rate of 69% across 10 diverse tasks, surpassing the previous SOTA methods CogACT and π0 by margins of ...
- We compare FiS-VLA against four state-of-the-art (SOTA) VLA models, including ManipLLM , OpenVLA , π0 , and CogACT, where the latter two are dual-system methods but operate with ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in realworld tasks in terms of average success rate, while achieving a 117.7 Hz control ...
- In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing ...
- To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2’s contextual understanding to ...

## Abstract Cue
- Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation.
