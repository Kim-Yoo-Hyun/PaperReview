# Sampling-based Algorithms for Optimal Motion Planning

- Year/Venue: 2011 / IJRR
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, motion planning, RRT*, asymptotic optimality
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ompl.kavrakilab.org/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and failure otherwise.
- The robotic motion planning problem has received a considerable amount of attention, especially over the last decade, as robots started becoming a vital part of modern industry as ...
- Even though modern robots may possess significant differences in sensing, actuation, size, workspace, application, etc., the problem of navigating through a complex environment is embedded and essential in ...

## Core Idea
- The robotic motion planning problem has received a considerable amount of attention, especially over the last decade, as robots started becoming a vital part of modern industry as ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A number of negative results are provided, characterizing existing algorithms, e.g., showing that, under mild technical conditions, the cost of the solution returned by broadly used sampling-based algorithms ...
- During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in practice and possess ...
- Moreover, it is shown that the computational complexity of the new algorithms is within a constant factor of that of their probabilistically complete (but not asymptotically optimal) counterparts.

## Limitation
- In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to ...

## Contribution
- A number of negative results are provided, characterizing existing algorithms, e.g., showing that, under mild technical conditions, the cost of the solution returned by broadly used sampling-based algorithms ...
- During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in practice and possess ...
- Moreover, it is shown that the computational complexity of the new algorithms is within a constant factor of that of their probabilistically complete (but not asymptotically optimal) counterparts.

## Abstract Cue
- During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in practice and possess theoretical guarantees such as probabilistic completeness.
