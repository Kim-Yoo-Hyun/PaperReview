# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fast-in-Slow-A-Dual-System-VLA-Model-Unifying-Fast-Manipul/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation.
- However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2.

## 해결하려는 문제
- For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in realworld tasks in terms of average success rate, while achieving a 117.7 Hz control ...
- In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing ...
- To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2’s contextual understanding to ...

## 선행 연구 / 배경 단서
- Simultaneously, enabling robots to execute a broad spectrum of tasks while adapting to variations in objects and environments remains the core challenge.
- Block 1 Block 2 System 1 in System2 LLM Text prompts “Place the wine on the rack.” Feature Feature Robot state Robot state Action System 1 (a) Previous ...
