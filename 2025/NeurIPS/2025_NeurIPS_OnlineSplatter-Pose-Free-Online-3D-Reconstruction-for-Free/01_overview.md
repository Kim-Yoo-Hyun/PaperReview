# OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OnlineSplatter-Pose-Free-Online-3D-Reconstruction-for-Free/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- Real-time 3D reconstruction of freely moving objects from monocular video remains a fundamental challenge in computer vision, with far-reaching implications for robotics, augmented reality, and interactive 3D applications ...
- The challenge is especially acute in an online setting, where systems must update their understanding of objects as every new frame arrives, a capability essential for autonomous robots ...

## Core Idea
- We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle optimization.
- To differentiate and contextualize these tokens, we introduce

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Evaluations on real-world datasets demonstrate that OnlineSplatter significantly outperforms state-of-the-art pose-free reconstruction baselines, consistently improving with more observations while maintaining constant memory and runtime.
- This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies to analyze each ...
- We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤ t ≤ 4}): Tests the model’s ability ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach anchors reconstruction using the first frame and progressively refines the object representation through a dense Gaussian primitive field, maintaining constant computational cost regardless of video sequence ...
- We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle optimization.
- Evaluations on real-world datasets demonstrate that OnlineSplatter significantly outperforms state-of-the-art pose-free reconstruction baselines, consistently improving with more observations while maintaining constant memory and runtime.

## Abstract Cue
- Free-moving object reconstruction from monocular video remains challenging, particularly without reliable pose or depth cues and under arbitrary object motion.
