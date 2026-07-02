# ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding

- Year/Venue: 2023 / CVPR
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision, Vision-Language Model, point cloud, alignment
- Paper link: ./2023/CVPR/2023_CVPR_ULIP-Learning-a-Unified-Representation-of-Language-Images/paper.pdf
- Code/Project: https://github.com/salesforce/ULIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In its 2D counterpart, recent advances have shown that similar problems can be significantly alleviated by employing knowledge from other modalities, such as language.

## Core Idea
- Therefore, we introduce ULIP to learn a unified representation of images, texts, and 3D point clouds by pre-training with object triplets from the three modalities.
- To reduce the demand of 3D data, ULIP leverages image and text encoders that are pre-trained with large-scale image-text pairs, and aligns 3D representation to the pre-aligned image-text ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that ULIP effectively improves the performance of multiple recent 3D backbones by simply pre-training them on ShapeNet55 using our framework, achieving state-of-the-art performance in both standard ...
- ULIP also improves the performance of PointMLP by around 3% in 3D classification on ScanObjectNN, and outperforms PointCLIP by 28.8% on top-1 accuracy for zero-shot 3D classification on ...
- The recognition capabilities of current state-of-the-art 3D models are limited by datasets with a small number of annotated data and a pre-defined set of categories.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that ULIP effectively improves the performance of multiple recent 3D backbones by simply pre-training them on ShapeNet55 using our framework, achieving state-of-the-art performance in both standard ...
- Therefore, we introduce ULIP to learn a unified representation of images, texts, and 3D point clouds by pre-training with object triplets from the three modalities.
- To reduce the demand of 3D data, ULIP leverages image and text encoders that are pre-trained with large-scale image-text pairs, and aligns 3D representation to the pre-aligned image-text ...

## Abstract Cue
- The recognition capabilities of current state-of-the-art 3D models are limited by datasets with a small number of annotated data and a pre-defined set of categories.
