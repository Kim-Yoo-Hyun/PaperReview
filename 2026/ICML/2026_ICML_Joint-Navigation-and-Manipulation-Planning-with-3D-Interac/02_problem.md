# Problem

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Robotics, 3D Vision, Navigation
- Paper link: ./2026/ICML/2026_ICML_Joint-Navigation-and-Manipulation-Planning-with-3D-Interac/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The code is available at https://github.com/kekeZ66/3D-IC Object grasping Navigating to the vicinity of the goal then switching to grasping/placing Object placing Step3 Receptacle navigation Step1 Object navigation (a) ...
- Most existing methods treat navigation and manipulation as separate stages, which can yield navigation endpoints that are poor for manipulation or manipulation-friendly poses that are globally inefficient.
- A hierarchical policy then scores these chains by jointly considering feasibility (via VLM reasoning over waypointcentric 3D features) and transition cost, selecting the best trade-off between success and ...

## 해결하려는 문제
- To address this, we propose 3D Interaction Chains (3D-IC), a unified framework that couples multi-stage navigation and manipulation planning.
- Experiments in simulation and on a real Stretch 3 robot demonstrate consistent gains in both task success and trajectory efficiency.
- The code is available at https://github.com/kekeZ66/3D-IC Object grasping Navigating to the vicinity of the goal then switching to grasping/placing Object placing Step3 Receptacle navigation Step1 Object navigation (a) ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
