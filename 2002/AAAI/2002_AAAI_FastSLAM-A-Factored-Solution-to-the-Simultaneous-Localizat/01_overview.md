# FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

- Year/Venue: 2002 / AAAI
- Category: 3D Geometry, Reconstruction, and SLAM
- Tags: Robotics, SLAM, particle filter, state estimation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this paper we approach the SLAM problem from a Bayesian point of view.
- The problem of simultaneous localization and mapping, also known as SLAM, has attracted immense attention in the mobile robotics literature.
- SLAM addresses the problem of building a map of an environment from a sequence of landmark measurements obtained from a moving robot.

## Core Idea
- We develop a tree-based data structure that reduces the running time of FastSLAM to O(M log K), making it significantly faster than existing EKF-based SLAM algorithms.
- The problem of simultaneous localization and mapping, also known as SLAM, has attracted immense attention in the mobile robotics literature.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and realworld data.
- In a set of experiments specifically aimed to elucidate the scaling properties of the approach, we evaluated the map and robot pose errors as a function of the ...
- Overall, the results indicate favorably scaling to large number of landmarks and small particle sets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and realworld data.
- However, few approaches to this problem scale up to handle the very large number of landmarks present in real environments.

## Abstract Cue
- The ability to simultaneously localize a robot and accurately map its surroundings is considered by many to be a key prerequisite of truly autonomous robots.
