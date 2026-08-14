# Problem

- Year/Venue: 2002 / AAAI
- Category: 3D Geometry, Reconstruction, and SLAM
- Tags: Robotics, SLAM, particle filter, state estimation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- In this paper we approach the SLAM problem from a Bayesian point of view.
- The problem of simultaneous localization and mapping, also known as SLAM, has attracted immense attention in the mobile robotics literature.
- SLAM addresses the problem of building a map of an environment from a sequence of landmark measurements obtained from a moving robot.

## 해결하려는 문제
- Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and realworld data.
- However, few approaches to this problem scale up to handle the very large number of landmarks present in real environments.

## 선행 연구 / 배경 단서
- We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to the full range ...
- We develop a tree-based data structure that reduces the running time of FastSLAM to O(M log K), making it significantly faster than existing EKF-based SLAM algorithms.
- The problem of simultaneous localization and mapping, also known as SLAM, has attracted immense attention in the mobile robotics literature.
