# Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation

- Year/Venue: 2025 / ICLR Spotlight
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, point cloud, 3D Vision
- Authors: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Min Wu, Ming-Ming Cheng, Ender Konukoglu, Serge Belongie
- Paper: https://openreview.net/forum?id=jXvwJ51vcK
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Few-shot 3D point cloud segmentation (FS-PCS) aims at generalizing models to segment novel categories with minimal annotated support samples.
- Method cue: Under this easy-to-achieve setup, we present the MultiModal Few-Shot SegNet (MM-FSS), a model effectively harnessing complementary information from multiple modalities.
- Result cue: While existing FS-PCS methods have shown promise, they primarily focus on unimodal point cloud inputs, overlooking the potential benefits of leveraging multimodal information.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: semantic, alignment, point cloud, 3D Vision.
- 초록에서 확인되는 주요 cue: Few-shot, FS-PCS, While, Under, MultiModal, Few-Shot, SegNet, MM-FSS.
