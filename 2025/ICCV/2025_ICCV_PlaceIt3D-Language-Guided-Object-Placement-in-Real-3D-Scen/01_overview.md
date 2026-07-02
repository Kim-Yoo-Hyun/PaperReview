# PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_PlaceIt3D-Language-Guided-Object-Placement-in-Real-3D-Scen/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The task demands tackling four intertwined challenges: (a) one-to-many ambiguity in valid placements; (b) precise geometric and physical reasoning; (c) joint understanding across the scene, the asset, and ...
- The first three challenges mirror the complexities of synthetic scene generation, while the metadata-free, noisy-scan scenario is inherited from language-guided 3D visual grounding.

## Core Idea
- We introduce the task of Language-Guided Object Placement in Real 3D Scenes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- As shown in Figure 1, the placement must also respect the physical constraints of the space and of the 3D asset.
- We inaugurate this task by introducing a benchmark and evaluation protocol, releasing a dataset for training multi-modal large language models (MLLMs), and establishing a first nontrivial baseline.
- We believe this challenging setup and benchmark will provide a foundation for evaluating and advancing MLLMs in 3D understanding. ∗ Work done during an internship at Niantic.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We inaugurate this task by introducing a benchmark and evaluation protocol, releasing a dataset for training multi-modal large language models (MLLMs), and establishing a first nontrivial baseline.
- We introduce the task of Language-Guided Object Placement in Real 3D Scenes.
- As shown in Figure 1, the placement must also respect the physical constraints of the space and of the 3D asset.

## Abstract Cue
- Introduction At two to three years old, neurotypical children learn to follow two-step instructions like “Get your shoes and put them on the shelf” .
