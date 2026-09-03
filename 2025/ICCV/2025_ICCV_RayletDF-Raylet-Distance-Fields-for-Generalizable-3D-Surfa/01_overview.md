# RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfaces and require per-scene training, lacking the desired generalizabil ...를 문제로 두고, Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a new raylet distance field followed by a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we present a generalizable method for 3D surface reconstruction from raw point clouds or pre-estimated 3D Gaussians by 3DGS from RGB images.
- **p. 1 / Abstract - extractive body cue:** Unlike existing coordinate-based methods which are often computationally intensive when rendering explicit surfaces, our proposed method, named RayletDF, introduces a new technique called raylet distance ...
- **p. 1 / Abstract - extractive body cue:** Our pipeline consists of three key modules: a raylet feature extractor, a raylet distance field predictor, and a multi-raylet blender.
- **p. 1 / Abstract - extractive body cue:** These components work together to extract fine-grained local geometric features, predict raylet distances, and aggregate multiple predictions to reconstruct precise surface points.
- **p. 1 / Abstract - extractive body cue:** We extensively evaluate our method on multiple public real-world datasets, demonstrating superior performance in surface reconstruction from point clouds or 3D Gaussians.
- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfaces and require ...
- **p. 1 / 1. Introduction - extractive body cue:** However, it still falls short in rendering high-quality depth views, due to its failure in capturing fine-grained surface geometry, though various constraints such as depth ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we present a generalizable 3D surface representation pipeline to accurately recover 3D geometry.
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive body cue:** If the input 3D scene P is a set of 3D Gaussians recovered by 3DGS [30] from RGBs, we follow the technique [31, 74] to ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive body cue:** Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded in both training ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive body cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets for both training or test in the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction) |
| State/latent | Given, specific, scene, input, point, cloud, query, sample, multiple, raylets, training, test | geometry, map, object/relationship state | p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | With this merit of raylets, we simply formulate the problem of generalizable 3D surface reconstruction into learning raylet distance fields from visual observations. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we present a generalizable 3D surface representation pipeline to accurately recover 3D geometry.
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive body cue:** If the input 3D scene P is a set of 3D Gaussians recovered by 3DGS [30] from RGBs, we follow the technique [31, 74] to ...
- **p. 6 / 4.1. Evaluation on 3D Gaussians - extractive body cue:** From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best accuracy, outperforming the ...
- **p. 6 / 4.1. Evaluation on 3D Gaussians - extractive body cue:** Essentially, this is because our learned raylet distance representations capture the local surface geometric patterns which tend to be generalizable at various scenes. • The ...
- **p. 5 / 4. Experiments - extractive body cue:** In addition, we also evaluate the reconstructed 3D meshes, reporting Accuracy, Completion, Precision, Recall, Chamfer-L1 distance, Normal Consistency, and F-scores with a threshold of 5cm.
- **p. 5 / 4.1. Evaluation on 3D Gaussians - extractive body cue:** Results & Analysis: Table 1 compares the quantitative results of all methods for estimating distance values of all query rays from test views.
- **p. 7 / 4.4. Ablations - extractive body cue:** Results of all ablated models on ScanNet/ScanNet++.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Evaluation on 3D Gaussians), p. 6 (4.1. Evaluation on 3D Gaussians) |
| Embodiment/environment | Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and 100 scenes for training and test; 2) ScanNet++ [71] comprising ... | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 6 (4.3. Evaluation on Raylet Sampling in Testing) |
| Dataset/benchmark | For example, when trained on ARKitScenes or ScanNet/ScanNet++, our method achieves {0.067, 0.130} meters in ADE on the novel MultiScan dataset respectively, while the baselines often have more than 0.20 meters errors. | role, split, size and leakage | p. 5 (4. Experiments), p. 6 (4.3. Evaluation on Raylet Sampling in Testing), p. 6 (4.2. Evaluation on Point Clouds), p. 7 (4.3. Evaluation on Raylet Sampling in Testing) |
| Metric | In addition, we also evaluate the reconstructed 3D meshes, reporting Accuracy, Completion, Precision, Recall, Chamfer-L1 distance, Normal Consistency, and F-scores with a threshold of 5cm. | definition, denominator, direction and uncertainty | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on 3D Gaussians) |
| Baseline/ablation | Baselines: We choose 5 representative groups of methods as our baselines: 1) the state-of-the-art per-scene optimization based 3D Gaussians splatting methods GOF [74] and PGSR [9] particularly designed for high-fidelity surface reconstr ... | fair input/data/compute/action matching | p. 5 (4. Experiments), p. 1 (Figure/Table caption), p. 6 (4.2. Evaluation on Point Clouds) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field module, ...
- **p. 7 / 5. Conclusion - extractive body cue:** Remarkably, thanks to the learned local raylet features, it exhibits excellent generalizability to new and unseen scenes in testing, while all baselines fail to do ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive body cue:** This validates the generalizability and robustness of our simple design.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfaces and require per-scene training, lacking the desired generalizabil ...를 문제로 두고, Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a new raylet distance field followed by a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.5. Sampling Raylets for Training and Test), p. 4 (3.5. Sampling Raylets for Training and Test), p. 6 (4.1. Evaluation on 3D Gaussians) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
