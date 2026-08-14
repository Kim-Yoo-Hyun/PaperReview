# FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects

- Year/Venue: 2022 / RSS
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, scene flow, articulated objects, point cloud, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://flowbot3d.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To address these challenges, we propose to separate this problem into one of “affordance learning” and “motion planning.” If a robot can predict the potential movements of an ...
- Thus, we tackle the problem of manipulating articulated objects by learning to predict the motion of individual parts on articulated objects.
- While humans can rapidly adapt to novel articulated objects, constructing robotic manipulation agents that can generalize in the same way poses significant challenges, since the complex structure of ...

## Core Idea
- We propose a visionbased system that learns to predict the potential motions of the parts of a variety of articulated objects to guide downstream motion planning of the ...
- To address these challenges, we propose to separate this problem into one of “affordance learning” and “motion planning.” If a robot can predict the potential movements of an ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Results show that our system achieves state-of-theart performance in both simulated and real-world experiments.
- We then deploy an analytical motion planner based on this vector field to achieve a policy that yields maximum articulation.
- We train a single vision model entirely in simulation across all categories of objects, and we demonstrate the capability of our system to generalize to unseen object instances ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Results show that our system achieves state-of-theart performance in both simulated and real-world experiments.
- To address these challenges, we propose to separate this problem into one of “affordance learning” and “motion planning.” If a robot can predict the potential movements of an ...
- We propose a visionbased system that learns to predict the potential motions of the parts of a variety of articulated objects to guide downstream motion planning of the ...

## Abstract Cue
- —We explore a novel method to perceive and manipulate 3D articulated objects that generalizes to enable a robot to articulate unseen classes of objects.
