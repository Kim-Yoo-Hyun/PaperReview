# GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/b8932994f80e23f6dd535f0762ed3ef4-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/246879. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Xiao Zhao, Chang Liu, Mingxu Zhu, Zheyuan Zhang, Linna Song, Qingliang Luo, Chufan Guo, Kuifeng Su
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision, 3D detection
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/b8932994f80e23f6dd535f0762ed3ef4-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf)

## Why This Paper Is Here

GaussianFusion은 카메라와 LiDAR의 관측을 공통 3D 가우시안 집합에 모아 차량 주변의 물체와 점유 공간을 추정한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we break from the conventional BEV paradigm and propose a new universal framework for multimodal fusion based on 3D Gaussian representation.
- **p. 1 / ABSTRACT - extractive body cue:** This approach naturally unifies multi-modal features within a shared and continuous 3D Gaussian space, effectively preserving edge and fine texture details.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Since different sensors present data in varying formats, such as cameras providing perspective semantic data and Lidar capturing 3D spatial information, multi-modal fusion faces significant ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Leveraging the distinct characteristics of each sensor helps reduce prediction uncertainty, leading to more accurate and robust perception outcomes (Liu et al., 2023b; Bai et ...

## Core Idea

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.
- **p. 6 / 6 Cameras - extractive body cue:** This Gaussian prior enables better alignment of crossmodal features to the "likely object extent," thereby enhancing fusion effectiveness-a capability absent in conventional square-shaped initialization.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 6 / 6 Cameras - extractive body cue:** We then project the 3D reference points onto the BEV feature map, where each Gaussian query qi ↔Qi is updated through deformable attention, expressed as: ...
- **p. 6 / 6 Cameras - extractive body cue:** To update the Gaussian properties, we propose an iterative optimization strategy of predicting offsets instead of predicting a set of new Gaussian distributions as adopted ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 다중 카메라와 라이다 |
| 표현 | 두 모달리티의 특징을 결합하는 가우시안 |
| 출력 | 3D 상자와 공간 점유 및 의미 |
| 평가 | 3D 검출·점유 추정의 정확도 |

[원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=4) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=8)

## Main Claims and Actual Contribution

- 센서 관측을 순방향 투영해 가우시안을 초기화하고, 공유 인코더가 모달리티 간 attention으로 위치와 특징을 반복 갱신한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=6)
- nuScenes와 Waymo에서 3D 물체 검출을 비교하고, 검출 지표와 별도로 복셀 점유 및 의미 예측을 평가했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (4.1 DATASET), p. 9 (4.1 DATASET) |
| Embodiment/environment | It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively. | hardware/simulator version and reset protocol | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET) |
| Dataset/benchmark | We further conduct experiments on the Waymo Open Dataset (Sun et al., 2020) to evaluate the generalization capability of our approach. | role, split, size and leakage | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET), p. 9 (4.1 DATASET), p. 8 (4.1 DATASET) |
| Metric | We utilize the official evaluation metric nuScenes Detection Score (NDS) and mean Average Precision (mAP) for 3D detection. | definition, denominator, direction and uncertainty | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 9 (4.1 DATASET) |
| Baseline/ablation | In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S (Hu et al., 2023a), GaussianFusion shows superior performance, outperforming them ... | fair input/data/compute/action matching | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 7 (4.1 DATASET) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4.1 DATASET - extractive body cue:** 4.7 LIMITATIONS Several approaches-covering both detection (Wang et al., 2023b) and Occ (Zhang et al., 2024b)-employ carefully designed temporal fusion modules to enhance performance.
- **p. 10 / 4.1 DATASET - extractive body cue:** A promising direction for future work is to explore motion-aware Gaussian updates, for instance by predicting velocity-guided offsets, enabling more coherent 4D scene modeling over ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras)이다.

## 검색 태그 근거

LiDAR와 다중 카메라 특징에 대응하는 초기 가우시안을 만들어 공통 좌표계에서 결합한다. 출력은 3D 물체 상자와 주변 공간의 의미 점유다. [원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=4) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b8932994f80e23f6dd535f0762ed3ef4-Paper-Conference.pdf#page=8)
