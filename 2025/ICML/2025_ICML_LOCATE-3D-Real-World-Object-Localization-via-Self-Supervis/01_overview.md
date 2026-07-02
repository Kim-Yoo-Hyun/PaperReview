# LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

- Year/Venue: 2025 / ICML Spotlight/Poster
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_LOCATE-3D-Real-World-Object-Localization-via-Self-Supervis/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on real-world devices.

## Core Idea
- Furthermore, when also trained with our L3DD dataset (L OCATE 3D+), the model demonstrates even stronger performance, improving across all metrics while maintaining the same architecture and training ...
- We present the overall results in Table 1.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In this work, we develop L OCATE 3D (see Figure 1), a state-of-the-art model for 3D-R EF E XP.
- We present L OCATE 3D, a model for localizing objects in 3D scenes from referring expressions like “the small coffee table between the sofa and the lamp.” L ...
- At one end of the spectrum are methods that train specialized models for this task (Jain et al., 2021; Chen et al., 2022) on small benchmark datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present L OCATE 3D, a model for localizing objects in 3D scenes from referring expressions like “the small coffee table between the sofa and the lamp.” L ...
- In this work, we develop L OCATE 3D (see Figure 1), a state-of-the-art model for 3D-R EF E XP.
- Once trained, the 3D-JEPA encoder is finetuned alongside a language-conditioned decoder to jointly predict 3D masks and bounding boxes.

## Abstract Cue
- the 3D world grounded in human natural language is essential.
