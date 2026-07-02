# VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

- Year/Venue: 2024 / CoRL
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, VLM, zero-shot
- Paper link: ./2024/CoRL/2024_CoRL_VLM-Grounder-A-VLM-Agent-for-Zero-Shot-3D-Visual-Grounding/paper.pdf
- Code/Project: https://github.com/InternRobotics/VLM-Grounder
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, estimating a 3D bounding box from a single image can be problematic due to limited field-of-view and inaccurate depth information.
- However, existing visual grounding datasets are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.
- VLM-Grounder (ours) Projection 3D Localization Object 1 is a black cabinet at (x1, y1, z1).

## Core Idea
- To explore this, we propose a Visual-Retrieval Benchmark.
- PC Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 ScanRefer TGNN InstanceRefer 3DVG-Transformer BUTD-DETR é é é é é é é é é é 37.3 34.3 40.2 47.6 52.2 24.3 ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on ScanRefer and Nr3D datasets show VLM-Grounder outperforms previous zero-shot methods, achieving 51.6% Acc@0.25 on ScanRefer and 48.0% Acc on Nr3D, without relying on 3D geometry or ...
- We report the performance of the baselines from their original papers, and the results on the same 250 validation samples are provided in the supplementary material.
- For our experiments, we sample one frame from every 20 frames of the original ScanNet image sequences.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on ScanRefer and Nr3D datasets show VLM-Grounder outperforms previous zero-shot methods, achieving 51.6% Acc@0.25 on ScanRefer and 48.0% Acc on Nr3D, without relying on 3D geometry or ...
- In this work, we present VLM-Grounder, a novel framework using vision-language models (VLMs) for zero-shot 3D visual grounding based solely on 2D images.

## Abstract Cue
- : 3D visual grounding is crucial for robots, requiring integration of natural language and 3D scene understanding.
