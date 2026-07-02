# Method

- Year/Venue: 2025 / CoRL
- Category: Navigation and Embodied AI
- Tags: Navigation, mobile manipulation, VLM
- Paper link: ./2025/CoRL/2025_CoRL_MoTo-A-Zero-shot-Plug-in-Interaction-aware-Navigation-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base ...
- Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.
- Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training.

## 원리적 동기
- In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- We can control the robot by solving an optimization problem that minimizes the distance between the two keypoints and considers several additional constraints, including collision avoidance, smoothness, and ...
- To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base ...

## 핵심 방법론
- Overall SR Average SR Step FindObj (↑) Pick (↑) FindRec (↑) Home-Robot (RL) Home-Robot (Heuristic) UniTeam 66.60% 65.40% 66.13% 61.10% 54.80% 62.65% 50.90% 43.70% 54.69% 14.80% 7.30% 17.96% ...
- Partial Success Rates Method FindObj (↑) Pick (↑) FindRec (↑) Overall SR Average SR Cost w/o Collision w/o Smoothness w/o Margin 66.93% 66.76% 65.95% 60.95% 61.48% 60.77% 49.24% ...
- When AK and TK make contact, a large margin is required for the robotic arm to enable subsequent fixed-base manipulation.
- We define the horizontal distance between the endeffector and the robot base center as the arm radius r, bounded by constants rmin and rmax .
- Given the robot’s design, r is a function of the arm pose r = g(θtarm ).
