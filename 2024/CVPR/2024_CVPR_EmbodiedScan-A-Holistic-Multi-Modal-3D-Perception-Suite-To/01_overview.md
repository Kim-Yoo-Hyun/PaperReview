# EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

- Year/Venue: 2024 / CVPR
- Category: Benchmarks and Datasets
- Tags: 3D Vision, Embodied AI, dataset
- Paper link: ./2024/CVPR/2024_CVPR_EmbodiedScan-A-Holistic-Multi-Modal-3D-Perception-Suite-To/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Nonetheless, subtle but significant discrepancies exist between this expectation and research problems examined within the computer vision community.
- Most previous studies have primarily revolved around scene-level input and output problems from a global view , i.e., taking reconstructed 3D point clouds or meshes as inputs and ...
- Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small or lack comprehensive annotations to support the aforemen- Dataset #Scans #Imgs #Objs #Cats #Prompts Ego Capture ...

## Core Idea
- We use cross-entropy loss and sceneclass affinity loss for training.
- Given the multi-level sparse visual features FkS and text features from the text encoder, we use a multi-modal fusion transformer model for vision-language information interactions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- It is capable of processing an arbitrary number of multi-modal inputs and demonstrates remarkable 3D perception capabilities, both within the two series of benchmarks we set up, i.e., ...
- To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.
- Building upon this database, we introduce a baseline framework named Embodied Perceptron.
- It is capable of processing an arbitrary number of multi-modal inputs and demonstrates remarkable 3D perception capabilities, both within the two series of benchmarks we set up, i.e., ...

## Abstract Cue
- In the realm of computer vision and robotics, embodied agents are expected to explore their environment and carry out human instructions.
