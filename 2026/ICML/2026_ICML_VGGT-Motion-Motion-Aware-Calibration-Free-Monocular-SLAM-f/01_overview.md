# VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/65079.
> PDF retrieval source: https://openreview.net/pdf/dd631f65ff2ca6199a6897ee3816879152720eef.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Zhuang Xiong, Chen Zhang, Qingshan Xu, Wenbing Tao
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, depth, SLAM, camera pose, 3D Vision
- Official paper: https://icml.cc/virtual/2026/poster/65079
- Full-text retrieval: https://arxiv.org/pdf/2602.05508.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

VGGT-Motion은 내부 보정값이 없는 단안 영상열을 움직임에 따라 서브맵으로 나누고 긴 경로에서 카메라 궤적을 일관되게 맞춘다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Despite recent progress in calibration-free monocular SLAM via 3D vision foundation models, scale drift remains severe on long sequences.
- **p. 1 / Abstract - extractive body cue:** Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive.
- **p. 1 / Abstract - extractive body cue:** To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first propose a motion-aware submap construction mechanism that uses optical flow to guide adaptive partitioning, prune static redundancy, and encapsulate turns for stable ...
- **p. 1 / Abstract - extractive body cue:** We then design an anchor-driven direct Sim(3) registration strategy.
- **p. 1 / 1. Introduction - extractive body cue:** However, the quadratic complexity (O(N 2)) of their Transformer-based architectures imposes severe memory constraints and computational bottlenecks, rendering direct deployment on long-horizon sequences infeasible.
- **p. 2 / 1. Introduction - extractive body cue:** VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency while such rigid adaptations improve scalability, they introduce critical limitations that hinder efficiency and global consistency:

## Core Idea

- **p. 3 / 3. Method - extractive body cue:** Then, we develop an anchor-driven direct Sim(3) registration algorithm to align submaps and optimize their poses.
- **p. 4 / 3.1. Motion-Aware Submap Construction - extractive body cue:** Foundation-model inference is highly sensitive to motion dynamics.
- **p. 3 / 3. Method - extractive body cue:** We first construct motion-aware submaps that segment the sequence into reliable regimes and infer local geometry with the foundation model VGGT.
- **원문 대조:** Overlap 및 loop anchor가 추가된 submap sequence를 VGGT에 입력해 local point maps, camera poses, pixel-wise confidence maps를 얻는다. 이 출력들을 이후 submap registration에 사용한다. ([PDF p. 4](https://arxiv.org/pdf/2602.05508#page=4), §3.1, Eq. (5)).
- **원문 대조:** Submap pose는 edge별 information-weighted squared residual에 Huber loss를 적용한 합을 최소화해 추정한다. 첫 pose X_1=I를 고정하고 Levenberg–Marquardt로 푼다. ([PDF p. 5](https://arxiv.org/pdf/2602.05508#page=5), §3.3 Lightweight Pose Graph Optimization, Eq. (12)).
- **p. 5 / 3.2. Anchor-Driven Direct Sim(3) Registration - extractive body cue:** Since h retains its original metric state, no re-inference is required, enabling direct loop closure alignment.
- **p. 6 / 3.3. Lightweight Pose Graph Optimization - extractive body cue:** Overall, our backend performs sparse Sim(3) optimization over a small set of submaps, yielding a globally consistent trajectory at low computational cost.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the estimated motion state s(t), we partition the input sequence into submaps that are geometrically informative and conducive to robust monocular scale estimation. | camera/depth stream, pose, map와 language goal | p. 4 (3.1. Motion-Aware Submap Construction), p. 4 (3.1. Motion-Aware Submap Construction) |
| State/latent | Given, estimated, motion, state, partition, input, sequence, submaps, geometrically, informative, conducive, robust | robot pose, free-space/semantic map와 local goal | p. 4 (3.1. Motion-Aware Submap Construction), p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3.1. Motion-Aware Submap Construction) |
| Output/action | (5) Here, the outputs include local point maps Pk, camera poses Tk, and pixel-wise confidence maps Ck, all of which are used for subsequent inter-submap registration. | collision-free trajectory 또는 velocity command | p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3.1. Motion-Aware Submap Construction), p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration) |
| Objective/outcome | This selection ensures a balanced receptive field, minimizing boundary artifacts and maximizing geometric consistency between two adject submaps. | goal reach, safety, localization error와 replanning latency | p. 5 (3.2. Anchor-Driven Direct Sim(3) Registration), p. 5 (3.3. Lightweight Pose Graph Optimization), p. 6 (3.3. Lightweight Pose Graph Optimization) |

## Main Claims and Actual Contribution

- 광류로 정지 구간의 중복과 회전 구간을 구분하고 공유 앵커를 이용해 서브맵 사이의 유사변환을 추정한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=5)
- 서브맵 자세 그래프와 루프 폐쇄를 적용하고 장거리 주행 시퀀스에서 궤적 오차와 중복 제거의 영향을 측정했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/xiong26o/xiong26o.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (4.5. Ablation Studies), p. 6 (4.3. Zero-Shot Generalization & Scalability) |
| Embodiment/environment | Hyperparameters are fixed across benchmarks and dataset-specific thresholds are held constant for all sequences. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Absolute Trajectory Error (ATE ↓) RMSE (m) comparison on the KITTI dataset. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.4. Efficiency), p. 7 (4.4. Efficiency) |
| Metric | Figure 15. Trajectory visualizations on long-range generalization benchmarks (4Seasons, Complex Urban, A2D2). Subplots show diverse segments, color denotes APE magnitude after Sim(3) alignment. Analysis Precision in Short, Loop-Free Seg ... | definition, denominator, direction and uncertainty | p. 19 (Figure/Table caption), p. 8 (4.5. Ablation Studies), p. 16 (Figure/Table caption) |
| Baseline/ablation | As shown in Figure 5, our pipeline consistently outperforms state-of-the-art foundation-modelbased methods (VGGT-Long and VGGT-SLAM) across all five benchmarks. | fair input/data/compute/action matching | p. 7 (4.4. Efficiency), p. 8 (4.5. Ablation Studies), p. 16 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.3. Zero-Shot Generalization & Scalability - extractive body cue:** The challenges of these datasets cause baselines like MASt3R-SLAM, Fast3R, and CUT3R to frequently suffer Out-of-Memory (OOM) or Tracking-Lost (TL) failures.
- **p. 6 / 4.2. Comparison on Standard Benchmarks - extractive body cue:** Foundation-model-based methods such as MASt3R-SLAM, CUT3R, and Fast3R frequently encounter Out-of-Memory (OOM) or Tracking-Lost (TL) failures, indicating limited scalability in large outdoor scenes.
- **p. 7 / 4.4. Efficiency - extractive body cue:** Absolute Trajectory Error (ATE) and Translation Drift are reported. "TL" and "OOM" denote Tracking Lost and Out-of-Memory failures, respectively.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Our Topology-Aware strategy in MASP prevents this failure mode via Turning Segment Encapsulation.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 12. Additional trajectory visualizations on TUM-Mono sequences 39, 45, 46, 47, and 48. The color scale represents the Absolute Pose Error (APE) magnitude after ...
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** Instead of providing valid geometric constraints, these redundant frames accumulate sensor noise and environmental disturbances.
- **p. 16 / Figure/Table caption - extractive body cue:** Table 8. Absolute Trajectory Error (ATE) RMSE (m) comparison on representative TUM-Mono sequences.VGGT-Motion (Ours) demonstrates superior robustness across all handheld sequences compared to submap-based baselines.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Motion-Aware Submap Construction), p. 3 (3. Method)이다.
