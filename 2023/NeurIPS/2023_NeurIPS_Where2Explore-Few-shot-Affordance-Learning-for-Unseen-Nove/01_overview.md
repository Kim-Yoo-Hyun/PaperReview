# Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

- Year/Venue: 2023 / NeurIPS
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/where2explore/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This limitation hinders the efficiency and safety of real-world applications of robots.
- Many previous works have been done on perceiving and manipulating articulated objects .
- However, conducting real-world interactions with diverse objects or acquiring 3D models encompassing potential categories can be prohibitively time-consuming and costly.

## Core Idea
- As shown in Figure 2, we propose the ‘Where2Explore’ framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category fewshot exploration.
- To harness this commonality, we introduce ‘Where2Explore’, an affordance learning framework that effectively explores novel categories with minimal interactions on a limited number of instances.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments in simulated and real-world environments demonstrate our framework’s capacity for efficient few-shot exploration and generalization.
- We conduct experiments under two different manipulation action types (pushing and pulling).
- For the training stage, to filter out randomness and prove the universal effectiveness of our framework, we conduct experiments using 4 different training category combinations, which are {cabinet, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments in simulated and real-world environments demonstrate our framework’s capacity for efficient few-shot exploration and generalization.
- To harness this commonality, we introduce ‘Where2Explore’, an affordance learning framework that effectively explores novel categories with minimal interactions on a limited number of instances.
- Our framework explicitly estimates the geometric similarity across different categories, identifying local areas that differ from shapes in the training categories for efficient exploration while concurrently transferring affordance ...

## Abstract Cue
- Articulated object manipulation is a fundamental yet challenging task in robotics.
