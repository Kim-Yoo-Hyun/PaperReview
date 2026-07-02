# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Scaffolding-Dexterous-Manipulation-with-Vision-Language-Mo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite the intrinsic advantages of dexterous hands over simpler end-effectors, existing learning paradigms have struggled to cope with their complexity .
- Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
- However, sourcing suitable trajectories—particularly for dexterous hands—remains a significant challenge.

## 해결하려는 문제
- Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- Given a task description (e.g., “open the cabinet”) and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then ...

## 선행 연구 / 배경 단서
- The prevailing approach for training generalist policies – imitation learning from demonstrations – has achieved limited success with robot hands, primarily due to the challenges of collecting accurate ...
- Despite the intrinsic advantages of dexterous hands over simpler end-effectors, existing learning paradigms have struggled to cope with their complexity .
