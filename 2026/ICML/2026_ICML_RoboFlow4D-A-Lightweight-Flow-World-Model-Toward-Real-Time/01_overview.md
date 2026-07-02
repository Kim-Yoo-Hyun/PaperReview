# RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_RoboFlow4D-A-Lightweight-Flow-World-Model-Toward-Real-Time/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Although prior work has explored predictive flow planners to guide 3D manipulation, existing approaches often rely on modular pipelines stacking multiple submodels, resulting in high computational overhead and ...
- To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D space.

## Core Idea
- To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D space.
- We validate the generalization of our approach on 4 representative real-world tasks. (1) Pickand-Place: Pick up the cup and place it in the white box. (2) Stack: Pick ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments in both simulation and realworld settings demonstrate that RoboFlow4D consistently improves manipulation success rates and computational efficiency, advancing flow-guided planning for embodied intelligence.
- Furthermore, RoboFlow4D achieves 120× speedup over modular pipelines and reduces model scale by >24% compared to other flow models.
- Top left: System-level comparison of various flow-based planning. (a) 2D flow-based planning (Vecerik et al., 2024; Xu et al., 2024) predicts pixel-level flow on images using a modular ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments in both simulation and realworld settings demonstrate that RoboFlow4D consistently improves manipulation success rates and computational efficiency, advancing flow-guided planning for embodied intelligence.
- To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D space.
- Top left: System-level comparison of various flow-based planning. (a) 2D flow-based planning (Vecerik et al., 2024; Xu et al., 2024) predicts pixel-level flow on images using a modular ...

## Abstract Cue
- Planning and acting in 3D environments is a fundamental capability for robotic manipulation in the real world.
