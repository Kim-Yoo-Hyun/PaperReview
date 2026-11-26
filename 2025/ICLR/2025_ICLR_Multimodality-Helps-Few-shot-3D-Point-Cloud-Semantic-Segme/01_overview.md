# Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b21a7ea42cbcd1c29a7a88c444cce45-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/111762. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Min Wu, Ming-Ming Cheng, Ender Konukoglu, Serge Belongie
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, point cloud, 3D Vision, 3D segmentation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b21a7ea42cbcd1c29a7a88c444cce45-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf)

## Why This Paper Is Here

MM-FSS는 적은 수의 정답 점군으로 새 범주를 분할할 때 언어 라벨과 이용 가능한 2D 영상 특징을 함께 활용한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Few-shot 3D point cloud segmentation (FS-PCS) aims at generalizing models to segment novel categories with minimal annotated support samples.
- **p. 1 / ABSTRACT - extractive body cue:** While existing FS-PCS methods have shown promise, they primarily focus on unimodal point cloud inputs, overlooking the potential benefits of leveraging multimodal information.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we address this gap by introducing a multimodal FS-PCS setup, utilizing textual labels and the potentially available 2D image modality.
- **p. 1 / ABSTRACT - extractive body cue:** Under this easy-to-achieve setup, we present the MultiModal Few-Shot SegNet (MM-FSS), a model effectively harnessing complementary information from multiple modalities.
- **p. 1 / ABSTRACT - extractive body cue:** MM-FSS employs a shared backbone with two heads to extract intermodal and unimodal visual features, and a pretrained text encoder to generate text embeddings.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address this challenge, few-shot 3D point cloud semantic segmentation (FS-PCS) has recently attracted increasing attention, enabling models to generalize to unseen/novel categories with just ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing FS-PCS methods (Zhao et al., 2021; Xu et al., 2023; Zhu et al., 2023; Mao et al., 2022; Wang et al., 2023; Zhang et ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from different ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (ii) We introduce a novel model, MM-FSS, to effectively exploit information from different modalities, which includes multimodal correlation fusion, multimodal semantic fusion, and test-time adaptive ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** To this end, we propose two novel modules for cross-modal knowledge fusion: MCF and MSF.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we propose a simple yet effective Test-time Adaptive Cross-modal Calibration (TACC) technique to mitigate training bias inherent in few-shot models (Cheng et al., 2022).
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Different from the existing setup, we propose a multimodal FS-PCS setup where two additional modalities exist: the textual modality and the 2D image modality.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To utilize the potentially available 2D modality, we propose to use the visual encoder of LSeg to generate 2D visual features, which exhibit excellent generalizability ...
- **p. 7 / 3 METHODOLOGY - extractive body cue:** (5) Then, our MSF module consists of K MSF blocks, with the correlation input to the current block denoted as Ck (k ∈{0, 1, · ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Both intermodal and unimodal features are then forwarded to the Multimodal Correlation Fusion (MCF) module to produce multimodal correlations between support and query point clouds.

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 소수의 라벨 점군, 질의 점군과 클래스 이름 |
| 표현 | 영상으로 사전학습한 점 특징과 텍스트 특징 |
| 출력 | 질의 점의 클래스 |
| 평가 | 소수 예시를 쓰는 점별 의미 분할 |

[원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=4) · [원문 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=5) · [원문 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=7)

## Main Claims and Actual Contribution

- 모달리티별 대응을 융합한 뒤 텍스트 의미로 대응을 정제하고, 시험 시 모달리티 간 보정으로 학습 범주에 대한 편향을 줄인다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=6)
- ScanNet과 S3DIS의 소수 예시 분할에서 비교하고, 융합과 시험 시 보정 모듈을 각각 제거해 성능 차이를 측정했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | (2021), we divide the large-scale scenes into 1m × 1m blocks. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | Similarly, it achieves +4.53% and +8.58% improvements on the S3DIS dataset in the 1/2-way settings, respectively. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | This performance gap underscores our model's superior ability to utilize multimodal knowledge for FS-PCS and the importance of considering commonly-ignored multimodal information to enhance few-shot generalization for future research. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Baseline/ablation | In contrast, MM-FSS consistently outperforms the former state-of-the-art across all settings, demonstrating superior cross-modal knowledge integration to enhance novel class segmentation. | fair input/data/compute/action matching | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Using only Gq (1:0) yields the lowest performance due to the IF head's limitations in utilizing support samples for learning novel classes.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant advancements.
- **p. 17 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive body cue:** In the first step, we concentrate on training the IF head to learn robust 3D features aligned with 2D modality, providing a solid foundation for ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 METHODOLOGY), p. 7 (3 METHODOLOGY)이다.

## 검색 태그 근거

소수의 라벨이 붙은 점군과 범주 이름으로 질의 점군을 분할한다. 짝지어진 RGB의 특징은 표현 사전학습에서 감독으로 쓰며, 추론에서는 점군과 텍스트를 사용한다. [원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=4) · [원문 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=5) · [원문 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b21a7ea42cbcd1c29a7a88c444cce45-Paper-Conference.pdf#page=7)
