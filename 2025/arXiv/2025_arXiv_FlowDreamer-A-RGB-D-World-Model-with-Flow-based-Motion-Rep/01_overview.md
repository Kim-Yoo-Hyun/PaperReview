# FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, RGB-D, 3D scene flow, robot manipulation, 4D reasoning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Existing visual world models have undergone rapid development in recent years.

## Core Idea
- As opposed to canonical approaches that handle dynamics prediction mostly implicitly and reconcile it with visual rendering in a single model, we introduce FlowDreamer, which adopts 3D scene ...
- For the Language Table environment, we use the official simulation environment.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The results demonstrate that FlowDreamer achieves better performance compared to other baseline RGB-D world models by 7% on semantic similarity, 11% on pixel quality, and 6% on success ...
- FlowDreamer achieves better results on future frame prediction and visual planning tasks in various robot manipulation domains. planning algorithms .
- We conduct experiments on 4 different benchmarks, covering both video prediction and visual planning tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The results demonstrate that FlowDreamer achieves better performance compared to other baseline RGB-D world models by 7% on semantic similarity, 11% on pixel quality, and 6% on success ...
- FlowDreamer achieves better results on future frame prediction and visual planning tasks in various robot manipulation domains. planning algorithms .
- As opposed to canonical approaches that handle dynamics prediction mostly implicitly and reconcile it with visual rendering in a single model, we introduce FlowDreamer, which adopts 3D scene ...

## Abstract Cue
- FlowDreamer RGB-D images This paper investigates training better visual world models for robot manipulation, i.e., models that can predict future visual observations by conditioning on past frames and robot actions.
