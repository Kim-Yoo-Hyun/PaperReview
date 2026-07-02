# SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning
- Paper link: ./2025/ICML/2025_ICML_SAM2Act-Integrating-Visual-Foundation-Model-with-A-Memory/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- While significant progress has been made in robotic manipulation, existing approaches often fall short in generalization to complex environmental variations and addressing memorydependent tasks.
- Significant progress has been made in robotic manipulation through prior work.

## Core Idea
- Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory.
- To bridge this gap, we introduce SAM2Act, a multi-view robotic transformerbased policy that leverages multi-resolution upsampling with visual representations from largescale foundation model.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- SAM2Act achieves a state-of-the-art average success rate of 86.8% across 18 tasks in the RLBench benchmark, and demonstrates robust generalization on The Colosseum benchmark, with only a 4.3% ...
- SAM2Act+ achieves an average success rate of 94.3% on memory-based tasks in MemoryBench, significantly outperforming existing approaches and pushing the boundaries of memory-based robotic systems.
- Humans excel in such environments because they can interact with their surroundings to achieve specific goals, generalize to unseen scenarios, and retain knowledge from past experiences (Smith & ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory.
- SAM2Act achieves a state-of-the-art average success rate of 86.8% across 18 tasks in the RLBench benchmark, and demonstrates robust generalization on The Colosseum benchmark, with only a 4.3% ...
- To bridge this gap, we introduce SAM2Act, a multi-view robotic transformerbased policy that leverages multi-resolution upsampling with visual representations from largescale foundation model.

## Abstract Cue
- Robotic manipulation systems operating in diverse, dynamic environments must exhibit three critical abilities: multitask interaction, generalization to unseen scenarios, and spatial memory.
