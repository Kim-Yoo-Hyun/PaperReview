# Where2Act: From Pixels to Actions for Articulated 3D Objects

- Year/Venue: 2021 / ICCV
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, affordance, articulated objects, active perception, point cloud
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://cs.stanford.edu/~kaichun/where2act/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- push One of the fundamental goals of visual perception is to allow agents to meaningfully interact with their environment.
- In this paper, we take a step towards that long-term goal – we extract highly localized actionable information related to elementary actions such as pushing or pulling for ...
- For example, given a drawer, our network predicts that applying a pulling force on the handle opens the drawer.

## Core Idea
- We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the regions over articulated ...
- We propose a learning-from-interaction framework with an online data sampling strategy that allows us to train the network in simulation (SAPIEN) and generalizes across categories.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show two high-rated proposals (left) and two with lower scores (right) due to interaction orientations and potential robot-object collisions.
- We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the regions over articulated ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the regions over articulated ...
- We propose a learning-from-interaction framework with an online data sampling strategy that allows us to train the network in simulation (SAPIEN) and generalizes across categories.
- We show two high-rated proposals (left) and two with lower scores (right) due to interaction orientations and potential robot-object collisions.

## Abstract Cue
- push One of the fundamental goals of visual perception is to allow agents to meaningfully interact with their environment.
