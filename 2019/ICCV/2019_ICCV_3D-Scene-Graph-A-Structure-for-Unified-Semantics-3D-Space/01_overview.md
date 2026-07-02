# 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera

- Year/Venue: 2019 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, semantic, geometry, Graph Reasoning
- Paper link: ./2019/ICCV/2019_ICCV_3D-Scene-Graph-A-Structure-for-Unified-Semantics-3D-Space/paper.pdf
- Code/Project: https://3dscenegraph.stanford.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- obj1 obj1 obj2 (0.8, 0.3, - 0.1) obj2 0.85 obj2 class: bed color: blue, brown material: wood, fabric area: 2.2 m2 shape: prism rectangular action affordance: sit on, ...
- Introduction B1 Where should semantic information be grounded and what structure should it have to be most useful and invariant?
- This is a fundamental question for a content that preoccupies a number of domains, such as Computer Vision and Robotics.

## Core Idea
- 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- obj1 obj1 obj2 (0.8, 0.3, - 0.1) obj2 0.85 obj2 class: bed color: blue, brown material: wood, fabric area: 2.2 m2 shape: prism rectangular action affordance: sit on, ...
- Introduction B1 Where should semantic information be grounded and what structure should it have to be most useful and invariant?
- This is a fundamental question for a content that preoccupies a number of domains, such as Computer Vision and Robotics.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## Abstract Cue
- obj1 obj1 obj2 (0.8, 0.3, - 0.1) obj2 0.85 obj2 class: bed color: blue, brown material: wood, fabric area: 2.2 m2 shape: prism rectangular action affordance: sit on, lay on obj1, obj2, S: True (1.6, 0.0, 0.0) 1.75 S2 S S1 class: living room shape: ...
