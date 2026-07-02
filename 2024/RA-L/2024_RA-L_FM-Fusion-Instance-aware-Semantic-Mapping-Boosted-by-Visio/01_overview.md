# FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

- Year/Venue: 2024 / RA-L
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, semantic
- Paper link: ./2024/RA-L/2024_RA-L_FM-Fusion-Instance-aware-Semantic-Mapping-Boosted-by-Visio/paper.pdf
- Code/Project: https://github.com/HKUST-Aerial-Robotics/FM-Fusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- —Semantic mapping based on the supervised object detectors is sensitive to image distribution.
- In real-world environments, the object detection and segmentation performance can lead to a major drop, preventing the use of semantic mapping in a wider domain.
- On the other hand, the development of vision-language foundation models demonstrates a strong zero-shot transferability across data distribution.

## Core Idea
- We propose a probabilistic label fusion method to predict close-set semantic classes from open-set label measurements.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method achieves 40.3 mean average precision (mAP) on the ScanNet semantic instance segmentation task.
- It outperforms the traditional semantic mapping method significantly.
- On the other hand, the development of vision-language foundation models demonstrates a strong zero-shot transferability across data distribution.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method achieves 40.3 mean average precision (mAP) on the ScanNet semantic instance segmentation task.
- We evaluate the zero-shot performance of our method in ScanNet and SceneNN datasets.
- We propose a probabilistic label fusion method to predict close-set semantic classes from open-set label measurements.

## Abstract Cue
- —Semantic mapping based on the supervised object detectors is sensitive to image distribution.
