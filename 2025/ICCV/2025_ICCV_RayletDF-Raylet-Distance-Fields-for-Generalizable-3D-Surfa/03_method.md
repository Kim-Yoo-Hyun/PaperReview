# Method - RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.5. Sampling Raylets for Training and Test), p. 4 (3.5. Sampling Raylets for Training and Test)): Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded in both training and test.

## Method Body Digest

- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded in both training ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...
- **p. 2 / 1. Introduction - extractive PDF cue:** With this merit of raylets, we simply formulate the problem of generalizable 3D surface reconstruction into learning raylet distance fields from visual observations.
- **p. 2 / 1. Introduction - extractive PDF cue:** In particular, our pipeline comprises three modules: 1) a raylet feature extractor to extract geometry features from an input 3D scene for a query raylet; ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given RGB/D images and/or point clouds, a series of 3D representations has † Equal contribution * Corresponding author been developed to recover 3D geometry, including ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** If the input 3D scene P is a set of 3D Gaussians recovered by 3DGS [30] from RGBs, we follow the technique [31, 74] to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, the point-based method 3D Gaussian Splatting (3DGS) [30] has emerged as an appealing alternative to those coordinate-based methods, thanks to its impressive real-time performance ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given RGB/D images and/or point clouds, a series of 3D representations has † Equal contribution * Corresponding author been developed to recover 3D geometry, including ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we present a generalizable 3D surface representation pipeline to accurately recover 3D geometry.

## Source Evidence Cues

- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded in both training ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded ... | p. 4 (3.5. Sampling Raylets for Training and Test), p. 4 (3.5. Sampling Raylets for Training and Test) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we ... | p. 4 (3.5. Sampling Raylets for Training and Test) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded ... | p. 4 (3.5. Sampling Raylets for Training and Test) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, specific, scene, input, point, cloud, query, sample, multiple, raylets, training, test, following, steps | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, specific, scene, input, point, cloud, query, sample, multiple, raylets | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, generic, pipeline, explicit, surface, reconstruction, either, point, clouds, Gaussians | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...
- **p. 2 / 1. Introduction - extractive PDF cue:** With this merit of raylets, we simply formulate the problem of generalizable 3D surface reconstruction into learning raylet distance fields from visual observations.
- **p. 2 / 1. Introduction - extractive PDF cue:** In particular, our pipeline comprises three modules: 1) a raylet feature extractor to extract geometry features from an input 3D scene for a query raylet; ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given RGB/D images and/or point clouds, a series of 3D representations has † Equal contribution * Corresponding author been developed to recover 3D geometry, including ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** If the input 3D scene P is a set of 3D Gaussians recovered by 3DGS [30] from RGBs, we follow the technique [31, 74] to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, the point-based method 3D Gaussian Splatting (3DGS) [30] has emerged as an appealing alternative to those coordinate-based methods, thanks to its impressive real-time performance ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Recently, the point-based method 3D Gaussian Splatting (3DGS) [30] has emerged as an appealing alternative to those coordinate-based methods, thanks to its ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Early learning methods to model explicit 3D structures mainly include voxel grids [14, 67, 68], point clouds [17], octree [54], meshes [29] ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Early learning methods to model explicit 3D structures mainly include voxel grids [14, 67, 68], point clouds [17], octree [54], meshes [29] ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Note that, if there is no ball intersected, meaning that the ray shoots outside the target 3D surface, the ray is discarded in both training ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple raylets ...
- **p. 6 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** Regarding our designed multi-raylet blender in Section 3.4, the single hyperparameter T of this module can be different in training and test phase, allowing flexibility ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Note, there, ball, intersected, meaning, shoots, outside, target, surface, discarded, training, test, Given, specific, scene, input, point, cloud, query, sample.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and ... | p. 5 (4. Experiments), p. 6 (4.3. Evaluation on Raylet Sampling in Testing) |
| Semantic / temporal fusion | Baselines: We choose 5 representative groups of methods as our baselines: 1) the state-of-the-art per-scene optimization based 3D Gaussians splatting methods GOF ... | p. 5 (4. Experiments), p. 1 (Figure/Table caption) |
| Robot query / planning handoff | From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best ... | p. 6 (4.1. Evaluation on 3D Gaussians), p. 6 (4.1. Evaluation on 3D Gaussians) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablations - extractive PDF cue:** To evaluate the effectiveness of each module and the sensitivity of hyperparameters, we conduct the following ablations on the merged ScanNet/ScanNet++ dataset, and the input ...
- **p. 7 / 4.4. Ablations - extractive PDF cue:** In this ablation, the hyperparameter T is chosen as {1, 5, 10, 20}.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field module, ...
- **p. 7 / 5. Conclusion - extractive PDF cue:** Remarkably, thanks to the learned local raylet features, it exhibits excellent generalizability to new and unseen scenes in testing, while all baselines fail to do ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** This validates the generalizability and robustness of our simple design.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.5. Sampling Raylets for Training and Test), p. 4 (3.5. Sampling Raylets for Training and Test), objective 본문 anchor 없음, temporal p. 1 (1. Introduction), p. 2 (2. Related Works), p. 2 (2. Related Works), p. 3 (3.2. Raylet Feature Extractor), p. 4 (3.5. Sampling Raylets for Training and Test), p. 4 (3.5. Sampling Raylets for Training and Test).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
