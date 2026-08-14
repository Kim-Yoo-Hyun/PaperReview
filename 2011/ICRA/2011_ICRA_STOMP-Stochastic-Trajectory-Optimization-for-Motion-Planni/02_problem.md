# Problem

- Year/Venue: 2011 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, motion planning, trajectory optimization, stochastic optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://moveit.github.io/moveit_tutorials/doc/stomp_planner/stomp_planner_tutorial.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. costs corresponding to ...
- The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated trajectory with lower ...
- A cost function based on a combination of obstacle and smoothness cost is optimized in each iteration.

## 해결하려는 문제
- We demonstrate our approach through both simulation and experimental results with the PR2 mobile manipulation robot.
- No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. costs corresponding to ...
- — We present a new approach to motion planning using a stochastic trajectory optimization framework.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
