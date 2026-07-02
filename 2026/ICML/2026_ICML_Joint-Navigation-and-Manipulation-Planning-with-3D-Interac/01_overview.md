# Joint Navigation and Manipulation Planning with 3D Interaction Chains

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Robotics, 3D Vision, Navigation
- Paper link: ./2026/ICML/2026_ICML_Joint-Navigation-and-Manipulation-Planning-with-3D-Interac/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The code is available at https://github.com/kekeZ66/3D-IC Object grasping Navigating to the vicinity of the goal then switching to grasping/placing Object placing Step3 Receptacle navigation Step1 Object navigation (a) ...
- Most existing methods treat navigation and manipulation as separate stages, which can yield navigation endpoints that are poor for manipulation or manipulation-friendly poses that are globally inefficient.
- A hierarchical policy then scores these chains by jointly considering feasibility (via VLM reasoning over waypointcentric 3D features) and transition cost, selecting the best trade-off between success and ...

## Core Idea
- To address this, we propose 3D Interaction Chains (3D-IC), a unified framework that couples multi-stage navigation and manipulation planning.
- In this paper, we propose 3D Interaction Chains (3D-IC), a framework that unifies the modeling of all task stages in OVMM through joint decision-making to improve both success ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments in simulation and on a real Stretch 3 robot demonstrate consistent gains in both task success and trajectory efficiency.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this, we propose 3D Interaction Chains (3D-IC), a unified framework that couples multi-stage navigation and manipulation planning.
- Experiments in simulation and on a real Stretch 3 robot demonstrate consistent gains in both task success and trajectory efficiency.
- The code is available at https://github.com/kekeZ66/3D-IC Object grasping Navigating to the vicinity of the goal then switching to grasping/placing Object placing Step3 Receptacle navigation Step1 Object navigation (a) ...

## Abstract Cue
- Step4 Step2 Open-vocabulary mobile manipulation (OVMM) requires long-horizon navigation in unseen environments and object-centric manipulation.
