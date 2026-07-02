# Problem

- Year/Venue: 2025 / CoRL
- Category: Navigation and Embodied AI
- Tags: Navigation, mobile manipulation, VLM
- Paper link: ./2025/CoRL/2025_CoRL_MoTo-A-Zero-shot-Plug-in-Interaction-aware-Navigation-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- We can control the robot by solving an optimization problem that minimizes the distance between the two keypoints and considers several additional constraints, including collision avoidance, smoothness, and ...
- However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.

## 해결하려는 문제
- Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional ...
- Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.
- To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base ...

## 선행 연구 / 배경 단서
- MoTo Get the Water Cook Food Pick up the Fruit Fixed-base Manipulation Mobile Trajectory Arm Trajectory AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be plugged into any ...
- In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- We can control the robot by solving an optimization problem that minimizes the distance between the two keypoints and considers several additional constraints, including collision avoidance, smoothness, and ...
