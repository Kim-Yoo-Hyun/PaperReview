# How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation

- Year/Venue: 2025 / ICML Poster
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICML/2025_ICML_How-Do-Images-Align-and-Complement-LiDAR-Towards-a-Harmoni/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Recently, a few studies have sought to overcome this challenge by integrating LiDAR inputs with camera images, leveraging the rich and dense texture information provided by the latter.
- However, LiDAR inherently faces limitations in detecting small or distant objects due to its radial emission pattern, which results in sparse returns along each laser ray (Li et ...

## Core Idea
- To address these issues, we propose Image-Assists-LiDAR (IAL), a novel multimodal 3D panoptic segmentation framework.
- We present comprehensive comparison results for LiDAR panoptic segmentation performance on the nuScenes validation and test sets, as shown in Table 2 and Table 3.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our IAL framework achieves state-of-the-art performance compared to previous multi-modal 3D panoptic segmentation m
- While these approaches have shown promising results, they still face challenges, such as misalignment during data augmentation and the reliance on postprocessing steps.
- Next, we adopt a transformer decoder to directly predict panoptic segmentation results.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Next, we adopt a transformer decoder to directly predict panoptic segmentation results.
- While these approaches have shown promising results, they still face challenges, such as misalignment during data augmentation and the reliance on postprocessing steps.
- Our IAL framework achieves state-of-the-art performance compared to previous multi-modal 3D panoptic segmentation m

## Abstract Cue
- 3D Panoptic segmentation simultaneously assigns semantic labels and identifies distinct instances, effectively unifying 3D semantic (Zhao et al., 2021; Xu et al., 2023b) and instance (Li & Zhao, 2024) segmentation to provide a holistic understanding of the scene.
