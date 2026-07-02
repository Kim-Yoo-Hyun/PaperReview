# ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Planning, 3D geometry, Robotics, VLM
- Paper link: ./2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/paper.pdf
- Code/Project: https://github.com/huangwl18/ReKep
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We study ReKep in the context of the sequential manipulation problem, where each task involves multiple stages that have spatio-temporal dependencies (e.g., “grasping”, “aligning”, and “pouring” in the ...
- Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify ...
- However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges.

## Core Idea
- We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and ...
- In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Despite promising results, we also identify several limitations which are discussed in Sec.
- In this section, we perform an empirical investigation by manually inspecting the failure cases of the experiments reported in Tab.
- We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and ...
- In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation.
- We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented ...

## Abstract Cue
- : Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors.
