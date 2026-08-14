# UMPNet: Universal Manipulation Policy Network for Articulated Objects

- Year/Venue: 2022 / RA-L
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, active perception, articulated objects, manipulation policy
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ump-net.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- — We introduce the Universal Manipulation Policy Network (UMPNet) – a single image-based policy network that infers closed-loop action sequences for manipulating articulated objects.
- To infer a wide range of action trajectories, the policy supports 6DoF action representation and varying trajectory length.
- To handle a diverse set of objects, the policy learns from objects with different articulation structures and generalizes to unseen objects or categories.

## Core Idea
- — We introduce the Universal Manipulation Policy Network (UMPNet) – a single image-based policy network that infers closed-loop action sequences for manipulating articulated objects.
- To support effective multistep interaction, we introduce a novel Arrow-of-Time action attribute that indicates whether an action will change the object state back to the past or forward ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To achieve this goal, we formulate an action trajectory by its initial 3D position and a sequence of action directions, which allows the network to
- The action trajectories inferred by the policy network (shown in Fig.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- — We introduce the Universal Manipulation Policy Network (UMPNet) – a single image-based policy network that infers closed-loop action sequences for manipulating articulated objects.
- To support effective multistep interaction, we introduce a novel Arrow-of-Time action attribute that indicates whether an action will change the object state back to the past or forward ...
- In this paper, we introduce the Universal Manipulation Policy Network (UMPNet) – a single policy network that discovers possible manipulation policies for an articulated object from visual observations ...

## Abstract Cue
- — We introduce the Universal Manipulation Policy Network (UMPNet) – a single image-based policy network that infers closed-loop action sequences for manipulating articulated objects.
