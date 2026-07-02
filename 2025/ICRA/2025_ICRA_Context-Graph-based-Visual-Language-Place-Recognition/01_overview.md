# Context Graph-based Visual-Language Place Recognition

- Year/Venue: 2025 / ICRA
- Category: 3D Large Multimodal Models
- Tags: Graph Reasoning
- Paper link: ./2025/ICRA/2025_ICRA_Context-Graph-based-Visual-Language-Place-Recognition/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, these approaches still fail under drastic changes and require large amounts of labeled data to train models, presenting a significant limitation.
- This paper addresses the problem of VPR, which involves accurately recognizing the location corresponding to a given query image.
- Thus, accurately recognizing the location corresponding to a given query image through VPR becomes an essential problem.

## Core Idea
- In this paper, we introduce a novel VPR approach that remains robust to scene changes and does not require additional training.
- Additionally, our approach does not require additional training by utilizing pre-trained weights and enables an understanding of image context by considering the relationship between segmentation regions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To achieve this, a robot must have the ability to determine whether its current location has been previously visited by comparing the incoming sensor data with a database ...
- The experiments representation techniques and off-the-shelf convolutional neural network (CNN) descriptors.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we introduce a novel VPR approach that remains robust to scene changes and does not require additional training.
- To address this, end-to-end training approaches have been proposed to overcome the limitations of hand-crafted features.
- Our method constructs semantic image descriptors by extracting pixel-level embeddings using a zero-shot, language-driven semantic segmentation model.

## Abstract Cue
- — In vision-based robot localization and SLAM, Visual Place Recognition (VPR) is essential.
