# Planning-oriented Autonomous Driving

- Year/Venue: 2023 / CVPR
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: Planning, sensor fusion, 3D perception
- Paper link: ./2023/CVPR/2023_CVPR_Planning-oriented-Autonomous-Driving/paper.pdf
- Code/Project: https://github.com/OpenDriveLab/UniAD
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation ...
- Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning.

## Core Idea
- We introduce Unified Autonomous Driving (UniAD), a comprehensive framework up-to-date that incorporates full-stack driving tasks in one network.
- Mask” represent cross-attention and the attention mask in the pixel-agent interaction respectively. “Mask Feat.” denotes the reuse of the mask feature for instance-level occupancy.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With extensive ablations, the effectiveness of using such a philosophy is proven by substantially outperforming previous state-of-the-arts in all aspects.
- In order to perform a wide diversity of tasks and achieve advanced-level intelligence, contemporary approaches either deploy standalone models for individual tasks, or design a multi-task paradigm with ...
- We instantiate UniAD on the challenging nuScenes benchmark.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- With extensive ablations, the effectiveness of using such a philosophy is proven by substantially outperforming previous state-of-the-arts in all aspects.
- We introduce Unified Autonomous Driving (UniAD), a comprehensive framework up-to-date that incorporates full-stack driving tasks in one network.
- In order to perform a wide diversity of tasks and achieve advanced-level intelligence, contemporary approaches either deploy standalone models for individual tasks, or design a multi-task paradigm with ...

## Abstract Cue
- Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning.
