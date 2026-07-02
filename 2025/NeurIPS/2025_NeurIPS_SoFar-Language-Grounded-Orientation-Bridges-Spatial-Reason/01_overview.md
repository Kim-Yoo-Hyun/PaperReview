# SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SoFar-Language-Grounded-Orientation-Bridges-Spatial-Reason/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- While prior works emphasize position relationship, orientation understanding is equally critical for defining the full 6-DoF of object pose or end-effector poses .
- These annotations are from Objaverse and generated automatically by prompting GPT-4o with rich semantic queries covering both intra-object spatial reasoning and inter-object manipulation contexts—eliminating the need for costly ...

## Core Idea
- In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the “plug-in” direction of a USB ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrated the effectiveness and generalization of our S O FAR, e.g., zero-shot 48.7% successful rate on Open6DOR and zero-shot 74.9% successful rate on SIMPLER-Env.
- 7, S O FAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead.
- We train different model variants on OrienText300K, and the results in Table 2 report performance across different angular thresholds ranging from 45° to 5°.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrated the effectiveness and generalization of our S O FAR, e.g., zero-shot 48.7% successful rate on Open6DOR and zero-shot 74.9% successful rate on SIMPLER-Env.
- In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the “plug-in” direction of a USB ...

## Abstract Cue
- While spatial reasoning has made progress in object localization relationships, it often overlooks object orientation—a key factor in 6-DoF fine-grained manipulation.
