# Method

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, VLA, trajectory representation, spatial reasoning, task generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://rt-trajectory.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose a policy conditioning method using such rough trajectory sketches, which we call RTTrajectory, that is practical, easy to specify, and allows the policy to effectively perform ...
- We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- During policy training, we first perform hindsight trajectory labeling to obtain trajectory conditioning labels from the demonstration dataset (Section 3.2).

## 원리적 동기
- The pursuit of generalist robot policies has been a perennial challenge in robotics.
- We propose a policy conditioning method using such rough trajectory sketches, which we call RTTrajectory, that is practical, easy to specify, and allows the policy to effectively perform ...

## 핵심 방법론
- We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- During policy training, we first perform hindsight trajectory labeling to obtain trajectory conditioning labels from the demonstration dataset (Section 3.2).
- 3.2 HINDSIGHT TRAJECTORY LABELS In this section, we describe how we acquire training trajectory conditioning labels from the demonstration dataset.
- We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
