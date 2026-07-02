# ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ViSPLA-Visual-Iterative-Self-Prompting-for-Language-Guided/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on ...
- Formally, we can represent the affordance detection problem as a mapping function fθ : (P) 7→ A, where P ∈ RN ×3 denotes a point cloud with N ...
- Language-guided affordance prediction offers a mathematically elegant solution to this complex problem.

## Core Idea
- Project Website We propose ViSPLA, a novel iterative self-prompting framework for language-guided 3D affordance detection that incorporates differential geometric feedback for progressive mask refinement.
- While existing approaches model this as a direct mapping fθ : (P, L) 7→ M, we introduce an iterative refinement process, as already described in section 1: Mt ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.
- In this work, we introduce ViSPLA, a novel iterative selfprompting framework that leverages the intrinsic geometry of predicted masks for continual refinement.
- To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision.

## Abstract Cue
- We address the problem of language-guided 3D affordance prediction, a core capability for embodied agents interacting with unstructured environments.
