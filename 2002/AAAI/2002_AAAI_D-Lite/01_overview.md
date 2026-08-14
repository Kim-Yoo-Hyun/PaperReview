# D* Lite

- Year/Venue: 2002 / AAAI
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, path planning, incremental search, Navigation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Heuristic search methods, such as A* (Nilsson 1971), on the other hand, use heuristic knowledge in form of approximations of the goal distances to focus the search and ...
- Motivation Consider a goal-directed robot-navigation task in unknown terrain, where the robot always observes which of its eight adjacent cells are traversable and then moves with cost one ...

## Core Idea
- To gain insight into its behavior, we present various theoretical properties of LPA* that also apply to D* Lite.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We believe that these results provide a strong foundation for further research on fast replanning methods in artificial intelligence and robotics.
- Since the actual planning times are implementation and machine dependent, they make it difficult for others to reproduce the results of our performance comparison.
- We prove properties about D* Lite and demonstrate experimentally the advantages of combining incremental and heuristic search for the applications studied.

## Limitation
- D* Lite builds on our LPA*, that has a solid theoretical foundation, a strong similarity to A*, is efficient (since it does not expand any vertices whose gvalues ...

## Contribution
- We believe that these results provide a strong foundation for further research on fast replanning methods in artificial intelligence and robotics.
- We prove properties about D* Lite and demonstrate experimentally the advantages of combining incremental and heuristic search for the applications studied.

## Abstract Cue
- Incremental heuristic search methods use heuristics to focus their search and reuse information from previous searches to find solutions to series of similar search tasks much faster than is possible by solving each search task from scratch.
