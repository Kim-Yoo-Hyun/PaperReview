# Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.14365.
> PDF retrieval source: https://arxiv.org/pdf/2304.14365. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Official paper: https://arxiv.org/abs/2304.14365
- Full-text retrieval: https://arxiv.org/pdf/2304.14365
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While the resulting 3D bounding boxes are compact, the level of expressiveness they provide is restricted, as illustrated in Figure 1: (1) 3D bounding box representation erases the geometric details of objects, ...를 문제로 두고, The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; (2) We put forward a rigorous automatic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; ...
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- **p. 1 / Abstract - extractive body cue:** To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.
- **p. 10 / 6 Experiments - extractive body cue:** For token selection, uncertain selection and top-k selection are on par and they significantly outperform the random selection as expected.
- **p. 10 / 6 Experiments - extractive body cue:** Both techniques improve performance.
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR view ...
- **p. 8 / 6 Experiments - extractive body cue:** We adopt the metrics of Intersection-over-Union (IoU) and mean Intersection-over-Union(mIoU) to evaluate performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While the resulting 3D bounding boxes are compact, the level of expressiveness they provide is restricted, as illustrated in Figure 1: (1) 3D bounding box representation erases the geometric details of objects, ...를 문제로 두고, The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; (2) We put forward a rigorous automatic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
