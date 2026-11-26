# UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cb2266111eadcfa2c02187ace64e2183-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247830. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Chen Shi, Shaoshuai Shi, Xiaoyang Lyu, Chunyang Liu, Kehua Sheng, Bo Zhang, Li Jiang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, LiDAR, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cb2266111eadcfa2c02187ace64e2183-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf)

## Why This Paper Is Here

UniSplat은 여러 카메라의 연속 주행 영상에서 공간·시간 정보를 희소한 3D 격자에 모아 움직이는 장면을 순차 복원한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Feed-forward 3D reconstruction for autonomous driving has advanced rapidly, yet existing methods struggle with the joint challenges of sparse, non-overlapping camera views and complex scene ...
- **p. 1 / ABSTRACT - extractive body cue:** We present UniSplat, a general feed-forward framework that learns robust dynamic scene reconstruction through unified latent spatio-temporal fusion.
- **p. 1 / ABSTRACT - extractive body cue:** UniSplat constructs a 3D latent scaffold, a structured representation that captures geometric and semantic scene context by leveraging pretrained foundation models.
- **p. 1 / ABSTRACT - extractive body cue:** To effectively integrate information across spatial views and temporal frames, we introduce an efficient fusion mechanism that operates directly within the 3D scaffold, enabling consistent ...
- **p. 1 / ABSTRACT - extractive body cue:** To ensure complete and detailed reconstructions, we design a dual-branch decoder that generates dynamic-aware Gaussians from the fused scaffold by combining point-anchored refinement with voxel-based ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To enable faster inference, feed-forward reconstruction methods have emerged to synthesize novel views in a single forward pass (Xu et al., 2025; Chen et al., ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation.
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 주행 카메라의 연속 영상과 기하 보정값 |
| 표현 | 공간·시간 정보를 통합한 희소 3D 격자 |
| 출력 | 순차 복원한 동적 3D 가우시안 |
| 평가 | 주행 자료의 새 시점 재구성 |

[원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=4) · [원문 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=5) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=8)

## Main Claims and Actual Contribution

- 점에 고정한 가우시안을 정제하는 경로와 복셀에서 새 가우시안을 생성하는 경로를 결합하고, 정적 가우시안은 메모리에 보존한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=6)
- 주행 시퀀스의 새 시점과 현재 카메라 시야 밖 장면 완성을 비교하고 두 생성 경로와 메모리의 역할을 분석했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS) |
| Dataset/benchmark | We adopt image resolutions of 350 × 518 for the Waymo dataset and 224 × 406 for the nuScenes dataset. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Using only point-anchored Gaussians results in a performance degradation of 0.46 in PSNR, 0.02 in SSIM, and an increase of 0.08 in LPIPS error, underscoring the critical role of voxel-generated Gaussians in ... | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The third row illustrates a failure case in which a moving pedestrian is misclassified as static.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The voxel-only variant is excluded from comparison as it fails catastrophically at long-range rendering (Wei et al., 2025), yielding consistently poor performance across all metrics.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Specifically, replacing the default model with MoGe-2 (Wang et al., 2025e), a recently introduced open-domain geometry estimation method, yields consistent performance, which indicates that our ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance.
- **p. 17 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The final dual-branch decoder effectively combines these complementary strengths, recovering sharp details while maintaining robust structural integrity in novel views.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS)이다.

## 검색 태그 근거

여러 주행 카메라의 시계열 영상을 희소한 3D 구조로 융합한다. 라이다는 영상에서 예측하는 스케일의 학습 목표를 만드는 데 쓰인다. 별도 평가 변형은 추론에도 라이다 스케일을 사용한다. [원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=4) · [원문 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=5) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/cb2266111eadcfa2c02187ace64e2183-Paper-Conference.pdf#page=8)
