# Problem

- Year/Venue: 2023 / NeurIPS
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/where2explore/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- This limitation hinders the efficiency and safety of real-world applications of robots.
- Many previous works have been done on perceiving and manipulating articulated objects .
- However, conducting real-world interactions with diverse objects or acquiring 3D models encompassing potential categories can be prohibitively time-consuming and costly.

## 해결하려는 문제
- Extensive experiments in simulated and real-world environments demonstrate our framework’s capacity for efficient few-shot exploration and generalization.
- To harness this commonality, we introduce ‘Where2Explore’, an affordance learning framework that effectively explores novel categories with minimal interactions on a limited number of instances.
- Our framework explicitly estimates the geometric similarity across different categories, identifying local areas that differ from shapes in the training categories for efficient exploration while concurrently transferring affordance ...

## 선행 연구 / 배경 단서
- This limitation hinders the efficiency and safety of real-world applications of robots.
- Many previous works have been done on perceiving and manipulating articulated objects .
- Moreover, this approach could still fail with the emergence of new object categories or designs (e.g., a cup with novel geometries resembling a gourd as shown in Figure ...
