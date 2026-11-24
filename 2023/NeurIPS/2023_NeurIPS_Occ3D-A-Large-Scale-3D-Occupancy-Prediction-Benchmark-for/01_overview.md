# Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.14365.
> PDF retrieval source: https://arxiv.org/pdf/2304.14365. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / NeurIPS
- Authors: Xiaoyu Tian, Tao Jiang, Longfei Yun, Yucheng Mao, Huitong Yang, Yue Wang, Yilun Wang, Hang Zhao
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Official paper: https://arxiv.org/abs/2304.14365
- Full-text retrieval: https://arxiv.org/pdf/2304.14365
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Occ3D는 자율주행 장면의 복셀별 점유와 의미 범주를 평가하기 위해 관측 가시성을 표시한 두 벤치마크를 구축한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/cabfaeecaae7d6540ee797a66f0130b0-Paper-Datasets_and_Benchmarks.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic perception requires the modeling of both 3D geometry and semantics.
- **p. 1 / Abstract - extractive body cue:** Existing methods typically focus on estimating 3D bounding boxes, neglecting finer geometric details and struggling to handle general, out-of-vocabulary objects.
- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- **p. 1 / Abstract - extractive body cue:** To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.
- **p. 1 / Abstract - extractive body cue:** This pipeline comprises three stages: voxel densification, occlusion reasoning, and image-guided voxel refinement.
- **p. 2 / 1 Introduction - extractive body cue:** While the resulting 3D bounding boxes are compact, the level of expressiveness they provide is restricted, as illustrated in Figure 1: (1) 3D bounding box ...
- **p. 2 / 1 Introduction - extractive body cue:** These limitations call for a general and coherent representation that can model the detailed geometry and semantics of objects both within and outside of the ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; ...
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- **p. 1 / Abstract - extractive body cue:** To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.
- **p. 1 / Abstract - extractive body cue:** Robotic perception requires the modeling of both 3D geometry and semantics.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We formalize the 3D occupancy prediction task as follows: a model needs to jointly estimate the occupancy state and semantic label of every voxel in the scene from images [2, 24, 5]. | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | formalize, occupancy, prediction, task, follows, model, needs, jointly, estimate, state, semantic, label | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations. | policy/controller trajectory 또는 measured result | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 여러 관측을 모아 복셀을 채운 뒤 가림을 판정하고 이미지 경계를 이용해 레이블을 정제한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/cabfaeecaae7d6540ee797a66f0130b0-Paper-Datasets_and_Benchmarks.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/cabfaeecaae7d6540ee797a66f0130b0-Paper-Datasets_and_Benchmarks.pdf#page=5)
- Waymo와 nuScenes 기반 평가를 구성하고 카메라 특징에서 거친 점유 예측을 세밀하게 만드는 CTF-Occ를 비교한다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/cabfaeecaae7d6540ee797a66f0130b0-Paper-Datasets_and_Benchmarks.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/cabfaeecaae7d6540ee797a66f0130b0-Paper-Datasets_and_Benchmarks.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 10 (6 Experiments), p. 10 (6 Experiments) |
| Embodiment/environment | To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo. | hardware/simulator version and reset protocol | p. 8 (6 Experiments), p. 9 (6 Experiments) |
| Dataset/benchmark | Occ3D-nuScenes contains 700 training scenes and 150 validation scenes. | role, split, size and leakage | p. 8 (6 Experiments), p. 9 (6 Experiments), p. 8 (6 Experiments), p. 9 (6 Experiments) |
| Metric | OHEM Loss Token Selection Strategy IoU mIoU random uncertain top-k PED CC ✓ 4.16 10.03 14.06 ✓ ✓ 5.07 12.95 16.62 ✓ ✓ 6.27 13.85 17.37 ✓ ✓ 7.04 14.16 18.43 | definition, denominator, direction and uncertainty | p. 10 (6 Experiments), p. 8 (6 Experiments), p. 7 (Figure/Table caption) |
| Baseline/ablation | Our method outperforms previous methods by remarkable margins, increasing the mIoU by 1.97. | fair input/data/compute/action matching | p. 10 (6 Experiments), p. 10 (6 Experiments), p. 9 (6 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (1) 3D bounding box representation erases the geometric details of objects, a construction vehicle has a mechanical arm that protrudes from the main ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our Occ3D dataset demonstrates rich semantic and geometric expressiveness. (a) Diversity of scenes in the Occ3D dataset; (b) Out-of-vocabulary objects, also known as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the label generation pipeline. The pipeline consists of three main steps: voxel densification, occlusion reasoning, and image-guided voxel refinement.Voxel densification consists ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Initially, in voxel densification, we increase the density of the point clouds by performing multi-frame aggregation for both static and dynamic objects separately. ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR view ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (Abstract)이다.
